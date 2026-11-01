# Operational-Phase Information Gate

Status: migration candidate
Authority: repository governance
Source: curated resolution of STAR-T-GATE Inbox #13 FIND-OPE-007
External reference: ISO 19650-3:2020 identity/status only via TIVERIT-EXTERNAL-STANDARDS-REGISTRY-001

## Purpose

This gate defines how TIVERIT determines whether an information-management activity belongs to, crosses into, or depends on the operational phase of an asset without importing or reconstructing protected external-standard requirements.

## Scope boundary

TIVERIT recognizes operational-phase information management as a legitimate governed domain. This gate does not, by itself, claim that TIVERIT implements or conforms with ISO 19650-3:2020.

TIVERIT delivery-phase requirements may produce information intended for later operational use. That downstream purpose does not automatically place the operational process itself within TIVERIT's governed scope.

Operational requirements become project-governing only when established by an applicable authority or instrument, including law/regulation, contract or appointment, appointing-party/client information requirements, explicit organizational/project adoption, asset-management requirements, or another authorized operational information instrument.

## Gate

When a workflow, information container, exchange, deliverable, role, or requirement may extend beyond delivery into operation, determine its operational-phase applicability before assuming that delivery governance also governs operational use.

The gate result shall be one of:

- `operational_requirements_applicable` — an authoritative operational-phase requirement is identified;
- `delivery_to_operation_interface_only` — TIVERIT governs a delivery output or handover interface, while the downstream operational process remains outside the presently established TIVERIT scope;
- `no_operational_requirement_identified` — governing instruments have been checked and no operational-phase requirement is identified for the activity;
- `operational_applicability_unresolved` — required project evidence is missing, ambiguous, contradictory, or unavailable.

A missing answer shall not be normalized to `no_operational_requirement_identified`.

## Required evidence when applicable

Record, where available:

- the governing instrument or authority;
- applicable external standard identity and edition if incorporated;
- affected asset, information container, exchange, system, role, workflow, or deliverable;
- the boundary between delivery responsibility and operational responsibility;
- responsible project or asset authority for interpreting or approving operational information requirements;
- project or organizational control/instruction implementing the requirement;
- unresolved conflicts or evidence gaps.

## Routing behavior

If `operational_requirements_applicable`, route the activity to the authorized operational information-management controls and do not infer those controls from delivery-phase TIVERIT rules.

If `delivery_to_operation_interface_only`, TIVERIT may govern the delivery-side preparation, validation, exchange, or handover requirement that is already independently established, but shall not infer continuing operational governance after the defined interface.

If `operational_applicability_unresolved`, stop any reasoning or automation that depends on knowing the operational governance state and request or route for authoritative evidence.

If `no_operational_requirement_identified`, ordinary in-scope TIVERIT rules may proceed without creating an implied operational-phase obligation.

## External-standard boundary

ISO 19650-3:2020 is registered as an external reference. Official ISO metadata identifies it as the published Edition 1 operational-phase standard and currently subject to revision. ISO/DIS 19650-3 Edition 2 is under development and is change-monitoring evidence only unless an authorized governing instrument explicitly adopts it.

Where a governing instrument incorporates an external edition, exact applicable requirements must be verified from authorized access and mapped through the external-standard alignment mechanism. TIVERIT shall not invent clause content or infer compliance from terminology similarity.

## Revision boundary

The developing ISO 19650 revision must not silently rewrite TIVERIT scope. A future published edition or restructured ISO 19650 process requires an explicit impact review through the external-standards gateway before TIVERIT mappings or scope declarations change.

## Reasoning rule

Handover is an interface, not an automatic transfer of governance. TIVERIT shall distinguish information prepared for operation from governance of the operational process itself, and unresolved operational applicability remains explicit.
