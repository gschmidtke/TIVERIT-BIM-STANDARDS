# Curator Record — STAR-T-GATE Inbox Queue Round 001

Status: curated queue disposition record
Curator: Zara / ChatGPT
Source queue: `https://github.com/gschmidtke/STAR-T-GATE-INBOX/issues`
Standards tracking issue: `gschmidtke/TIVERIT-BIM-STANDARDS#6`

## Curation principle

STAR-T-GATE Inbox items are uncurated evidence. Their presence in the Inbox does not make them governing knowledge. This record establishes curator disposition against the current governed state and preserves unresolved dependencies without silently promoting proposals.

## Inbox #1 — First STAR-T-GATE Inbox test

**Disposition:** `resolved_by_current_state`

**Reason:** transport test only. It successfully demonstrated that an external client can submit intake through the STAR-T-GATE Inbox Worker without direct GitHub write access. No normative or procedural promotion is required.

**Retention:** retain as transport evidence.

## Inbox #2 — Test observation submission

**Disposition:** `resolved_by_current_state`

**Reason:** transport test only. It confirmed an additional external-client submission path through the Worker. No governance promotion is required.

**Retention:** retain as transport evidence.

## Inbox #3 — Authority to approve a BIM model for formal project use

**Disposition:** `held_unresolved`

**Target:** `STANDARDS`

**Reason:** the observation identifies a real authority-mapping gap that remains unresolved in the current governed corpus. Coordination sign-off is assigned, but broader formal-use / reliance acceptance authority is conditional on purpose, information state, project BEP/RACI, and appointment context. No universal named role should be inferred.

**Current action:** retain as an active Standards curation dependency. Resolve separately through explicit authority mapping by information state and purpose rather than through STAR-T-GATE infrastructure.

## Inbox #4 — Standards / BEP interview improvement

**Disposition:** `partially_promoted`

**Promoted through:** `gschmidtke/TIVERIT-BIM-STANDARDS#3`

**Accepted and implemented:**
- project-source decomposition before questioning;
- machine-readable deferral structure;
- validation-result semantics;
- bounded pre-assembly unresolved-data closure pass;
- confirmation of material normalization.

**Not promoted as new governance:**
- a redundant interim-validation checkpoint, because per-answer validation already existed in the governed workflow.

**Close recommendation:** close the Inbox issue once a source-queue disposition comment can be recorded, with the merged PR linked.

## Inbox #5 — Sheet Standards

**Disposition:** `partially_promoted`

**Promoted through:** `gschmidtke/TIVERIT-BIM-STANDARDS#4`

**Accepted and implemented:**
- dedicated L4 sheet/titleblock/documentation governance object;
- governed titleblock usage and change control;
- unique/stable sheet identity principles;
- governed titleblock metadata and revision representation;
- sheet composition, annotation, pre-issue QA, and related governance.

**Not promoted / still live:**
1. `sheet_series_value_semantics` — proposed G/0/1/2/3/4/5/6/D content-class meanings remain unconfirmed.
2. `titleblock_shared_parameter_guids` — titleblock parameter GUIDs remain unresolved in the S8 registry, limiting machine-checkable verification.
3. `issued_sheet_container_identity_mapping` — mapping issued sheet containers such as PDFs into the seven-token container identity grammar remains ungoverned.

**Close recommendation:** do not close as fully resolved. Keep the source issue open or replace it with linked child gap records until the three live dependencies are governed or explicitly rejected.

## Queue state after this round

- #1 — `resolved_by_current_state`
- #2 — `resolved_by_current_state`
- #3 — `held_unresolved`
- #4 — `partially_promoted`
- #5 — `partially_promoted`

## Source-queue write limitation

During this curator round, the connected GitHub integration could read `STAR-T-GATE-INBOX` but could not comment, close, label, or edit issues there. Therefore the authoritative curator disposition is recorded here in Standards, while the source issues remain unchanged until a connection with write permission records the same dispositions back to the Inbox.

This write limitation does not change the evidence or authority status of the Inbox items.
