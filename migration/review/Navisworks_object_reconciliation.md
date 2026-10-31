# Navisworks Object Reconciliation — Round 001

**Status:** curator reconciliation record  
**Source:** Confluence BST  
**Target:** current `main` of `gschmidtke/TIVERIT-BIM-STANDARDS`  
**Date:** 2026-10-31

## Curator conclusion

Navisworks was incorrectly classified at domain level as `migration_missing`. Current `main` already contains a normalized Revit-to-Navisworks export instruction and a Navisworks coordination workflow, plus general S5 coordination, ACC records/exchange, clash-type, and issue-lifecycle objects. The correct domain disposition is therefore **`partially_migrated`**.

This round reconciles the source objects individually and migrates only the bounded content that is both source-supported and not already represented.

## Source-to-repository reconciliation

| Confluence page | Source maturity | Current-main relationship | Disposition | Curator action |
| --- | --- | --- | --- | --- |
| 8093711 — JSON - Navisworks Export Settings | machine-readable instruction set | `TIVERIT-BIM-INS-REVIT-NAVIS-EXPORT-001` preserves the five instruction steps and provenance | `migrated` | No duplicate object. Retain unresolved Export Preset Registry dependency. |
| 8126475 — S5 – Navisworks Project Setup for Coordination | governed narrative standard | Existing Navisworks workflow compresses setup but does not preserve the source setup requirements as a distinct object | `partially_migrated` → migrated in this round | Add `TIVERIT-BIM-STD-S5-NAVISWORKS-PROJECT-SETUP-001`. |
| 6324279 — S5 – Navisworks Clash Detection Matrix – Standard Setup | governed narrative standard | Existing clash-type registry and workflow cover categories/execution but not matrix/profile metadata and traceability | `partially_migrated` → migrated in this round for governed fields | Add `TIVERIT-S5-NAVISWORKS-CLASH-MATRIX-FIELDS-001`; do not invent discipline pairs or numeric tolerances. |
| 10944513 — Navisworks Federation & Coordination Standards | DRAFT with unresolved TODOs | Mature principles overlap S6 and the Navisworks workflow | `source_evidence_only` | Do not promote exact append toggles, thresholds, folder maps, role assignments, or other unresolved TODO content. |
| 8159247 — Metadata and Export Settings for Navisworks | DRAFT with unresolved TODOs | Explicitly points to page 8093711 as governed values source; current export instruction already carries that authority | `merged_into_other_object` | Do not create competing export profiles from unresolved draft values. |
| 6357084 — ACC Model Coordination vs Navisworks – Clash & Issue Workflows | DRAFT / REVIEW decision | Current Navisworks workflow and S5 ACC objects already preserve the system-of-record boundary | `merged_into_other_object` | Do not newly elevate the draft tool-preference recommendation. |
| 7864324 — Metadata and Deliverables Standards for Navisworks | DRAFT with extensive TODOs | General S7 deliverable/handover governance exists; source-specific record criteria and storage remain unresolved | `source_evidence_only` | Keep as evidence for later S7 reconciliation; do not promote draft folder paths or record classifications. |
| 6357099 — Gaps in Navisworks | gap inventory | Historical source-side gap list | `source_evidence_only` | Use only to test whether gaps were subsequently addressed. |

## Governed content added in this round

### Navisworks project setup

The new project-setup standard preserves source-backed requirements for:

- traceable NWF/coordination-container provenance;
- valid governed source-model state and identity;
- shared-coordinate alignment before checks;
- prohibition of ad-hoc transforms as permanent fixes;
- documented, time-bounded temporary transforms tied to source correction;
- governed/reproducible search and selection sets;
- contextual review/viewpoint evidence;
- pre-use integrity validation;
- blocking reliance on invalid configuration unless governed deviation exists;
- traceable shared-configuration changes and authority boundaries.

It does **not** invent project folders, exact software toggles, numeric tolerances, or unresolved owner/approver assignments.

### Clash matrix

The new registry preserves the matrix/profile fields that must remain traceable when Navisworks clash results support governed coordination:

- test identity;
- model/set scope;
- check type;
- project tolerance basis;
- priority/criticality;
- grouping/deduplication basis;
- matrix/profile version;
- coordination cycle;
- responsibility/routing basis;
- approved deviations.

It deliberately does not invent a discipline-pair matrix or enterprise numeric tolerance values.

## Remaining Navisworks gaps after Round 001

The following remain unresolved and should not be silently promoted:

1. Concrete governed export-preset values / preset registry.
2. Complete approved discipline-pair clash matrix and project profile values, if an enterprise default is intended.
3. Navisworks deliverable/record criteria, retention, and canonical CDE storage mappings where the source remains draft/TODO.
4. Detailed viewpoint naming/redaction/packaging rules.
5. Navisworks-specific meeting/RFI/sign-off implementation details beyond the existing S5 system-of-record boundary.
6. Executable conformance tests for NWF/NWC federation, coordinate, property, and matrix compliance.

These are now explicit residual gaps, not evidence that the whole Navisworks domain is absent.
