# BEP Assembly Map

This map provides a deterministic consumption path for humans and AI agents assembling a project BEP from the repository.

## 1. Establish project facts before drafting

Collect or mark unresolved:

- project name / code / location;
- appointing party and lead appointed party;
- appointment stage and whether the document is pre-appointment or post-appointment;
- project phases / milestones;
- client/project information requirements supplied externally;
- named organizations and people;
- nominated information-management roles;
- CDE platform(s) and contractual system of record;
- model/container scope and disciplines;
- software/version constraints;
- federation and coordinate strategy;
- required exchanges / deliverables;
- project-specific LOIN / LOD / LOI;
- delivery dates and task-team responsibilities.

Never infer missing project facts from a standard.

## 2. Governance and authority — S1

Start with:

- `standards/S1-core-governance/TIVERIT-BIM-STD-S1-CORE-GOV-EP001.json`
- `standards/S1-core-governance/TIVERIT-BIM-STD-S1-ROLES-001.json`
- role registry / individual role definitions under `registries/` and the role-definition corpus.

Use for BEP sections covering governance, authority, approval, escalation, role boundaries, and the distinction between platform capability and decision authority.

Project instance required: named person/organization mapped to governed role ID.

## 3. Information requirements and delivery planning — S2

Read:

- `TIVERIT-BIM-STD-S2-INF-REQ-EP001`
- `TIVERIT-BIM-STD-S2-PIR-001`
- `TIVERIT-BIM-STD-S2-AIR-001`
- `TIVERIT-BIM-STD-S2-LOD-LOI-001`
- `TIVERIT-BIM-STD-S2-MIDP-001`
- `TIVERIT-BIM-STD-S2-TIDP-001`
- `TIVERIT-BIM-STD-S2-SEL-GOV-001`

Use for information demand, exchange milestones, LOIN/LOD/LOI logic, MIDP/TIDP structure, permitted reliance, and information-purpose alignment.

Project instance required: actual requirement rows, milestones, delivery dates, task-team assignments, LOIN values, and external EIR/AIR/PIR content where applicable.

## 4. Production environment / CDE — S3

Read:

- `standards/S3-production-environment/TIVERIT-BIM-STD-S3-PROD-EP001.json`
- applicable CDE/folder/permission registries and workflows.

Use for CDE state model, production versus contractual systems of record, folder/state mappings, permissions versus authority, and project information-container handling.

Project instance required: actual project CDE, folder/project identifiers, access assignments, contractual repository, and any approved project-specific deviations.

## 5. Identity and naming — S4

Read the S4 identity/naming standard and controlled naming registries.

Use for container identity, stable root naming, discipline/scope codes, workset syntax, and controlled vocabularies.

Project instance required: project codes, originator/discipline/location/type values, approved project-specific code sets, and any client naming overlays.

## 6. Coordination / review / acceptance — S5

Read S5 coordination, review, sign-off, gate, issue, and readiness objects plus the applicable coordination workflows.

Use for model federation review, issue handling, clash/review gates, readiness checks, sign-off distinction, and evidence needed for project acceptance decisions.

Project instance required: review cadence, participants, issue platform, acceptance authority, project thresholds where governed externally, and milestone dates.

## 7. Collaboration, federation, linking and coordinates — S6

Read the S6 collaboration/linking/shared-coordinates standard, link registry structures, and Revit implementation instructions where relevant.

Use for model ownership, read-only reference behavior, link registration, standalone coordination/spatial authority, shared-coordinate relationships, and federation structure.

Project instance required: actual model list, owners, discipline/source containers, federation membership, coordinate authority, survey/base-point source, link relationships, and approved exceptions.

## 8. Submission, exchange and handover — S7

Read the S7 submission/deliverable/handover objects and exchange workflows.

Use for what may be relied upon, published-state conditions, exchange packaging, submission versus acceptance, delivery evidence, and handover requirements.

Project instance required: deliverable schedule, file/formats, exchange dates, recipients, contractual acceptance process, and client-specific submission channels.

## 9. Information structure / semantics — S8

Read S8 information-structure and shared-parameter governance, plus relevant registries.

Use for parameters, stable parameter identity, classification, semantics, bindings, and information consistency.

Project instance required: project-required property/parameter sets, classification selections, category/binding scope, and information-delivery purpose.

## 10. Software and automation authority — S9

Read:

- `standards/S9-tool-authority-automation/TIVERIT-BIM-STD-S9-TOOLS-AUTHORITY-EP001.json`
- `registries/tool-authority/REG-S9-TOOL-AUTHORITY-001.json`
- `registries/automation/REG-S9-AUTOMATION-001.json`

Use for tool-authority boundaries and automation governance.

Project instance required: actual approved software products, versions, plug-ins, exchange versions, automation used in production, and owner/support role.

Until tool-authority entries are populated and approved, product assignments remain project decisions and must not be inferred from source-era examples.

## 11. Recommended BEP section packing order

A project BEP can be assembled in this practical order:

1. document status and appointment context;
2. project and parties;
3. objectives / project information context;
4. governance, roles and authority;
5. information requirements and LOIN;
6. delivery planning — MIDP/TIDP;
7. CDE and information-state process;
8. information-container identity / naming;
9. production methods and model breakdown;
10. collaboration, federation and coordinates;
11. coordination, review and issue process;
12. software/version/tool table;
13. information structure, parameters and classification;
14. exchanges, submissions and handover;
15. responsibility / RACI table;
16. deviations, unresolved inputs and approvals;
17. governing-object reference register.

## 12. Missing-data behavior

When the repository supplies the rule but not the project value:

- instantiate the relevant starter table;
- mark the value `TBC`, `TBD`, or `not supplied`;
- identify who has authority to supply/approve it;
- do not fill the gap with general best practice unless the BEP explicitly labels it as a proposal awaiting approval.

## 13. Pre-appointment vs post-appointment

For **pre-appointment** BEP drafting, proposed methods, resources, role assignments, software and delivery plans may legitimately be offered as proposals where the appointment process requires them.

For **post-appointment** BEP drafting, replace proposals with appointed/project-approved values wherever those are available and explicitly retain unresolved items as action items rather than assumptions.

The repository does not itself determine appointment facts. Those come from the project/contract context.
