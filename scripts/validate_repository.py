from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker, RefResolver

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
FORWARD_REFERENCE_REGISTER = ROOT / "migration" / "reference-forward-declarations.json"

# Deliberately assembled at runtime so the retired token itself never appears in repository text.
FORBIDDEN_TOKEN = bytes([84, 65, 73, 84]).decode("ascii")
TEXT_SUFFIXES = {".json", ".md", ".py", ".yml", ".yaml", ".txt", ".csv"}

CANONICAL_DIRS = [
    "constitution",
    "standards",
    "workflows",
    "instructions",
    "configurations",
    "registries",
    "modules",
    "engine",
]

TYPE_TO_SCHEMA = {
    "standard": "standard.schema.json",
    "registry": "registry.schema.json",
    "workflow": "workflow.schema.json",
    "role": "role.schema.json",
}

REFERENCE_KEYS = {
    "referenced_standards",
    "referenced_workflows",
    "interfaces_with_roles",
    "parent_role",
    "specializations",
}

# Controlled repository namespaces. New namespace families require curator approval
# and must be registered here before references using them can validate.
CANONICAL_REFERENCE_PATTERN = re.compile(
    r"^(?:TIVERIT-|ROLE-|REG-|REQ-|W-|BIM-STD-|GAP-|REL-|LNK-|AUT-|MIG-)"
)

# Detect structured repository-ID-like values that would otherwise escape the known
# namespace matcher. Requiring at least three hyphen-delimited segments avoids
# treating simple external references such as ISO-19650 as repository object IDs.
IDENTIFIER_LIKE_PATTERN = re.compile(
    r"^[A-Z][A-Z0-9]*(?:-[A-Z0-9][A-Z0-9.]*){2,}$"
)

# These are deliberate conceptual labels used in relationship fields, not repository
# object identities. They remain exempt until/unless promoted into governed objects.
REFERENCE_LITERAL_EXEMPT_PATTERNS = (
    re.compile(r"^GATE-[A-Z0-9-]+$"),
)


def load_json(path: Path):
    try:
        with path.open("r", encoding="utf-8") as fh:
            return json.load(fh)
    except Exception as exc:
        raise ValueError(f"{path.relative_to(ROOT)}: invalid JSON: {exc}") from exc


def validate_forbidden_token(errors: list[str]):
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if FORBIDDEN_TOKEN.lower() in text.lower():
            errors.append(f"{path.relative_to(ROOT)}: contains forbidden retired organization token")


def validate_schema_files(errors: list[str]) -> dict[str, dict]:
    loaded: dict[str, dict] = {}
    for path in sorted(SCHEMAS.glob("*.schema.json")):
        try:
            schema = load_json(path)
            Draft202012Validator.check_schema(schema)
            loaded[path.name] = schema
            print(f"SCHEMA OK  {path.relative_to(ROOT)}")
        except Exception as exc:
            errors.append(str(exc))
    return loaded


def make_validator(schema_name: str, schemas: dict[str, dict]):
    schema = schemas[schema_name]
    schema_path = (SCHEMAS / schema_name).resolve()
    base_schema = schemas["base-object.schema.json"]
    base_id = base_schema.get("$id")
    store = {
        base_id: base_schema,
        (SCHEMAS / "base-object.schema.json").resolve().as_uri(): base_schema,
        "./base-object.schema.json": base_schema,
    }
    resolver = RefResolver(base_uri=schema_path.as_uri(), referrer=schema, store=store)
    return Draft202012Validator(schema, resolver=resolver, format_checker=FormatChecker())


def iter_canonical_json():
    for dirname in CANONICAL_DIRS:
        base = ROOT / dirname
        if base.exists():
            yield from sorted(base.rglob("*.json"))


def validate_objects(schemas: dict[str, dict], errors: list[str]):
    for path in iter_canonical_json():
        try:
            obj = load_json(path)
        except Exception as exc:
            errors.append(str(exc))
            continue
        if not isinstance(obj, dict):
            errors.append(f"{path.relative_to(ROOT)}: canonical JSON root must be an object")
            continue
        obj_type = obj.get("type")
        schema_name = TYPE_TO_SCHEMA.get(obj_type)
        if not schema_name:
            print(f"SKIP       {path.relative_to(ROOT)} (no v0.1 schema for type={obj_type!r})")
            continue
        validator = make_validator(schema_name, schemas)
        object_errors = sorted(validator.iter_errors(obj), key=lambda e: list(e.path))
        if object_errors:
            for err in object_errors:
                location = ".".join(str(p) for p in err.path) or "<root>"
                errors.append(f"{path.relative_to(ROOT)}:{location}: {err.message}")
        else:
            print(f"OBJECT OK  {path.relative_to(ROOT)}")


def collect_all_ids(value, ids: set[str]):
    if isinstance(value, dict):
        object_id = value.get("id")
        if isinstance(object_id, str) and object_id:
            ids.add(object_id)
        for child in value.values():
            collect_all_ids(child, ids)
    elif isinstance(value, list):
        for child in value:
            collect_all_ids(child, ids)


