# AI Operating Contract — TIVERIT BIM Standards

This repository is the **normative governance layer** in a wider reasoning and production stack. An AI must determine which repository owns the question before answering or acting.

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

## Required routing sequence

For inquiries that span more than one layer, reason in this order:

1. **USG** — resolve purpose and required outcome.
2. **TIVERIT BIM Standards** — apply normative constraints, authority, and acceptance requirements.
3. **ARPL** — select or learn operational production logic consistent with the purpose and standards.
4. **Tool/API/executor** — determine capability and perform the action.
5. **Validation** — compare observed results against both the resolved purpose and the governing standard.

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
- TIVERIT BIM Standards does not invent project purpose when intent is unresolved; redirect to USG.
- ARPL is operational precedent, not normative authority. A successful ARPL technique does not override a governing standard.
- A tool or API capability does not establish permission or professional acceptability.
- Execution success does not equal compliance.
- If purpose, standard, and operational precedent conflict, do not silently choose one. Identify the contradiction and route it to the appropriate authority or curator.

## AI query-routing rule

Before answering a substantive BIM-production inquiry, classify the question as one or more of:

- `purpose_intent` → USG
- `normative_governance` → TIVERIT BIM Standards
- `bep_assembly` → TIVERIT BIM Standards BEP interview workflow
- `operational_precedent` → ARPL
- `technical_capability` → tool/API documentation
- `execution_observation` → executor/runtime evidence

If `bep_assembly` is the primary task, prefer the governed BEP interview workflow over free-form BEP drafting or direct operational-production routing.

If the current repository is not authoritative for the primary class, explicitly redirect to the repository that is.

For machine-readable routing metadata, see `registries/system-routing/TIVERIT-SYSTEM-ROUTING-001.json`.
