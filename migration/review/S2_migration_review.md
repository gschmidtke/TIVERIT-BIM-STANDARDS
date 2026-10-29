# S2 Information Requirements — Migration Review

Status: migration candidate review record.

## Source structure

The source corpus contains an older EP-001 baseline branch and a more mature review/production branch. The migration keeps one canonical S2 parent object and migrates the mature standalone L4 standards separately rather than duplicating folder-tree history.

## Migrated L4 standards

- `TIVERIT-BIM-STD-S2-INF-REQ-EP001`
- `TIVERIT-BIM-STD-S2-PIR-001`
- `TIVERIT-BIM-STD-S2-AIR-001`
- `TIVERIT-BIM-STD-S2-MIDP-001`
- `TIVERIT-BIM-STD-S2-TIDP-001`
- `TIVERIT-BIM-STD-S2-LOD-LOI-001`
- `TIVERIT-BIM-STD-S2-SEL-GOV-001`
- `TIVERIT-BIM-STD-S2-PARAM-SP-GOV-001` (already migrated)

## S2 → S8 boundary

S2 defines information demand, purpose, timing, reliance, and delivery requirements. S8 provides semantic structure and technical carriers including parameters, classification, and asset/lifecycle schemas.

The source explicitly supports these dependencies:

- S2 core demand informs S8 information structures.
- Shared Parameter governance is S2 policy; S8 GAP-S8-01 provides registry/carrier implementation.
- AIR feeds the S8 asset/lifecycle schema scaffold.
- LOD/LOI drives classification and non-graphical carrier requirements.
- PIR drives project-information parameter demand.
- SEL drives instance-level parameter binding needs.

## Conflicts and gaps retained

### CONF-S2-001 — competing hierarchy branches

Older EP-001 and later mature/review branches coexist. Migration resolves folder duplication structurally without claiming source supersession.

### CONF-S2-002 — Shared Parameters dual governance residence

The Shared Parameter policy object is explicitly S2 while its registry implementation is an S8 responsibility. Migration preserves this as a policy-versus-carrier separation.

### CONF-S2-003 — missing OIR standalone standard

OIR is in S2 scope but no standalone governed OIR L4 object exists in BST. No `TIVERIT-BIM-STD-S2-OIR-001` is invented.

### CONF-S2-004 — EIR distributed implementation

EIR is in scope but is implemented through BEP/pre-appointment and delivery-core assets rather than a standalone S2 L4 standard. No missing standard is fabricated.

### CONF-S2-005 — MIDP/TIDP layer ambiguity

MIDP and TIDP remain L4 governed standards. Runtime MIDP/TIDP records in the BEP engine are treated as downstream dynamic data structures.

### CONF-S2-006 — draft lifecycle state

Standalone production standards remain `migration_candidate` because their Confluence source metadata is draft/unratified.

### CONF-S2-007 — unresolved external roles

`Client / Owner` and `FM Lead / FM Function` remain unresolved external/adjacent role references and are not assigned invented role IDs.

## Naming enforcement

Raw source files containing retired organization naming are not committed. Neutral provenance uses page IDs, versions, sections, and TIVERIT-only generated content.
