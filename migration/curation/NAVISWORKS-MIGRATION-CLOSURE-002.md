# Navisworks Migration Closure — Round 002

Date: 2026-10-31

## Decision

The object-level Navisworks migration is complete. Remaining unresolved values are project/configuration inputs rather than missing migration objects.

## Source reconciliation

Eight Confluence source objects were reconciled against current repository authority:

- **JSON - Navisworks Export Settings (8093711):** migrated into `TIVERIT-BIM-INS-REVIT-NAVIS-EXPORT-001`.
- **S5 – Navisworks Project Setup for Coordination (8126475):** migrated into `TIVERIT-BIM-STD-S5-NAVISWORKS-PROJECT-SETUP-001` and the Navisworks coordination workflow.
- **S5 – Navisworks Clash Detection Matrix – Standard Setup (6324279):** migrated into the Navisworks clash-matrix field registry, clash-rule registry, and coordination workflow.
- **Navisworks Federation & Coordination Standards (10944513):** draft/TODO source. Mature federation and coordinate principles are represented by the project-setup standard, S6 coordinate governance, and Navisworks conformance tests. Exact software toggles and unresolved values were not promoted.
- **Metadata and Export Settings for Navisworks (8159247):** merged into the existing Revit-to-Navisworks export instruction; proposed profiles remain unresolved configuration evidence.
- **ACC Model Coordination vs Navisworks – Clash & Issue Workflows (6357084):** system-of-record, issue traceability, meeting, verification and sign-off boundaries are integrated into the Navisworks workflow and existing S5/S7 authority. Draft tool-preference language was not promoted.
- **Metadata and Deliverables Standards for Navisworks (7864324):** source output taxonomy is represented in `TIVERIT-S7-NAVISWORKS-OUTPUT-TYPES-001`; formal deliverable/record status remains governed by S7 rather than by file format.
- **Gaps in Navisworks (6357099):** retained as historical gap evidence; all seven gap categories now have explicit repository dispositions.

## Historical gap closure

1. **Human-readable export governance** — covered by the migrated export instruction and rendered repository output.
2. **Deliverables and handover outputs** — output types are registered; formal deliverable/record classification is governed by S7 and project exchange/records requirements.
3. **Coordination meetings / sign-off** — integrated into `TIVERIT-BIM-WF-S5-NAVISWORKS-COORDINATION-001`; Navisworks supports technical review but does not create acceptance authority.
4. **Federation & coordinates** — covered by the Navisworks project-setup standard, S6 shared-coordinate governance, and federation integrity conformance.
5. **QA / reporting / auditability** — covered by setup validation, evidence requirements, system-of-record traceability, and two abstract Navisworks conformance tests.
6. **Navisworks-specific roles & responsibilities** — no new tool-specific role created. Existing Project BIM Coordinator and Project BIM Manager roles already govern coordination execution, issue lifecycle, readiness evidence, and sign-off responsibilities without duplicating authority.
7. **Navisworks ↔ ACC / CDE interaction** — the workflow preserves the project-designated system-of-record boundary and applies ACC-specific synchronization only when ACC is the governed project system.

## New closure objects

- `registries/deliverables/TIVERIT-S7-NAVISWORKS-OUTPUT-TYPES-001.json`
- `conformance/abstract/S5/ATS-S5-NAVISWORKS-FEDERATION-INTEGRITY-001.json`
- `conformance/abstract/S5/ATS-S5-NAVISWORKS-TEMP-TRANSFORM-001.json`
- enriched `workflows/S5/TIVERIT-BIM-WF-S5-NAVISWORKS-COORDINATION-001.json`
- updated `migration/inventory/Navisworks_source_inventory.json`

## Explicitly unresolved — not migration gaps

The following remain intentionally project/configuration-driven:

- exact exporter toggles and exporter-version compatibility;
- project clash tolerances and discipline-pair matrix values;
- project/client-specific CDE paths and retention durations;
- viewpoint naming/redaction rules where not otherwise governed;
- owner/approver assignments that depend on BEP/RACI or appointment context.

These values must be supplied by the applicable project governance or configuration registry before execution; they are not authorized to be invented during migration.

## Authority boundary

Migration completion does not make Navisworks an acceptance authority. Navisworks remains a technical coordination and evidence-generation environment. Formal issue state, exchange, acceptance, sign-off, records, and permitted reliance remain governed by the applicable S5/S7 rules, BEP/RACI, and project-designated system of record.
