from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
FIXTURES_ROOT = ROOT / "conformance" / "fixtures"
ETS_ROOT = ROOT / "conformance" / "executable"
PARAMETER_REGISTRY = ROOT / "registries" / "parameters" / "TIVERIT-BIM-STD-S8-SP-REG-001.json"
RESULT_SCHEMA = ROOT / "schemas" / "conformance-result.schema.json"

IMPLEMENTATION_VERSION = "0.1.0-pilot"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def build_result(*, fixture: dict, result: str, observations: list[dict], ats_id: str, requirement_id: str, ets_id: str) -> dict:
    return {
        "requirement_id": requirement_id,
        "ats_id": ats_id,
        "ets_id": ets_id,
        "tested_subject_id": fixture["id"],
        "observation_timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "result": result,
        "observations": observations,
        "implementation": {
            "name": "TIVERIT repository conformance fixture runner",
            "version_or_build": IMPLEMENTATION_VERSION,
            "platform": "Python 3.12"
        },
        "evidence_artifacts": [fixture["id"]]
    }


def check_s8_shared_parameters(fixture: dict) -> dict:
    registry = load_json(PARAMETER_REGISTRY)
    active_entries = {
        entry["id"].lower(): entry
        for entry in registry.get("entries", [])
        if entry.get("status") == "active" and isinstance(entry.get("id"), str)
    }
    unresolved_names = {
        entry.get("name")
        for entry in registry.get("unresolved_entries", [])
        if isinstance(entry, dict) and isinstance(entry.get("name"), str)
    }

    source_observations = fixture.get("simulated_observations", [])
    evidence: list[dict] = []
    failures: list[str] = []
    indeterminate: list[str] = []

    if not source_observations:
        indeterminate.append("No observed shared-parameter evidence was supplied.")

    for index, observed in enumerate(source_observations):
        guid = observed.get("guid")
        name = observed.get("name")
        data_type = observed.get("data_type")
        finding = {
            "observation_index": index,
            "observed_guid": guid,
            "observed_name": name,
            "observed_data_type": data_type,
        }

        if isinstance(guid, str) and guid.strip():
            governed = active_entries.get(guid.lower())
            if governed is None:
                finding["finding"] = "unknown_guid"
                failures.append(f"Unknown governed shared-parameter GUID: {guid}")
            else:
                finding["governed_name"] = governed.get("name")
                finding["governed_data_type"] = governed.get("data_type")
                local_failures = []
                if not isinstance(name, str) or not name:
                    indeterminate.append(f"Observation {index} is missing parameter name evidence.")
                    finding["finding"] = "missing_name_evidence"
                elif name != governed.get("name"):
                    local_failures.append(
                        f"GUID {guid} name mismatch: observed {name!r}, governed {governed.get('name')!r}."
                    )
                if not isinstance(data_type, str) or not data_type:
                    indeterminate.append(f"Observation {index} is missing data_type evidence.")
                    finding["finding"] = "missing_data_type_evidence"
                elif data_type != governed.get("data_type"):
                    local_failures.append(
                        f"GUID {guid} data type mismatch: observed {data_type!r}, governed {governed.get('data_type')!r}."
                    )
                if local_failures:
                    failures.extend(local_failures)
                    finding["finding"] = "governed_definition_conflict"
                elif finding.get("finding") is None:
                    finding["finding"] = "match"
        else:
            if isinstance(name, str) and name in unresolved_names:
                finding["finding"] = "source_identity_unresolved"
                indeterminate.append(
                    f"Parameter {name!r} exists only as an unresolved source row without a governed GUID."
                )
            else:
                finding["finding"] = "missing_governed_identity"
                indeterminate.append(
                    f"Observation {index} lacks a governed GUID and cannot be resolved from the migrated registry."
                )

        evidence.append(finding)

    if failures:
        result = "fail"
    elif indeterminate:
        result = "indeterminate"
    else:
        result = "pass"

    evidence.append({
        "summary": {
            "failure_count": len(failures),
            "indeterminate_count": len(indeterminate),
            "failures": failures,
            "indeterminate_reasons": indeterminate,
        }
    })

    return build_result(
        fixture=fixture,
        result=result,
        observations=evidence,
        requirement_id="REQ-S8-004",
        ats_id="ATS-S8-PARAM-004",
        ets_id="ETS-S8-PARAM-004-PYTHON",
    )


IMPLEMENTATIONS = {
    "ETS-S8-PARAM-004-PYTHON": check_s8_shared_parameters,
}


def load_ets_states() -> dict[str, str]:
    states: dict[str, str] = {}
    for path in sorted(ETS_ROOT.rglob("*.json")):
        obj = load_json(path)
        ets_id = obj.get("id")
        if isinstance(ets_id, str):
            states[ets_id] = obj.get("implementation_state", "")
    return states


def validate_result(result: dict, schema: dict) -> list[str]:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [error.message for error in sorted(validator.iter_errors(result), key=lambda e: list(e.path))]


def main() -> int:
    result_schema = load_json(RESULT_SCHEMA)
    ets_states = load_ets_states()
    executed = 0
    skipped = 0
    errors: list[str] = []

    for path in sorted(FIXTURES_ROOT.rglob("*.json")):
        fixture = load_json(path)
        ets_id = fixture.get("ets_id")
        expected = fixture.get("expected_result")
        implementation = IMPLEMENTATIONS.get(ets_id)

        if implementation is None:
            skipped += 1
            state = ets_states.get(ets_id, "unknown")
            print(f"FIXTURE SKIP {fixture.get('id')} -> {ets_id} ({state})")
            continue

        executed += 1
        evidence = implementation(fixture)
        schema_errors = validate_result(evidence, result_schema)
        if schema_errors:
            errors.append(
                f"{fixture.get('id')}: emitted conformance result violates result schema: {schema_errors}"
            )
            continue

        actual = evidence.get("result")
        if actual != expected:
            errors.append(
                f"{fixture.get('id')}: expected {expected!r} but implementation returned {actual!r}"
            )
            print(f"FIXTURE FAIL {fixture.get('id')} expected={expected} actual={actual}")
        else:
            print(f"FIXTURE OK   {fixture.get('id')} -> {actual}")

    if executed == 0:
        errors.append("No implemented conformance fixtures were executed.")

    print(f"\nExecuted fixtures: {executed}; skipped specification-only fixtures: {skipped}")

    if errors:
        print("\nCONFORMANCE FIXTURES FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("\nCONFORMANCE FIXTURES PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
