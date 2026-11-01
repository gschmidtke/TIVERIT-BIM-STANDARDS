# TIVERIT BIM Standards Repository Architecture

## Object-oriented repository

The repository does not reproduce the Confluence page tree. Canonical content is organized by governance function and object type.

```text
constitution/      L1-L3 authority, doctrine, architecture
standards/         L4 governed normative standards
workflows/         L5 executable workflows/processes
instructions/      L6 tool and user instructions
configurations/    L7 presets and machine payloads
registries/        governed controlled vocabularies and indexes
modules/           S1-S9 semantic module manifests
engine/            automation engines that consume governed data
schemas/           JSON Schema definitions
conformance/       test contracts, executable checks, fixtures, evidence schemas
bridges/           external interoperability projections such as IDS/bSDD/IFC
render/            generators and templates for human/AI publication
dist/              generated distributions, reports, and exchange artifacts
provenance/        immutable source traceability
migration/         migration mappings, gaps, and review artifacts
archive/           non-canonical historical material
inbox/             curator staging/recovery and historical provenance; not public entry
```

Public proposal intake is external to this repository through the STAR-T-GATE Inbox route declared in `STAR-T-GATE.json`. The STAR-T-GATE Worker records submissions in `gschmidtke/STAR-T-GATE-INBOX` as uncurated evidence; repository-local `inbox/` content does not become authoritative by being stored or merged.

## Standards ecosystem planes

The repository operates as four coordinated planes. These planes describe the system role of an artifact and are separate from both governance layer and S1-S9 domain.

### 1. Normative plane

Defines what must, must not, should, or may be true. The normative plane contains constitutional doctrine, standards, workflows, instructions, configurations, and governed registries. Only this plane establishes repository authority.

### 2. Conformance plane

Defines how compliance is demonstrated. Conformance artifacts reference stable normative requirement IDs but do not redefine them.

The conformance chain is:

```text
REQ-*  normative requirement
  ↓
ATS-*  abstract test specification
  ↓
ETS-*  executable test specification / implementation binding
  ↓
evidence
  ↓
PASS / FAIL / NOT_APPLICABLE / INDETERMINATE
```

An abstract test defines the evidence and pass/fail logic without depending on a specific application. Executable tests bind an abstract test to a concrete implementation such as Revit/ZEN, IFC, Solibri, ACC APIs, scripts, or a governed human verification procedure.

`FIX-*` fixture objects sit beside, not inside, the execution chain. They define controlled positive, negative, not-applicable, and indeterminate cases used to prove that an ETS implementation produces the expected result and evidence behavior.

Tool-specific executable logic must not be embedded into L4 normative standards merely because the requirement is machine-checkable.

### 3. Interoperability plane

Projects governed TIVERIT requirements into external machine-readable formats such as IDS, bSDD mappings, IFC mappings, or future exchange standards.

External formats are derived representations, not alternate sources of authority. If a bridge artifact conflicts with the normative source, the normative source governs.

### 4. Publication plane

Produces human- and AI-consumable views from canonical machine-readable content. Markdown, HTML, PDF, role-specific manuals, AI context packages, reports, and similar outputs are generated representations and are not edited as parallel standards.

The governing principle is:

**Author once; project many representations.**

## Three independent coordinates

Every governed artifact is understood through three independent questions:

1. **Domain — S1-S9:** what governance subject does this belong to?
2. **Layer — L1-L7:** at what level of authority or implementation does it operate?
3. **System role:** is it normative, conformance, interoperability, publication, or migration/support material?

Folder location may express a primary function, but it does not replace metadata or governed relationships.

## Layer model

The L1-L7 layer is a governance coordinate carried by normative-plane objects. Conformance, interoperability, and publication artifacts use their own system-role contracts rather than pretending to occupy a normative governance layer.

## Module model

S1-S9 are semantic coordinates. An object may belong to multiple modules. Module membership is therefore stored as metadata rather than inferred exclusively from file paths.

## Conformance architecture

### Requirement ownership

Normative requirements remain owned by their governing standard. Conformance objects only reference requirement IDs.

Example:

```text
REQ-S6-COORD-003
  normative owner: S6
  statement: coordination file contains no physical modeled elements

ATS-S6-COORD-003
  defines evidence and pass/fail semantics

ETS-S6-COORD-003-REVIT
  binds the ATS to a Revit/ZEN implementation

FIX-S6-COORD-003-PASS / FAIL / INDETERMINATE
  verify that the implementation behaves as specified
```

A second ETS may implement the same ATS for IFC or another platform without changing the normative requirement.

### Abstract test specification (ATS)

An ATS should define, at minimum:

- stable ATS ID
- referenced requirement ID
- test intent
- applicability conditions
- required evidence
- pass condition
- fail condition
- not-applicable condition where relevant
- indeterminate/error condition where relevant
- permitted implementation classes
- provenance and lifecycle metadata

ATS objects must remain tool-neutral unless the normative requirement itself is explicitly tool-specific.

### Executable test specification (ETS)

An ETS should define, at minimum:

- stable ETS ID
- referenced ATS ID
- implementation/tool binding
- supported versions or capability constraints
- input contract
- execution method or callable implementation reference
- evidence output contract
- failure/error behavior
- implementation state
- provenance and lifecycle metadata

