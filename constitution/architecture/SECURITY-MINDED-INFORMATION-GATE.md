# Security-Minded Information Gate

Status: migration candidate
Authority: repository governance
Source: curated resolution of STAR-T-GATE Inbox #13 FIND-SEC-004
External reference: ISO 19650-5:2020 identity/status only via TIVERIT-EXTERNAL-STANDARDS-REGISTRY-001

## Purpose

This gate defines how TIVERIT determines whether project information requires security-minded handling without importing or reconstructing protected external-standard requirements.

## Scope boundary

TIVERIT recognizes security-minded information management as a governed project concern. TIVERIT does not, by this gate alone, claim implementation of or conformance with ISO 19650-5.

Security requirements become project-governing only when established by an applicable authority or instrument, including law/regulation, contract or appointment, appointing-party/client information requirements, explicit organizational/project adoption, or another authorized project security instrument.

## Gate

Before information-management workflows assume unrestricted ordinary handling, determine whether a security requirement or sensitivity condition has been established.

The gate result shall be one of:

- `security_requirements_applicable` — an authoritative security requirement or sensitivity condition is identified;
- `no_security_requirement_identified` — the available governing instruments have been checked and no security requirement is identified;
- `security_applicability_unresolved` — required project evidence is missing, ambiguous, contradictory, or unavailable.

A missing answer shall not be normalized to `no_security_requirement_identified`.

## Required evidence when applicable

Record, where available:

- the governing instrument or authority;
- applicable external standard identity and edition if incorporated;
- affected information, information container, system, asset, zone, role, workflow, or deliverable at the level authorized for recording;
- responsible project authority for interpreting or approving security controls;
- project control or instruction that implements the requirement;
- unresolved conflicts or evidence gaps.

Do not store sensitive project content in this public repository merely to prove that a security requirement exists.

## Routing behavior

If `security_requirements_applicable`, route the information/workflow to the authorized project security controls and restrict downstream assumptions to what those controls actually establish.

If `security_applicability_unresolved`, stop any reasoning or automation that depends on knowing the security state and request or route for the missing authoritative evidence.

If `no_security_requirement_identified`, ordinary TIVERIT information-management rules may proceed, but the result is not a declaration that the project, asset, or information is inherently non-sensitive.

## External-standard boundary

ISO 19650-5:2020 is registered as an external reference. Its existence does not make it automatically applicable. Where a governing instrument incorporates it, the exact applicable requirements must be verified from authorized access and mapped through the external-standard alignment mechanism. TIVERIT shall not invent clause content or infer compliance from terminology similarity.

## Project implementation boundary

This gate establishes routing and evidence requirements only. It does not prescribe project-specific access groups, classifications, permissions, encryption, retention, redaction, distribution, incident response, or other security controls. Those controls require their own authorized project or organizational source.

## Reasoning rule

Security is a gate before unrestricted information handling, not a retroactive label. Unknown security applicability remains explicit and must not be converted into permission by default.
