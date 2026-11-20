# Information Decision and Authority Architecture

Status: migration candidate
Authority: repository governance
Source: curator resolution for ISO-IMP-005 and residual acceptance-authority gap
External evidence: ISO 19650-1:2018 clauses 12.3 and 12.5; ISO 19650-2:2018 clauses 5.6.4 and 5.7.1-5.7.4; ISO 19650-4:2022 clauses 6.1-6.3, verified from authorized curator source access

## Purpose

This architecture prevents TIVERIT from replacing or obscuring the applicable ISO 19650 information-management decision sequence with enterprise-native abstractions.

Where ISO 19650 applies, its CDE transition and information-model delivery semantics form the backbone. TIVERIT adds executable controls and supplementary project decisions without renaming the ISO responsibilities or creating a parallel approval/authorization/acceptance system.

## Core rule

A workflow action, CDE permission, status transition, file publication, software operation, automation, coordination role, or technical capability does not by itself assign or create the responsibility for an ISO 19650 review, approval, authorization or acceptance activity.

Every governed decision or transition event shall remain traceable to:

- the applicable ISO 19650 activity or explicitly identified TIVERIT supplementary decision;
- the affected information scope;
- the information state before and after where a transition occurs;
- the declared purpose, status or permitted use;
- the responsible ISO 19650 party/function or authorized supplementary project role;
- the governing appointment, information requirement, BEP/RACI, contract or other authority basis where applicable;
- the review/decision evidence and outcome;
- the technical transition actor where different from the responsible decision party.

## ISO 19650 backbone

### A. Work in Progress to Shared

For ISO 19650-governed information, the transition from Work in Progress to Shared follows the applicable review and approval-for-sharing process.

TIVERIT maps this transition to ISO 19650-4 Decision A. Where ISO 19650-2 applies, task-team review and approval for sharing under 5.6.4 is the upstream activity that permits information to enter the Shared state.

The platform user or automation executing the transition is not thereby assigned the task-team approval responsibility.

### B. Shared information-model delivery

Where ISO 19650-2 applies, the canonical information-model delivery sequence is:

1. task team submits information for lead appointed party authorization (5.7.1);
2. lead appointed party reviews and authorizes the information model (5.7.2);
3. lead appointed party submits the authorized information model for appointing party acceptance (5.7.3);
4. appointing party reviews and accepts or rejects the information model (5.7.4).

TIVERIT shall preserve these activities and party responsibilities rather than replace them with generic enterprise labels such as `authorize_for_formal_exchange` or `accept_for_declared_use`.

### C. Shared to Published

TIVERIT maps the Shared-to-Published transition to ISO 19650-4 Decision B. Where ISO 19650-2 applies, the applicable authorization and acceptance activities above shall be complete and traceable before the resulting Published transition is treated as governed.

Published is therefore the resulting CDE information state. It does not replace the evidence identifying the review, authorization, acceptance, responsible parties, status and permitted use that produced the transition.

### D. Archived

Archived preserves the historical record of information-container transactions, revisions, statuses and decision evidence. Movement to Archived is not an additional approval, authorization, acceptance or handover decision.

## TIVERIT supplementary decisions

TIVERIT may govern additional decisions where they are useful or required by project governance. These decisions are supplementary to the ISO backbone and shall not be represented as ISO-equivalent decisions unless an applicable project instrument explicitly combines responsibilities without obscuring the ISO activities.

### quality_verification

Purpose: determine whether produced information satisfies applicable internal production and quality-control requirements before downstream review.

Quality verification may provide evidence to the ISO review process but does not itself constitute approval for sharing, lead-appointed-party authorization or appointing-party acceptance.

### coordination_signoff

Purpose: record that information has passed the governed TIVERIT coordination gate for the declared coordination scope and purpose.

Coordination sign-off may support review before sharing or information-model review, but it does not replace task-team approval for sharing, lead-appointed-party authorization, appointing-party acceptance, milestone approval or handover acceptance.

### milestone_approval

Purpose: record a project or contractual milestone decision where the governing project instrument establishes such an event.

Milestone approval remains separate from the ISO 19650 information-model delivery sequence unless the governing project instrument explicitly combines decisions while preserving the underlying ISO responsibilities and evidence.

### handover_acceptance

Purpose: record a lifecycle, contractual, custody or responsibility-transfer decision at handover where required by the applicable project instruments.

Handover acceptance shall identify the receiving authority, accepted scope, declared purpose, transfer boundary and evidence. It shall not be inferred solely from prior ISO authorization/acceptance, file transfer, Published status or movement to Archived.

## Responsibility and authority resolution

Where ISO 19650 applies, first identify the ISO activity and responsible party/function. Then resolve the actual project actor from the applicable appointment and project governance.

`ISO activity -> responsible ISO party/function -> project appointment / information-management arrangements -> project actor -> evidence`

For a TIVERIT supplementary decision, resolve:

`supplementary decision + purpose + scope -> governing project instrument -> authorized project role -> decision evidence`

Relevant authority sources may include:

1. law or regulation;
2. contract or appointment;
3. appointing-party information requirements or information protocol;
4. explicitly incorporated external standard where applicable;
5. BEP, project RACI or other authorized project governance;
6. TIVERIT enterprise normative rule where TIVERIT legitimately establishes a supplementary responsibility.

Where the project mapping is insufficient, the result shall remain unresolved. TIVERIT shall not substitute a likely enterprise job title merely because that role has platform access or participates in the workflow.

## Platform and transition boundary

CDE permissions govern technical capability. They do not independently assign the ISO party responsibility for approval, authorization or acceptance.

Accordingly:

- a CDE operator may execute a transition after the responsible ISO activity is complete and evidenced;
- the transition actor may differ from the responsible decision party;
- ACC issue closure, review completion, folder placement, transmittal creation or publication action does not replace the ISO activity;
- TIVERIT coordination sign-off does not automatically authorize Work in Progress-to-Shared or Shared-to-Published transitions;
- Decision A and Decision B evidence shall remain traceable even where the platform represents the result only as a state/status change.

## Applicability boundary

This architecture does not make ISO 19650 automatically applicable to every TIVERIT project. Applicability remains governed by the External Standards Gateway and the applicable project instruments.

When ISO 19650 is applicable, however, TIVERIT shall preserve its party/activity semantics rather than substituting an enterprise-native decision taxonomy.

## Conformance direction

Machine-readable conformance should fail or remain unresolved when:

- a Work in Progress-to-Shared transition lacks the applicable review/approval-for-sharing evidence;
- a Shared-to-Published transition lacks the applicable authorization/acceptance evidence;
- ISO 19650-2 applies but lead-appointed-party authorization and appointing-party acceptance are collapsed or omitted;
- a platform role or technical transition actor is treated as the responsible ISO party without project mapping;
- TIVERIT coordination sign-off, milestone approval or handover acceptance is substituted for an ISO approval, authorization or acceptance activity;
- the submitted/accepted information scope, status or permitted use cannot be identified;
- project-specific responsibility is silently replaced by an enterprise job-title default.

## Curator disposition

ISO-IMP-005 is confirmed as a real TIVERIT governance impact. The corrected architecture is an ISO 19650 backbone with TIVERIT supplementary executable governance. Remaining work is project-role mapping and conformance coverage, not creation of alternative TIVERIT approval/authorization/acceptance classes.
