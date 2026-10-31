# Revit Object Migration Round 005 — Phasing / Design Options

Status: curator migration record; non-normative.

## Scope

This round reconciles Appendix E source material concerning Revit view phasing, phase filters, and Design Option visibility against the current governed repository.

Primary source pages:
- Confluence 7241762 — View Standards – Instructions, Definitions, Workflows
- Confluence 7798793 — Revit Standards and Workflow Guidelines
- Confluence 6193190 — Category & Subcategory Graphics Standards and Guidelines

## Current-main finding

Current main already contained:
- `TIVERIT-BIM-INS-REVIT-VIEWS-001`, including phase/phase-filter verification;
- `TIVERIT-S4-REVIT-VIEW-PURPOSE-FIELDS-001`, including a machine-readable `PHASE_FILTER` basis;
- `ATS-REVIT-VIEW-TEMPLATE-001`, which checks governed display state.

Therefore this round does not create a separate L4 phasing or Design Options standard.

## Curator decision

Promote the missing machine-readable control layer and conformance coverage while keeping project-instance values project-bound.

Added:
- `registries/revit/TIVERIT-S4-REVIT-PHASE-OPTION-CONTROL-FIELDS-001.json`
- `conformance/abstract/S4/ATS-REVIT-PHASING-001.json`
- `conformance/abstract/S4/ATS-REVIT-DESIGN-OPTIONS-001.json`
- `migration/inventory/Revit_phasing_design_options_source_inventory.json`

Updated:
- `instructions/revit/TIVERIT-BIM-INS-REVIT-VIEWS-001.json`

## Governed interpretation

1. Phase and phase-filter state is governed project data when it materially affects a view's declared purpose.
2. Recurring phase/option display should be controlled through approved view-template or governed mapping logic where feasible.
3. Design Option views should inherit the governed project primary option unless a view-specific option display is explicitly required and traceable.
4. Phase filters and Design Options may change graphics/visibility, so their result must remain consistent with the governed view purpose and graphics intent.
5. Material departures require a traceable exception basis.

## Deliberately not promoted

The following source content remains noncanonical/project-specific:
- example phases such as Existing, Demolition, and New Construction;
- example phase-filter combinations;
- a universal enterprise phase sequence;
- default primary Design Options by discipline;
- option-set names or option naming syntax;
- project-specific workset/Design Option combinations.

The source explicitly leaves discipline primary-option defaults unresolved, so migration must not manufacture that authority.

## Result

Round 005 closes the executable migration gap for phase/view alignment and Design Option visibility without creating a competing phase taxonomy or project-option standard.