An ETS may exist in `specified_not_implemented` state. Such an ETS defines the executable contract but must not be represented as operational until its callable implementation and fixture verification exist.

Executable implementations may inspect or enforce governed requirements but may not create new authority or silently modify the meaning of the referenced requirement.

### Conformance fixtures

A fixture is a controlled regression case for an ETS. Fixtures must reference a real ETS and define an expected result plus the evidence assertions that must be observed.

Fixture classes are:

- `positive` — expected `pass`
- `negative` — expected `fail`
- `not_applicable` — expected `not_applicable`
- `indeterminate` — expected `indeterminate`

Synthetic fixtures define expected behavior but are not production evidence. Real model files or other binary test assets may later be associated with fixture objects where needed.

### Evidence

Evidence is an observation or result produced by an ETS or governed human verification. Evidence is not approval by itself.

Evidence should preserve at minimum:

- requirement ID
- ATS ID
- ETS ID or human verification method
- subject/container identity
- observation timestamp
- observed values or findings
- result state
- implementation/version identity
- traceable evidence artifact references

Acceptance and reliance remain governed by the applicable S1/S5/S7 authority rules.

### Conformance result states

The baseline result vocabulary is:

- `pass`
- `fail`
- `not_applicable`
- `indeterminate`

`indeterminate` means the requirement could not be evaluated reliably; it must never be silently converted to `pass`.

## Interoperability architecture

`bridges/` contains mappings and generators from TIVERIT canonical requirements into external formats. A bridge should record which requirement IDs it represents and any loss of expressiveness.

Examples:

```text
bridges/ids/
bridges/bsdd/
bridges/ifc/
```

IDS is expected to be most suitable for structured information requirements such as entity, property, classification, datatype, and value constraints. Geometry or application-state requirements may require executable conformance implementations instead.

## Publication architecture

`render/` contains generation logic and templates. `dist/` contains generated outputs only.

```text
canonical JSON
  ├─> Markdown / HTML
  ├─> PDF/manual views
  ├─> role-specific views
  ├─> AI context packages
  ├─> reports
  └─> external exchange artifacts
```

Generated output must be reproducible from canonical content and must not become an independent editing surface for normative requirements.

## Requirement maturity model

The roadmap uses a maturity scale to describe how far a requirement has progressed beyond prose:

- `M0` — human prose only
- `M1` — structured requirement with stable ID
- `M2` — machine-readable relationships and semantics
- `M3` — abstract conformance test exists
- `M4` — at least one executable verification is implemented and fixture-verified
- `M5` — interoperability projection exists where appropriate
- `M6` — automated evidence-producing governance is operational

A specified-but-not-implemented ETS does not by itself advance a requirement to M4.

Not every requirement is expected to reach M6. Some governance and professional-judgment requirements may appropriately remain human-verifiable.

## Canonical object envelope

Canonical normative JSON objects share a common envelope defined by `schemas/base-object.schema.json`:

- `id`
- `legacy_ids`
- `type`
- `title`
- `status`
- `version`
- `effective_date`
- `supersedes`
- `superseded_by`
- `authority`
- `layer`
- `modules`
- `scope`
- `relationships`
- `verification`
- `provenance`

Object identity and object version are separate dimensions. The stable `id` persists across governed revisions. `version` records the governed content revision, while `effective_date` records when that revision becomes authoritative. Migration candidates and drafts may omit those lifecycle values while source reconciliation is incomplete; an object cannot be promoted to `active` unless both `version` and `effective_date` are present and valid.

Non-normative planes use dedicated schemas that preserve lifecycle, domain, provenance, and reference integrity without falsely assigning L1-L7 normative authority.

## Identifier namespaces

Repository identity is governed by a controlled namespace taxonomy rather than by one literal prefix. `TIVERIT-*` remains the primary repository namespace. Typed families such as `ROLE-*`, `REG-*`, `REQ-*`, `GAP-*`, `REL-*`, `LNK-*`, `AUT-*`, and `MIG-*` are permitted only for their declared semantic object classes. `ATS-*` and `ETS-*` are reserved for abstract and executable conformance specifications. `FIX-*` is reserved for governed conformance regression fixtures. `BIM-STD-*` is retained only for explicitly curator-approved specialist standard identities. `W-*` is a migration/source workflow namespace pending normalization and is not preferred for new canonical workflows.

New namespace families require curator approval and validator registration.

## Reference integrity

Canonical cross-references are validated against IDs present in the repository. References to governed objects that are not yet migrated must be declared individually in `migration/reference-forward-declarations.json` with a rationale. Wildcard exemptions are not permitted. When a referenced object is migrated or a stale source reference is repaired, its forward declaration must be removed.

Reference fields also reject structured identifier-like values whose namespace is not governed. This prevents a misspelled or invented prefix from bypassing referential validation merely because it fails the known-prefix matcher.

Conformance-specific references are also validated directly: ATS objects must resolve to real requirements, ETS objects must resolve to real ATS objects, and FIX objects must resolve to real ETS objects.

## Migration rule

Confluence remains source authority during migration. GitHub objects are `migration_candidate` until reviewed and promoted.

Historical traceability is retained through neutral source metadata such as Confluence page IDs, versions, and source links.
