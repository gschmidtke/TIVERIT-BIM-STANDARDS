# S3 Migration Review

Status: migration candidate. No new curator decisions are asserted by this document.

Integrated architecture:
- TIVERIT-BIM-STD-S3-PROD-EP001 is the parent S3 production-environment/CDE governance standard.
- CDE information states, folder architecture, platform permissions, records/retention, and ACC onboarding remain separate machine-readable objects.
- S3 provides the governed CDE/container infrastructure consumed by S5 and S7.
- S2 governs required information, delivery timing, and permitted use; S8 governs semantic structure and metadata carriers.

Open curator conflicts:
1. ACC internal system of record versus contract-designated client CDE as contractual/legal source of truth.
2. Detailed 00_Admin / 10_WIP / 20_Shared / 30_Published / 40_Coordination hierarchy versus earlier three-subfolder layout.
3. Information Manager, Project BIM Manager, and CDE Manager all hold Project Administrator capability; no technical privilege split is invented.
4. Tool-neutral doctrine versus ACC-specific implementation remains unresolved.
5. TODO scaffold content is not promoted.

Provenance hygiene:
S3_source_pages.json was not committed because raw titles, URLs, and breadcrumbs contain retired naming. Canonical objects use neutral page-ID provenance only.

No new S3 curator decision has been accepted yet. The Shared Parameter Registry namespace decision remains parked separately.
