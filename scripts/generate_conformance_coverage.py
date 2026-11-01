#!/usr/bin/env python3
"""Generate the repository conformance-coverage inventory.

Coverage is descriptive, not normative: missing ATS/ETS coverage is visible but is not
itself a conformance failure, and executable automation is not required where governance
legitimately permits human verification.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "conformance" / "coverage" / "TIVERIT-CONFORMANCE-COVERAGE-001.json"


def objects(folder: Path, object_type: str):
    result = []
    for path in sorted(folder.rglob("*.json")) if folder.exists() else []:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if data.get("type") == object_type:
            result.append(data)
    return result


def build_inventory():
    instructions = objects(ROOT / "instructions", "instruction")
    ats = objects(ROOT / "conformance" / "abstract", "abstract_test")
    ets = objects(ROOT / "conformance" / "executable", "executable_test")

    ats_by_governing = defaultdict(list)
    for item in ats:
        ats_by_governing[item.get("governing_object_id")].append(item["id"])
    ets_by_ats = defaultdict(list)
    for item in ets:
        ets_by_ats[item.get("ats_id")].append(item["id"])

    states = Counter(item.get("implementation_state", "unspecified") for item in ets)
    callable_count = sum(bool((item.get("implementation_binding") or {}).get("callable_reference")) for item in ets)

    return {
        "id": "TIVERIT-CONFORMANCE-COVERAGE-001",
        "type": "conformance_coverage_inventory",
        "status": "generated_observation",
        "authority": "informational",
        "purpose": "Expose current ATS/ETS coverage without converting incomplete executable coverage into a conformance failure.",
        "semantics": {
            "instruction_direct_ats": "Counts only ATS objects whose governing_object_id is the instruction ID; semantic similarity is never inferred.",
            "ats_ets": "Counts only ETS objects whose ats_id names the ATS.",
            "no_direct_ats": "A visibility state, not a defect by itself.",
            "no_ets": "A visibility state, not a defect by itself; human verification may remain legitimate where the ATS permits it.",
            "coverage_is_not_authority": "The inventory reports repository relationships only and creates no requirement or implementation obligation."
        },
        "summary": {
            "instruction_count": len(instructions),
            "instructions_with_direct_ats": sum(bool(ats_by_governing.get(item["id"])) for item in instructions),
            "instructions_without_direct_ats": sum(not bool(ats_by_governing.get(item["id"])) for item in instructions),
            "ats_count": len(ats),
            "ats_with_ets": sum(bool(ets_by_ats.get(item["id"])) for item in ats),
            "ats_without_ets": sum(not bool(ets_by_ats.get(item["id"])) for item in ats),
            "ets_count": len(ets),
            "ets_implementation_states": dict(sorted(states.items())),
            "ets_with_callable_reference": callable_count
        },
        "generation": {
            "script": "scripts/generate_conformance_coverage.py",
            "method": "Repository-local relationship scan using governing_object_id and ats_id; no inferred semantic links."
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
