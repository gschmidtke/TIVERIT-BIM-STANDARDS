# Curator Decision Log

This log records accepted curator decisions that alter migration treatment or canonical repository architecture. All affected objects remain `migration_candidate` until repository cutover.

## 2026-10-29

### D-01 — Shared Parameter Registry namespace
**Decision:** Rename the Shared Parameter Registry to the S8-aligned canonical migration identifier `TIVERIT-BIM-STD-S8-SP-REG-001` and repair all live cross-references.

**Rationale:** S2 governs information demand; S8 governs semantic structure and parameter carriers. The registry is an S8 implementation artifact.

### D-08 — System of record by scope
**Decision:** ACC is the internal production/coordination system of record. Where the project contract or BEP explicitly designates a client CDE as the contractual/legal source of truth, that external system governs contractual submission status.

**Rationale:** Internal operational authority and contractual record authority are separate scopes.

### D-09 — Project Administrator capability
**Decision:** Information Manager, Project BIM Manager, and CDE Manager remain three distinct governed roles even where each requires Project Administrator capability in ACC.

**Rationale:** Platform capability does not establish professional, contractual, or governance authority. Capability and authority are separate dimensions.

### D-10 — Canonical S3 folder hierarchy
**Decision:** Adopt `00_Admin / 10_WIP / 20_Shared / 30_Published / 40_Coordination` under `/02_Design_and_Coordination` as the canonical migration-candidate hierarchy. The earlier three-subfolder layout is superseded for migration implementation.

**Rationale:** The detailed hierarchy aligns container state, coordination, publishing, and downstream S5/S7 workflows.

## Earlier accepted role decisions

Role-specific curator decisions remain recorded in `migration/review/Roles_curator_decision_proposal.md` and continue to govern role migration.
