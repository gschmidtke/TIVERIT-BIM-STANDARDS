# S1 / S9 Curator Migration Proposal

Status: migration review only; non-canonical.

## Purpose

This proposal converts the S1 and S9 source extraction into a repository-native migration plan. It does not promote any object to canonical authority.

## S1 proposed decomposition

S1 should not be copied from the legacy Confluence layer stack. The repository already has a different accepted governance architecture. The recommended repository-native decomposition is:

1. **S1 constitutional/doctrine parent** — declares the boundary between organizational standards and project execution, authority as a governance decision, permitted-use/reliance principles, lifecycle intent, and delegation to downstream standards.
2. **Role authority references** — S1 references the existing governed role registry and role definitions rather than enumerating all roles again.
3. **Downstream reliability references** — S1 points to S2 for information demand and LOD/LOI, S5 for coordination/readiness evidence, and S7 for formal exchange/acceptance and permitted reliance.
4. **Open model-use taxonomy gap** — required versus optional model uses by phase/stakeholder remains unresolved and must not be invented during migration.

### S1 source resolutions

- Historical contractual-precedence gap: resolved in later S1 source.
- Historical permitted-use/reliance gap: resolved constitutionally and delegated downstream.
- Historical role-matrix gap: resolved architecturally through dedicated role registry/definitions; further RACI/function matrices may remain future enhancements.
- Historical reliability/suitability gap: delegated to downstream standards and substantially represented in migrated S2/S5/S7 content.
- Model-use taxonomy gap: still open.

## S9 proposed decomposition

Recommended canonical structure:

1. **S9 parent standard** — tool legitimacy, tool-domain authority, boundary discipline, automation-as-execution, governed interoperability, and toolchain stability.
2. **Tool Authority Matrix registry** — separate governed controlled artifact; initially unpopulated until curator accepts source-supported rows.
3. **Automation Registry** — separate governed controlled artifact; scaffold fields are source-supported, but real automation entries require explicit curated data.
4. **Tool/domain specializations** — Revit, manufacturing authoring/repository, electrical/controls, constrained documentation, and cross-tool exchanges inherit the S9 parent and may have their own standards/workflows where source material justifies them.
5. **Execution content** — scripts, add-ins, export procedures, UI actions and configurations remain L5-L7 execution/configuration objects and must not be embedded in the S9 parent.

## Source-supported Tool Authority candidates

The source supports the following candidate authority relationships for later curator approval:

- Revit → BIM spatial context and multidisciplinary BIM authoring.
- Inventor → manufacturing/fabrication geometry and detailed mechanical authoring.
- Vault → manufacturing design lifecycle, released manufacturing data, revision/release provenance.
- EPLAN → electrical connectivity, circuits, loads, voltage/phase, panel hierarchy and source electrical logic.
- BIM authoring model → physical device placement, spatial coordination, cable tray/conduit routing geometry and coordination presentation.
- AutoCAD → constrained documentation/output only where explicitly designated; never primary BIM or manufacturing authority.
- Automation → no independent authority; execution only under governed rules.

These are migration candidates, not yet canonical Tool Authority Matrix rows.

## Critical distinctions to preserve

1. **Human authority ≠ tool authority.** A tool being authoritative for an information domain does not grant a person approval authority.
2. **Tool authority ≠ CDE record authority.** A source authoring system may own design truth while the CDE owns the formally published/transmitted project information container.
3. **Mirroring ≠ authority transfer.** Data copied into another system remains governed by its declared source unless a governed transfer of authority occurs.
4. **Automation ≠ authority.** Scripts, APIs, add-ins and agents execute or inspect governed rules; they do not create or redefine them.

## Proposed curator decisions

- **D-S1-01** — Accept repository-native S1 decomposition rather than legacy layer-stack reproduction.
- **D-S1-02** — Accept that role enumeration remains in the existing role registry and is referenced by S1.
- **D-S1-03** — Keep model-use taxonomy as an explicit unresolved gap.
- **D-S9-01** — Accept S9 parent migration as the next canonical standard slice.
- **D-S9-02** — Keep Automation Registry and Tool Authority Matrix as separate governed artifacts.
- **D-S9-03** — Treat the source-supported tool/domain rows as candidate data requiring explicit curator acceptance before registry population.

No decision in this file is considered accepted merely by the file's existence.

## Provenance

Primary Confluence page IDs: 2326578, 2818168, 4456460, 7700534, 2228282, 2719840, 5308417, 4554779, 6127640, 7241747, 7307304, 6357114.

Repository cross-checks: `GOVERNANCE.md`, `ARCHITECTURE.md`, existing role registry and `ROLE-TOOL-AUTHORITY-001`.
