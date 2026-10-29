# Workflow Reference Reconciliation

Status: migration review  
Source authority during migration: Confluence page `6127632` (source version 1)  
Repository target: `workflows/` on `build/repository-foundation`

## Purpose

Reconcile unresolved semantic `W-*` workflow references against the source workflow catalogue before creating additional canonical workflow objects.

The source catalogue defines **16 explicit workflows** across W0-W8. It also defines atomic instruction clusters beneath those workflows. This review therefore does **not** assume that every unresolved `W-*` reference deserves an independent workflow object.

Classification vocabulary:

- **canonical_source_workflow** — directly corresponds to one of the 16 source workflows.
- **semantic_alias_or_subflow** — narrower label that is substantially covered by a source workflow or its instruction sequence; should normally be repaired to the canonical workflow instead of migrated separately.
- **cross_workflow_composite** — spans more than one source workflow and should not be collapsed without curator review.
- **source_unsupported_placeholder** — not represented as an explicit workflow in the source catalogue; do not create solely to satisfy references.
- **needs_targeted_source_check** — plausible workflow concept, but the catalogue alone is insufficient to determine whether a separate source page exists.

## Source workflow catalogue

| Source ID | Source workflow | Primary intent |
|---|---|---|
| W0.1 | Standards Adoption | applicability, scope, authority, adoption |
| W0.2 | Deviation & Exception | deviation request, impact, approval, publication |
| W1.1 | Project Model Setup | template, identity, coordinates, worksets |
| W1.2 | CDE / ACC Project Setup | folder structure, permissions, baseline publication |
| W2.1 | Model Identity Definition | model role, discipline, purpose, naming, metadata |
| W2.2 | Workset Management | workset definition, assignment, protection |
| W3.1 | Link Creation | source/host identification, placement, settings, validation |
| W3.2 | Link Update & Maintenance | reload, version/reference integrity, coordinate alignment |
| W4.1 | Parameter Definition | parameter definition, ownership, binding, deployment |
| W4.2 | Data Population | population, completeness, allowed values, audit evidence |
| W5.1 | Model Coordination | federation, coordination checks, findings, actions |
| W5.2 | Issue Tracking | issue creation, ownership, due dates, resolution evidence |
| W6.1 | Sheet Setup | sheet genesis, titleblocks, views, completeness |
| W6.2 | Schedule Export | schedule selection, export, validation, logging |
| W7.1 | Model Health Check | diagnostics, worksets/links/reference integrity, escalation |
| W7.2 | QA/QC Validation | required checks, remediation, approve/reject model state |
| W8.1 | IFC / Exchange Export | export preset, exchange generation, validation |
| W8.2 | Project Closeout | archive, package deliverables/logs, closeout index |

> Note: the source page describes these as a 16-workflow catalogue but enumerates 18 named workflow rows when W0.1-W8.2 are counted. This numerical inconsistency is preserved as a source issue and must not be silently corrected into authority.

## Reconciliation of unresolved semantic references

### Governance and standards

| Unresolved reference | Classification | Likely source target | Migration treatment |
|---|---|---|---|
| `W-GOVERNED-PRODUCTION-INTAKE` | cross_workflow_composite | W0.1 + W1.1 | Do not create from catalogue alone; concept spans adoption/scope and project setup. |
| `W-STANDARDS-EVOLUTION` | needs_targeted_source_check | W0.2 partial | Catalogue covers deviations, not full standards lifecycle/change governance. Search source before deciding. |
| `W-GOVERNANCE-ARBITRATION` | source_unsupported_placeholder | none explicit | Keep unresolved unless separate source page exists. |
| `W-STANDARDS-REVIEW-PIPELINE` | needs_targeted_source_check | W0.1/W0.2 partial | Review/evolution is broader than either explicit workflow. |
| `W-GOVERNANCE-ESCALATION` | semantic_alias_or_subflow | W0.2 | Escalation is part of deviation/exception handling; likely repair to W0.2 unless separate source evidence exists. |
| `W-GATE-ACCEPTANCE` | cross_workflow_composite | W7.2 + S5 acceptance governance | Do not invent a workflow; acceptance authority is broader than QA/QC execution. |
| `W-GATE-VERIFICATION` | semantic_alias_or_subflow | W7.2 | Verification/checking aligns to QA/QC Validation; acceptance remains separate. |

### Project initiation, CDE, permissions, onboarding

