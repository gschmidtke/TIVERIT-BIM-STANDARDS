# S3 Migration Review

Status: migration candidate. Curator decisions D-08, D-09, and D-10 accepted on 2026-10-29.

Integrated architecture:
- `TIVERIT-BIM-STD-S3-PROD-EP001` is the parent S3 production-environment/CDE governance standard.
- CDE information states, folder architecture, platform permissions, records/retention, and ACC onboarding remain separate machine-readable objects.
- S3 provides the governed CDE/container infrastructure consumed by S5 and S7.
- S2 governs required information, delivery timing, and permitted use; S8 governs semantic structure and metadata carriers.

Accepted curator decisions:
1. **D-08 — System of record by scope.** ACC is the internal coordination/production system of record. Where the contract/BEP explicitly designates a client CDE as the contractual/legal source of truth, that external system governs contractual submission status. This is a scope split, not a contradiction.
2. **D-09 — Project Administrator capability.** Information Manager, Project BIM Manager, and CDE Manager remain three distinct governed roles even where all three require ACC Project Administrator capability. Platform capability does not imply equivalent professional/governance authority.
3. **D-10 — Folder hierarchy.** The canonical migration-candidate `/02_Design_and_Coordination` hierarchy is `00_Admin / 10_WIP / 20_Shared / 30_Published / 40_Coordination`. The earlier three-subfolder scheme is superseded for migration implementation.

Remaining S3 source conditions:
- Tool-neutral doctrine versus ACC-specific implementation is preserved as doctrine-versus-implementation layering, not flattened.
- TODO scaffold content is not promoted.

Provenance hygiene:
`S3_source_pages.json` was not committed because raw titles, URLs, and breadcrumbs contain retired naming. Canonical objects use neutral page-ID provenance only.
