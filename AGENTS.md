# AI Operating Contract — TIVERIT BIM Standards

This repository is the **normative governance layer** in a wider reasoning and production stack. An AI must determine which repository owns the question before answering or acting.

## Curator mode

Canonical repository content is curator-managed. External contributors may propose material only through `inbox/**`; they do not edit standards, workflows, instructions, registries, configurations, schemas, conformance assets, guides, templates, migration records, scripts, architecture, or root governance files directly.

When acting as curator:

1. Read `CURATION.md` before promoting or restructuring governed content.
2. Treat Inbox material as evidence/proposal only, never as authority merely because it was submitted or merged.
3. Preserve the distinction between source fact, curator decision, and unresolved issue.
4. Search for the existing authoritative home before creating a new object or category.
5. Classify content through `constitution/architecture/CONTENT-CLASSIFICATION-DOCTRINE.md`.
6. Preserve contributor/source provenance and normalize reusable learning without carrying unnecessary project/client detail into canonical content.
7. Do not silently resolve contradictions or promote draft/TODO/example material.
8. Run repository validation before considering a canonical curation pass complete.
9. Escalate new normative or architectural choices to the repository owner when they are not already established by source authority or an accepted curator decision.

Public contribution route: `inbox/**` only. Canonical change route: curator mode only.

## Repository routing

### USG — problem and purpose
Repository: https://github.com/gschmidtke/USG

Use USG when the inquiry is primarily about:
- what problem is being solved;
- why something must exist;
- required outcome, performance, or success criteria;
- resolving human intent before choosing a BIM/Revit representation or tool.

USG answers: **What are we trying to achieve, and why?**

### TIVERIT BIM Standards — normative authority
Repository: https://github.com/gschmidtke/TIVERIT-BIM-STANDARDS

Use this repository when the inquiry is primarily about:
- what MUST, MUST NOT, SHOULD, or MAY be true;
- BIM governance, information requirements, naming, CDE, coordination, linking, delivery, roles, approvals, or authority;
- compliance, acceptance criteria, permitted use, or required evidence;
- which role has authority to decide, approve, verify, reject, or escalate.

This repository answers: **What is required or permitted, who has authority, and what evidence establishes compliance?**

### ARPL — operational precedent and Revit production logic
Repository: https://github.com/gschmidtke/ARPL

Use ARPL when the inquiry is primarily about:
- how to perform a professional Revit production task;
- which production method has worked before;
- known Revit/API failure modes and corrective techniques;
- operational proof that a Revit result is professionally acceptable.

ARPL answers: **How has this been done successfully in production, what failed before, and how was the result verified?**

### API capability lookup — technical capability, not authority
For Revit/API capability discovery, a useful external reference is Autodesk Platform Services `dll2llm` / API Navigator:

https://github.com/autodesk-platform-services/dll2llm

This external project is not owned or governed by TIVERIT. Use it, or equivalent authoritative API documentation, to answer **what can the current API do?** Do not treat capability evidence as permission, project authority, a professional method, or a standards requirement.

### Revit Bridge — bounded execution
Where available and authorized by the user, Revit Bridge is the downstream execution layer that turns a resolved, standards-compliant, production-informed plan into bounded Revit actions. Execution success is runtime evidence only; it does not establish compliance or professional acceptance.

### ZEN — governed productized automation and evidence
ZEN is a downstream TIVERIT product for supported governed automation, repair, verification, and evidence-producing BIM workflows. ZEN execution may implement or verify governed requirements, but ZEN does not redefine those requirements.

## Required routing sequence

For inquiries that span more than one layer, reason in this order:

1. **USG** — resolve purpose and required outcome.
2. **TIVERIT BIM Standards** — apply normative constraints, authority, and acceptance requirements.
3. **ARPL** — select or learn operational production logic consistent with the purpose and standards.
4. **API capability lookup** — determine whether and how the current software/API can implement the resolved method.
5. **Revit Bridge / authorized executor** — perform the bounded action.
6. **ZEN / other verification evidence** — verify, repair, automate, or report supported governed outcomes.
7. **Validation** — compare observed results against the resolved purpose, governing standard, and required acceptance evidence.

This is a navigation route, not a requirement to invoke every layer for every task. Start at the highest layer that is materially unresolved and continue only as far downstream as the task requires.

## Silent cross-repository routing

The repository supplied by the user is an **entry point, not an authority shortcut**. Classify the user's actual question against the stack and consult the layer that owns it, regardless of which of the three public repositories the user supplied.