| Unresolved reference | Classification | Likely source target | Migration treatment |
|---|---|---|---|
| `W-PROJECT-SETUP` | semantic_alias_or_subflow | W1.1 | Repair to canonical project model setup unless broader project setup source exists. |
| `W-CDE-SETUP` | canonical_source_workflow | W1.2 | Strong direct correspondence. |
| `W-FOLDER-PROVISIONING` | semantic_alias_or_subflow | W1.2 | Folder creation is an instruction cluster within W1.2. |
| `W-PERMISSIONS-MANAGEMENT` | semantic_alias_or_subflow | W1.2 | Permission assignment belongs within W1.2; ongoing maintenance may require separate source evidence. |
| `W-CDE-MAINTENANCE` | needs_targeted_source_check | W1.2 partial | Catalogue defines setup, not an explicit ongoing maintenance workflow. |
| `W-CDE-GOVERNANCE` | cross_workflow_composite | W0.1 + W1.2 | Governance and setup are distinct concerns; do not collapse without source review. |
| `W-MEMBER-ONBOARDING` | semantic_alias_or_subflow | W1.2 | User/member access onboarding is consistent with permissions/access setup. |
| `W-BEP-AUTHORING` | source_unsupported_placeholder | none explicit | No explicit BEP authoring workflow in catalogue; retain unresolved for targeted source search. |

### Model authoring and discipline production

| Unresolved reference | Classification | Likely source target | Migration treatment |
|---|---|---|---|
| `W-MODEL-AUTHORING` | cross_workflow_composite | W1.1 + W2.1 + W2.2 | Too broad to become one workflow from this catalogue. |
| `W-DISCIPLINE-AUTHORING` | cross_workflow_composite | W1.1 + W2.1 + W2.2 | Discipline-specific production is not a separate explicit source workflow. |
| `W-MODELING-CRAFT` | source_unsupported_placeholder | none explicit | L6 production instruction concern, not explicit workflow in catalogue. |
| `W-AUDIO-BIM-AUTHORING` | source_unsupported_placeholder | none explicit | Discipline specialization absent from generic catalogue. |
| `W-CONTROLS-BIM-AUTHORING` | source_unsupported_placeholder | none explicit | Same. |
| `W-ELECTRICAL-BIM-AUTHORING` | source_unsupported_placeholder | none explicit | Same. |
| `W-LIGHTING-BIM-AUTHORING` | source_unsupported_placeholder | none explicit | Same. |
| `W-MECHANICAL-BIM-AUTHORING` | source_unsupported_placeholder | none explicit | Same. |
| `W-SFX-BIM-AUTHORING` | source_unsupported_placeholder | none explicit | Same. |
| `W-SHOWSET-AUTHORING` | source_unsupported_placeholder | none explicit | Same. |
| `W-VIDEO-BIM-AUTHORING` | source_unsupported_placeholder | none explicit | Same. |
| `W-POOLED-CAPACITY-DISPATCH` | source_unsupported_placeholder | none explicit | Resource-dispatch concept is not present in W0-W8 catalogue. |
| `W-TECH-PORTFOLIO-COORDINATION` | source_unsupported_placeholder | none explicit | Portfolio-level coordination is not present in catalogue. |
| `W-TECH-FEDERATED-REVIEW` | semantic_alias_or_subflow | W5.1 | Federation review substantially aligns to Model Coordination; technical specialization needs separate source evidence if retained. |
| `W-TECH-MILESTONE-RELEASE` | cross_workflow_composite | W7.2 + W8.2 | Verification/release spans QA and delivery/closeout; do not invent as one workflow. |

### Identity, parameters, registries, and information operations

| Unresolved reference | Classification | Likely source target | Migration treatment |
|---|---|---|---|
| `W-PARAMETER-OPERATIONS` | cross_workflow_composite | W4.1 + W4.2 | Parameter definition and population are two explicit workflows; reference should be repaired contextually, not mapped blindly. |
| `W-REGISTRY-GOVERNANCE` | needs_targeted_source_check | W4.1 partial | Registry governance is broader than parameter definition and may exist elsewhere. |
| `W-SP-REGISTRY-MERGE` | semantic_alias_or_subflow | W4.1 | Shared-parameter registry merge is an implementation-specific parameter-governance operation; likely instruction/subflow, not new workflow. |
| `W-CITIZEN-TXT-GENERATION` | semantic_alias_or_subflow | W4.1 | Generated shared-parameter carrier creation is an instruction-level operation subordinate to parameter governance. |
| `W-MIDP-MANAGEMENT` | needs_targeted_source_check | none explicit | S2 defines MIDP governance, but the W0-W8 catalogue has no explicit MIDP workflow. Search source. |
| `W-PROJECT-DELIVERY-PLANNING` | needs_targeted_source_check | none explicit | Delivery planning is not an explicit W0-W8 workflow. |
| `W-SCHEDULE-ALIGNMENT` | source_unsupported_placeholder | none explicit | Could be delivery-planning subflow, but catalogue does not support it directly. |
| `W-TIDP-DELIVERY` | needs_targeted_source_check | W8.1/W8.2 partial | Delivery-plan execution is broader than exchange export; search source before mapping. |

