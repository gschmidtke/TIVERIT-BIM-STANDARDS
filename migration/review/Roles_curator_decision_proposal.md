# Roles Curator Decisions

Status: accepted in curator review on 2026-10-28.

These decisions are approved for migration implementation. They define how the role registry and individual role-definition objects are to be generated. Role objects remain `migration_candidate` until validation and repository cutover; acceptance here resolves the identified governance conflicts for migration purposes.

## Accepted decisions

### CONF-ROLE-001 — BIM Coordinator identifier

**Decision:** `ROLE-PROJECT-BIM-COORDINATOR-001` is the canonical project role. `ROLE-BIM-COORDINATOR-001` is treated as an earlier scaffold identifier superseded for project coordination use.

### CONF-ROLE-002 — BIM Manager identifier

**Decision:** `ROLE-PROJECT-BIM-MANAGER-001` is the canonical project role. `ROLE-BIM-MANAGER-001` is retired as an obsolete generic scaffold identifier. Enterprise governance remains with `ROLE-BIM-DIRECTOR-001`; standards custody remains with `ROLE-BIM-STANDARDS-MGR-001`.

### CONF-ROLE-005 — Information Manager / Project BIM Manager / CDE Manager

**Decision:** Preserve three distinct governed functions:

- `ROLE-PROJECT-BIM-MANAGER-001` — project information-governance authority and BIM execution governance.
- `ROLE-INFORMATION-MANAGER-001` — information-requirements and information-management oversight where the project or appointment explicitly requires that function.
- `ROLE-CDE-MANAGER-001` — technical platform administration, onboarding, configuration, and permissions implementation.

Project Admin permission overlap is platform capability, not role equivalence. One person may hold more than one role where project organization permits it.

### CONF-ROLE-006 — Generic vs granular Discipline Leads

**Decision:** Use an inheritance/specialization model.

`ROLE-DISCIPLINE-LEAD-001` is the abstract/base governed role containing common discipline-lead authority and responsibilities. Granular roles inherit the base role and add domain-specific scope.

The generic role is not used as a substitute when a governed granular role exists.

### CONF-ROLE-007 — Issue lifecycle authority

**Decision:** Use delegated, tiered closure authority.

- Project BIM Manager owns the project issue-governance framework and retains final governance authority.
- Project BIM Coordinator may close routine coordination and QA issues where predefined acceptance criteria are met.
- Issue Owner owns administrative tracking and lifecycle progression.
- Responsible Party owns the technical correction.
- Governance exceptions, disputed closures, milestone-critical items, and matters outside delegated thresholds escalate to Project BIM Manager.

A future issue-severity/closure-threshold matrix is required for full machine-checkability.

### CONF-ROLE-008 — Discipline Lead vs Design Lead approval

**Decision:** Separate technical/documentation readiness from design/package approval.

- Discipline Lead approves discipline BIM/model readiness, technical correctness within discipline scope, and documentation suitability.
- Design Lead approves integrated design/package content for design intent and design-delivery release.
- Project leadership retains contractual acceptance/release authority where applicable.

CDE permission level does not define professional authority; it constrains available platform actions.

### CONF-ROLE-009 — Pre-publish QA gate

**Decision:** Adopt tiered gatekeeping.

- QA/QC Authority defines acceptance criteria and validation evidence requirements.
- BIM Detailer executes governed pre-publish checks and may reject a model/package that fails objective checklist criteria.
- Project BIM Coordinator governs the pre-publish workflow and validates readiness for federation/share/publish states.
- Project BIM Manager retains project governance authority above the operational gate.

The BIM Detailer determines readiness against defined checks and does not receive contractual or governance acceptance authority.

## Decisions intentionally deferred for insufficient evidence

### CONF-ROLE-003 — Technical PM

Keep as unresolved external organizational role reference. No governed role ID is created yet.

### CONF-ROLE-004 — Production Manager

Keep as unresolved external/adjacent delivery-role reference. No governed role ID is created yet.

### CONF-ROLE-010 — AVLC Lead / FM Lead

Do not create dedicated governed roles from the current evidence.

- `AVLC Lead` remains unresolved pending an organizational decision on whether it denotes the Technical Director, a cluster of discipline leads, or a dedicated role.
- `FM Lead` remains unresolved pending definition as an internal information role or an external client/facility-operator role.

## Additional unresolved reference

`IT / Network Lead` remains an unresolved interface role because the source contains no governed definition or role ID.

## Implementation instruction

The accepted decisions above are now the authority for generating the migration-candidate role definitions, aliases/supersession relationships, inheritance relationships, and cross-reference rules in `REG-ROLE-001`. Individual role objects remain non-active until schema validation, cross-reference validation, and formal repository cutover are complete.
