# S8 Information Structure, Parameters & Classification — Migration Review

Status: migration candidate review

## Source authority

The primary S8 source pair is:

- Confluence page `2883653` — machine-readable L4 S8 standard module
- Confluence page `2785403` — human-readable L4 S8 narrative

The later S8 review branch contains gap-closure scaffolds for Shared Parameters, Classification, and Asset/Lifecycle data. These are retained as implementation evidence and are not treated as replacement S8 standards.

## Source package findings

The S8 extraction identifies:

- 23 relevant pages/containers
- 40 normative statements across the core standard and implementation scaffolds
- 3 explicit S8 implementation gaps
- 8 semantic domains
- classification references including Uniclass 2015, OmniClass, and client-specific classifications
- 7 source conflicts
- 3 missing machine-readable artifact groups

## Migration treatment

### CONF-S8-001 — duplicate hierarchy branches

Migration interpretation:

- pages `2883653` and `2785403` are the primary L4 S8 source pair
- the later branch under folder `2457604` is treated as gap-closure/review material
- no second canonical S8 standard is created

Status: `migration_interpretation_applied`

### CONF-S8-002 — conflicting layer assignments

Repository treatment follows the TIVERIT GitHub object architecture:

- normative S8 standard -> L4 standard
- executable process/workflow -> L5 workflow
- user/tool instruction -> L6 instruction
- concrete registry/configuration/data artifact -> L7 registry/configuration
- source scaffolds whose layer semantics do not cleanly match the canonical architecture remain migration evidence until transformed into a concrete governed object

Status: `curator_review_required` for any future promotion of scaffold objects.

### CONF-S8-003 — built-in Revit parameters vs Shared Parameter Registry

Existing canonical Shared Parameters governance excludes built-in Revit parameters from the Shared Parameter Registry. Sheet Number, Sheet Name, and Project Name may remain required project/titleblock information but are not represented as shared-parameter GUID registry entries unless a distinct custom shared parameter is explicitly governed.

Status: `migration_rule_applied`

### CONF-S8-004 — unresolved semantic owner roles

`AVLC Lead` and `FM Lead` remain unresolved role hooks. No governed IDs are invented. The semantic-domain registry preserves these owner functions as unresolved.

Status: `source_data_required`

### CONF-S8-005 — incomplete tables and placeholders

Missing repository links, checker/script references, managed CDE paths, and unpopulated canonical-module links are not copied as canonical configuration.

Status: `source_data_required`

### CONF-S8-006 — unpopulated source traceability index

The source traceability row is incomplete. GitHub relationships are built directly from explicit source relationships rather than treating the incomplete table row as authority.

Status: `migration_interpretation_applied`

### CONF-S8-007 — Shared Parameter Registry namespace collision

The current migrated registry retains ID `TIVERIT-BIM-STD-S4-SP-REG-001` because that is the already established migration candidate. S8 source evidence clearly places Shared Parameter governance under S8.3 and identifies the First Citizen Set as an implementation of that semantic layer.

The architectural question remains whether the registry should be renamed into an S8 namespace or keep its current identifier with S8 module membership and explicit S8 relationships.

Status: `curator_review_required`

## Missing artifacts

The following source-described artifacts do not exist as complete machine-readable artifacts in BST and are not invented during migration:

- authoritative central Shared Parameter master registry source corresponding to `SPR-CORE`
- classification registry artifacts `CLS-SYS` and `CLS-MAP`
- concrete asset/lifecycle schema definitions corresponding to the S8.5/S7 handover scaffolds

## Shared Parameters integration

The existing Shared Parameters vertical slice is treated as an operational child of S8:

S8 L4 semantic standard
→ Shared Parameters L4 governance standard
→ Shared Parameter Registry L5 workflow
→ Shared Parameter L7 registry/data

The relationship does not make S8 the owner of Revit-specific implementation details; it establishes S8 as the semantic authority for parameter meaning, consistency, classification, and lifecycle data structure.

## Authority status

All migrated S8 objects remain `migration_candidate`. Nothing in this review promotes S8 or its implementation artifacts to active authority before repository cutover.