def iter_reference_values(obj):
    if not isinstance(obj, dict):
        return

    relationships = obj.get("relationships")
    if isinstance(relationships, dict):
        for relation_type, values in relationships.items():
            if isinstance(values, list):
                for value in values:
                    if isinstance(value, str):
                        yield f"relationships.{relation_type}", value
            elif isinstance(values, str):
                yield f"relationships.{relation_type}", values

    for key in REFERENCE_KEYS:
        values = obj.get(key)
        if isinstance(values, list):
            for value in values:
                if isinstance(value, str):
                    yield key, value
        elif isinstance(values, str):
            yield key, values


def is_exempt_reference_literal(value: str) -> bool:
    return any(pattern.fullmatch(value) for pattern in REFERENCE_LITERAL_EXEMPT_PATTERNS)


def load_forward_references(errors: list[str]) -> set[str]:
    if not FORWARD_REFERENCE_REGISTER.exists():
        errors.append(
            "migration/reference-forward-declarations.json: missing explicit forward reference register"
        )
        return set()
    try:
        register = load_json(FORWARD_REFERENCE_REGISTER)
    except Exception as exc:
        errors.append(str(exc))
        return set()

    entries = register.get("forward_references", [])
    if not isinstance(entries, list):
        errors.append(
            "migration/reference-forward-declarations.json: forward_references must be an array"
        )
        return set()

    declared: set[str] = set()
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            errors.append(
                f"migration/reference-forward-declarations.json:forward_references.{index}: must be an object"
            )
            continue
        ref_id = entry.get("id")
        reason = entry.get("reason")
        if not isinstance(ref_id, str) or not ref_id:
            errors.append(
                f"migration/reference-forward-declarations.json:forward_references.{index}: missing id"
            )
            continue
        if not CANONICAL_REFERENCE_PATTERN.match(ref_id):
            errors.append(
                f"migration/reference-forward-declarations.json:forward_references.{index}: "
                f"unrecognized governed namespace for {ref_id!r}"
            )
            continue
        if not isinstance(reason, str) or not reason.strip():
            errors.append(
                f"migration/reference-forward-declarations.json:forward_references.{index}: missing reason for {ref_id}"
            )
            continue
        if ref_id in declared:
            errors.append(
                f"migration/reference-forward-declarations.json: duplicate forward reference {ref_id}"
            )
            continue
        declared.add(ref_id)
    return declared


def validate_referential_integrity(errors: list[str]):
    objects: list[tuple[Path, dict]] = []
    known_ids: set[str] = set()
    top_level_locations: dict[str, list[str]] = {}

    for path in iter_canonical_json():
        try:
            obj = load_json(path)
        except Exception:
            continue
        if not isinstance(obj, dict):
            continue
        objects.append((path, obj))
        collect_all_ids(obj, known_ids)
        top_level_id = obj.get("id")
        if isinstance(top_level_id, str) and top_level_id:
            top_level_locations.setdefault(top_level_id, []).append(str(path.relative_to(ROOT)))

    for object_id, locations in sorted(top_level_locations.items()):
        if len(locations) > 1:
            errors.append(
                f"duplicate top-level object id {object_id!r} declared in: {', '.join(sorted(locations))}"
            )

    forward_references = load_forward_references(errors)
    used_forward_references: set[str] = set()

    for path, obj in objects:
        for field, target in iter_reference_values(obj):
            if not CANONICAL_REFERENCE_PATTERN.match(target):
                if IDENTIFIER_LIKE_PATTERN.fullmatch(target) and not is_exempt_reference_literal(target):
                    errors.append(
                        f"{path.relative_to(ROOT)}:{field}: structured reference {target!r} uses an "
                        "unrecognized namespace; correct the identifier or register the namespace through governance"
                    )
                continue
            if target in known_ids:
                continue
            if target in forward_references:
                used_forward_references.add(target)
                print(f"FORWARD OK {path.relative_to(ROOT)}:{field} -> {target}")
                continue
            errors.append(
                f"{path.relative_to(ROOT)}:{field}: unresolved canonical reference {target!r}; "
                "add the target object or declare the specific ID in migration/reference-forward-declarations.json"
            )

    unused = sorted(forward_references - used_forward_references)
    for ref_id in unused:
        errors.append(
            f"migration/reference-forward-declarations.json: stale/unused forward reference {ref_id!r}"
        )


def validate_all_json_syntax(errors: list[str]):
    for path in sorted(ROOT.rglob("*.json")):
        if ".git" in path.parts:
            continue
        try:
            load_json(path)
        except Exception as exc:
            errors.append(str(exc))


def main() -> int:
    errors: list[str] = []
    validate_forbidden_token(errors)
    validate_all_json_syntax(errors)
    schemas = validate_schema_files(errors)
    required_schemas = {
        "base-object.schema.json",
        "standard.schema.json",
        "registry.schema.json",
        "workflow.schema.json",
        "role.schema.json",
    }
    missing = required_schemas.difference(schemas)
    if missing:
        errors.append(f"Missing or invalid required schemas: {sorted(missing)}")
    else:
        validate_objects(schemas, errors)
        validate_referential_integrity(errors)
    if errors:
        print("\nVALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("\nVALIDATION PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
