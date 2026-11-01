# Information Decision and Authority Taxonomy

Status: migration candidate
Authority: repository governance
Source: curator resolution candidate for ISO-IMP-005 and residual acceptance-authority gap
External evidence: ISO 19650-1:2018 clauses 12.3 and 12.5; ISO 19650-2:2018 clauses 5.6.4 and 5.7.1-5.7.4; ISO 19650-4:2022 clauses 6.1-6.3, verified from authorized curator source access

## Purpose

This taxonomy prevents TIVERIT from collapsing technically and contractually distinct information decisions into a generic concept of approval or acceptance.

It defines TIVERIT-native decision classes and the minimum authority contract needed to determine who may make each decision. It does not make ISO 19650 automatically applicable to a project and does not assign a universal enterprise job title to project-specific contractual authority.

## Core rule

A workflow action, CDE permission, status transition, file publication, software operation, automation, coordination role, or technical capability does not by itself create decision authority.

Every governed decision event shall identify:

- `decision_type`;
- `decision_scope`;
- `information_state_before` and `information_state_after` where a transition occurs;
- `declared_purpose` or permitted use affected by the decision;
- `authority_domain` required for the decision;
- `authorized_role` or an explicit unresolved project assignment;
- `authority_basis` establishing why that role may act;
- `decision_evidence` recording the decision and outcome.

## Decision classes

### 1. quality_verification

Purpose: determine whether produced information satisfies applicable internal production and quality-control requirements before downstream review.

This is not coordination sign-off, authorization for formal issue, appointing-party acceptance, or permission for reliance unless another governed authority explicitly combines those events.

### 2. approve_for_sharing

Purpose: approve information produced by an originating task team for transition from work in progress into a shared collaborative state.

Default authority principle: the authority belongs to the originating information-production/task-team function established by the applicable project governance. TIVERIT shall not infer a Project BIM Manager, CDE Manager, or software user as the approver merely because that person can execute the transition.

### 3. coordination_signoff

Purpose: record that information has passed the governed coordination gate for the declared coordination scope and purpose.

This is a TIVERIT coordination decision. It does not by itself constitute authorization for formal issue, appointing-party/client acceptance, milestone acceptance, handover acceptance, or unrestricted reliance.

Existing S5 role assignments may govern this event where supported by the project RACI or delegated authority.

### 4. authorize_for_formal_exchange

Purpose: determine that the coordinated information model or information set is authorized to proceed to formal exchange, issue, publication, or submission for downstream acceptance for the declared purpose.

This authority shall be assigned by the applicable appointment, contract, BEP/RACI, information protocol, or other governed project instrument. TIVERIT shall not assign it universally to the Project BIM Manager.

### 5. accept_for_declared_use

Purpose: determine that submitted information satisfies the acceptance criteria for a declared deliverable, purpose, reliance, or use by the receiving/appointing authority.

Acceptance shall identify the accepted scope and permitted use. Acceptance does not transfer authorship or information-production responsibility and shall not be inferred merely from a CDE status, download, receipt, review participation, or technical publication event.

### 6. milestone_approval

Purpose: record a project or contractual milestone decision where the governing instrument establishes such an approval event.

Milestone approval is not automatically equivalent to coordination sign-off, authorization, or information acceptance. If a project intentionally combines events, the authority basis and combined scope shall be explicit.

### 7. handover_acceptance

Purpose: accept a defined information deliverable or information model at a delivery-to-operation, contractual, or responsibility-transfer boundary.

Handover acceptance shall identify the receiving authority, accepted scope, declared purpose, transfer boundary, and evidence. It shall not be inferred from file transfer or archive state alone.

## Authority resolution contract

For each decision event, resolve authority in this order:

`decision type + purpose + scope + information state -> required authority domain -> governing authority basis -> authorized project role -> decision evidence`

The `authority_basis` shall reference an applicable source such as:

1. law or regulation;
2. contract or appointment;
3. appointing-party/client information requirement or information protocol;
4. explicitly incorporated external standard where applicable;
5. BEP, project RACI, or other authorized project governance;
6. TIVERIT enterprise normative rule where TIVERIT actually establishes the authority.

Where no sufficient authority basis exists, the result shall be `authority_unresolved`. The system shall not substitute a likely job title.

## State-transition rule

A decision may cause or authorize a CDE state/status transition, but the transition is evidence/execution of the decision rather than the source of authority.

Accordingly:

- CDE permission does not create authority;
- executing a status transition does not prove that the executor held the underlying decision authority;
- a person may execute a transition on behalf of an authorized decision maker if the decision record and delegation/execution basis are traceable;
- coordination sign-off shall not automatically set a container to an accepted/published state unless the applicable governance explicitly establishes that consequence;
- acceptance for a declared use shall be traceable to both the decision evidence and the authority basis.

## ISO alignment note

Authorized curator review of ISO 19650 source evidence confirms that the source framework distinguishes originating-team approval for sharing, lead-party authorization of an information model, and appointing-party acceptance. ISO 19650-4 also distinguishes approval for sharing from authorization/acceptance for publication.

TIVERIT adopts the distinction as a useful governance separation, but this taxonomy is independently authored TIVERIT doctrine. Exact project applicability and role assignment remain subject to the External Standards Gateway and governing project instruments.

## Required reconciliation

The following existing TIVERIT language shall be audited against this taxonomy before normative promotion:

- `TIVERIT-BIM-STD-S5-ACCEPTANCE-STATUS-LINK-EP001`;
- S5 coordination sign-off requirements and role assignments;
- S7 submission, deliverable, reliance and handover requirements;
- S3 CDE state-transition rules;
- role authority definitions and project RACI/BEP authority declarations;
- conformance rules that treat a technical status transition as proof of acceptance.

In particular, requirements that currently use `acceptance`, `approval`, `sign-off`, `authorization`, or `accepted state` without a declared decision type shall be classified and repaired rather than normalized by terminology alone.

## Conformance direction

Future machine-readable authority validation should fail or remain unresolved when:

- a governed decision has no decision type;
- the acting role lacks a traceable authority basis;
- technical execution is presented as authority;
- coordination sign-off is used as universal formal acceptance;
- authorization and receiving-party acceptance are collapsed where the governing process distinguishes them;
- acceptance evidence does not identify scope and declared purpose;
- a project-specific authority assignment is silently replaced by an enterprise default.

## Curator disposition

ISO-IMP-005 is therefore confirmed as a real TIVERIT governance impact. The appropriate correction is not to copy ISO role names into TIVERIT, but to establish explicit decision semantics and resolve the authorized role from the governing authority basis for each project context.
