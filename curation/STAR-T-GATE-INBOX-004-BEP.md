# Curator record — STAR-T-GATE Inbox #4

Status: curated change candidate
Curator: Zara / ChatGPT
Source: `gschmidtke/STAR-T-GATE-INBOX#4`
Target: `STANDARDS`
Primary governed object: `workflows/BEP/TIVERIT-BIM-WF-BEP-INTERVIEW-ASSEMBLY-001.json`
Companion guide: `guides/bep/BEP-INTERVIEW-PROTOCOL.md`

## Curation principle

Inbox material is evidence or proposal, not authority merely because it was submitted. Each observation was checked against the current BEP workflow and protocol before deciding whether it represents a governance gap, a machine-readability gap, or execution/conformance evidence.

## Accepted changes

### 1. Project-source decomposition before questioning

**Decision:** accept and normalize.

The existing workflow already requires project sources to be loaded and already-supported facts to be extracted before questioning. The refinement is to make decomposition explicit: supplied EIR/AIR/PIR, contract material, schedules, model lists, and comparable project sources shall be mapped to every dependent BEP project-data target they govern or constrain before the gap queue is created.

This prevents an EIR from being treated as one monolithic `BEP-Q-004` answer when it also determines or constrains LOIN/LOD/LOI, naming, exchanges, information structure, software/interoperability, acceptance routes, and other downstream project data.

**Intended workflow refinement:** strengthen `BEP-WF-02`/`BEP-WF-03` so source extraction produces both known facts and a source-to-target dependency map before `BEP-WF-04` creates the gap queue.

### 2. Machine-readable deferral record

**Decision:** accept.

The companion protocol already requires a deferred item to record:

- topic/question;
- required project datum;
- reason for deferral;
- required responder or approval authority if known;
- dependency or source needed;
- affected BEP section.

The workflow JSON currently names `deferred` in the project-state model without restating this structure. This is a machine-readability gap, not a new policy requirement.

**Intended workflow refinement:** add a `deferral_record` definition to the workflow JSON and require every formally deferred item to contain those six fields.

### 3. Validation-result semantics

**Decision:** accept.

The workflow uses `unresolved`, `gap`, and `fail` as validation outcomes but does not define their reader-facing semantics. Add the following semantics:

- `pass`: available evidence establishes that the applicable requirement is satisfied.
- `unresolved`: a determination cannot yet be made because required information, evidence, dependency, or authority is incomplete.
- `gap`: required content, evidence, dependency, or project definition is absent or incomplete, but available evidence does not establish nonconformance.
- `fail`: available evidence establishes nonconformance with an applicable governed requirement.

These result classes shall not be silently collapsed into a generic failure state. A `gap` or `unresolved` result affects readiness and must remain visible, but is not evidence of nonconformance by itself.

### 4. Pre-assembly unresolved-data closure pass

**Decision:** partial accept.

The current completion condition legitimately permits explicitly unresolved and formally deferred data. That rule remains unchanged. However, before assembly, unresolved project-instance data that the current user could reasonably answer should be presented once for a direct answer opportunity.

The closure pass shall not force answers, re-ask formally deferred questions whose dependency has not changed, or convert unresolved values into assumptions. Items that remain unresolved continue into the unresolved/deferred register.

### 5. Material normalization confirmation

**Decision:** accept.

The current protocol permits natural-language answers to be normalized into project-instance data. Add a distinction between formatting normalization and material normalization:

- formatting-only normalization may be accepted without confirmation;
- normalization that changes meaning, scope, granularity, interpretation, authority implication, or dependency shall be echoed to the user for confirmation before it becomes an accepted project fact.

## Not promoted as new governance

### Interim validation checkpoints

**Decision:** do not add a redundant new validation checkpoint.

`BEP-WF-06` already requires every answer to be validated against governing objects, project evidence, dependencies, and applicable validation rules before project state is updated. Therefore the Inbox observation that validation occurs only at final assembly is not correct as a description of the governed workflow.

Retain this observation as execution/conformance evidence: an external AI failed to make the already-governed per-answer validation behavior visible or effective. This evidence may justify future improvements to clarity, testability, or conformance checks, but does not justify duplicating the rule.

## Curated implementation target

The intended repository change is deliberately narrow:

1. strengthen source decomposition in `BEP-WF-02`/`BEP-WF-03`;
2. add machine-readable deferral-record fields;
3. add validation-result semantics;
4. add a pre-assembly unresolved-data closure pass before assembly;
5. add material-normalization confirmation behavior;
6. preserve `BEP-WF-06` as the existing per-answer validation mechanism rather than adding redundant interim validation.

No Inbox statement is promoted directly to normative authority by this record. The workflow remains `migration_candidate`; the actual workflow edit must be validated against repository schemas and local curator rules before promotion or merge.
