# Reasoning Stack Routing Doctrine

## Purpose

The TIVERIT BIM Standards repository occupies the **normative authority layer** between resolved intent and operational production logic.

Its role is not to determine project purpose and not to teach every production technique. Its role is to define what is required or permitted, who has authority, and what evidence demonstrates compliance.

## Stack position

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

## Repository responsibilities

### USG
Public repository: https://github.com/gschmidtke/USG

Owns resolution of human need into a software-neutral specification of the required built outcome before tool or representation choices are made.

Primary question: **What are we trying to achieve, and why?**

### TIVERIT BIM Standards
Public repository: https://github.com/gschmidtke/TIVERIT-BIM-STANDARDS

Owns normative BIM governance, including requirements, prohibitions, permitted practices, authority boundaries, compliance criteria, and evidence expectations.

Primary question: **What must or may be true, who may decide, and what proves compliance?**

### ARPL
Public repository: https://github.com/gschmidtke/ARPL

Owns curated operational production precedent for Revit: techniques, failures, corrections, and verification of production outcomes.

Primary question: **How has this been done successfully before, what failed, and how was the result verified?**

## Routing rules

1. If the inquiry is about unresolved purpose, required outcome, performance intent, or success criteria before BIM/tool representation, route to USG.
2. If the inquiry is about BIM requirements, governance, roles, permissions, acceptance, naming, information structure, coordination, linking, delivery, or compliance, route to TIVERIT BIM Standards.
3. If the inquiry is about how to implement a professional Revit task, known production techniques, API behavior, recurring failure modes, or operational proof, route to ARPL.
4. If the inquiry spans layers, resolve in order: purpose → normative constraint → operational precedent → technical capability → execution → validation.
5. Never infer normative authority from technical capability or prior success.
6. Never treat ARPL precedent as permission to violate a governing standard.
7. Never treat a Standards rule as a substitute for unresolved project purpose.
8. Never let observed execution success substitute for validation against both purpose and standard.

## Conflict handling

If the layers disagree:

- Purpose vs Standard: stop and escalate; intent does not override governance automatically.
- Standard vs ARPL: the Standard governs; ARPL must adapt or be marked incompatible/deprecated for that context.
- ARPL vs API capability: investigate implementation alternatives or record the new failure mode.
- API success vs observed result: observed professional outcome governs validation; successful execution alone is insufficient.

## Learning boundary

Operational learning may propose a standards change, but it cannot amend normative authority directly.

```text
Observation
   ↓
ARPL operational learning
   ↓
Repeated or material contradiction
   ↓
Standards amendment proposal
   ↓
Curator review
   ↓
Governed Standards change
```

This separation preserves three distinct knowledge classes:

- **USG:** resolved intent and purpose.
- **TIVERIT BIM Standards:** normative authority.
- **ARPL:** operational precedent.

Each class must redirect inquiries outside its authority to the repository that owns them.
