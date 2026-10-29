# Shared Parameters Migration Review

Status: migration candidate review

## Source package

Rovo extracted the Shared Parameters vertical slice from Confluence BST on 2026-10-28. The package contains 11 source pages, 17 structured assets, 26 identifiers, 34 relationships, and 42 normative statements.

## Curator decisions required

### MIG-SP-CLASS-001 — S2 vs S4 classification

Confluence page `3702785` declares the machine-readable governance spine as module `S2`, layer `L4`.

The narrative counterpart on page `3670017` declares classification `S4 – SELF / Shared Parameters`.

Migration treatment:

- canonical candidate currently uses `TIVERIT-BIM-STD-S2-PARAM-SP-GOV-001`
- the alternative S4 classification is preserved as source evidence by page ID rather than as a second canonical identifier
- no claim is made yet that S2 is the permanent final classification

Resolution status: `curator_review_required`

### MIG-SP-CONFLICT-001 — Citizen promotion behavior

The source workflow contains two incompatible behaviors:

1. one merge rule states that a previously unseen GUID is added directly as `CITIZEN`, lane `A`, lifecycle `active_citizen` unless explicitly set otherwise
2. governance notes in the same source state that promotion from `VISITOR` to `CITIZEN` is an explicit governance act and that no project can silently promote a parameter

Migration treatment:

- automatic promotion is disabled in the TIVERIT migration candidate
- new GUIDs remain proposed/visitor until explicit governance approval
- source wording remains available through Confluence provenance

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

Rovo's resolution pass confirmed that the referenced CSV/TXT artifacts are not attached anywhere in BST. Therefore these ten GUIDs are an external-source dependency rather than an unresolved Confluence lookup.

Migration treatment:

- these rows remain under `unresolved_entries`
- they are not represented as governed registry entries until authoritative external source data is supplied and verified
- the remaining 19 rows with explicit GUIDs are represented as migration candidates
- built-in Revit parameter conflicts remain subject to curator review

Resolution status: `external_source_required`

## Naming policy

Repository content uses `TIVERIT` exclusively. Historical traceability is retained through neutral Confluence page IDs, versions, sections, and page links.

## Authority status

Nothing in this vertical slice is `active` yet. All migrated objects remain `migration_candidate` until curator review resolves the items above and validation succeeds.
