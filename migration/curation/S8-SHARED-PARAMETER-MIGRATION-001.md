# S8 Shared Parameter Migration Round 001

## Scope

Object-level reconciliation of GAP-S8-01 against current `main`, using Confluence source pages 5177345, 7241788, and 3768321 plus STAR-T-GATE Inbox issue #8 as uncurated evidence.

## Curator conclusion

The repository already contained the core procedural model for shared-parameter governance: GUID-first identity, Visitor-by-default intake, explicit governance promotion to Citizen, deterministic Citizen TXT generation, and GUID-based delta comparison. The remaining structural gap was a dedicated shared-parameter registry contract plus explicit lifecycle/deprecation conformance.

Inbox #8 was therefore not promoted as submitted. It was adapted into the existing architecture.

## Promoted/adapted concepts

- GUID is authoritative stable parameter identity.
- Registry entries can carry governed binding type and applicable categories when known.
- Owner/steward and applicable-context fields are valid registry metadata when authoritative evidence exists.
- Registry entries require explicit lifecycle status.
- Deprecated/superseded parameter use requires conformance handling.
- A dedicated JSON Schema now documents the shared-parameter registry contract.

## Not promoted from Inbox #8

- Hard-coded SP-01 through SP-05 module structure.
- A mandatory weekly drift-monitoring cadence.
- Separate `citizenship` plus `lane` fields that encode the same governance distinction twice.
- `Fast lane` / `Slow lane` vocabulary not supported by the governing source scaffold.
- Closed enterprise enumerations for group names or data types where source/project/tool evolution may legitimately add values.
- Uppercase-only canonical-name normalization as a universal authority rule.

## Existing conformance reused

- `ATS-S8-PARAM-004` already tests registry identity and central-definition consistency.
- `ATS-S8-PARAM-006` already tests uncontrolled parameter creation.
- `ATS-REVIT-PARAM-BINDING-001` already tests Revit instance/type/category binding when governed binding evidence exists.

New conformance added only for the uncovered lifecycle case:

- `ATS-S8-PARAM-DEPRECATION-001`.

## Unresolved source values

Ten rows remain unresolved because source page 7241788 contains `(from CSV)` rather than exact GUIDs:

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

These values must not be invented. Their source CSV or another authoritative record must provide exact GUID/data-definition evidence before promotion.

## Disposition

- GAP-S8-01 structural governance: **migrated**.
- First Citizen Set source values: **partially migrated** pending recovery of ten explicit GUID gaps.
- STAR-T-GATE Inbox #8: **partially promoted** as curator evidence and structural input.

This distinction prevents an unresolved source-data problem from being misclassified as a missing governance architecture problem.
