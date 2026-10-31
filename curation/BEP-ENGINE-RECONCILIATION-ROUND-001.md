# BEP Engine Reconciliation — Round 001

## Scope

Source-side production-readiness material was reconciled against current `main`, centered on Confluence page 14090241 (`BEP Interview Production — Punch List (Readiness to Production)`) and the BEP Automation Modules read-me.

## Current-main state confirmed

Current main already contains a substantial governed BEP engine spine:

- `workflows/BEP/TIVERIT-BIM-WF-BEP-INTERVIEW-ASSEMBLY-001.json`
- `guides/bep/BEP-INTERVIEW-PROTOCOL.md`
- `guides/bep/BEP-ASSEMBLY-MAP.md`
- project templates under `templates/project/`
- a software-environment question (`BEP-Q-008`)
- `templates/project/software-lock-template.csv`

Therefore the source punch list is not treated as proof that those capabilities are absent.

## Source-object dispositions

| Source readiness item | Current-main disposition |
| --- | --- |
| Normalize v0.4 data paths | `superseded` by the current governed project-state/question-target architecture; source-era runtime paths are not canonicalized into Standards |
| Replace generic collection builder with typed builders | `partially_migrated`; current project templates and governed registries separate major object classes, while runtime transforms/builders remain ordinary engine implementation work |
| Fix `counts.named_im_individuals` | `intentionally_not_promoted`; this is a source-runtime implementation defect, not a Standards requirement |
| Separate preview/publishing instructions from engine logic | `migrated`; current protocol/guide content is separated from the machine-readable L5 workflow |
| Define transform inputs and output contracts | `partially_migrated`; the current workflow defines project-state targets, source decomposition and outputs; detailed runtime transform interfaces remain implementation work |
| Add software-environment interview/output | `migrated_structurally`; BEP-Q-008 and the software template already exist, and this round completes the source-backed capture-field contract |
| Populate Automation Modules subfolder | `merged_into_other_object`; the durable domain decomposition is represented by the governed question catalogue plus the new module catalog; source-era runtime package naming is not promoted |
| End-to-end BEP run | `migrated_to_conformance_contract`; this round adds an abstract completeness test. A runnable ETS/generator remains future implementation and must not be claimed as present |
| Template alignment drift automation/nightly check | `ordinary_standards_evolution`; not required to establish source-migration completeness |

## Changes in this round

1. Added `TIVERIT-BEP-SOFTWARE-ENVIRONMENT-FIELDS-001` to define the project capture contract for authoring, coordination, checking, issue, viewer, schedule/cost and publishing environments without approving products.
2. Expanded `software-lock-template.csv` to carry the source-backed fields while retaining project-specific values as unresolved until supplied.
3. Added `TIVERIT-BEP-INTERVIEW-MODULE-CATALOG-001`, mapping the current question catalogue into reusable governed interview domains without recreating obsolete runtime package conventions.
4. Added `ATS-BEP-INTERVIEW-COMPLETENESS-001`, which makes end-to-end interview completeness testable at the abstract conformance layer.

## Remaining implementation work

The following are **not migration gaps** after this round:

- executable interview/generator code;
- concrete object-transform implementations;
- unit tests for runtime transform code;
- an executable ETS that compiles a sample input into a rendered BEP;
- telemetry, multilingual prompts, role-specific prompt views and quick-start presets;
- automated nightly drift checks.

They are ordinary product/automation evolution and should be implemented without changing the authority model established by the governed workflow.

## Authority boundary

Interview completion does not approve a BEP. Software selections, authority assignments, project facts, acceptance routes and deviations remain project/governance decisions supported by evidence and applicable S1-S9 objects.
