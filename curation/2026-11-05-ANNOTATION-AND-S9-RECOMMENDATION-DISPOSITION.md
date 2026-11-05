# Standards Curator — annotation and S9 recommendation disposition
Date: 2026-11-05
Status: CURATOR TRIAGE; EVIDENCE-DEPENDENT ITEMS OPEN
Evaluated against: gschmidtke/TIVERIT-BIM-STANDARDS main @ e2cb86712 (2026-11-01)
Source: Owner's detail-view annotation recommendations and PM S9 ZEN automation governance concern.

## Annotation standards (S4/S8)
Existing `registries/revit/TIVERIT-S4-REVIT-ANNOTATION-TYPE-FIELDS-001.json` defines annotation class, stable type identity, use, discipline, display properties, units/precision, parameters, library source and change control. **Partially migrated, not missing.** Detail-view source images and measurable properties were not available in this repository inspection. No font, text height, lineweight, leader, arrowhead or precision value is promoted by assumption.

Next: prepare a source-backed evidence matrix per detail view: source reference, observed annotation class, actual text, paper text size, view scale, family/type, leaders, arrows, dimensions/precision, graphic hierarchy and evidence quality. Map each finding to existing registry fields; distinguish observed project example, proposed enterprise rule and project-specific configuration. Curator review and Owner decision required for new enterprise defaults.

## S9 ZEN automation
`registries/automation/REG-S9-AUTOMATION-001.json` currently has `entries: []`, `status: migration_candidate`. **ZEN is not registered or approved** for governed production automation by this registry. Do not invent a certified entry. BAUMEISTER to return version/build, action-by-action read/write effects, data targets, owner role, input/output, risk, approval provenance, logging, reproducible tests and exceptions. Specifically distinguish ACC Gate report actions/Ping Only from write operations. After evidence review curator may propose an `AUT-*` candidate in draft/pilot state; approval remains governed.

## Curator disposition
- Existing annotation fields: RETAIN; no duplicate standard.
- Detail-view numerical conventions: HOLD — SOURCE EVIDENCE NEEDED.
- ZEN automation registry: HOLD — TECHNICAL EVIDENCE + APPROVAL NEEDED.
- Do not claim production approval, cutover or universal graphic defaults.

## PM return
Dispatch annotation evidence extraction to an authorized preparer; BAUMEISTER to supply S9 technical evidence. Track both as OPEN and reconcile returns before further Standards promotion. No GitHub permission reassignment for temporary role coverage.
