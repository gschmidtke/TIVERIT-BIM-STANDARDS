# TIVERIT BIM Standards

TIVERIT BIM Standards is a governed, machine-readable BIM standards repository for human use, automation, validation, AI-assisted workflows, Revit, Autodesk Construction Cloud, and related BIM systems.

## Position in the reasoning stack

This repository is the **normative governance layer** between resolved purpose and operational production logic.

```text
USG
Problem / purpose / required resolution
    ↓
TIVERIT BIM Standards
Normative requirements / authority / compliance evidence
    ↓
ARPL
Operational precedent / Revit production logic / failure memory
    ↓
Capability lookup / tool API
    ↓
Execution
    ↓
Observed evidence
    ↓
Validation against purpose + standard
```

Public repositories:

- USG — https://github.com/gschmidtke/USG — resolves what must be achieved and why before tool selection.
- TIVERIT BIM Standards — https://github.com/gschmidtke/TIVERIT-BIM-STANDARDS — defines what is required or permitted, who has authority, and what evidence proves compliance.
- ARPL — https://github.com/gschmidtke/ARPL — records how professional Revit production tasks have been executed, what failed, and how successful results were verified.

An AI or human inquiry should be routed to the repository that owns the question. If an inquiry spans layers, use the order **purpose → normative constraint → operational precedent → technical capability → execution → validation**. See `AGENTS.md`, `constitution/architecture/REASONING-STACK-ROUTING.md`, and `registries/system-routing/TIVERIT-SYSTEM-ROUTING-001.json`.

## Governance model

This repository separates public contribution from canonical authority.

- `inbox/` is the future public contribution surface.
- Canonical standards, schemas, registries, workflows, instructions, configurations, and engine content are curator-controlled.
- Public contribution does not directly modify canonical authority.
- Promotion from `inbox/` into canonical content requires curator review, validation, and an explicit governed change.

During the repository build and migration phase, the repository remains public so the architecture can be inspected and refined openly.

## Source migration

The initial corpus is being migrated from the TIVERIT BIM Standards Confluence space. The migration inventory covers 284 pages and preserves the existing S1–S9 modular framework, L1–L7 governance architecture, role definitions, workflows, registries, machine-readable assets, and BEP automation components.

## Canonical namespace

Canonical identifiers use the `TIVERIT` namespace. Historical traceability is preserved through neutral Confluence page IDs, versions, and source links rather than retired organization naming.

## Core principle

The repository is object-oriented rather than page-oriented. It distinguishes constitutional and external authority, normative standards, workflows, tool/user instructions, configurations and presets, registries, automation/engine components, and source provenance.

## Status

Repository foundation and schema v0.1 are under construction. Confluence remains the source authority during migration until the canonical GitHub corpus is validated and formally cut over.
