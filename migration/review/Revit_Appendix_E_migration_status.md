# Revit Appendix E migration status

Status: migration review

This review maps the 13-topic Appendix E Revit implementation checklist into the current repository architecture. Coverage means the source topic has been extracted and represented by a governed migration-candidate object or an already-migrated canonical supporting object. It does **not** mean unresolved source TODOs, examples, registries, or project-specific values have been promoted.

| # | Appendix E topic | Repository implementation | Coverage | Residual governed gaps |
|---|---|---|---|---|
| 1 | Revit Project Templates | `TIVERIT-BIM-INS-REVIT-TEMPLATES-001` | migrated | Concrete Template Catalogue, release pipeline, validation ruleset |
| 2 | View Standards | `TIVERIT-BIM-INS-REVIT-VIEWS-001` | migrated | Concrete View Template Registry and unresolved office-specific template names |
| 3 | Sheet & Titleblock Standards | `TIVERIT-BIM-INS-REVIT-TITLEBLOCK-001` | migrated | Concrete approved titleblock catalogue / sheet registry where required |
| 4 | Annotation Standards | `TIVERIT-BIM-INS-REVIT-ANNOTATION-001` | migrated | Exact governed annotation type/family catalogue and keynote/code catalogue |
| 5 | Category & Subcategory Graphics | `TIVERIT-BIM-INS-REVIT-GRAPHICS-001` | migrated | Concrete Object Styles / Line Weights / subcategory registry |
| 6 | Object Naming Standards | `TIVERIT-BIM-INS-REVIT-NAMING-001` plus S4 naming registries | migrated | Family Library catalogue; source example strings remain noncanonical |
| 7 | Parameter Standards | `TIVERIT-BIM-INS-REVIT-PARAMETERS-001`; `TIVERIT-BIM-STD-L6-SP-GEN-REG-001`; `TIVERIT-BIM-STD-L6-SP-GEN-TXT-001` | migrated | Remaining unresolved source GUID rows and incomplete binding/category data |
| 8 | Materials & Appearance | `TIVERIT-BIM-INS-REVIT-MATERIALS-001` | migrated | Governed Material Registry/Library and controlled appearance-asset lifecycle |
| 9 | Levels, Grids & References | `TIVERIT-BIM-INS-REVIT-LEVELS-GRIDS-001` | migrated | Authoritative level abbreviation registry and scope-box naming catalogue where required |
| 10 | Modeling Standards | `TIVERIT-BIM-INS-REVIT-MODELING-001` | migrated | Project-specific LOD/LOI matrices remain BEP/S2 concerns; source ranges are guidance only |
| 11 | Worksharing & Collaboration | `TIVERIT-BIM-INS-REVIT-WORKSHARING-001` | migrated | Tool/version-specific collaboration mechanics remain implementation detail under S6 |
| 12 | Documentation & Export Style | `TIVERIT-BIM-INS-REVIT-DOC-EXPORT-001`; `TIVERIT-BIM-INS-REVIT-NAVIS-EXPORT-001` | migrated | PDF/IFC preset registries and exact output configurations remain unresolved/future |
| 13 | QA / Review Checklists | `TIVERIT-BIM-INS-REVIT-QA-STYLE-001` | migrated | QA evidence can expand into ATS/ETS coverage; QA pass does not itself grant acceptance |

## Authority boundaries preserved

- S1-S9 remain the normative backbone; Appendix E is implementation guidance.
- S4 owns naming identity; Revit naming instructions implement it.
- S8 and the Shared Parameter Registry own governed parameter identity; TXT/project copies are carriers or observations.
- S6 owns collaboration/linking/shared-coordinate authority; Revit worksharing and datum instructions implement it.
- S5/S7 own coordination/readiness/exchange gates; Revit QA/export instructions produce evidence and prepare outputs but do not grant formal acceptance.
- Source items explicitly marked TODO, example, proposed, placeholder, or to-be-confirmed remain unresolved rather than silently promoted.

## Result

All 13 Appendix E checklist topics now have repository coverage at the appropriate implementation layer. Remaining work is configuration/registry completion, conformance expansion, and source-gap resolution—not further discovery of the Appendix E topic structure.
