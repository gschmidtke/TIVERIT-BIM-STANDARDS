# S8 Asset Metadata + Revit Model File Naming Closure 001

## Scope

This curator round closes two bounded gaps against current `main`:

1. **GAP-S8-03 — Governance Metadata / Asset Schema Registry** from Confluence page 4161550.
2. **STAR-T-GATE Inbox #10 — Revit model file naming cannot be resolved from governed repository content.**

## GAP-S8-03 finding

Current `main` already contains `TIVERIT-S7-ASSET-LIFECYCLE-SCHEMA-FIELDS-001`, which governs schema identity, purpose, origin, authoritative storage, lifecycle state/version, field domains, minimum requirements, extension/change/validation/evidence/exception rules and project applicability. Therefore the schema-catalogue portion of the historical S8 gap is already migrated through S7/S8 integration.

The residual source-backed S8 delta from Confluence page 4161550 is the **field-definition and carrier/mapping layer**:

- stable field and field-group identity;
- intended semantic meaning;
- data type and governed value domain;
- lifecycle-use-based requiredness;
- source system / producing responsibility;
- mapping from model/asset/database source to governed schema fields;
- carrier mechanism;
- transformation/mapping rules;
- validation and sequencing/dependency references.

This round adds:

- `TIVERIT-S8-ASSET-FIELD-DEFINITION-FIELDS-001`
- `TIVERIT-S8-ASSET-CARRIER-MAPPING-FIELDS-001`
- `ATS-S8-ASSET-FIELD-TRACEABILITY-001`

The S8 L4 standard now has no remaining structural `implementation_gaps`.

### Boundary

No client-specific COBie table, proprietary asset template, complete field list, project population, approval authority, tool UI procedure, or export preset is invented or promoted. S2 creates information demand; S8 defines semantics and carrier traceability; S7 governs formal deliverable/handover schema reference and reliance.

## Inbox #10 finding

Inbox #10 correctly exposed an operational failure: STAR-T-GATE could not safely generate a Revit filename from supplied project facts without inventing codes. However, the canonical filename grammar was not absent.

Current `main` already contains:

- `SYNTAX-ISO19650-CONTAINER-001`: `{proj}-{originator}-{volume/system}-{level/location}-{type}-{role}-{number}.{ext}` as canonical cross-platform root identity;
- `SYNTAX-ACC-MODEL-FILE-001` as a non-canonical ACC/platform implementation mapping;
- D-13 separation of status/revision from root identity;
- controlled vocabularies for enterprise discipline/container roles/types, with explicit gaps for project/configuration values such as volume/zone and authoritative level abbreviations.

The actual gap was that the Revit L6 naming instruction did not explicitly classify **Revit model files** as information containers routed through that canonical syntax, nor did the repository define a machine-readable contract that tells an agent which project-instance token values must be supplied before generation.

This round therefore adds:

- `TIVERIT-S4-REVIT-MODEL-FILE-NAMING-FIELDS-001`
- `ATS-REVIT-MODEL-FILE-NAMING-001`
- explicit model-file routing in `TIVERIT-BIM-INS-REVIT-NAMING-001`

### Naming authority boundary

The standard governs token order, delimiter and identity behavior. Project-specific values such as project code, originator code, volume/system code, level/location code and sequence remain project-instance data unless a governed enterprise vocabulary supplies them.

A missing required code produces an **unresolved / indeterminate** result. It does not authorize invention of an abbreviation, placeholder, project-local convention or competing Revit-only filename grammar.

## Dispositions

- GAP-S8-03: `migrated` at structural governance level.
- Inbox #10: `partially_promoted` / `resolved_by_current_state_plus_bounded_extension` — the canonical grammar already existed; this round closes the Revit routing and required-input contract gap while preserving unresolved project/configuration vocabularies.

## Remaining related work

- Recover the ten unresolved shared-parameter GUIDs recorded in S8 source migration.
- Populate project-specific naming code sets through BEP/EIR/project registries where required.
- Do not treat incomplete global level/zone/purpose vocabularies as permission to invent project values.
