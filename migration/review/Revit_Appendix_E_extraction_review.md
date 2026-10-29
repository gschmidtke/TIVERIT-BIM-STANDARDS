# Revit Appendix E — Extraction Review

Status: migration review only; non-canonical.

## Source coverage

The Appendix E checklist defines thirteen Revit implementation topics. Direct Confluence extraction has captured the substantive source pages for all thirteen topics:

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
- L5 coordinates governed workflows, release gates, orchestration, and registries/protocols where applicable.
- L6 contains Revit-specific implementation and user/tool instructions describing how a governed requirement is implemented in Revit.
- L7 holds exact presets, controlled template payloads, export settings, mappings, and other machine configuration once confirmed.

Several source pages currently mix these levels and therefore require decomposition during migration rather than one-to-one page conversion.

## Strong existing dependencies

The source itself establishes these recurring dependencies:

- S2 governs LOD/LOI and information requirements consumed by Revit modeling and documentation.
- S4 governs stable identity and naming; Revit object/view/sheet naming implements that authority locally.
- S6 governs worksharing, linking, shared coordinates, and model relationships; the Revit worksharing page implements those rules.
- S8 governs semantic parameter definitions and the Shared Parameter Registry; Revit Parameter Standards consume rather than redefine that authority.
- S5 governs coordination/readiness and should consume Revit QA evidence rather than being replaced by a Revit checklist.
- S7 governs formal exchange; Revit PDF/NWC/IFC export instructions implement exchange preparation but do not define formal acceptance.

## Child-asset findings

### Dedicated Titleblock Instruction Set — page 10846209

This is a real L6 executable instruction asset, not merely a parent-page scaffold. It defines atomic/testable steps for:

- loading and protecting approved titleblock families;
- populating Project Information;
- creating sheets from approved titleblocks;
- applying sheet number/name rules inherited from the parent standard;
- populating required titleblock parameters;
- using Revit's revision system instead of manual revision text;
- running pre-issue sheet-level QA;
- capturing evidence through schedules, PDFs, screenshots, automation logs, and QA checklists.

The source identifier is `INS-REVIT-TITLEBLOCK-01`, explicitly marked as a placeholder that may be adjusted to the governed repository scheme. Source status is Draft v0.1.0.

Important migration rule: this instruction executes the parent rule but does not make the parent's proposed sheet-numbering pattern canonical.

### Workflow & Instruction Catalogue — page 6127632

This is a substantive draft catalogue, not a list of pages. It defines:

- the distinction `Instructions execute. Workflows coordinate.`;
- W0–W8 workflow domains;
- canonical workflow and instruction fields;
- automation readiness classes MANUAL / ASSISTED / AUTOMATABLE;
- W1.1 Project Model Setup;
- W2.2 Workset Management;
- W3.1 Link Creation and W3.2 Link Update/Maintenance;
- W6.1 Sheet Setup;
- W7.1 Model Health and W7.2 QA/QC Validation;
- W8.1 Exchange Export.

This catalogue is highly relevant to the Revit implementation migration because it already names the workflow/instruction slots into which Appendix E content can map. However, several registries named by the catalogue are explicitly future and must not be fabricated during migration.

### Navisworks Export Settings JSON — page 8093711

This is a substantive machine-readable instruction set with ID `IS-W6-NAVIS-EXPORT`. It contains five instructions:

1. select approved Navisworks export configuration;
2. configure geometry/element conversion;
3. configure coordinate/positioning using shared coordinates;
4. configure property/data export;
5. execute export and record evidence.

The source explicitly requires shared-coordinate validation and records export evidence. It also states that Navisworks exports are coordination artifacts, not contractual deliverables unless explicitly designated.

The source references an `Export Preset Registry (future)`, so the instruction set exists, but a concrete export-preset registry does not yet exist in the extracted source.

### Revit Template Workflows JSON Governance — page 7700489

This page defines the intended governance model for Revit templates, including:

