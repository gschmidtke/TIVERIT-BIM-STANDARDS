# BEP Interview Protocol

## Purpose

This guide explains how a human or AI should use the governed BEP interview workflow when a user asks to create, complete, or review a project BIM Execution Plan.

The governing procedural object is:

`workflows/BEP/TIVERIT-BIM-WF-BEP-INTERVIEW-ASSEMBLY-001.json`

The interview is not a fixed questionnaire to be replayed from the beginning. It is a **gap-driven interaction protocol**.

## Trigger

Use this protocol when the user asks for a task such as:

- create a BEP;
- prepare a pre-appointment BEP;
- prepare or complete a post-appointment BEP;
- review a BEP and fill its missing project data;
- generate a BEP from project documents, contract material, EIR/AIR/PIR information, schedules, model lists, or related project sources.

## Required startup sequence

Before asking the user project questions:

1. Read `guides/bep/README.md`.
2. Read `guides/bep/BEP-ASSEMBLY-MAP.md`.
3. Read `workflows/BEP/TIVERIT-BIM-WF-BEP-INTERVIEW-ASSEMBLY-001.json`.
4. Read project sources already supplied by the user.
5. Extract supported project facts from those sources.
6. Compare the known project state with the data required for the requested BEP type and maturity.
7. Ask only for unresolved, contradictory, or insufficiently evidenced project information.

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

## Role and authority deferral

If the current user cannot authoritatively answer a required question, do not force an answer and do not invent one.

Record the item as deferred with:

- topic/question;
- required project datum;
- reason for deferral;
- required responder or approval authority if known;
- dependency or source needed;
- BEP section affected.

The BEP may still be drafted with the item clearly marked unresolved where that is appropriate to the requested stage.

## Project facts versus governed rules

Keep these classes separate during the interview:

1. **Governed repository rule** — what the standards require or permit.
2. **Project fact** — a value supported by the contract, project source, appointed person, or user.
3. **Proposal** — a suggested project choice awaiting approval.
4. **Deviation candidate** — a proposed departure from a governed standard.
5. **Unresolved item** — required information not yet supplied or supported.

Never convert a proposal or unresolved item into a confirmed project fact merely to complete the document.

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

## Completion condition

The interview is complete when each datum required for the requested BEP state is one of:

- supported and captured;
- explicitly unresolved;
- formally deferred;
- identified as a conflict requiring resolution;
- recorded as a deviation candidate.

Interview completion does **not** mean BEP approval.

## Assembly

After the interview reaches a complete state:

1. assemble the BEP using `BEP-ASSEMBLY-MAP.md`;
2. reference governed object IDs;
3. populate project-instance tables under `templates/project/`;
4. mark proposals, unresolved values, and deviations explicitly;
5. produce a governing-object reference register;
6. produce an unresolved/deferred-item register;
7. run the workflow validation rules;
8. present the resulting BEP as a draft/review package unless approval is independently evidenced.

## Provenance

This protocol preserves the durable interaction concepts from Confluence source pages 5832715, 6160402, 6225931, 6553603, and 14090241 while removing source-era organization-specific runtime, role-code, tool, and precedence assumptions.
