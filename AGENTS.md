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

## BEP assembly tasks

When asked to create, review, or complete a BIM Execution Plan (BEP), do not discover the repository ad hoc. Start with:

- `guides/bep/README.md`
- `guides/bep/BEP-ASSEMBLY-MAP.md`
- the project-instance starter tables under `templates/project/`

Use the BEP assembly map in S1 → S9 order and distinguish three classes of information:

1. **governed repository content** — standards, roles, registries, workflows and instructions;
2. **project/contract facts** — parties, appointments, milestones, software versions, model lists, coordinate source, actual LOIN, delivery dates and similar values supplied by the project;
3. **unresolved items** — values not supplied or not yet governed.

Never invent class 2 values from class 1 rules. Mark missing values `TBC`, `TBD`, `not supplied`, or explicitly as a proposal requiring approval.

During migration, Confluence remains source authority until formal cutover. GitHub objects marked `migration_candidate` are the current normalized drafting source on the migration branch; preserve that status and do not describe them as formally cut-over authority.

A BEP is a project instantiation and reference document. It may reference governed object IDs and approved project deviations, but it must not silently become a competing source of standards authority.

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
- `operational_precedent` → ARPL
- `technical_capability` → tool/API documentation
- `execution_observation` → executor/runtime evidence

If the current repository is not authoritative for the primary class, explicitly redirect to the repository that is.

For machine-readable routing metadata, see `registries/system-routing/TIVERIT-SYSTEM-ROUTING-001.json`.