- scope tiers: enterprise-baseline, office-localized, discipline-specialized;
- discipline and purpose dimensions;
- minimum intended registry fields;
- semantic-version concepts for template content;
- lifecycle gates Draft → Internal Review → Approval → Publish;
- validation categories for naming, structure, parameters, discipline payloads, and version bump logic;
- distribution and deprecation concepts;
- audit requirements.

But it explicitly says the following concrete JSON artifacts still need to be added:

- Revit Template Catalogue registry;
- Template Release Pipeline;
- Validation Ruleset.

Therefore those assets are source-intended but not source-existing. They must remain gaps until explicitly created through curator action.

### Shared Parameter child assets

The child extraction reconfirmed a mature, separate parameter implementation chain:

- JSON Shared Parameter Registry Governance Workflow — page 3768321;
- Central Shared Parameter Registry First Citizen Set — page 7241788;
- Build Central Shared Parameter Registry instruction — page 7733257;
- Generate SP TXT from Registry instruction — page 7700497.

These reinforce the existing repository doctrine: the registry is authority; TXT is generated output. These assets belong to the already-migrated Shared Parameter slice rather than being duplicated under Appendix E.

## Source maturity observations

### Relatively mature source content

- Modeling Standards: clear principles for over-modeling, LOD/LOI, in-place vs loadable families, groups vs assemblies, linked vs workshared models, model containment, circular links, and shared-coordinate dependence.
- Worksharing & Collaboration: clear operational rules for central/local usage, worksets, borrowing etiquette, links worksets, prohibited personal worksets, and central maintenance.
- Sheet & Titleblock: strong structure for sheet identity, titleblock governance, required metadata, composition, revisions/issues, and parameter dependencies.
- Titleblock Instruction Set: strong atomic execution and validation structure.
- Parameter Standards: clear registry-first and GUID stability concepts, plus instance/type selection principles.
- Workflow & Instruction Catalogue: mature capability map for placing Revit instructions into governed workflow slots.

### Source content requiring curator normalization

- View naming patterns contain local/example discipline and type tokens that should be reconciled with S4 scoped namespaces.
- Sheet numbering syntax is explicitly proposed and code tables remain TODO.
- Template filename patterns and embedded versioning rules may conflict with stable-identity doctrine if treated as canonical identity rather than implementation labels.
- Template governance describes concrete registry/workflow/ruleset artifacts that do not yet exist.
- Graphics/material tables include example numerical values that are not yet confirmed organization-wide.
- Levels/grid schemes include example-only naming and directional rules.
- Documentation & Export Style is DRAFT and contains incomplete PDF settings and TODO IFC defaults.
- QA / Review Checklists is DRAFT and should become evidence-producing L6 checks linked to S5 rather than independent acceptance authority.
- Navisworks export JSON is operationally substantial but refers to a future Export Preset Registry.

## Confirmed gaps / future assets

The current extraction does not support claiming that these concrete assets already exist:

- Revit Template Catalogue Registry;
- Template Release Pipeline;
- Template Validation Ruleset;
- Export Preset Registry;
- governed Sheet Registry;
- governed QA/QC Checklist Registry.

They are referenced as required/future/TODO in source governance, which is different from being existing canonical source objects.

## Candidate migration decomposition

The likely target is not thirteen L4 standards. A cleaner structure is:

- one Revit implementation architecture / manifest;
- focused L6 instructions by topic;
- L5 workflows that orchestrate those instructions;
- L7 registries/configurations only where exact source-backed values exist;
- references back to existing S2–S8 normative objects;
- only genuinely tool-independent requirements promoted or linked at L4.

## Next extraction step

Continue below the parent topics into exact instruction/workflow/configuration assets, prioritizing:

- W1.1 project model setup instruction pages;
- W2.2 workset management instruction pages;
- W3.1/W3.2 Revit linking instructions;
- W6.1 sheet setup instruction pages beyond the titleblock instruction already found;
- W7.1/W7.2 model-health and QA instructions;
- W8.1 export instructions and any exact IFC/PDF presets;
- any concrete Workset, Sheet, Template, View Template, Export Preset, or QA/QC registries.

The purpose of the next pass is to distinguish source-existing executable assets from source-planned gaps before any canonical migration object is created.
