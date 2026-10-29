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

### D-11 — Canonical cross-platform container identity grammar
**Decision:** The seven-token hyphen-delimited BEP/ISO-style pattern `{proj}-{originator}-{volume/system}-{level/location}-{type}-{role}-{number}.{ext}` is the canonical cross-platform container identity grammar. The ACC underscore filename scheme is retained only as an implementation/display mapping and does not establish a second canonical identity grammar.

**Rationale:** Container identity must remain portable across authoring, CDE, coordination, exchange, manufacturing, and future platform contexts rather than being defined by one platform implementation.

### D-12 — Scoped discipline-code namespaces
**Decision:** Discipline-code namespaces may coexist by governed scope. Enterprise/container identity uses the 3–4 letter discipline namespace. Tool-internal Revit view, sheet, family, or similar object naming may use compact/single-letter discipline codes only where the governing tool instruction explicitly defines that local namespace.

**Rationale:** The two code schemes serve different naming surfaces. Scoped coexistence preserves existing tool conventions without allowing local abbreviations to redefine enterprise container identity.

### D-13 — Stable root identity; revision and status are metadata dimensions
**Decision:** Suitability/status and revision are removed from canonical root container identity. They remain governed, mutable metadata/revision dimensions associated with the stable container identity. Platform filenames may display or carry these values only as derived implementation labels where required; changing status or revision shall not redefine the root identity.

**Rationale:** Identity must persist across lifecycle transitions. Treating mutable revision or suitability as root identity would fragment history and risk broken references.

### D-14 — Standalone Coordination File belongs to S6
**Decision:** `BIM-STD-CF-001` is canonically owned by S6. S5 consumes its verified spatial output for coordination intake but does not own the spatial-authority standard.

**Rationale:** The artifact's primary function is governance of shared coordinates, master datums, and model onboarding alignment, which is core S6 scope.

### D-15 — Coordinate authority flows outward from the coordination file
**Decision:** Discipline models consume/acquire the approved spatial framework from `BIM-STD-CF-001`. Peer-to-peer coordinate publication is not treated as an equivalent governance path.

**Rationale:** A single directional authority path prevents circular coordinate authority and uncontrolled spatial drift.

### D-16 — Tool-neutral S6 doctrine; tool-specific mechanics remain implementation-layer
**Decision:** S6 L4 remains tool-neutral. Revit Central/Local mechanics, worksets, and specific shared-coordinate commands are retained as L6 implementation instructions rather than universal L4 requirements.

**Rationale:** Tool-independent governance must define required outcomes and authority boundaries without making one authoring application's mechanics universal.

### D-17 — Federation responsibilities split by governance owner
**Decision:** S6 owns spatial alignment, link relationships, and federation prerequisites. S5 owns clash/review/sign-off activity. S3 owns CDE storage, folder state, and platform administration.

**Rationale:** Federation-related source material crosses several governance domains; separating responsibilities prevents duplicated or conflicting authority.

## Earlier accepted role decisions

Role-specific curator decisions remain recorded in `migration/review/Roles_curator_decision_proposal.md` and continue to govern role migration.
