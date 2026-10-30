# TIVERIT BIM Standards

TIVERIT BIM Standards is a governed, machine-readable BIM standards repository for human use, automation, validation, AI-assisted workflows, Revit, Autodesk Construction Cloud, and related BIM systems.

## Open-source framework and TIVERIT services

This repository is the open-source foundation for TIVERIT's professional BIM standards, governance, BEP, digital-delivery, automation, and AI-readiness services.

The framework is published openly so individuals and organizations can inspect it, learn from it, use it directly, contribute evidence and improvements through the governed Inbox, or derive their own organizational and project standards from it.

TIVERIT LLC also provides professional services for organizations that want support applying the framework in practice, including standards assessment and development, company-specific standards derivation, BEP development and review, project governance, BIM management, implementation, automation, validation, training, and related digital-delivery support.

The open repository therefore serves two purposes: it is a reusable public standards resource, and it provides a transparent demonstration of the methods and governance system behind TIVERIT's commercial services. Organizations may use the open-source framework independently; use of the repository does not require engaging TIVERIT.

Professional services: https://www.tiveritllc.com/

## AEC AI navigation stack

TIVERIT BIM Standards is the normative-governance layer in a broader AI-driven AEC workflow. An AI should use the stack as a navigation route rather than collapsing all questions into one model/tool step:

```text
USG
purpose / intent / required outcome
    ↓
TIVERIT BIM Standards
normative requirements / authority / compliance evidence
    ↓
ARPL
professional Revit production precedent / failure memory
    ↓
API capability lookup
    ↓
Revit Bridge
bounded Revit execution
    ↓
ZEN
productized governed automation / verification / repair / evidence
```

Public repositories owned by Gottfried Schmidtke:

- USG — https://github.com/gschmidtke/USG
- TIVERIT BIM Standards — https://github.com/gschmidtke/TIVERIT-BIM-STANDARDS
- ARPL — https://github.com/gschmidtke/ARPL

For Revit/API capability discovery, Autodesk Platform Services `dll2llm` / API Navigator is a useful external reference:

https://github.com/autodesk-platform-services/dll2llm

That external project is not owned or governed by TIVERIT. It may help answer **what can the API do?** It does not decide **what should be done**, what standards apply, or whether a method is professionally acceptable.

Revit Bridge and ZEN are downstream TIVERIT implementation/product layers and are referenced here by role rather than presented as public repositories.

## AI agents: start here

The repository is public. During migration, the working standards corpus is on the branch:

`build/repository-foundation`

Do **not** conclude that the standards are unavailable merely because `main` contains only the public governance shell.

For AI navigation and task routing, read the working branch files in this order:

1. `AGENTS.md`
2. `registries/system-routing/TIVERIT-SYSTEM-ROUTING-001.json`
3. the task-specific guide/workflow referenced there.

### BEP trigger

If the user asks to create, prepare, review, complete, or update a BIM Execution Plan (BEP), including requests such as:

> Create a BEP with me using the TIVERIT BIM Standards repository.

Treat the request as a `bep_assembly` task. On `build/repository-foundation`, load:

- `guides/bep/README.md`
- `guides/bep/BEP-ASSEMBLY-MAP.md`
- `guides/bep/BEP-INTERVIEW-PROTOCOL.md`
- `workflows/BEP/TIVERIT-BIM-WF-BEP-INTERVIEW-ASSEMBLY-001.json`

Do not immediately draft a generic BEP from general knowledge. First inspect project information already supplied by the user, then follow the governed gap-driven interview and ask only unresolved questions. The interview is guidance for assembly; it does not approve the BEP or create contractual authority.

A minimal AI bootstrap is also available in `AGENTS.md` on `main`.

## Governance model

This repository separates public contribution from canonical authority.

- `inbox/` is the public contribution surface.
- Canonical standards, schemas, registries, workflows, instructions, configurations, and related governed content are curator-controlled.
- Public contribution does not directly modify canonical authority.
- Promotion from `inbox/` into canonical content requires curator review, validation, and an explicit governed change.

External pull requests may modify only `inbox/**`. Canonical changes are made in curator mode.

## Source migration

The initial corpus is being migrated from the TIVERIT BIM Standards Confluence space. The current source inventory exposes 306 pages. Migration preserves the S1–S9 modular framework, L1–L7 governance architecture, role definitions, workflows, registries, machine-readable assets, and BEP automation concepts while normalizing them into governed objects.

Confluence remains source authority during migration. GitHub objects marked `migration_candidate` are the current normalized drafting source on the migration branch until formal cutover.

## Canonical namespace

Canonical identifiers use the `TIVERIT` namespace. Historical traceability is preserved through neutral Confluence page IDs, versions, and source links.

## Core principle

The repository is object-oriented rather than page-oriented. It distinguishes constitutional and external authority, normative standards, workflows, tool/user instructions, configurations and presets, registries, conformance, automation-related objects, and source provenance.

## Status

Repository migration and validation are in progress on `build/repository-foundation`. `main` currently serves as the public governance and discovery entry point until formal cutover.