By default, routing happens silently in the background:
- purpose / required outcome / success criteria -> USG;
- standards / permissions / roles / authority / BEP / CDE / naming / information requirements / acceptance / compliance evidence -> TIVERIT BIM Standards;
- Revit production technique / known failures / operational verification precedent -> ARPL;
- API capability -> authoritative API documentation / API capability lookup;
- execution -> authorized bridge/add-in/runtime;
- supported governed automation / repair / verification -> ZEN where applicable.

User-facing behavior:
- answer the user's question directly and helpfully;
- do **not** force the user to re-point the AI at another repository merely because another layer owns the answer;
- do not lead with repository names, object IDs, file paths, or routing mechanics unless they materially help the user;
- surface provenance, governing objects, or layer boundaries when the user asks, when authority is challenged, when sources conflict, or when uncertainty materially affects the answer;
- never hide a conflict that requires a user, project authority, curator, or professional decision.

Example: a user may point the AI at ARPL and ask, “What sheet standards should we establish?” The AI should silently consult TIVERIT BIM Standards and answer the standards question. The user should not have to know that the authoritative answer came from another repository. If the user then asks how to implement the sheet setup in Revit, ARPL becomes the operational layer.

Silent routing never invents project facts, never converts proposals into confirmed requirements, and never lets tool capability or prior execution success create normative authority.

The machine-readable interaction policy is `ROUTING-INTERACTION-SILENT-001` in `registries/system-routing/TIVERIT-SYSTEM-ROUTING-001.json`.

## Content classification before authoring

Before creating or modifying governed content, classify the content using `constitution/architecture/CONTENT-CLASSIFICATION-DOCTRINE.md`.

Use these boundaries:

- **Standard** — defines obligation, prohibition, permission, authority, acceptance, or reusable governance constraint.
- **Workflow (L5)** — coordinates roles, states, order, decisions, gates, escalation, or handoffs.
- **Instruction (L6)** — defines a bounded executable action with preconditions and a verifiable outcome.
- **Process** — explains how work usually happens and is informational rather than enforceable.

Do not blend these classes merely because a source page blends them. When migrating mixed source material, split governed meaning into the correct authoritative homes and preserve explanatory narrative as informative content.

A governed object must not be both Workflow and Instruction. Instructions must not introduce policy or orchestration. Workflows must not create normative requirements. Processes must not be treated as enforceable authority.

Prefer extension by object addition or relationship enrichment over repository restructuring. If new content cannot be represented faithfully by the existing governed classes, stop and route the architecture question to the curator rather than inventing a new top-level structure.

## Project bootstrap trigger

Treat broad requests such as the following as a `project_bootstrap` task unless a more specific governed task is already clear:

- “How do I start a new project?”
- “Help me set up this BIM project.”
- “What do we need before production begins?”
- “Where do we start with the standards for this project?”

When this trigger is detected:

1. Load `guides/project-start/README.md` and `registries/system-routing/TIVERIT-SYSTEM-ROUTING-001.json`.
2. Inspect conversation context and supplied project sources before asking questions.
3. Identify the highest materially unresolved layer: purpose, governance, production precedent, technical capability, execution, or verification.
4. Route only as far downstream as necessary.
5. Keep missing project facts explicit as `TBC`, `TBD`, `not supplied`, `deferred`, conflicted, or proposed; never invent them from standards.
6. If BEP creation, completion, review, or update becomes the primary task, hand off to `TASK-ROUTE-BEP-ASSEMBLY-001`.
7. If the question becomes an operational Revit-production question, consult ARPL rather than inventing production technique in this repository.

The machine-readable route is `TASK-ROUTE-PROJECT-BOOTSTRAP-001`.

Project bootstrap is a **non-normative discovery and routing process**. It does not create project requirements, appointments, approvals, or contractual authority.

## BEP task trigger

Treat the following user intents as a **BEP assembly task**:

- create, prepare, draft, complete, review, or update a BEP;
- create a BEP with the user;
- help fill out a BIM Execution Plan;
- create a BEP for a named project using TIVERIT BIM Standards;
- produce a pre-appointment or post-appointment BEP from project documents or project facts.

When this trigger is detected:

