from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, RefResolver

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"

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
}


def load_json(path: Path):
    try:
        with path.open("r", encoding="utf-8") as fh:
            return json.load(fh)
    except Exception as exc:
        raise ValueError(f"{path.relative_to(ROOT)}: invalid JSON: {exc}") from exc


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

    resolver = RefResolver(
        base_uri=schema_path.as_uri(),
        referrer=schema,
        store=store,
    )
    return Draft202012Validator(schema, resolver=resolver)


def iter_canonical_json():
    for dirname in CANONICAL_DIRS:
        base = ROOT / dirname
        if not base.exists():
            continue
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

        object_id = obj.get("id")
        if isinstance(object_id, str) and "TAIT" in object_id.upper():
            errors.append(
                f"{path.relative_to(ROOT)}: canonical id contains legacy TAIT namespace: {object_id}"
            )

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

    validate_all_json_syntax(errors)
    schemas = validate_schema_files(errors)

    required_schemas = {
        "base-object.schema.json",
        "standard.schema.json",
        "registry.schema.json",
        "workflow.schema.json",
    }
    missing = required_schemas.difference(schemas)
    if missing:
        errors.append(f"Missing or invalid required schemas: {sorted(missing)}")
    else:
        validate_objects(schemas, errors)

    if errors:
        print("\nVALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("\nVALIDATION PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
