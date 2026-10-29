# S4 Model Identity, Naming & Structure — Migration Review

Status: migration candidate review with curator decisions D-11 through D-13 accepted.

## Source authority

Primary S4 source pair:
- Confluence page `2588789` — structured L4 S4 standard
- Confluence page `2719832` — paired L4 narrative

Supporting L4 micro-standards:
- page `4587521` — container patterns and model breakdown
- page `4489217` — family naming principles

Implementation and tool-specific evidence includes ACC naming, Revit object/view/sheet/datum/workset naming, BEP container naming, Inventor, and E-PLAN identity sources.

## Migration treatment

S4 is positioned between S2/S8 and S3/S5/S7:

S2 information demand -> S8 semantic meaning -> S4 identity/naming/segmentation -> S3 CDE implementation -> S5 coordination/verification -> S7 exchange/handover.

Shared Parameter semantic ownership remains with S8 and `TIVERIT-BIM-STD-S8-SP-REG-001`.

S3 retains ownership of CDE folder architecture. S4 governs the identities and names of containers placed within those folders.

Identity, revision, suitability/status, CDE state, and S5 issue state remain separate dimensions.

## Provenance hygiene

The raw S4 extraction package is not copied into canonical repository content. One retired originator-code example occurred in `S4_identifiers.json`; that value is excluded from migrated objects. Neutral Confluence page IDs preserve traceability.

## Accepted curator decisions

### CONF-S4-001 / D-11 — Canonical cross-platform filename grammar

The seven-token hyphen-delimited BEP/ISO-style pattern is the canonical cross-platform container identity grammar:

`{proj}-{originator}-{volume/system}-{level/location}-{type}-{role}-{number}.{ext}`

The ACC underscore filename scheme remains a downstream implementation/display mapping only. It does not establish an independent canonical root identity.

Status: `resolved_by_curator`.

### CONF-S4-002 / D-12 — Scoped discipline-code namespaces

Enterprise and CDE container identity uses the governed 3–4 letter discipline namespace. Compact or single-letter discipline codes may remain valid only for tool-internal naming surfaces where an explicit governing instruction defines them.

Status: `resolved_by_curator`.

### CONF-S4-003 / D-13 — Stable root identity versus mutable status/revision

Suitability/status and revision are governed mutable dimensions associated with the stable container identity. They do not form part of canonical root identity. Platform-specific labels may display them where necessary without redefining the underlying identity.

Status: `resolved_by_curator`.

## Source gaps retained

- no authoritative machine-readable registry for zone/volume codes
- purpose-code vocabulary is incomplete
- level abbreviations contain example/TODO material
- several Appendix E naming pages remain draft/example scaffolds
- container breakdown has qualitative criteria but no governed file-size, element-count, or polygon thresholds

## Role treatment

Governed role IDs are retained where explicitly cross-checked. Informal source functions such as Naming Owner, Model Manager, and Package Owner are not promoted to new role IDs or silently mapped as canonical aliases.

## Authority status

All S4 objects remain `migration_candidate`. Acceptance of D-11 through D-13 resolves migration treatment but does not promote S4 to active authority before repository cutover.