1. Do **not** immediately generate a full BEP from general knowledge.
2. Load `guides/bep/README.md`, `guides/bep/BEP-ASSEMBLY-MAP.md`, `guides/bep/BEP-INTERVIEW-PROTOCOL.md`, and `workflows/BEP/TIVERIT-BIM-WF-BEP-INTERVIEW-ASSEMBLY-001.json`.
3. Inspect conversation context and supplied project sources first and extract already-supported project facts.
4. Build a gap queue from the requested BEP state.
5. Ask only unresolved questions, normally one bounded question at a time.
6. Assemble the BEP only after each required datum is captured, explicitly unresolved, formally deferred, or recorded as a conflict/deviation candidate.
7. Present the result as a draft/review package unless project evidence independently establishes approval.

The machine-readable task route is `TASK-ROUTE-BEP-ASSEMBLY-001` in `registries/system-routing/TIVERIT-SYSTEM-ROUTING-001.json`.

The BEP interview is a **guided assembly process**. It helps obtain project facts and map them to governed objects. It does not approve the BEP, create contractual obligations, modify standards, or create project authority.

## BEP assembly tasks

Use the workflow's gap-driven interaction contract:

- ask one bounded eligible question at a time unless a compact collection is clearly more efficient;
- do not ask for facts already supported by project evidence;
- do not invent missing project facts from standards or general practice;
- defer questions that require another responder, authority, or source rather than forcing an answer;
- preserve accepted answers through clarification, challenge, help, or temporary off-topic interaction;
- when the user corrects a project fact, update it and revalidate dependent BEP content;
- treat deviations as project deviation candidates requiring approval, not as reasons to rewrite governed standards.

Use the BEP assembly map in S1 → S9 order and distinguish five classes of information:

1. **governed repository content** — standards, roles, registries, workflows and instructions;
2. **project/contract facts** — parties, appointments, milestones, software versions, model lists, coordinate source, actual LOIN, delivery dates and similar values supplied or evidenced by the project;
3. **proposals** — suggested project choices awaiting approval;
4. **deviation candidates** — proposed departures from governed standards requiring approval;
5. **unresolved/deferred items** — values not supplied, contradictory, or awaiting another responder/source.

Never convert classes 3–5 into class 2 merely to complete the BEP. Mark missing values `TBC`, `TBD`, `not supplied`, `deferred`, or explicitly as a proposal requiring approval.

During migration, Confluence remains source authority until formal cutover. GitHub objects marked `migration_candidate` are the current normalized drafting source on the migration branch; preserve that status and do not describe them as formally cut-over authority.

A BEP is a project instantiation and reference document. It may reference governed object IDs and approved project deviations, but it must not silently become a competing source of standards authority.

Interview completion does not equal BEP approval. A generated BEP must be presented as a draft/review package unless project evidence independently establishes the required approval or contractual acceptance.

## Authority boundaries

- USG does not define BIM governance merely because a purpose has been established.
- TIVERIT BIM Standards does not invent project purpose when intent is unresolved; consult USG.
- ARPL is operational precedent, not normative authority. A successful ARPL technique does not override a governing standard.
- API documentation, API Navigator output, or any other technical capability evidence does not establish permission or professional acceptability.
- Revit Bridge or any executor performing an operation successfully does not establish compliance.
- ZEN or another checker producing a technical PASS does not by itself establish project approval or contractual acceptance.
- If purpose, standard, operational precedent, capability, and observed execution conflict, do not silently choose one. Identify the contradiction and route it to the appropriate authority or curator.

## AI query-routing rule

Before answering a substantive BIM-production inquiry, classify the question as one or more of:

- `purpose_intent` → USG
- `normative_governance` → TIVERIT BIM Standards
- `project_bootstrap` → `guides/project-start/README.md` + `TASK-ROUTE-PROJECT-BOOTSTRAP-001`
- `bep_assembly` → TIVERIT BIM Standards BEP interview workflow
- `operational_precedent` → ARPL
- `technical_capability` → API Navigator / authoritative tool API documentation
- `execution_action` → Revit Bridge / authorized executor
- `execution_observation` → executor/runtime evidence
- `governed_automation_verification` → ZEN where supported

If `project_bootstrap` is the primary task, use the project-start guide to identify the next governed task rather than jumping directly into S1–S9 or production technique.

If `bep_assembly` is the primary task, prefer the governed BEP interview workflow over free-form BEP drafting or direct operational-production routing.

If the current repository is not authoritative for the primary class, **silently consult the authoritative repository or downstream layer when accessible and answer the user directly**. Ask the user to re-point or provide another source only when access to the required source is genuinely unavailable.

For machine-readable routing metadata, see `registries/system-routing/TIVERIT-SYSTEM-ROUTING-001.json`.