### Linking, federation, coordination, clashes, and issues

| Unresolved reference | Classification | Likely source target | Migration treatment |
|---|---|---|---|
| `W-COORDINATION-RESOLUTION` | cross_workflow_composite | W5.1 + W5.2 | Resolution spans coordination findings and issue lifecycle. |
| `W-COORDINATION-ROUTINE` | semantic_alias_or_subflow | W5.1 | Strong semantic match to recurring Model Coordination. |
| `W-CLASH-DETECTION` | semantic_alias_or_subflow | W5.1 | Explicitly represented as coordination checks inside W5.1; do not create separately from catalogue alone. |
| `W-CLASH-RESOLUTION-EDIT` | semantic_alias_or_subflow | W5.1 + W5.2 | Resolution/edit is downstream of coordination finding; may also be an authoring instruction rather than workflow. |
| `W-ISSUE-LIFECYCLE-MANAGEMENT` | canonical_source_workflow | W5.2 | Strong direct correspondence. |
| `W-ZONE-FEDERATED-REVIEW` | semantic_alias_or_subflow | W5.1 | Zone scope is project specialization of Model Coordination unless separate source exists. |
| `W-ZONE-SCOPE-GATEKEEPING` | source_unsupported_placeholder | none explicit | Scope gatekeeping is not defined by catalogue. |
| `W-CONSTRUCTABILITY-REVIEW` | needs_targeted_source_check | W5.1 partial | Coordination framework may host it, but constructability review is not explicitly named. |

### QA, validation, review, and acceptance

| Unresolved reference | Classification | Likely source target | Migration treatment |
|---|---|---|---|
| `W-PRE-PUBLISH-QA` | semantic_alias_or_subflow | W7.2 | Strong alignment with milestone QA/QC validation before publication. |
| `W-PRE-PUBLISH-VALIDATION` | semantic_alias_or_subflow | W7.2 | Same. |
| `W-QAQC-AUDIT` | semantic_alias_or_subflow | W7.2 | QA/QC audit is covered by W7.2 checks/remediation/evidence. |
| `W-MODEL-VALIDATION-ACCEPTANCE` | cross_workflow_composite | W7.2 + S5 acceptance | Catalogue includes approve/reject model state, but repository governance distinguishes technical QA evidence from formal acceptance. Do not collapse without review. |
| `W-DESIGN-REVIEW` | needs_targeted_source_check | W5.1 partial | Model Coordination may support design review but source does not explicitly equate them. |
| `W-SUBMITTAL-APPROVAL` | source_unsupported_placeholder | none explicit | No submittal workflow in catalogue. |
| `W-DOCUMENTATION-APPROVAL` | source_unsupported_placeholder | none explicit | W6.1 handles sheet setup, not approval authority. |
| `W-CLIENT-REVIEW-ACCEPTANCE` | source_unsupported_placeholder | none explicit | Client review/acceptance is not an explicit catalogue workflow. |
| `W-STAGE-GATES` | cross_workflow_composite | W7.2 + governance | Stage-gate concept spans QA and authority and needs targeted source evidence. |

### Documentation, exchange, release, and handover

| Unresolved reference | Classification | Likely source target | Migration treatment |
|---|---|---|---|
| `W-VIEW-SHEET-SETUP` | semantic_alias_or_subflow | W6.1 | View/sheet setup is substantially covered by Sheet Setup plus L6 view instructions. |
| `W-INFORMATION-EXCHANGE` | semantic_alias_or_subflow | W8.1 | Strong match to exchange-export workflow, but verify whether broader non-file exchange is intended. |
| `W-INTEROPERABILITY-EXCHANGE` | semantic_alias_or_subflow | W8.1 | Strong match to IFC / Exchange Export. |
| `W-CONTRACTOR-INFORMATION-EXCHANGE` | semantic_alias_or_subflow | W8.1 | Project/party specialization of exchange unless separate source exists. |
| `W-ZONE-SHOWSET-PACKAGE-RELEASE` | cross_workflow_composite | W7.2 + W8.1/W8.2 | Release package includes QA plus exchange/packaging; not one explicit source workflow. |
| `W-DELIVERABLE-HANDOVER` | semantic_alias_or_subflow | W8.2 | Strong match to Project Closeout package/handover intent. |

