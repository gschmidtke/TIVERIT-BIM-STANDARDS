# AI Bootstrap — TIVERIT BIM Standards

This repository is public. The full working standards corpus is currently on:

`build/repository-foundation`

`main` is the public governance and discovery entry point during migration. Do not treat the limited content on `main` as evidence that the standards are unavailable.

## AEC AI routing context

Use the broader navigation stack when a task spans intent, governance, production logic, API capability, execution, and verification:

`USG -> TIVERIT BIM Standards -> ARPL -> API capability lookup -> Revit Bridge -> ZEN / evidence`

Routing meaning:
- **USG** resolves purpose, required outcome, constraints, and acceptance invariants: `https://github.com/gschmidtke/USG`.
- **TIVERIT BIM Standards** governs standards, authority, compliance, BEP, information-management, and project/company requirements.
- **ARPL** supplies professional Revit production precedent, known failures, and verification logic: `https://github.com/gschmidtke/ARPL`.
- **API capability lookup** answers what the current software/API can actually do. Autodesk Platform Services `dll2llm` / API Navigator is a useful external reference: `https://github.com/autodesk-platform-services/dll2llm`. It is not owned or governed by TIVERIT and is not normative authority.
- **Revit Bridge** is the downstream bounded execution layer where applicable.
- **ZEN** is a downstream TIVERIT product for governed automation, verification, repair, and evidence in supported workflows.

Do not confuse these questions:

- **USG:** what are we trying to achieve?
- **TIVERIT:** what is required or permitted?
- **ARPL:** what production method has worked and how is it verified?
- **API capability:** can the software/API perform the required operation?
- **Bridge:** execute the authorized operation.
- **ZEN/evidence:** verify, repair, automate, or report supported governed outcomes.

A downstream capability or successful execution must never override upstream intent, standards, user authority, or professional acceptance.

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