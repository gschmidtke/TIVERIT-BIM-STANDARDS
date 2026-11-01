# BEP Consumption Guide

This guide is the project-deliverable consumption layer for assembling a BIM Execution Plan (BEP) from the governed repository.

It does **not** create new standards, project facts, appointments, contractual requirements, or acceptance authority. It tells a human or AI which governed objects to consult, which project facts must be supplied externally, and which project-instance tables must be completed rather than invented.

## How to start with an AI

A user may simply say something like:

> Create a BEP with me using the TIVERIT BIM Standards repository.

That request should trigger the governed BEP interview workflow rather than immediate free-form drafting.

**Mandatory interview consumption rule:** before asking substantive project questions, the AI shall read `guides/bep/BEP-INTERVIEW-PROTOCOL.md` together with `BEP-ASSEMBLY-MAP.md` and `workflows/BEP/TIVERIT-BIM-WF-BEP-INTERVIEW-ASSEMBLY-001.json`. The protocol is the human/AI operational interpretation of the machine-readable workflow and shall not be skipped merely because the workflow JSON has been loaded.

The AI should first inspect the conversation and supplied project sources, decompose requirements sources into the downstream BEP data they support or constrain, reuse already-supported facts, then guide the user through only the remaining project-data gaps. The interview normally proceeds one bounded question at a time until the required information is captured, explicitly unresolved, formally deferred, identified as a conflict, or recorded as a deviation candidate.

During the interview, materially normalized interpretations must be confirmed, every answer must be validated as it is accepted, and deferrals must preserve the complete governed deferral record. Before assembly, the AI runs the bounded project-instance closure sweep defined in `BEP-INTERVIEW-PROTOCOL.md`. Validation results must preserve the distinction between `pass`, `unresolved`, `gap`, and `fail`.

The interview is a guide for assembling a BEP. It does not approve the BEP, create contractual obligations, alter standards, or create project authority. The resulting BEP remains a draft/review package unless approval is independently evidenced.

For the machine-readable task route, see `TASK-ROUTE-BEP-ASSEMBLY-001` in `registries/system-routing/TIVERIT-SYSTEM-ROUTING-001.json`.

## Purpose

Use this guide when the task is:

- prepare a pre-appointment or post-appointment BEP;
- review a BEP against TIVERIT BIM Standards;
- assemble project-specific roles, CDE rules, naming, coordination, delivery planning, software, federation, LOIN, MIDP/TIDP, or responsibility information;
- determine which missing values are project inputs rather than repository gaps.

## Drafting status during migration

Confluence remains source authority until formal cutover. Canonical-shaped GitHub objects marked `migration_candidate` are the current normalized drafting source on the migration branch and should be used for BEP drafting with their status preserved. They must not be represented as formally cut-over authority until governance changes that status.

When a project fact is missing, write `TBC`, `TBD`, `not supplied`, or an equivalent unresolved state. Do not substitute general industry practice and do not infer contractual commitments.

## Assembly sequence

Use `BEP-ASSEMBLY-MAP.md` in this folder. The recommended order is:

1. collect project facts and appointment context;
2. resolve governance and role authority from S1;
3. resolve information demand, LOIN and delivery planning from S2;
4. resolve CDE / production environment from S3;
5. resolve identity and naming from S4;
6. resolve coordination/review/sign-off from S5;
7. resolve collaboration, federation, linking and coordinates from S6;
8. resolve exchanges, deliverables and reliance from S7;
9. resolve parameters/classification/semantics from S8;
10. resolve software and automation authority from S9;
11. populate project-instance tables from `templates/project/`;
12. identify unresolved contractual/project inputs explicitly;
13. generate the BEP as a project document that references governed object IDs rather than restating standards as a competing source.

## Project-input starter tables

The following files are non-normative starter structures:

- `templates/project/bep-project-inputs.csv`
- `templates/project/loin-template.csv`
- `templates/project/raci-template.csv`
- `templates/project/midp-starter.csv`
- `templates/project/software-lock-template.csv`
- `templates/project/federation-coordinates-template.csv`

Their column structures are intended to reduce assembly friction. Rows are project data and must be supplied or approved by the project authority.

## Authority rule

A BEP should **reference and instantiate** standards; it should not silently redefine them.

If a project needs a deviation from a governed standard, record the deviation, approving authority, reason, scope, and effective period. Do not edit the governing standard merely to make the BEP internally consistent.
