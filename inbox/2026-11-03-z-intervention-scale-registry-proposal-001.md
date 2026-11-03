# Standards Intake — Z0–Z4 Intervention-Level Classification

**Status:** INTAKE — CURATION REQUIRED  
**Date:** 2026-11-03  
**Source:** Owner T-System / Z-System naming proposal  
**Curator preliminary disposition:** APPROPRIATE CANDIDATE — DO NOT MODIFY REGISTRY YET  
**Owning domain:** S9 Tool Authority / Automation  
**Candidate object:** `registries/automation/REG-S9-AUTOMATION-001.json`

## Purpose

Evaluate whether the proposed Z0–Z4 human-intervention scale should become a governed field in the S9 Automation Registry.

This intake is **separate from the BPL naming-adoption decision**. T-System and Z-System identity belongs primarily in BPL. Standards should govern only the automation-classification semantics needed for governed BIM production.

## Current registry state

`REG-S9-AUTOMATION-001` is currently a `migration_candidate` / `migration_candidate_only` registry spine with no populated automation entries. Its current record schema governs identity, scope, tool/platform, governing references, owner role, version, governance status, inputs/outputs, risk classification, approval reference and evidence-logging expectations.

No intervention-level field currently exists.

## Proposed classification

The intervention level SHALL describe **human intervention required during the bounded governed task envelope**. It SHALL NOT express intelligence, reliability, professional validity, governance authority or ARPL precedent maturity.

Candidate values:

- `Z0` — manual: human performs the task; automation absent or non-operative.
- `Z1` — assisted: automation provides guidance or partial action; human remains primary operator/decision-maker.
- `Z2` — step-confirmed: bounded automation steps require human confirmation at defined gates.
- `Z3` — supervised autonomous/batch: after authorized start, automation can execute the bounded workflow without step-by-step confirmation under defined supervision/monitoring and exception handling.
- `Z4` — zero intervention within envelope: after authorized start, the nominal bounded workflow requires no human input through defined completion and validation; interrupt/escalation remains available and required human acceptance/sign-off remains separately governed.

## Candidate schema additions

Curator should assess fields equivalent to:

- `intervention_level` — enum `Z0`–`Z4`;
- `task_envelope` or governed reference defining what the level applies to;
- `intervention_level_evidence` — evidence references supporting the declared level;
- `interrupt_authority` — who/what may stop the automation;
- `exception_escalation` — required behavior when nominal execution cannot continue;
- `human_signoff_required` — whether and where acceptance/approval remains human;
- `level_assessed_on` / version linkage so an automation version cannot inherit a level without evidence.

Exact field names remain a curator/schema-design decision.

## Promotion / demotion rule to design

An automation SHALL NOT self-declare a higher Z level merely because it technically runs unattended.

Promotion should require evidence appropriate to scope and risk, including as applicable:

- bounded task envelope;
- governing references and authority;
- repeat execution evidence;
- failure / exception behavior;
- validation coverage and acceptance criteria;
- interrupt / escalation behavior;
- evidence / audit logging;
- rollback / recovery expectations;
- approval reference;
- known limitations / excluded conditions.

Evidence contradiction or changed scope/version must be capable of lowering or invalidating a previously assigned level.

## Separation requirements

The schema SHALL preserve these distinctions:

- `intervention_level` ≠ `governance_status` (`draft`, `pilot`, `approved`, `deprecated`);
- `intervention_level` ≠ risk/impact classification;
- `intervention_level` ≠ ARPL precedent/evidence maturity;
- `Z4` ≠ permission to execute;
- `Z4` ≠ compliance or professional acceptance;
- `Z4` ≠ removal of human interrupt, escalation or sign-off authority.

A Z4 automation could still be draft, high-risk, unauthorized for a particular project, or supported by weak precedent. Those states must remain independently represented.

## Current claim hold

Until this schema is curated and actual automation entries are assessed against evidence, Z0–Z4 remains a **proposed classification system**, not a certification already granted to ZEN or another automation.

A performance observation, unattended run, or successful batch may be evidence input but does not automatically assign Z3 or Z4.

## Curator next action

1. Check compatibility with `TIVERIT-BIM-STD-S9-TOOLS-AUTHORITY-EP001`, `REG-S9-TOOL-AUTHORITY-001`, the generic registry schema, and current S9 authority semantics.
2. Reconcile Claude / ARPL-curator feedback after it returns through BPL PM.
3. Decide whether intervention level belongs directly in `REG-S9-AUTOMATION-001`, in an adjacent governed field-definition object, or requires a schema extension first.
4. Only after curation, implement the smallest machine-readable change and appropriate conformance coverage.
