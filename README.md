# TIVERIT BIM Standards

TIVERIT BIM Standards is a governed, machine-readable BIM standards repository for human use, automation, validation, AI-assisted workflows, Revit, Autodesk Construction Cloud, and related BIM systems.

## Position in the reasoning stack

This repository is the **normative governance layer** between resolved purpose and operational production logic.

```text
USG
Problem / purpose / required resolution
    ↓
TIVERIT BIM Standards
Normative requirements / authority / compliance evidence
    ↓
ARPL
Operational precedent / Revit production logic / failure memory
    ↓
Capability lookup / tool API
    ↓
Execution
    ↓
Observed evidence
    ↓
Validation against purpose + standard
```

Public repositories:

- USG — https://github.com/gschmidtke/USG — resolves what must be achieved and why before tool selection.
- TIVERIT BIM Standards — https://github.com/gschmidtke/TIVERIT-BIM-STANDARDS — defines what is required or permitted, who has authority, and what evidence proves compliance.
- ARPL — https://github.com/gschmidtke/ARPL — records how professional Revit production tasks have been executed, what failed, and how successful results were verified.

An AI or human inquiry should be routed to the repository that owns the question. If an inquiry spans layers, use the order **purpose → normative constraint → operational precedent → technical capability → execution → validation**. See `AGENTS.md`, `constitution/architecture/REASONING-STACK-ROUTING.md`, and `registries/system-routing/TIVERIT-SYSTEM-ROUTING-001.json`.

## BEP assembly entry point

For creating or reviewing a BIM Execution Plan (BEP), do not reverse-engineer the repository from S1–S9 manually. Start with:

- `guides/bep/README.md` — BEP consumption rules and migration-status handling;
- `guides/bep/BEP-ASSEMBLY-MAP.md` — deterministic S1→S9 read order and BEP section packing map;
- `templates/project/` — non-normative starter tables for project inputs, LOIN, RACI, MIDP, software/version lock, and federation/coordinates.

The BEP consumption layer separates **governed rules** from **project/contract facts**. Missing project values must remain `TBC`, `TBD`, `not supplied`, or an explicitly labeled proposal requiring approval; they must not be inferred from a standard.

During migration, Confluence remains source authority until formal cutover. GitHub objects marked `migration_candidate` are the current normalized drafting source on the migration branch and should be used for drafting with that status preserved.

## Standards ecosystem

The S1–S9 backbone is the normative plane of a larger standards ecosystem. The repository is intended to distinguish four system roles:

```text
                         PURPOSE / INTENT
                              USG
                               │
                               ▼
                    TIVERIT BIM STANDARDS
                         NORMATIVE PLANE
     constitution → standards → workflows → instructions
                  → configurations → registries
                               │
                 stable requirement identifiers
                               │
             ┌─────────────────┼─────────────────┐
             ▼                 ▼                 ▼
       CONFORMANCE       INTEROPERABILITY     PUBLICATION
       ATS / ETS         IDS / bSDD / IFC     MD / HTML / PDF
       fixtures          mappings             AI views
       evidence          generators           reports
             │                 │                 │
             └─────────────────┼─────────────────┘
                               ▼
                       execution / checking
                         ZEN / AI / APIs
                               │
                               ▼
                           evidence
                               │
                               ▼
                              ARPL
                 operational precedent / failure memory
```

The four planes have different authority:

- **Normative** — defines what must, must not, should, or may be true. This is the authoritative standards corpus.
- **Conformance** — defines how compliance is demonstrated. It may include abstract test specifications, executable tests, fixtures, and evidence schemas, but it does not redefine the requirement.
- **Interoperability** — projects governed requirements into external formats such as IDS, bSDD, or IFC mappings. These projections do not become alternate sources of authority.
- **Publication** — generates human- and AI-readable views from the canonical corpus. Generated documents are derived outputs, not independently authored standards.

The repository therefore follows the principle **author once; project many representations**.

## Governance coordinates

Repository objects are understood through three independent coordinates:

1. **Domain — S1–S9:** what governance subject the object belongs to.
2. **Layer — L1–L7:** at what governance abstraction the object operates.
3. **System role:** whether the object is normative, conformance, interoperability, publication, or migration support.

The S1–S9 backbone is:

```text
S1  Governance / Authority
S2  Information Requirements
S3  Production Environment
S4  Identity / Naming / Structure
S5  Coordination / Review / Sign-Off
S6  Collaboration / Linking / Shared Coordinates
S7  Submission / Deliverables / Handover
S8  Information Structure / Parameters / Classification
S9  Tool / Automation Authority
```

## Ecosystem roadmap

The repository will evolve in six stages. Stages are architectural maturity steps, not permission to bypass curator governance.

### Stage 1 — Normative foundation

Complete and reconcile the S1–S9 backbone, roles, workflows, registries, implementation instructions, provenance, version lifecycle, and referential integrity. Every normative requirement should have a stable requirement ID, authority level, verification classification, provenance, relationships, and governed status.

### Stage 2 — Ecosystem architecture

Formalize the four-plane model and establish structural contracts for:

