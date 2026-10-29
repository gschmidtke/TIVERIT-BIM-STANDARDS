# Revit Appendix E — Extraction Review

Status: migration review only; non-canonical.

## Source coverage

The Appendix E checklist defines thirteen Revit implementation topics. Direct Confluence extraction has now captured the substantive source pages for all thirteen topics:

1. Revit Project Templates — page 7503875
2. View Standards — page 7241762
3. Sheet & Titleblock Standards — page 6357066
4. Annotation Standards — page 5799975
5. Category & Subcategory Graphics — page 6193190
6. Object Naming Standards — page 6651935
7. Parameter Standards — page 6422556
8. Materials & Appearance Standards — page 7700481
9. Levels, Grids & Reference Standards — page 6684703
10. Modeling Standards — page 7733249
11. Worksharing & Collaboration Style — page 7340051
12. Documentation & Export Style — page 7438366
13. QA / Review Checklists — page 6422564

Checklist source: Confluence page 7831553.

## Extraction treatment

Source material is intentionally not normalized into canonical rules during extraction. The following source markers remain authoritative for migration treatment until curator review: DRAFT, TODO, EXAMPLE ONLY, proposed, placeholder role names, unspecified links, unconfirmed numerical values, and unconfirmed tool settings.

No example discipline codes, sheet-series codes, template names, material names, view-template names, workset names, export filenames, tolerances, graphical settings, or parameter examples are treated as approved standards merely because they appear in a source page.

## Architectural classification

Appendix E is primarily the Revit implementation layer. It should not establish a second authority hierarchy parallel to S1–S9.

Working classification:

- L4 authority remains in tool-independent standards where a requirement states what must be true.
- L6 contains Revit-specific implementation and user/tool instructions describing how a governed requirement is implemented in Revit.
- L7 will hold exact presets, controlled template payloads, export settings, mappings, and other machine configuration once confirmed.

Several source pages currently mix these levels and therefore require decomposition during migration rather than one-to-one page conversion.

## Strong existing dependencies

The source itself establishes these recurring dependencies:

- S2 governs LOD/LOI and information requirements consumed by Revit modeling and documentation.
- S4 governs stable identity and naming; Revit object/view/sheet naming implements that authority locally.
- S6 governs worksharing, linking, shared coordinates, and model relationships; the Revit worksharing page implements those rules.
- S8 governs semantic parameter definitions and the Shared Parameter Registry; Revit Parameter Standards consume rather than redefine that authority.
- S5 governs coordination/readiness and should consume Revit QA evidence rather than being replaced by a Revit checklist.
- S7 governs formal exchange; Revit PDF/NWC/IFC export instructions implement exchange preparation but do not define formal acceptance.

## Source maturity observations

### Relatively mature source content

- Modeling Standards: clear principles for over-modeling, LOD/LOI, in-place vs loadable families, groups vs assemblies, linked vs workshared models, model containment, circular links, and shared-coordinate dependence.
- Worksharing & Collaboration: clear operational rules for central/local usage, worksets, borrowing etiquette, links worksets, prohibited personal worksets, and central maintenance.
- Sheet & Titleblock: strong structure for sheet identity, titleblock governance, required metadata, composition, revisions/issues, and parameter dependencies.
- Parameter Standards: clear registry-first and GUID stability concepts, plus instance/type selection principles.

### Source content requiring curator normalization

- View naming patterns contain local/example discipline and type tokens that should be reconciled with S4 scoped namespaces.
- Sheet numbering syntax is explicitly proposed and code tables remain TODO.
- Template filename patterns and embedded versioning rules may conflict with stable-identity doctrine if treated as canonical identity rather than implementation labels.
- Graphics/material tables include example numerical values that are not yet confirmed organization-wide.
- Levels/grid schemes include example-only naming and directional rules.
- Documentation & Export Style is DRAFT and contains incomplete PDF settings and TODO IFC defaults.
- QA / Review Checklists is DRAFT and should become evidence-producing L6 checks linked to S5 rather than independent acceptance authority.

## Candidate migration decomposition

The likely target is not thirteen L4 standards. A cleaner structure is:

- one Revit implementation architecture / manifest;
- focused L6 instructions by topic;
- L7 registries/configurations for confirmed exact values;
- references back to existing S2–S8 normative objects;
- only genuinely tool-independent requirements promoted or linked at L4.

## Next extraction step

Before canonical migration, cross-check these Appendix E sources against any dedicated child instruction pages and existing machine-readable source assets, especially titleblock instructions, Revit template/content registries, Navisworks export settings, and consolidated Revit instruction/index pages. This will identify duplicates, superseded scaffolds, and more authoritative exact settings.
