# Revit Object Migration Round 003 — Worksets & Worksharing

## Scope

Object-level reconciliation of Appendix E source content for Revit worksets, multi-user authoring, borrowing/ownership etiquette, model maintenance, upgrades, and recovery against current `main`.

## Curator findings

Current `main` already contained `TIVERIT-BIM-INS-REVIT-WORKSHARING-001` and `ATS-REVIT-WORKSET-001`. The remaining migration gap was not absence of worksharing doctrine; it was the missing machine-readable classification of workset purposes and the absence of conformance coverage for the broader session/maintenance/upgrade/recovery behavior.

## Promoted in this round

- `registries/revit/TIVERIT-S6-REVIT-WORKSET-PURPOSE-FIELDS-001.json`
- `registries/revit/TIVERIT-S6-REVIT-WORKSHARING-SESSION-FIELDS-001.json`
- `conformance/abstract/S6/ATS-REVIT-WORKSHARING-SESSION-001.json`
- `migration/inventory/Revit_worksets_worksharing_source_inventory.json`

## Deliberately not promoted

The following source content remains example, placeholder, project configuration, or unresolved authority rather than enterprise default:

- literal example workset names such as `Shared Levels and Grids`, `Links_Arch`, `Architecture_Main`, `Imports_Working`, and similar;
- fixed discipline/zone workset breakdowns or a universal maximum workset count;
- the example weekly audit/compact cadence;
- file-based Central/Local mechanics as a universal rule where approved cloud worksharing uses different mechanics;
- placeholder Project Manager, BIM Support, BIM Standards Lead, or other role labels where project RACI must govern;
- firm-specific support channels, monitoring tools, notification procedures, and repository paths.

## Authority boundary

S6 remains normative authority for collaboration/worksharing behavior and S4 remains authority for naming. The Revit instruction and these registries implement those rules; they do not create project acceptance or role authority. Tool state, element ownership, synchronization, or model maintenance evidence does not itself create approval authority.

## Result

Round 003 closes the structural migration gap for Revit worksets and worksharing. The broader Revit style-guide migration remains `partially_migrated` pending Families/Modeling, Phasing/Design Options, and QA/Pre-flight reconciliation.