```text
conformance/
  abstract/
  executable/
  fixtures/
  evidence/

bridges/
  ids/
  bsdd/
  ifc/

render/
  generators/
  templates/

dist/
  human/
  ids/
  machine/
  reports/
```

These structures must not be populated with invented placeholder authority merely to fill directories.

### Stage 3 — Abstract conformance

Connect machine-checkable and machine-assisted requirements to tool-neutral Abstract Test Specifications (ATS).

```text
REQ-S6-COORD-003
        ↓
ATS-S6-COORD-003
```

The requirement defines **what must be true**. The ATS defines **what evidence would prove it**. The ATS remains independent of Revit, ZEN, Solibri, IFC, or any other execution environment.

### Stage 4 — Executable conformance

Implement selected ATS rules as executable test specifications (ETS) using appropriate tools and APIs.

```text
requirement
    ↓
abstract test
    ↓
executable implementation
    ↓
evidence
    ↓
conformance result
```

ZEN, Revit APIs, IFC checkers, Solibri, ACC APIs, AI-assisted inspection, or human verification may implement a conformance test. None of them defines the underlying standard.

The first pilot should use a small set of high-value requirements from S4, S6, and S8, such as naming, workset structure, link registration, shared-coordinate conditions, coordination-file content, and governed parameter consistency.

### Stage 5 — Interoperability bridges

Project suitable requirements into external standards and checking ecosystems.

```text
TIVERIT requirement
        ↓
controlled mapping
        ↓
IDS / bSDD / IFC representation
        ↓
external checker or consuming system
```

S2 and S8 information requirements are strong candidates for IDS-based exchange. Geometry- or behavior-dependent checks remain in appropriate executable conformance implementations rather than being forced into an unsuitable bridge format.

### Stage 6 — Generated publication

Generate human- and AI-readable products from the canonical machine-readable corpus.

```text
canonical JSON
    ├── Markdown
    ├── HTML
    ├── PDF/manual
    ├── role-specific views
    ├── project extracts
    └── AI context packages
```

Human-readable outputs in `dist/` are disposable projections. Canonical content is edited at its governed source object, then regenerated.

## Requirement maturity

Requirement maturity should eventually be measurable independently of module-completion percentages.

```text
M0 — human prose only
M1 — structured requirement with stable ID
M2 — machine-readable relationships and semantics
M3 — abstract conformance test exists
M4 — at least one executable verification exists
M5 — interoperability projection exists where appropriate
M6 — evidence-producing automated governance
```

Not every requirement should reach the same maturity level. Some governance decisions remain legitimately human-verifiable. The maturity model exists to make automation readiness visible rather than to force all governance into code.

## Recommended implementation sequence

1. Maintain and reconcile the S1–S9 normative backbone.
2. Formalize the four-plane architecture and repository contracts.
3. Continue migration of the Revit implementation family into the correct L6/L7 structures.
4. Select a small pilot set of S4/S6/S8 requirements.
5. Create tool-neutral ATS objects for those requirements.
6. Implement the first ZEN/Revit executable checks and evidence results.
7. Define reusable evidence/result schemas.
8. Generate the first human-readable standard view directly from canonical JSON.
9. Create a small IDS bridge from suitable S2/S8 requirements.
10. Scale only after the full requirement → test → execution → evidence → publication chain is proven.

The long-term objective is a standards ecosystem in which each inquiry can answer:

```text
What governs this?
How can it be verified?
Can it be projected into an external standard?
How is it published for humans and AI?
What system may execute or inspect it?
What evidence comes back?
```

## Governance model

This repository separates public contribution from canonical authority.

- `inbox/` is the future public contribution surface.
- Canonical standards, schemas, registries, workflows, instructions, configurations, and engine content are curator-controlled.
- Public contribution does not directly modify canonical authority.
- Promotion from `inbox/` into canonical content requires curator review, validation, and an explicit governed change.

During the repository build and migration phase, the repository remains public so the architecture can be inspected and refined openly.

## Source migration

The initial corpus is being migrated from the TIVERIT BIM Standards Confluence space. The migration inventory preserves the existing S1–S9 modular framework, the repository L1–L7 governance architecture, role definitions, workflows, registries, machine-readable assets, and BEP automation components.

## Canonical namespaces

Canonical repository-owned identifiers use a controlled namespace taxonomy. `TIVERIT-*` is the primary namespace; typed semantic families such as `ROLE-*`, `REG-*`, `REQ-*`, and other explicitly governed prefixes are permitted for their defined object classes. New namespace families require curator approval and validator registration. See `GOVERNANCE.md` for the authoritative namespace policy.

Historical traceability is preserved through neutral Confluence page IDs, versions, and source links.

## Core principle

The repository is object-oriented rather than page-oriented. It distinguishes constitutional and external authority, normative standards, workflows, tool/user instructions, configurations and presets, registries, conformance assets, interoperability bridges, generated publications, automation/engine components, and source provenance.

## Status

Repository foundation and schema v0.1 are under construction. Confluence remains the source authority during migration until the canonical GitHub corpus is validated and formally cut over. S1–S9 now exist as the normative backbone on the migration branch; implementation, conformance, interoperability, and generated publication layers remain under development.
