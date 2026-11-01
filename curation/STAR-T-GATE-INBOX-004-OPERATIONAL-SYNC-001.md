# STAR-T-GATE Inbox #4 — BEP interview operational synchronization

## Purpose

Close the gap between the already-curated BEP workflow refinements from PR #3 / structural engine reconciliation from PR #24 and the human/AI consumption layer that actually tells an interview agent how to behave.

## Finding

The machine-readable workflow already contained the curated Inbox #4 controls, but `guides/bep/BEP-INTERVIEW-PROTOCOL.md` still reflected the earlier, thinner interaction guidance. In addition, `guides/bep/README.md` did not make consumption of the protocol explicit even though the workflow loads that README. This created an execution risk: an agent could load the workflow/consumption guide yet fail to operationalize all curated behaviors consistently.

## Changes

1. Updated `guides/bep/BEP-INTERVIEW-PROTOCOL.md` to operationalize:
   - EIR/AIR/PIR and project-source decomposition into downstream BEP targets before questioning;
   - question suppression for sufficiently evidenced targets;
   - complete machine-readable deferral records;
   - material-normalization confirmation;
   - visible per-answer validation;
   - distinct `pass` / `unresolved` / `gap` / `fail` semantics;
   - bounded pre-assembly project-instance closure sweep;
   - explicit no-authority-invention boundary.
2. Updated `guides/bep/README.md` so an AI following the consumption route is explicitly required to load the interview protocol, assembly map and workflow before substantive questioning.
3. Extended `ATS-BEP-INTERVIEW-COMPLETENESS-001` so the operational behaviors above are evidence expectations for a claimed complete interview state.

## Authority boundary

This synchronization does not create BEP approval authority, contractual acceptance authority, project facts, software approvals or new project role assignments. It implements already-curated interview behavior and makes it testable/consumable.

## Inbox #4 completion condition

Inbox #4 may be closed after this synchronization is merged and repository validation is green. The interim-validation proposal remains satisfied by the existing per-answer validation mechanism rather than by adding a duplicate checkpoint.