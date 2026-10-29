# Conformance Plane

The `conformance/` tree defines how normative TIVERIT BIM Standards requirements are evaluated. It does not create or modify normative authority.

## Core chain

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

## Directory contract

```text
conformance/
  abstract/       tool-neutral abstract test specifications (ATS)
  executable/     tool/platform implementation bindings (ETS)
  fixtures/       governed test inputs and expected outcomes
  evidence/       evidence schemas and result contracts
```

Directories should be created when their first governed artifact is added; empty placeholder authority is not required.

## Authority boundary

- Normative requirements remain owned by `standards/` or other normative-plane objects.
- ATS objects define how a requirement can be proven without depending on one software implementation.
- ETS objects implement an ATS for a specific tool or capability.
- Evidence records observations and result states.
- Evidence is not approval or acceptance by itself.
- S1/S5/S7 continue to govern authority, review, acceptance, reliance, and sign-off.
- S9 governs tool and automation authority; an executable checker cannot become normative merely because it can run automatically.

## Abstract Test Specification (ATS)

An ATS should contain at least:

- stable `ATS-*` ID
- referenced `REQ-*` ID
- test intent
- applicability criteria
- required evidence
- pass condition
- fail condition
- `not_applicable` condition where relevant
- `indeterminate` condition where relevant
- permitted implementation classes
- lifecycle/provenance information

An ATS should be tool-neutral unless the requirement being tested is itself explicitly tool-specific.

## Executable Test Specification (ETS)

An ETS should contain at least:

- stable `ETS-*` ID
- referenced `ATS-*` ID
- implementation/tool binding
- supported versions or capability constraints
- input contract
- execution/callable reference
- evidence output contract
- error and indeterminate behavior
- lifecycle/provenance information

Multiple ETS implementations may satisfy the same ATS. For example, one ATS may have a Revit/ZEN implementation and an IFC implementation.

## Evidence contract

Conformance evidence should preserve, at minimum:

- normative requirement ID
- ATS ID
- ETS ID or governed human verification method
- tested subject/container identity
- observation timestamp
- observed values or findings
- result state
- implementation/version identity
- references to retained evidence artifacts

Baseline result states are:

- `pass`
- `fail`
- `not_applicable`
- `indeterminate`

`indeterminate` must never be silently treated as `pass`.

## First pilot

The first conformance pilot should use a small set of source-backed, already-migrated requirements rather than attempt full-corpus automation. Candidate domains are S4 identity/naming, S6 linking/shared coordinates, and S8 parameters/semantics.

No pilot ATS or ETS is canonical until its referenced requirement, evidence logic, and implementation behavior have been reviewed under repository governance.
