# BEP Assembly Map

This map provides a deterministic consumption path for humans and AI agents assembling a project BEP from the repository.

## 1. Establish project facts before drafting

Collect or mark unresolved:

- project name / code / location;
- appointing party, prospective or appointed lead appointed party, and relevant task teams where ISO 19650 applies;
- appointment stage and whether the document is pre-appointment or post-appointment;
- project phases / milestones;
- appointing-party exchange information requirements and other project information requirements supplied externally;
- named organizations and people;
- nominated information-management roles/functions and the governing basis for any delegation;
- CDE platform(s) and contractual system of record;
- information-container/model scope and disciplines;
- software/version, hardware and IT-infrastructure constraints or proposals;
- federation and coordinate strategy;
- required exchanges / deliverables;
- project-specific LOIN / LOD / LOI;
- delivery dates and task-team responsibilities;
- project information standard and information production methods/procedures, including proposed amendments;
- pre-appointment capability/capacity evidence, mobilization plan and information-delivery risk evidence where applicable.

Never infer missing project facts or ISO party/function mappings from a standard or TIVERIT job title.

## 2. ISO 19650-2 pre-appointment sequence when applicable

When ISO 19650-2:2018 is applicable and a pre-appointment BEP/tender response is being prepared, use clauses 5.3.2-5.3.7 as the canonical sequence. TIVERIT questions operationalize this sequence and may add supplementary project governance, but shall not replace or reorder the ISO responsibilities.

### 2.1 Pre-appointment BIM execution plan — 5.3.2

The prospective lead appointed party establishes the delivery team's pre-appointment BIM execution plan. Capture or mark unresolved:

- proposed individuals undertaking the information management function for the delivery team, including the evidence requested by the appointment process;
- information delivery strategy: approach to the appointing party's exchange information requirements, collaborative information-production objectives, organizational/commercial relationships and proposed task-team composition;
- proposed federation strategy;
- high-level responsibility matrix for information-model elements and key deliverables;
- proposed additions/amendments to project information production methods and procedures;
- proposed additions/amendments to the project information standard;
- proposed software, versions, hardware and IT infrastructure.

### 2.2 Task-team capability and capacity — 5.3.3

Each task team assesses its capability and capacity. Capture evidence concerning information-management capability, information-production capability, relevant experience, education/training, staffing capacity and available IT/hardware/infrastructure/support. Do not replace task-team assessments with a single unsupported delivery-team assertion.

### 2.3 Delivery-team capability and capacity — 5.3.4

The prospective lead appointed party aggregates the task-team assessments into a delivery-team summary covering capability to manage and produce information and capacity for timely delivery. Preserve the distinction between source task-team assessments and the aggregated summary.

### 2.4 Mobilization plan — 5.3.5

Capture proposed approach, timescales and responsibilities for mobilization, including testing production methods/procedures, task-team exchanges and delivery to the appointing party; configuring/testing project and distributed CDE arrangements; implementing/testing required technology; developing shared resources; education/training; recruitment; and support for organizations or individuals joining during the appointment.

### 2.5 Information-delivery risk register — 5.3.6

Capture risks to timely information delivery and intended management actions. At minimum route for consideration assumptions about exchange information requirements, delivery milestones, the information protocol, the information delivery strategy, adoption/amendment of the project information standard and production methods/procedures, and mobilization needed to achieve capability/capacity.

### 2.6 Tender-response compilation — 5.3.7

Treat the pre-appointment BIM execution plan, delivery-team capability/capacity summary, mobilization plan and information-delivery risk assessment as distinct governed tender-response components where available. A BEP alone shall not be represented as the complete ISO 19650-2 tender response.

## 3. Governance and authority — S1

Start with:

- `standards/S1-core-governance/TIVERIT-BIM-STD-S1-CORE-GOV-EP001.json`
- `standards/S1-core-governance/TIVERIT-BIM-STD-S1-ROLES-001.json`
- `registries/roles/role-resolution-map.json`
- role registry / individual role definitions under `registries/` and the role-definition corpus.

Use for TIVERIT governance, approval, escalation and role boundaries. Where ISO 19650 applies, task-team, lead-appointed-party and appointing-party functions remain canonical and project-specific mapping must come from appointment/BEP/RACI or equivalent governing evidence.

