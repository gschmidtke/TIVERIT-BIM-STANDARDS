# Curation Record — Confluence Sheet Standards

## Status

Curated migration candidate.

## Source request

Repository owner requested retrieval of the existing BST Confluence sheet-standard material and curation into the TIVERIT BIM Standards repository.

## Source set reviewed

Primary source:
- Confluence BST page `6357066` — **Sheet & Titleblock Standards – Instructions, Definitions, Workflows**.

Supporting sources:
- `10846209` — **Titleblock Standards**.
- `6422564` — **Revit Style Guide - QA / Review Checklists**.
- `5799975` — **Annotation Standards – Instructions, Definitions, Workflows**.
- `6651935` — **Object Naming Standards for Revit**.
- `7438366` — **Revit Style Guide - Appendix E**.

Existing repository objects checked:
- `TIVERIT-BIM-INS-REVIT-TITLEBLOCK-001`.
- `TIVERIT-BIM-INS-REVIT-DOC-EXPORT-001`.
- `TIVERIT-BIM-STD-S4-IDENTITY-NAMING-EP001`.
- `TIVERIT-BIM-STD-S7-SUBMISSION-DELIVERABLES-HANDOVER-EP001`.
- `TIVERIT-BIM-STD-S8-INFO-STRUCTURE-PARAMS-CLASSIFICATION-EP001`.
- repository curation and content-classification doctrine.

## Classification decision

The primary Confluence page mixes L4 normative rules, L6 Revit execution guidance, examples, best-practice narrative, and unresolved TODO/proposed material. It must not be migrated as a page-shaped object.

Normative reusable constraints are curated into:

`TIVERIT-BIM-STD-S7-SHEET-TITLEBLOCK-DOCUMENTATION-001`

Existing L6 Revit execution remains in the titleblock, QA/style, and documentation/export instructions. The new standard does not duplicate click-level or execution sequence material.

## Accepted into normative migration candidate

- approved governed titleblocks for production sheets;
- prohibition on ungoverned local titleblock variants without governed exception/change;
- unique governed sheet identity;
- post-issue sheet-identity stability/change-control principle;
- no silent reuse of retired sheet numbers;
- human-readable governed sheet names;
- separate governed fields for client/alternate identifiers unless a project rule explicitly changes canonical identity;
- required titleblock data resolved through governed parameter/project sources;
- governance approval for new titleblock parameters;
- governed Revit revision representation and alignment with issue/transmittal records;
- prohibition on ad-hoc revision text/graphical substitution;
- cohesive, legible sheet-composition principle;
- approved view templates/naming and controlled view overrides;
- consistent reusable annotation/legend content;
- prohibition on unanchored floating annotation;
- pre-issue documentation QA;
- standards change control for sheet/titleblock rules.

## Preserved but not promoted

### Proposed sheet-number syntax

The source proposes `{DisciplineCode}{Series}-{Sequence}` with examples such as A1, SD, M2, X3, but explicitly says exact codes are to be finalized by the Standards Committee and contains multiple TODOs. These examples remain evidence, not canonical S4 syntax.

### Proposed sheet-name syntax

`{Level/Area} – {Content/Scope}` and Title Case are presented as recommended/source patterns. The naming source repeats them but does not remove the unresolved source status. The curated standard therefore requires governed human-readable naming without promoting this literal pattern as canonical.

### Special sheet series

G-series, discipline+S, discipline+D, and discipline+3 examples are typical/proposed/local-confirmation material. They are not promoted.

### Numeric composition limits

The source describes one main plan view as typical and explicitly leaves numeric limits and discipline exceptions unresolved. The curation promotes cohesion/readability, not a fabricated maximum view count.

### Exact titleblock parameter registry

The source lists expected fields but says names must exactly match the Shared Parameter Registry and contains unresolved links/TODOs. The curated standard requires applicable governed fields while leaving exact parameter identity to S8 and project information requirements.

### Draft export naming and folder examples

The existing documentation/export instruction already records that draft filename patterns and folder scaffolds are not promoted where current S3/S4/S7 authority is stronger. No PDF filename or `/Deliverables/01_PDF/` rule is created by this curation.

## Curator rationale

Confluence remains source authority during migration. The curation therefore preserves explicit source obligations while refusing to turn TODOs, examples, recommendations, or organization-specific placeholders into false canonical authority.

The new object fills the previously explicit dependency in `TIVERIT-BIM-INS-REVIT-TITLEBLOCK-001` for a dedicated governed sheet/titleblock parent standard while retaining S4 as naming authority, S8 as parameter/information-structure authority, and S7 as formal issue/deliverable authority.

Repository validation infrastructure is intentionally not part of this domain curation. The branch-local `canonical-validation.yml` experiment was removed because canonical validation is repository infrastructure already provided from `main`; this PR therefore remains limited to the sheet/titleblock governed object, its Revit instruction relationship, and this evidence-to-authority record.

## Validation / promotion state

The new object remains `migration_candidate`. It is not a formal cutover claim. Repository schema/reference/conformance validation is required before this curation branch is considered ready for promotion or merge.
