# Conformance Plane

The `conformance/` tree defines how governed TIVERIT BIM Standards objects are evaluated. It does not create or modify normative authority.

## Core chain

For normative requirements:

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

For governed implementation instructions, the same conformance chain may target the instruction explicitly:

```text
TIVERIT-BIM-INS-*  governed L6 instruction
  ↓
ATS-*              abstract proof contract for a stated instruction clause
  ↓
ETS-*              tool/platform implementation binding
  ↓
evidence
  ↓
PASS / FAIL / NOT_APPLICABLE / INDETERMINATE
```

`FIX-*` objects sit beside these chains as governed regression fixtures. They test whether an ETS implementation produces the expected result and evidence behavior for controlled cases.

## Directory contract

```text
conformance/
  abstract/       tool-neutral abstract test specifications (ATS)
  executable/     tool/platform implementation bindings (ETS)
  fixtures/       governed regression cases and expected outcomes
  evidence/       evidence schemas and result contracts
```

Directories should be created when their first governed artifact is added; empty placeholder authority is not required.

## Authority boundary

- Normative requirements remain owned by `standards/` or other normative-plane objects.
- L6 instructions remain implementation authority only within their governed scope; testing an instruction does not promote it above its parent standards.
- ATS objects define how a governed requirement or explicit instruction clause can be proven without depending on one software implementation.
- ETS objects bind an ATS to a specific tool or capability.
- FIX objects test ETS behavior but are not production evidence.
- Evidence records observations and result states.
- Evidence is not approval or acceptance by itself.
- S1/S5/S7 continue to govern authority, review, acceptance, reliance, and sign-off.
- S9 governs tool and automation authority; an executable checker cannot become normative merely because it can run automatically.

## Abstract Test Specification (ATS)

An ATS should contain at least:

- stable `ATS-*` ID
- one machine-resolvable `governing_object_id` identifying the canonical governed object that owns the tested rule
- `requirement_id` when the ATS tests a specific normative requirement within that governing object
- optional `governing_clause` when only a bounded step/clause of the governing object is tested
- test intent
- applicability criteria
- required evidence
- pass condition
- fail condition
- `not_applicable` condition where relevant
- `indeterminate` condition where relevant
- permitted implementation classes
- lifecycle/provenance information

`governing_object_id` is mandatory for every ATS. `requirement_id` is a secondary locator, not a substitute for the governing-object reference. Both identifiers must resolve against the canonical repository ID graph. This keeps requirement-level tests and instruction/clause-level tests machine-routable through one linkage convention.

An ATS should be tool-neutral unless the governed target being tested is itself explicitly tool-specific.

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
- implementation state
- lifecycle/provenance information

Multiple ETS implementations may satisfy the same ATS. For example, one ATS may have a Revit/ZEN implementation and an IFC implementation.

An ETS may be `specified_not_implemented`. In that state it is an executable contract, not proof that production code exists. A governed target reaches executable maturity only when a callable implementation exists and passes its governed fixtures.

## Conformance fixtures

A fixture uses the `FIX-*` namespace and references one ETS. It defines a controlled subject profile, simulated or real observations, an expected result, and expected evidence assertions.

Fixture classes are:

- `positive` → expected `pass`
- `negative` → expected `fail`
- `not_applicable` → expected `not_applicable`
- `indeterminate` → expected `indeterminate`

Synthetic fixtures are specification-level regression cases. They do not replace future real model fixtures or production evidence where those are required.

## Evidence contract

Conformance evidence should preserve, at minimum:

- governing object ID
- governing requirement ID or clause where applicable
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

## First normative pilot

The first pilot spans S4 identity/naming, S6 linking/shared coordinates, and S8 parameters/semantics. Seven ATS objects are present.

Two executable paths demonstrate different maturity states:

```text
REQ-S6-COORD-003
  ↓
ATS-S6-COORD-003
  ↓
ETS-S6-COORD-003-REVIT
  ↓
FIX pass / fail / indeterminate
  ↓
specified_not_implemented
```

This path is ready for a future Revit/ZEN callable but remains M3 until implementation exists and fixtures execute successfully.

```text
REQ-S8-004
  ↓
ATS-S8-PARAM-004
  ↓
ETS-S8-PARAM-004-PYTHON
  ↓
FIX pass / fail / indeterminate
  ↓
CI execution + schema-valid evidence
  ↓
verified
```

`REQ-S8-004` is the first requirement to reach **M4** under the repository maturity model. The Python ETS compares observed shared-parameter identities and structural fields against the governed central Shared Parameter Registry. The CI fixture runner executes governed positive, negative, and unresolved-source cases and fails if implementation behavior diverges from their expected results.

## Appendix E conformance wave

The first Appendix E implementation-conformance wave adds ATS/ETS coverage for six high-value Revit surfaces:

| Surface | ATS | Revit/ZEN ETS | Current state |
| --- | --- | --- | --- |
| Object naming | `ATS-REVIT-NAMING-001` | `ETS-REVIT-NAMING-001-REVIT` | specified, not implemented |
| View templates / display state | `ATS-REVIT-VIEW-TEMPLATE-001` | `ETS-REVIT-VIEW-TEMPLATE-001-REVIT` | specified, not implemented |
| Parameter identity / binding | `ATS-REVIT-PARAM-BINDING-001` | `ETS-REVIT-PARAM-BINDING-001-REVIT` | specified, not implemented |
| Worksets / containment | `ATS-REVIT-WORKSET-001` | `ETS-REVIT-WORKSET-001-REVIT` | specified, not implemented |
| Project-template content | `ATS-REVIT-TEMPLATE-CONTENT-001` | `ETS-REVIT-TEMPLATE-CONTENT-001-REVIT` | specified, not implemented |
| Levels / grids | `ATS-REVIT-DATUM-001` | `ETS-REVIT-DATUM-001-REVIT` | specified, not implemented |

These tests deliberately preserve unresolved governance dependencies. Missing View Template, Template Catalogue, workset-purpose, binding/category, naming-vocabulary, datum-source, transform, or tolerance data produces `indeterminate` rather than an assumed PASS.

No ATS, ETS, or fixture creates approval authority. Production acceptance remains governed by the normative standards and designated roles.
