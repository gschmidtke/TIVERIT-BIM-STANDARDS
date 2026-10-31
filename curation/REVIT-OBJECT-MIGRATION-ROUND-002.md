# Revit Object Migration Round 002 — Annotation & Tags

## Scope

Object-level reconciliation of Appendix E source content for Revit annotation types, tags/symbols, and keynote/annotation-code governance against current `main`.

## Curator findings

Current `main` already contained `TIVERIT-BIM-INS-REVIT-ANNOTATION-001` and the S8 shared-parameter registry. The remaining structural gap was the absence of machine-readable annotation-type governance, tag-to-parameter mapping governance, keynote/code-source governance, and conformance tests for controlled annotation and tag behavior.

## Promoted in this round

- `registries/revit/TIVERIT-S4-REVIT-ANNOTATION-TYPE-FIELDS-001.json`
- `registries/revit/TIVERIT-S8-REVIT-TAG-PARAMETER-MAPPING-FIELDS-001.json`
- `registries/revit/TIVERIT-S4-REVIT-KEYNOTE-CODE-FIELDS-001.json`
- `conformance/abstract/S4/ATS-REVIT-ANNOTATION-TYPE-001.json`
- `conformance/abstract/S8/ATS-REVIT-TAG-PARAMETER-MAPPING-001.json`
- `migration/inventory/Revit_annotations_tags_source_inventory.json`

## Authority boundary

The source provides durable governance principles but leaves many enterprise values unresolved. This round therefore promotes the fields and relationships that must be governed, not the source's TODO/example values.

## Deliberately not promoted

- TODO font families, paper text sizes, colors, line spacing, dimension precision, arrow/tick types, and tolerance values;
- placeholder door/equipment/grid/level/room/space tag family names;
- incomplete discipline-specific tag parameter lists and appearance rules;
- placeholder keynote/code owner, storage path, review cadence, edit-role names, and graphic style;
- any client/project-specific deviation not backed by an approved project rule.

## Result

Round 002 closes the structural repository gap for annotation and tag governance. It does not invent the unresolved enterprise catalogues. The broader Revit migration remains `partially_migrated` until worksets, family/modeling hygiene, phasing/design options, and QA/pre-flight are reconciled.
