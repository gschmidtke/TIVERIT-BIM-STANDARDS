# Project Start — Navigational Guide

**Status:** non-normative discovery and routing aid  
**Authority:** none — this guide does not create requirements, roles, approvals, or acceptance criteria

This guide helps a human or AI determine where to begin when the request is broadly phrased as **starting a project**. It routes the inquiry to existing governed sources and downstream production layers without inventing missing project facts.

## Front door

Start with the highest materially unresolved question:

| Question | Route |
| --- | --- |
| What are we trying to achieve, and why? | **USG** — https://github.com/gschmidtke/USG |
| What is required or permitted, who has authority, and what evidence proves compliance? | **TIVERIT BIM Standards** — this repository |
| How has the work been done successfully in Revit, what failed, and how was the result verified? | **ARPL** — https://github.com/gschmidtke/ARPL |
| Can the current API actually perform the required operation? | **API capability lookup** — authoritative API documentation; Autodesk Platform Services `dll2llm` / API Navigator may be useful: https://github.com/autodesk-platform-services/dll2llm |
| Is the task ready for bounded execution? | **Authorized Revit Bridge / executor** |
| Is governed automation, repair, verification, or evidence required in a supported workflow? | **ZEN** |

This is a navigation route, not a requirement to invoke every layer. Start at the highest unresolved layer and continue downstream only as far as the task requires.

## Project bootstrap

When the user says things such as:

- “How do I start a new project?”
- “Help me set up this BIM project.”
- “What do we need before production begins?”
- “Where do we start with the standards for this project?”

classify the request as `project_bootstrap` unless a more specific task such as `bep_assembly` is already clear.

Use the following routing sequence:

1. **Purpose / outcome** — determine whether project purpose and required outcomes are sufficiently resolved. If not, route to USG.
2. **Project evidence** — inspect supplied contract/project information before asking questions.
3. **Information requirements** — identify which S2 requirements and project facts are applicable or missing.
4. **Roles / authority** — consult `registries/roles/REG-ROLE-001.json` and applicable S1 governed objects. Do not invent appointments.
5. **BEP state** — if a BEP must be created, completed, reviewed, or updated, route to the governed `bep_assembly` workflow under `guides/bep/`.
6. **CDE / production environment** — consult S3 and applicable CDE registries for project production-environment governance.
7. **Identity / naming / structure** — consult S4 and applicable registries before production containers are created.
8. **Coordination / federation / shared coordinates** — consult S5/S6 where applicable.
9. **Information structure / parameters / classification** — consult S8 where applicable.
10. **Tools / versions / automation authority** — consult S9 and project software/version facts.
11. **Exchange / delivery requirements** — consult S7 for formal exchange, submission, acceptance, and handover requirements.
12. **Production start** — once purpose and governance are sufficiently resolved, route Revit production-method questions to ARPL.

The sequence is diagnostic, not a declaration that every project requires every item in the same form.

## Hard boundaries

- Missing project facts remain `TBC`, `TBD`, `not supplied`, `deferred`, or explicitly proposed; they are never invented from standards.
- This guide does not create contractual requirements or project appointments.
- A standard does not invent project purpose.
- ARPL precedent does not override TIVERIT governance.
- API capability does not establish permission or professional acceptability.
- Successful execution does not establish compliance or approval.
- ZEN or another checker producing a technical result does not by itself establish project acceptance.

## Common project-start routes

| User intent | Preferred next step |
| --- | --- |
| Create / prepare / complete / review a BEP | `guides/bep/README.md` and `TASK-ROUTE-BEP-ASSEMBLY-001` |
| Determine project roles / responsibilities | `registries/roles/REG-ROLE-001.json` and S1 |
| Establish information requirements | S2 + applicable information-requirements registries/templates |
| Set up the CDE / production environment | S3 + `registries/cde/` |
| Establish naming / container identity | S4 + `registries/naming/` |
| Establish federation / linking / coordinates | S5/S6 + applicable coordination/link registries |
| Define parameters / classification / information structure | S8 + applicable parameter/classification registries |
| Determine software/tool authority | S9 + tool-authority registries |
| Define submissions / exchanges / handover | S7 + delivery-state/deliverable registries |
| Start modelling or solve a Revit production task | ARPL |

## AI behavior

An AI entering through this guide should:

1. classify the request before answering;
2. inspect already supplied project evidence;
3. ask only for unresolved facts that materially block the next governed step;
4. prefer an existing task route when one exists;
5. keep unresolved items explicit rather than completing them by inference;
6. redirect to the correct upstream or downstream layer when the current repository does not own the question.

Companion routing sources:

- `AGENTS.md`
- `registries/system-routing/TIVERIT-SYSTEM-ROUTING-001.json`
- `constitution/architecture/REASONING-STACK-ROUTING.md`
- `guides/bep/README.md`

*This guide is a discovery layer only. Governed objects remain authoritative within their defined scope.*