## 4. Information requirements and delivery planning — S2

Read:

- `TIVERIT-BIM-STD-S2-INF-REQ-EP001`
- `TIVERIT-BIM-STD-S2-PIR-001`
- `TIVERIT-BIM-STD-S2-AIR-001`
- `TIVERIT-BIM-STD-S2-LOD-LOI-001`
- `TIVERIT-BIM-STD-S2-MIDP-001`
- `TIVERIT-BIM-STD-S2-TIDP-001`
- `TIVERIT-BIM-STD-S2-SEL-GOV-001`

Use for information demand, exchange milestones, LOIN/LOD/LOI logic, Master Information Delivery Plan / Task Information Delivery Plan structure, permitted reliance and information-purpose alignment.

Project instance required: actual requirement rows, milestones, delivery dates, task-team assignments, LOIN values and external EIR/AIR/PIR content where applicable.

## 5. Production environment / CDE — S3

Read the S3 production standard plus applicable CDE/folder/permission registries and workflows. Use for ISO CDE state implementation, production versus contractual systems of record, permissions versus authority and project information-container handling.

## 6. Identity and naming — S4

Read the S4 identity/naming standard and controlled naming registries. Project-specific code sets and client overlays remain project facts.

## 7. Coordination / review — S5

Read S5 coordination, review, sign-off, gate, issue and readiness objects plus applicable workflows. TIVERIT coordination is supplementary collaborative-production governance and shall not substitute for applicable ISO approval-for-sharing, authorization or acceptance.

## 8. Collaboration, federation, linking and coordinates — S6

Read the S6 collaboration/linking/shared-coordinates standard, link registry structures and relevant implementation instructions. Capture actual federation membership, model ownership, coordinate authority and approved exceptions.

## 9. Submission, exchange and handover — S7

Read S7 submission/deliverable/handover objects and exchange workflows. Where ISO 19650-2 applies, preserve the canonical information-model delivery sequence and distinguish it from supplementary milestone or handover decisions.

## 10. Information structure / semantics — S8

Read S8 information-structure and shared-parameter governance plus relevant registries. Capture project-required property/parameter sets, classifications, bindings and exchange schemas/formats.

## 11. Software and automation authority — S9

Read S9 tool-authority standards and registries. Platform capability or automation does not create information-management decision authority.

## 12. Recommended BEP section packing order

A project BEP can be assembled in this practical order:

1. document status and appointment context;
2. project and parties;
3. objectives and information-delivery strategy;
4. governance, information-management functions and authority;
5. information requirements and LOIN;
6. federation strategy, production methods and information standard proposals;
7. high-level responsibility matrix / RACI;
8. CDE and information-state process;
9. information-container identity / naming;
10. software, versions, hardware and IT infrastructure;
11. collaboration, federation and coordinates;
12. coordination, review and issue process;
13. information structure, parameters and classification;
14. delivery planning — TIDP/MIDP where applicable to appointment state;
15. exchanges, submissions and handover;
16. deviations, unresolved inputs and approvals;
17. governing-object reference register.

For a pre-appointment ISO 19650-2 tender-response package, additionally maintain the task-team capability/capacity assessments, aggregated delivery-team capability/capacity summary, mobilization plan and information-delivery risk assessment as distinct components rather than silently folding them into the BEP.

## 13. Missing-data behavior

When the repository supplies the rule but not the project value, instantiate the relevant starter table, mark the value `TBC`, `TBD`, `not supplied` or `unresolved` as appropriate, identify the source/authority needed, and do not fill the gap with general best practice unless explicitly labelled as a proposal awaiting approval.

## 14. Pre-appointment vs post-appointment

For **pre-appointment** BEP drafting, proposed methods, resources, function assignments, technology and delivery arrangements may legitimately be proposals where the appointment process requires them. The BEP is one component of the wider tender response where ISO 19650-2:2018 applies.

For **post-appointment** BEP drafting, the pre-appointment BEP is confirmed and developed through the applicable appointment-stage process. Replace proposals with appointed/project-approved values where available and explicitly retain unresolved items as action items rather than assumptions.

The repository does not itself determine appointment facts or ISO party/function assignments. Those come from the project/contract context.
