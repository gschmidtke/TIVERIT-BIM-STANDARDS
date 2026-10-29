# S1 / S9 Migration Review

## Status

S1 and S9 are migrated as `migration_candidate` objects. This review separates source fact, migration treatment, and unresolved governance issues. No object in this package is promoted to `active` by this migration.

## S1 — Core BIM Standards & Governance

### Source facts

- S1 is the governance foundation for the BIM standards system.
- The source divides S1 into three stable areas: Standards vs BEP, Roles/Responsibilities/Authority, and Information Management Principles.
- The source states that reusable standards govern non-project-specific rules while BEPs contain project-specific execution conditions and reference the standards.
- The source states that authority is a governance decision and must not be inferred from technical location or execution behavior.
- The source identifies gaps around contractual precedence, permitted reliance/suitability, role/RACI coverage, information-state reliability, and model-use taxonomy.

### Migration treatment

- `TIVERIT-BIM-STD-S1-CORE-GOV-EP001` is the L4 parent governance standard.
- `TIVERIT-BIM-STD-S1-ROLES-001` instantiates the source role/authority scaffold and references the existing governed role registry `REG-ROLE-001`.
- Source gaps for permitted use and information-state reliability are treated as addressed by migrated S2/S7 governance, subject to final cross-check at cutover.
- The role/RACI gap is treated as partially addressed: role definitions and authority statements exist, but complete cross-role authority coverage has not yet been proven.

### Unresolved S1 issues

- `GAP-S1-CONTRACT-PRECEDENCE-01`: no contractual order-of-precedence rule is invented. The source explicitly identifies this as missing.
- `GAP-S1-ROLE-AUTHORITY-COVERAGE-01`: a complete organization-wide role/RACI authority coverage test remains outstanding.
- `GAP-S1-MODEL-USE-TAXONOMY-01`: required vs optional model uses by phase/stakeholder remain unresolved.
- The separate constitutional object referenced historically is not created by this migration; the current repository governance/architecture remains the higher repository-level governance layer until a distinct constitutional object is deliberately curated.

## S9 — Authoring, Automation & Manufacturing Toolchains

### Source facts

- S9 governs tool legitimacy, authority boundaries, interoperability, and automation behavior.
- Tools do not acquire authority through convenience, popularity, legacy use, or technical capability.
- Automation is an execution layer, not an authority layer.
- Automation that affects governed information must be documented, repeatable, versioned, governed, and auditable.
- The source contains product-specific candidate mappings for BIM authoring, manufacturing, electrical/controls authoring, and constrained documentation.
- Two source governance gaps are explicit: a governed Automation Registry and a Tool Authority Matrix.

### Migration treatment

- `TIVERIT-BIM-STD-S9-TOOLS-AUTHORITY-EP001` is the L4 parent standard.
- `REG-S9-AUTOMATION-001` implements the source-defined Automation Registry scaffold as a machine-readable migration candidate.
- `REG-S9-TOOL-AUTHORITY-001` implements the Tool Authority Matrix scaffold as a machine-readable migration candidate.
- Both registries intentionally contain no approved production entries.
- Product-specific mappings found in the parent source are retained only as migration candidates until explicitly governed in the Tool Authority Registry.
- Tool configuration, UI procedures, deployment mechanics, and application-specific instructions remain downstream implementation-layer content.

### Unresolved S9 issues

- `GAP-S9-01`: registry structure now exists, but concrete automation assets, approval status, risk classification, owners, evidence requirements, and production allow-list state remain unpopulated.
- `GAP-S9-02`: registry structure now exists, but authoritative tool assignments by information domain remain unapproved.

## Cross-module boundaries

- S1 owns governance and authority principles.
- S2 owns information demand, suitability, and permitted use.
- S3 owns production environments, hosting, permissions implementation, and CDE/platform configuration.
- S4 owns identity and naming.
- S5 owns coordination, review, and internal readiness/sign-off mechanics.
- S6 owns collaboration, link relationships, and shared spatial authority.
- S7 owns formal exchange, submission, acceptance, and handover states.
- S8 owns semantic structure, parameters, classification, and governed information carriers.
- S9 owns tool legitimacy, tool-domain authority mapping, interoperability constraints, and automation governance.

## Automation consequence

S9 establishes the critical separation required for executable governance: automation may inspect, validate, transform, repair, or execute governed rules, but it does not own those rules and cannot create acceptance authority. This permits tools such as validators and governed add-ins to execute standards without becoming policy sources.
