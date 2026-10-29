# AI Bootstrap — TIVERIT BIM Standards

This repository is public. The full working standards corpus is currently on:

`build/repository-foundation`

`main` is the public governance and discovery entry point during migration. Do not treat the limited content on `main` as evidence that the standards are unavailable.

## Route to the working corpus

For substantive standards work, read these files from `build/repository-foundation`:

1. `AGENTS.md`
2. `registries/system-routing/TIVERIT-SYSTEM-ROUTING-001.json`
3. the task-specific guide, workflow, standard, registry, instruction, configuration, or conformance object identified by that routing.

## BEP assembly trigger

Treat user requests to create, prepare, draft, review, complete, update, or collaboratively build a BIM Execution Plan as task class:

`bep_assembly`

Examples include:

- "Create a BEP with me using the TIVERIT BIM Standards repo."
- "Help me prepare a post-appointment BEP."
- "Review and complete this BEP using TIVERIT standards."

When `bep_assembly` is detected, do not jump directly to free-form drafting. On `build/repository-foundation`, load:

- `guides/bep/README.md`
- `guides/bep/BEP-ASSEMBLY-MAP.md`
- `guides/bep/BEP-INTERVIEW-PROTOCOL.md`
- `workflows/BEP/TIVERIT-BIM-WF-BEP-INTERVIEW-ASSEMBLY-001.json`

Then:

1. inspect the conversation and supplied project sources;
2. extract already-supported project facts;
3. determine the requested BEP state;
4. build the unresolved gap queue;
5. ask only unresolved questions, normally one bounded question at a time;
6. validate answers against governed objects;
7. assemble the BEP when required data is captured, explicitly unresolved, deferred, conflicted, or recorded as a deviation candidate;
8. present the result as a draft/review package unless project evidence independently establishes approval.

The BEP interview is a guided assembly process. It does not approve the BEP, create contractual obligations, modify standards, or invent project facts.

## Public contribution boundary

External contributors may modify only:

`inbox/**`

Everything else is curator-managed canonical or governance content. Inbox material is evidence/proposal material and is never authoritative merely because it has been submitted or merged.

For contribution rules see `CONTRIBUTING.md`. For canonical changes see `CURATION.md`.