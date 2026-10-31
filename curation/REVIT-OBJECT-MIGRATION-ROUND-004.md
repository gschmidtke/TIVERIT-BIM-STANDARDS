# Revit Object Migration Round 004 — Families & Modeling Hygiene

## Scope

Object-level reconciliation of Appendix E source content for Revit family content, in-place family restrictions, reusable-content expectations, groups/assemblies, model-structure hygiene, and LOD/LOI dependencies against current `main`.

## Curator findings

Current `main` already contained:

- `instructions/revit/TIVERIT-BIM-INS-REVIT-MODELING-001.json`;
- `standards/S4-model-identity-naming/TIVERIT-BIM-STD-S4-FAMILY-NAMING-001.json`;
- `standards/S2-information-requirements/TIVERIT-BIM-STD-S2-LOD-LOI-001.json`.

The migration gap was therefore not absence of family/modeling doctrine. The missing layer was executable control for governed reusable family content, in-place exception evidence, and conformance checks for family/content misuse and modeling-construct anti-patterns.

## Promoted in this round

- `registries/revit/TIVERIT-S4-REVIT-FAMILY-CONTENT-FIELDS-001.json`
- `registries/revit/TIVERIT-S4-REVIT-INPLACE-EXCEPTION-FIELDS-001.json`
- `conformance/abstract/S4/ATS-REVIT-FAMILY-CONTENT-001.json`
- `conformance/abstract/S4/ATS-REVIT-MODELING-CONSTRUCT-001.json`
- `migration/inventory/Revit_families_modeling_hygiene_source_inventory.json`

## Deliberately not promoted

The following remain project data, source examples, or separate governance dependencies rather than enterprise defaults:

- source example parameter labels such as `Exception Flag`, `Rationale`, and `Approver`;
- a universal named approver for in-place exceptions;
- exhaustive family library inventories, discipline-specific family lists, or type catalogues;
- phase-based LOD ranges as fixed project requirements;
- visual richness or geometry complexity as evidence of information maturity or permitted reliance;
- project-specific model breakdown, linked-model partitioning, or worksharing choices already governed by S5/S6;
- detailed family-authoring geometry recipes that are not present as approved source authority.

## Authority boundary

S2 governs information need and LOD/LOI; S4 governs family identity and naming; S8 governs parameter identity and information carriers; S5/S6 govern model partitioning, linking, and collaboration. The Revit modeling instruction and new registries implement those authorities but do not create acceptance, approval, or reliance authority.

## Result

Round 004 closes the structural migration gap for Revit Families & Modeling Hygiene. The broader Revit style-guide migration remains `partially_migrated` pending Phasing / Design Options and QA / Pre-flight reconciliation.
