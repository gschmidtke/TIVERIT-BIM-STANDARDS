# Roles Curator Decision Proposal

Status: proposal only — no role is promoted to active authority by this document.

This review converts the Role Conflict Evidence Pack into explicit curator proposals while preserving unresolved items where the source remains insufficient.

## Proposed decisions supported by source evidence

### CONF-ROLE-001 — BIM Coordinator identifier

**Proposal:** Treat `ROLE-PROJECT-BIM-COORDINATOR-001` as the canonical project role. Treat `ROLE-BIM-COORDINATOR-001` as an earlier scaffold identifier that is superseded for project coordination use.

**Rationale:** The later dedicated JSON definition and narrative define the full project-scoped role and explicitly instruct that the project-scoped role ID be linked into `REG-ROLE-001`.

**Authority status:** proposed curator decision.

### CONF-ROLE-002 — BIM Manager identifier

**Proposal:** Treat `ROLE-PROJECT-BIM-MANAGER-001` as the canonical project role. Retire `ROLE-BIM-MANAGER-001` as an obsolete generic scaffold identifier.

**Rationale:** The registry and detailed narrative establish a single-project scope, while enterprise governance is assigned separately to `ROLE-BIM-DIRECTOR-001` and standards custody to `ROLE-BIM-STANDARDS-MGR-001`.

**Authority status:** proposed curator decision.

### CONF-ROLE-005 — Information Manager / Project BIM Manager / CDE Manager

**Proposal:** Preserve three distinct functions rather than treating them as aliases:

- `ROLE-PROJECT-BIM-MANAGER-001` — project information-governance authority and BIM execution governance.
- `ROLE-INFORMATION-MANAGER-001` — information-requirements and information-management oversight where the project or appointment explicitly requires that function.
- `ROLE-CDE-MANAGER-001` — technical platform administration, onboarding, configuration, and permissions implementation.

Project Admin permission overlap is treated as platform capability, not proof of role equivalence. A project may combine these functions in one person, but the governed role definitions remain distinct.

**Authority status:** proposed curator decision.

### CONF-ROLE-006 — Generic vs granular Discipline Leads

**Proposal:** Use an inheritance/specialization model.

`ROLE-DISCIPLINE-LEAD-001` becomes the abstract/base governed role containing common discipline-lead authority and responsibilities. Granular roles such as Showset, Audio, Video, Controls, SFX, Lighting, Mechanical, and Electrical inherit the base role and add domain-specific scope.

The generic role is not assigned as a substitute when a governed granular role exists.

**Authority status:** proposed curator decision.

### CONF-ROLE-007 — Issue lifecycle authority

**Proposal:** Establish delegated, tiered closure authority.

- Project BIM Manager owns the project issue-governance framework and retains final governance authority.
- Project BIM Coordinator may close routine coordination and QA issues where predefined acceptance criteria are met.
- Issue Owner owns administrative tracking and lifecycle progression.
- Responsible Party owns the technical correction.
- Governance exceptions, disputed closures, milestone-critical items, and matters outside delegated thresholds escalate to Project BIM Manager.

A future issue-severity/closure-threshold matrix is required to make this fully machine-checkable.

**Authority status:** proposed curator decision.

### CONF-ROLE-008 — Discipline Lead vs Design Lead approval

**Proposal:** Separate technical/documentation readiness from design/package approval.

- Discipline Lead approves discipline BIM/model readiness, technical correctness within discipline scope, and documentation suitability.
- Design Lead approves integrated design/package content for design intent and design-delivery release.
- Project leadership retains contractual acceptance/release authority where applicable.

CDE permission level does not define professional authority; it only constrains actions available in the platform.

**Authority status:** proposed curator decision.

### CONF-ROLE-009 — Pre-publish QA gate

**Proposal:** Adopt tiered gatekeeping.

- QA/QC Authority defines acceptance criteria and validation evidence requirements.
- BIM Detailer executes governed pre-publish checks and may reject a model/package that fails objective checklist criteria.
- Project BIM Coordinator governs the pre-publish workflow and validates readiness for federation/share/publish states.
- Project BIM Manager retains project governance authority above the operational gate.

The BIM Detailer determines readiness against defined checks; the role does not grant contractual or governance acceptance authority.

**Authority status:** proposed curator decision.

## Decisions intentionally deferred for insufficient evidence

### CONF-ROLE-003 — Technical PM

No governed role ID or sufficient boundary definition exists. Keep as unresolved external organizational role reference. Do not invent `ROLE-TECHNICAL-PM-001` yet.

### CONF-ROLE-004 — Production Manager

The source establishes a consulted relationship but does not define governed BIM authority. Keep as unresolved external/adjacent delivery-role reference.

### CONF-ROLE-010 — AVLC Lead / FM Lead

Do not create dedicated governed roles from the current evidence.

- `AVLC Lead` remains unresolved until the organization decides whether it means the Technical Director, a cluster of Audio/Video/Lighting/Controls discipline leads, or a dedicated role.
- `FM Lead` remains unresolved until the project/organization defines whether this is an internal information role or an external client/facility-operator role.

## Additional unresolved reference

`IT / Network Lead` remains an unresolved interface role because the source contains no governed definition or role ID.

## Promotion rule

These proposals must not be encoded as active authority until explicitly accepted in curator review. After acceptance, the canonical role registry and individual role-definition objects should be regenerated from the accepted decisions and validated before promotion.
