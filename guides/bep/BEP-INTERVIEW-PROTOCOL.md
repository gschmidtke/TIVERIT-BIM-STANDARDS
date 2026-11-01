# BEP Interview Protocol

## Purpose

This guide explains how a human or AI should use the governed BEP interview workflow when a user asks to create, complete, review, or update a project BIM Execution Plan.

The governing procedural object is:

`workflows/BEP/TIVERIT-BIM-WF-BEP-INTERVIEW-ASSEMBLY-001.json`

The machine-readable task trigger is:

`TASK-ROUTE-BEP-ASSEMBLY-001` in `registries/system-routing/TIVERIT-SYSTEM-ROUTING-001.json`.

The interview is not a fixed questionnaire to be replayed from the beginning. It is a **gap-driven interaction protocol** and a **guided assembly process**.

It helps the user supply project facts and map them to governed objects. It does not approve the BEP, create contractual obligations, modify standards, or create project authority.

## Trigger

Use this protocol when the user asks for a task such as:

- create a BEP;
- create a BEP with me using the TIVERIT BIM Standards repository;
- write, prepare, or draft a BIM Execution Plan;
- help fill out a BEP;
- prepare a pre-appointment BEP;
- prepare or complete a post-appointment BEP;
- review or update a BEP and resolve missing project data;
- generate a BEP from project documents, contract material, EIR/AIR/PIR information, schedules, model lists, or related project sources.

When the trigger is detected, prefer this governed interview workflow over free-form BEP drafting.

## Required startup sequence

Before asking the user project questions:

1. Read `guides/bep/README.md`.
2. Read `guides/bep/BEP-ASSEMBLY-MAP.md`.
3. Read `workflows/BEP/TIVERIT-BIM-WF-BEP-INTERVIEW-ASSEMBLY-001.json`.
4. Read project sources already supplied by the user.
5. Extract supported project facts from those sources.
6. **Decompose supplied EIR, AIR, PIR, contract material, schedules, model lists, and comparable project sources into every BEP data target and governed dependency they support or constrain.** Do not treat an EIR or other requirements source as one monolithic interview answer.
7. Retain source-to-target traceability including source reference, supported or constrained target, governing object/dependency when known, and evidence state.
8. Compare the known project state with the data required for the requested BEP type and maturity.
9. Build a gap queue containing only unresolved, contradictory, ambiguous, authority-insufficient, or insufficiently evidenced project information.
10. Ask only from that gap queue.

Do not generate a full BEP first and then back-fill questions. The interview exists to establish a sufficiently explicit project state before assembly.

## Core interaction rule

A question exists to resolve a required project-data gap. It is not asked merely because it appears in a question catalogue.

```text
required BEP information
        ↓
known from project evidence?
    yes             no
     ↓               ↓
 continue        eligible question
```

If the project source already supplies a valid answer, reuse it and retain source traceability.

If the project source and user answer conflict, do not silently choose one. Surface the conflict and request or identify the authority needed to resolve it.

A supplied requirements source may answer or constrain several later interview topics. For example, an EIR may establish or constrain LOIN/LOD/LOI, naming overlays, exchange versions, parameter requirements, software/interoperability conditions, delivery milestones, or acceptance routes. Those targets shall be populated or constrained during source decomposition before the question queue is generated.

## Interview behavior

The interview should normally ask one bounded question at a time.

The AI may accept natural conversation rather than demanding exact form fields. It should normalize the answer into project-instance data only when the answer is sufficiently clear.

Supported conversational events include:

- answer;
- clarification;
- challenge;
- correction;
- help request;
- deferral;
- restart request;
- temporary off-topic discussion.

Clarification or challenge does not reset accepted answers. A correction updates the affected project fact and triggers re-validation of dependent content.

### Normalization confirmation

Formatting-only normalization may be accepted without a confirmation round.

If normalization changes or selects meaning, scope, granularity, interpretation, authority implication, or dependency, echo the normalized interpretation to the user and obtain confirmation before storing it as an accepted project fact.

Example: if a supplied date range could mean either the overall programme window or a phase-specific delivery window, do not silently choose one interpretation.

### Per-answer validation

After each answer or correction, validate it against the applicable governed object(s), project evidence, dependencies, and validation rules before updating project state.

Do not postpone all validation until final assembly. If an answer exposes a cross-topic conflict, missing authority, or dependency, make that state visible while the interview is still active and route the affected datum accordingly.

## Role and authority deferral

If the current user cannot authoritatively answer a required question, do not force an answer and do not invent one.

Every deferred item shall record:

- topic/question;
- required project datum;
- reason for deferral;
- BEP section affected;
- required responder or approval authority, when known;
- dependency or source needed, when known.

Unknown routing metadata remains explicitly unknown; it is not fabricated merely to complete the record.

The BEP may still be drafted with the item clearly marked unresolved where that is appropriate to the requested stage.

## Project facts versus governed rules

Keep these classes separate during the interview:

1. **Governed repository rule** — what the standards require or permit.
2. **Project fact** — a value supported by the contract, project source, appointed person, or user.
3. **Proposal** — a suggested project choice awaiting approval.
4. **Deviation candidate** — a proposed departure from a governed standard.
5. **Unresolved item** — required information not yet supplied or supported.
6. **Deferred item** — required information intentionally routed to another responder, authority, or source.
7. **Conflict** — incompatible project evidence or requirements awaiting resolution.

Never convert a proposal, deviation candidate, unresolved item, deferred item, or conflict into a confirmed project fact merely to complete the document.

## Validation result semantics

Use the governed result classes distinctly:

- **pass** — available evidence establishes that the applicable requirement is satisfied;
- **unresolved** — a determination cannot yet be made because required information, evidence, dependency, or authority is incomplete;
- **gap** — required content, evidence, dependency, or project definition is absent or incomplete, but available evidence does not establish nonconformance;
- **fail** — available evidence establishes nonconformance with an applicable governed requirement.

Do not collapse `unresolved` or `gap` into `fail`. A gap or unresolved item can reduce approval/readiness without itself proving nonconformance.

When presenting a BEP quality result, make these states reader-visible so a reviewer can distinguish incomplete project definition from demonstrated nonconformance.

## Question-to-output contract

Each interview topic should connect six things:

```text
question / missing datum
        ↓
project-state target
        ↓
governing object(s)
        ↓
validation
        ↓
BEP output section
        ↓
remaining gap / approval state
```

The initial governed question catalogue is embedded in `TIVERIT-BIM-WF-BEP-INTERVIEW-ASSEMBLY-001` and covers appointment context, project identity, roles/authority, information requirements, model progression and authorized use, delivery planning, CDE, software, federation/coordinates, coordination/QA, exchanges/deliverables, information structure, external interfaces, and deviations.

Future questions should normally extend the catalogue or a governed subordinate catalogue without changing the overall architecture.

## Closing project-instance data sweep

Before assembly, run one bounded closure pass over unresolved project-instance data.

For each unresolved datum that the current user could reasonably answer, provide one direct opportunity to answer it. This is a closure opportunity, not a requirement to eliminate every unresolved state.

Do not:

- force an answer;
- silently default an unanswered value;
- re-ask a formally deferred item when its responder, evidence, or dependency has not changed;
- convert an unresolved value into an assumption;
- treat the closure pass as approval.

Items still unresolved after the closure pass remain in the unresolved/deferred register and remain visible in the assembled BEP.

## Completion condition

The interview is complete when each datum required for the requested BEP state is one of:

- supported and captured;
- explicitly unresolved after the applicable closure opportunity;
- formally deferred with the required deferral record;
- identified as a conflict requiring resolution;
- recorded as a deviation candidate.

Interview completion does **not** mean BEP approval.

## Assembly

After the interview reaches a complete state:

1. assemble the BEP using `BEP-ASSEMBLY-MAP.md`;
2. reference governed object IDs;
3. populate project-instance tables under `templates/project/`;
4. mark proposals, unresolved values, deferred items, conflicts, and deviations explicitly;
5. produce a governing-object reference register;
6. produce an unresolved/deferred-item register;
7. run the workflow validation rules using the governed `pass` / `unresolved` / `gap` / `fail` semantics;
8. present the resulting BEP as a draft/review package unless approval is independently evidenced.

## Minimum operational checks

An AI or other interview implementation claiming to follow this protocol should be able to demonstrate all of the following:

1. **Requirements-source decomposition:** when an EIR or comparable source governs several downstream values, those values are mapped before the corresponding questions are asked.
2. **Question suppression:** a sufficiently evidenced project datum is not asked again merely because its catalogue question exists.
3. **Complete deferral:** a deferred answer retains topic/question, datum, reason, affected BEP section, and known routing/dependency information.
4. **Material-normalization confirmation:** an ambiguous or materially transformed answer is confirmed before acceptance.
5. **Per-answer validation:** a conflict, missing authority, or dependency exposed by an answer is surfaced before final assembly rather than discovered only in the finished draft.
6. **Closure sweep:** unresolved answerable project facts receive one bounded final opportunity before assembly, while unchanged formal deferrals are not mechanically replayed.
7. **Result-state clarity:** `unresolved` and `gap` are not reported as `fail` unless evidence establishes nonconformance.
8. **No authority invention:** interview completion, software selection, coordination sign-off, or document assembly does not create acceptance authority or approve the BEP.

Failure of an implementation to demonstrate these behaviors is execution/conformance evidence and should not be repaired by inventing project facts or duplicating governance rules.

## Provenance

This protocol preserves the durable interaction concepts from Confluence source pages 5832715, 6160402, 6225931, 6553603, and 14090241 while removing source-era organization-specific runtime, role-code, tool, and precedence assumptions.

The operational refinements for requirements-source decomposition, complete deferral records, validation-result semantics, bounded pre-assembly closure, material-normalization confirmation, and visible per-answer validation were curated from STAR-T-GATE Inbox #4 and are governed by `TIVERIT-BIM-WF-BEP-INTERVIEW-ASSEMBLY-001`.