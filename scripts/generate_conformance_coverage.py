#!/usr/bin/env python3
"""Generate a factual conformance coverage inventory from repository relationships.

Coverage is intentionally descriptive, not normative: absence of ATS or ETS is visible
but is not treated as failure. Human-verification-only ATS remain legitimate.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "conformance" / "coverage" / "TIVERIT-CONFORMANCE-COVERAGE-001.json"


def load_jsons(folder: Path):
    rows = []
    if not folder.exists():
        return rows
    for path in sorted(folder.rglob("*.json")):
        if path == OUTPUT:
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        rows.append((path.relative_to(ROOT).as_posix(), data))
    return rows


def build_inventory():
    instructions = [(p, d) for p, d in load_jsons(ROOT / "instructions") if d.get("type") == "instruction"]
    ats = [(p, d) for p, d in load_jsons(ROOT / "conformance" / "abstract") if d.get("type") == "abstract_test"]
    ets = [(p, d) for p, d in load_jsons(ROOT / "conformance" / "executable") if d.get("type") == "executable_test"]

    ats_by_governing = defaultdict(list)
    for path, item in ats:
        ats_by_governing[item.get("governing_object_id")].append(item["id"])

    ets_by_ats = defaultdict(list)
    for path, item in ets:
        ets_by_ats[item.get("ats_id")].append({
            "id": item["id"],
            "implementation_state": item.get("implementation_state", "unspecified"),
            "callable": bool((item.get("implementation_binding") or {}).get("callable_reference")),
        })

    instruction_rows = []
    for path, item in instructions:
        linked = sorted(ats_by_governing.get(item["id"], []))
        instruction_rows.append({
            "instruction_id": item["id"],
            "path": path,
            "ats_ids": linked,
            "coverage_state": "ats_present" if linked else "no_direct_ats",
        })

    ats_rows = []
    for path, item in ats:
        implementations = sorted(ets_by_ats.get(item["id"], []), key=lambda x: x["id"])
        permitted = item.get("permitted_implementation_classes", [])
        ats_rows.append({
            "ats_id": item["id"],
            "path": path,
            "governing_object_id": item.get("governing_object_id"),
            "requirement_id": item.get("requirement_id"),
            "human_verification_permitted": "human_verification" in permitted,
            "ets": implementations,
            "coverage_state": "ets_present" if implementations else "no_ets",
        })

    states = Counter()
    callable_count = 0
    for _, item in ets:
        states[item.get("implementation_state", "unspecified")] += 1
        if (item.get("implementation_binding") or {}).get("callable_reference"):
            callable_count += 1

    return {
        "id": "TIVERIT-CONFORMANCE-COVERAGE-001",
        "type": "conformance_coverage_inventory",
        "status": "generated_observation",
        "authority": "informational",
        "purpose": "Expose current ATS/ETS coverage without converting incomplete executable coverage into a conformance failure.",
        "semantics": {
            "no_direct_ats": "No ATS currently names this instruction as its governing_object_id. This is a visibility state, not a defect by itself.",
            "no_ets": "No executable test currently names this ATS through ats_id. Human verification may still be legitimate where permitted by the ATS.",
            "specified_not_implemented": "An ETS contract exists but has no verified callable implementation yet.",
            "coverage_is_not_authority": "This inventory reports repository relationships only; it does not create requirements or require executable automation where governance permits human verification."
        },
        "summary": {
            "instruction_count": len(instructions),
            "instructions_with_direct_ats": sum(1 for r in instruction_rows if r["ats_ids"]),
            "instructions_without_direct_ats": sum(1 for r in instruction_rows if not r["ats_ids"]),
            "ats_count": len(ats),
            "ats_with_ets": sum(1 for r in ats_rows if r["ets"]),
            "ats_without_ets": sum(1 for r in ats_rows if not r["ets"]),
            "ats_permitting_human_verification": sum(1 for _, d in ats if "human_verification" in d.get("permitted_implementation_classes", [])),
            "ets_count": len(ets),
            "ets_implementation_states": dict(sorted(states.items())),
            "ets_with_callable_reference": callable_count,
        },
        "instructions": instruction_rows,
        "abstract_tests": ats_rows,
        "generation": {
            "script": "scripts/generate_conformance_coverage.py",
            "method": "Repository-local JSON relationship scan using governing_object_id and ats_id; no inferred semantic links."
        }
    }


def rendered():
    return json.dumps(build_inventory(), indent=2, ensure_ascii=False) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail when the committed inventory is stale.")
    args = parser.parse_args()
    expected = rendered()
    if args.check:
        actual = OUTPUT.read_text(encoding="utf-8") if OUTPUT.exists() else ""
        if actual != expected:
            raise SystemExit("Conformance coverage inventory is stale; run scripts/generate_conformance_coverage.py")
        print("Conformance coverage inventory is current.")
        return
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(expected, encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
