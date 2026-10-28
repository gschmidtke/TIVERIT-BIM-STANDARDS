# Shared Parameters Migration Review

Status: migration candidate review

## Source package

Rovo extracted the Shared Parameters vertical slice from Confluence BST on 2026-10-28. The package contains 11 source pages, 17 structured assets, 26 identifiers, 34 relationships, and 42 normative statements.

## Curator decisions required

### MIG-SP-CLASS-001 — S2 vs S4 classification

The machine-readable governance spine on Confluence page `3702785` declares:

- `TAIT-BIM-STD-S2-PARAM-SP-GOV-001`
- module `S2`
- layer `L4`

The narrative counterpart on page `3670017` declares:

- `TAIT-BIM-STD-S4-SHARED-PARAM-001`
- classification `S4 – SELF / Shared Parameters`

Migration treatment:

- canonical candidate currently uses `TIVERIT-BIM-STD-S2-PARAM-SP-GOV-001`
- the S4 source ID is preserved in `legacy_ids`
- no claim is made yet that S2 is the permanent final classification

Resolution status: `curator_review_required`

### MIG-SP-CONFLICT-001 — Citizen promotion behavior

The source workflow `TAIT-SP-REGISTRY-001` contains two incompatible behaviors:

1. `merge_into_registry_v1` states that a previously unseen GUID is added to the registry as `CITIZEN`, lane `A`, lifecycle `active_citizen` unless explicitly set otherwise.
2. The same source's governance notes state that promotion from `VISITOR` to `CITIZEN` is an explicit governance act and that no project can silently promote a parameter.

Migration treatment:

- automatic promotion is disabled in the TIVERIT migration candidate
- new GUIDs remain proposed/visitor until explicit governance approval
- the original legacy wording remains preserved in Confluence provenance

Resolution status: `curator_review_required`

### MIG-SP-DATA-001 — Missing GUIDs in First Citizen Set

The source registry page `7241788` contains ten rows with literal `GUID = "(from CSV)"`.

Affected rows:

- SHEET NUMBER
- SHEET NAME
- SHEET DISCIPLINE
- SHEET ISSUE DESCRIPTION
- SHEET ISSUE DATE
- PROJECT NAME
- PROJECT NUMBER
- PROJECT PHASE
- CLIENT NAME
- PROJECT LOCATION

Migration treatment:

- these rows are listed under `unresolved_entries`
- they are not represented as governed registry entries until the source GUID values are supplied and verified
- the remaining 19 rows with explicit GUIDs are represented as migration candidates

Resolution status: `source_data_required`

## Branding migration

Canonical objects use `TIVERIT` rather than `TAIT` in IDs, file patterns, titles, and organization references. Legacy TAIT identifiers remain in `legacy_ids` and source provenance so the transformation is traceable.

## Authority status

Nothing in this vertical slice is `active` yet. All migrated objects remain `migration_candidate` until curator review resolves the items above and validation succeeds.