### Tool and automation governance

| Unresolved reference | Classification | Likely source target | Migration treatment |
|---|---|---|---|
| `W-TOOL-VALIDATION` | source_unsupported_placeholder | none explicit | S9 governance may support this concept, but the W0-W8 catalogue does not. |
| `W-AUTOMATION-APPROVAL` | source_unsupported_placeholder | none explicit | Same; requires targeted S9 source search rather than inference. |

## High-confidence consolidation candidates

The following unresolved references can be reconciled with high confidence to source workflows, subject to checking the exact role context before rewriting each reference:

- `W-CDE-SETUP` → W1.2
- `W-PROJECT-SETUP` → W1.1
- `W-FOLDER-PROVISIONING` → W1.2
- `W-MEMBER-ONBOARDING` → W1.2
- `W-TECH-FEDERATED-REVIEW` → W5.1
- `W-COORDINATION-ROUTINE` → W5.1
- `W-CLASH-DETECTION` → W5.1
- `W-ISSUE-LIFECYCLE-MANAGEMENT` → W5.2
- `W-PRE-PUBLISH-QA` → W7.2
- `W-PRE-PUBLISH-VALIDATION` → W7.2
- `W-QAQC-AUDIT` → W7.2
- `W-VIEW-SHEET-SETUP` → W6.1
- `W-INFORMATION-EXCHANGE` → W8.1
- `W-INTEROPERABILITY-EXCHANGE` → W8.1
- `W-CONTRACTOR-INFORMATION-EXCHANGE` → W8.1
- `W-DELIVERABLE-HANDOVER` → W8.2

## References that should not be created from the catalogue alone

The following are either broader composites, role specializations, governance concepts, or unsupported placeholders and should remain unresolved until targeted source review establishes whether a separate source workflow exists:

- `W-GOVERNED-PRODUCTION-INTAKE`
- `W-STANDARDS-EVOLUTION`
- `W-GOVERNANCE-ARBITRATION`
- `W-STANDARDS-REVIEW-PIPELINE`
- `W-CDE-MAINTENANCE`
- `W-CDE-GOVERNANCE`
- `W-BEP-AUTHORING`
- `W-MODEL-AUTHORING`
- `W-DISCIPLINE-AUTHORING`
- `W-MODELING-CRAFT`
- all discipline-specific `*-BIM-AUTHORING` references
- `W-POOLED-CAPACITY-DISPATCH`
- `W-TECH-PORTFOLIO-COORDINATION`
- `W-TECH-MILESTONE-RELEASE`
- `W-PARAMETER-OPERATIONS`
- `W-REGISTRY-GOVERNANCE`
- `W-MIDP-MANAGEMENT`
- `W-PROJECT-DELIVERY-PLANNING`
- `W-SCHEDULE-ALIGNMENT`
- `W-TIDP-DELIVERY`
- `W-COORDINATION-RESOLUTION`
- `W-ZONE-SCOPE-GATEKEEPING`
- `W-CONSTRUCTABILITY-REVIEW`
- `W-MODEL-VALIDATION-ACCEPTANCE`
- `W-DESIGN-REVIEW`
- `W-SUBMITTAL-APPROVAL`
- `W-DOCUMENTATION-APPROVAL`
- `W-CLIENT-REVIEW-ACCEPTANCE`
- `W-STAGE-GATES`
- `W-ZONE-SHOWSET-PACKAGE-RELEASE`
- `W-TOOL-VALIDATION`
- `W-AUTOMATION-APPROVAL`

## Migration recommendation

1. Preserve the source W0-W8 workflow catalogue as the migration authority for workflow structure.
2. Do not create one canonical workflow per historical semantic `W-*` reference.
3. First migrate the explicit source workflows as governed workflow objects, preserving source status and provenance.
4. Then repair role references contextually to the appropriate canonical workflow IDs.
5. Retain composites and unsupported references in the forward register until targeted source search confirms or rejects them.
6. Remove a forward declaration only after every live reference to that ID has been repaired or the corresponding governed object has been migrated.
7. Keep technical QA/verification separate from approval/acceptance authority even when the source catalogue places approve/reject language inside a QA workflow.

## Immediate next migration slice

Migrate the high-value explicit workflows first:

1. W1.1 Project Model Setup
2. W1.2 CDE / ACC Project Setup
3. W5.1 Model Coordination
4. W5.2 Issue Tracking
5. W7.2 QA/QC Validation
6. W8.1 IFC / Exchange Export
7. W8.2 Project Closeout

These seven resolve or contextualize the largest number of existing forward references while touching S3-S8 backbone objects already present in the repository.
