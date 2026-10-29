# S4 Model Identity, Naming & Structure — Migration Review

Status: migration candidate review.

## Source authority

Primary S4 source pair:
- Confluence page `2588789` — structured L4 S4 standard
- Confluence page `2719832` — paired L4 narrative

Supporting L4 micro-standards:
- page `4587521` — container patterns and model breakdown
- page `4489217` — family naming principles

Implementation and tool-specific evidence includes ACC naming, Revit object/view/sheet/datum/workset naming, BEP container naming, Inventor, and E-PLAN identity sources.

## Migration treatment

S4 is positioned between S2/S8 and S3/S5/S7:

S2 information demand -> S8 semantic meaning -> S4 identity/naming/segmentation -> S3 CDE implementation -> S5 coordination/verification -> S7 exchange/handover.

Shared Parameter semantic ownership remains with S8 and `TIVERIT-BIM-STD-S8-SP-REG-001`.

S3 retains ownership of CDE folder architecture. S4 governs the identities and names of containers placed within those folders.

Identity, revision, suitability/status, CDE state, and S5 issue state remain separate dimensions.

## Provenance hygiene

The raw S4 extraction package is not copied into canonical repository content. One retired originator-code example occurred in `S4_identifiers.json`; that value is excluded from migrated objects. Neutral Confluence page IDs preserve traceability.

## Curator decisions required

### CONF-S4-001 — Competing external filename grammars

Source A, BEP page `11042817`, uses a seven-token hyphen-delimited ISO 19650-style pattern:

`{proj}-{originator}-{volume/system}-{level/location}-{type}-{role}-{number}.{ext}`

Source B, ACC implementation page `7241811`, uses a six-token underscore-delimited pattern:

`[ProjectCode]_[DisciplineCode]_[ModelRole/Trade]_[StatusCode]_[PurposeCode]_[Rev/Seq].rvt`

Status: `curator_review_required`.

No precedence is asserted during migration.

### CONF-S4-002 — Discipline-code namespace

Revit Appendix E evidence uses short/single-letter discipline codes for internal object naming, while CDE implementation sources use 3-4 letter codes such as ARC, STR, MEP and AVLC.

Status: `curator_review_required`.

Possible scoped coexistence is not treated as source fact until curator-approved.

### CONF-S4-003 — Mutable status/revision embedded in filename

The L4 S4 doctrine states identity remains stable across production phase and that model naming defines identity rather than suitability. The ACC filename pattern embeds `StatusCode` and `Rev/Seq`, which are mutable lifecycle dimensions.

Status: `curator_review_required`.

No migration rule currently authorizes renaming the root container identity whenever status or revision changes.

## Source gaps retained

- no authoritative machine-readable registry for zone/volume codes
- purpose-code vocabulary is incomplete
- level abbreviations contain example/TODO material
- several Appendix E naming pages remain draft/example scaffolds
- container breakdown has qualitative criteria but no governed file-size, element-count, or polygon thresholds

## Role treatment

Governed role IDs are retained where explicitly cross-checked. Informal source functions such as Naming Owner, Model Manager, and Package Owner are not promoted to new role IDs or silently mapped as canonical aliases.

## Authority status

All S4 objects created by this migration remain `migration_candidate`. No S4 source or implementation pattern is promoted to active authority by this review.
