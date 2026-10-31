# S8 Information Structure, Parameters & Classification — Migration Review

Status: migration candidate review

## Source authority

The primary S8 source pair is Confluence page `2883653` (machine-readable L4) and page `2785403` (human-readable L4). Later S8 review material remains gap-closure evidence rather than a replacement standard.

## Migration treatment

### CONF-S8-001 — duplicate hierarchy branches
Primary L4 source pair retained; later branch treated as review/gap-closure material.

### CONF-S8-002 — conflicting layer assignments
Repository treatment follows canonical layers: L4 standard, L5 workflow, L6 instruction, L7 registry/configuration.

### CONF-S8-003 — built-in Revit parameters
Built-in Revit parameters are excluded from the Shared Parameter Registry unless a distinct custom shared parameter is explicitly governed.

### CONF-S8-004 — unresolved semantic owner roles
`AVLC Lead` and `FM Lead` remain unresolved role hooks.

### CONF-S8-005 — incomplete tables/placeholders
Incomplete links, checker references, paths, and TODOs are not promoted.

### CONF-S8-006 — incomplete source traceability index
Explicit source relationships are used rather than incomplete scaffold rows.

### CONF-S8-007 — Shared Parameter Registry namespace
Curator decision D-01 accepted on 2026-10-29: the canonical migration-candidate registry identifier is `TIVERIT-BIM-STD-S8-SP-REG-001`. The former S4-style identifier is retained only as migration lineage on the registry object, not as a live cross-reference.

Status: `curator_resolved`

## Missing artifacts

- authoritative central Shared Parameter master registry source corresponding to `SPR-CORE`
- classification registry artifacts `CLS-SYS` and `CLS-MAP`
- concrete asset/lifecycle schema definitions corresponding to the S8.5/S7 handover scaffolds

## Shared Parameters integration

S8 L4 semantic standard → Shared Parameters L4 governance standard → Shared Parameter Registry L5 workflow → S8-aligned Shared Parameter L7 registry/data.

S8 is semantic authority for parameter meaning, consistency, classification, and lifecycle structure; it does not own tool-specific UI implementation.

## Authority status

All migrated S8 objects remain `migration_candidate`. Nothing is promoted to active authority before repository cutover.
