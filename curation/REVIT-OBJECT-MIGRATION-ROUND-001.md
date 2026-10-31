# Revit Object Migration Round 001 — Views, Templates & Graphics

## Scope

Object-level reconciliation of Appendix E source content for Revit views, project templates, and category/subcategory graphics against current `main`.

## Curator findings

Current `main` already contained normalized L6 instructions for Views, Templates, Graphics, and Annotation, plus abstract conformance tests for governed view-template use and template-content validation. The migration gap was therefore not absence of Revit doctrine; it was the missing machine-readable control layer required to make those instructions and ATS objects executable.

## Promoted in this round

- `registries/revit/TIVERIT-S4-REVIT-VIEW-PURPOSE-FIELDS-001.json`
- `registries/revit/TIVERIT-S3-REVIT-TEMPLATE-CONTENT-FIELDS-001.json`
- `registries/revit/TIVERIT-S4-REVIT-GRAPHICS-CONTROL-FIELDS-001.json`
- `migration/inventory/Revit_views_templates_graphics_source_inventory.json`

## Deliberately not promoted

The following source material is retained as examples, placeholders, or unresolved configuration rather than enterprise authority:

- example view-name patterns and suffixes;
- example view-template names;
- recommended detail levels, visual styles, and phase-filter combinations where applicability is not universally resolved;
- source template filename patterns containing organization placeholders;
- unapproved discipline-template catalogue entries;
- example lineweight values, RGB values, hatch names, and subcategory names marked for confirmation;
- placeholder owners, approvers, paths, template IDs, titleblock names, phases, and shared-parameter values.

## Annotation boundary

The Annotation Standards page is adjacent to this cluster but is not completed in Round 001. The existing L6 annotation instruction is retained. Its controlled type catalogue, tag/parameter mappings, keynote governance, and exact style values are deferred to a later Revit migration round.

## Result

Round 001 closes the structural gap between Revit Appendix E doctrine and executable repository control for Views, Templates, and Graphics. The broader Revit domain remains `partially_migrated` until the remaining object clusters are reconciled.