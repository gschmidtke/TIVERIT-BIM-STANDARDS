from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL_DIRS = [
    "constitution", "standards", "workflows", "instructions", "configurations",
    "registries", "modules", "engine", "conformance", "bridges",
]


def collect_ids(value, ids: set[str]) -> None:
    if isinstance(value, dict):
        object_id = value.get("id")
        if isinstance(object_id, str) and object_id:
            ids.add(object_id)
        for child in value.values():
            collect_ids(child, ids)
    elif isinstance(value, list):
        for child in value:
            collect_ids(child, ids)


def canonical_json_paths():
    for dirname in CANONICAL_DIRS:
        base = ROOT / dirname
        if base.exists():
            yield from sorted(base.rglob("*.json"))


def main() -> int:
    objects: list[tuple[Path, dict]] = []
    known_ids: set[str] = set()
    errors: list[str] = []

    for path in canonical_json_paths():
        try:
            obj = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(obj, dict):
            continue
        objects.append((path, obj))
        collect_ids(obj, known_ids)

    for path, obj in objects:
        if obj.get("type") != "abstract_test":
            continue

        governing_object_id = obj.get("governing_object_id")
        if not isinstance(governing_object_id, str) or not governing_object_id:
            errors.append(f"{path.relative_to(ROOT)}: missing governing_object_id")
        elif governing_object_id not in known_ids:
            errors.append(
                f"{path.relative_to(ROOT)}: unresolved governing_object_id {governing_object_id!r}"
            )

        requirement_id = obj.get("requirement_id")
        if requirement_id is not None:
            if not isinstance(requirement_id, str) or not requirement_id:
                errors.append(f"{path.relative_to(ROOT)}: invalid requirement_id")
            elif requirement_id not in known_ids:
                errors.append(
                    f"{path.relative_to(ROOT)}: unresolved requirement_id {requirement_id!r}"
                )

    if errors:
        print("ATS GOVERNING LINK VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("ATS GOVERNING LINK VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
