# S6 Migration Review — Collaboration, Linking & Shared Coordinates

## Status
S6 is integrated as a `migration_candidate` vertical slice. Source facts, accepted curator decisions, implementation-layer boundaries, and unresolved gaps remain explicitly separated.

## Migrated canonical candidates
- `TIVERIT-BIM-STD-S6-COLLAB-LINK-COORDS-EP001` — L4 tool-neutral S6 standard.
- `BIM-STD-CF-001` — L5 standalone coordination-file governance under S6 ownership.
- `TIVERIT-S6-LINK-REGISTRY-001` — L7 project link-registry migration candidate containing only source-evidenced fields.

## Accepted curator decisions
### D-14 — Standalone Coordination File belongs to S6
`BIM-STD-CF-001` is canonically owned by S6 because it governs shared coordinates and project datums. S5 consumes verified spatial output for coordination intake.

### D-15 — Coordinate authority flows outward from the coordination file
Discipline models consume/acquire the approved spatial framework from `BIM-STD-CF-001`. Peer-to-peer coordinate publication is not treated as an equivalent authority path.

### D-16 — Tool-neutral L4; tool-specific mechanics at L6
S6 L4 governs required outcomes and authority boundaries. Revit Central/Local mechanics, worksets, and specific coordinate commands remain implementation-layer instructions and do not redefine the tool-neutral standard.

### D-17 — Federation responsibilities split by governance owner
S6 owns spatial alignment and link/federation prerequisites. S5 owns clash/review/sign-off activity. S3 owns CDE storage, folder state, and platform administration.

## Cross-slice boundaries
- S2 defines information demand, MIDP/TIDP obligations, and required model roster.
- S3 provides governed CDE locations and container state.
- S4 defines stable container identity, discipline codes, and workset naming syntax.
- S6 governs runtime link relationships, spatial alignment, and collaboration mechanics.
- S5 consumes S6-verified link and spatial state for Gate A coordination intake.
- S7 consumes verified spatial relationships for formal exchange/handover.
- S8 supplies semantic/parameter definitions consumed by S6 without schema redefinition.

## Open source gaps retained
1. `GAP-S6-01` — machine-readable Link Registry remains incomplete as a runtime specification.
2. `GAP-S6-02` — step-by-step coordinate establishment procedure remains draft/preview source material.
3. `GAP-S6-03` — no governed exception model for Overlay vs Attachment.
4. `GAP-S6-04` — no discipline-specific Room Bounding governance.
5. `GAP-S6-05` — persistent cloud-link identity / URN handling is not formally specified.

Additional source omissions remain visible for default loaded state and phase-mapping behavior.

## Roles
S6 strengthens existing governed role boundaries:
- Project BIM Manager: spatial authority and coordinate-change authority.
- Project BIM Coordinator: Link Registry enforcement, spatial verification, federation intake, and deviation reporting.
- CDE Manager: platform/folder/permission provisioning.
- Information Manager: WIP/Shared transition and audit-trail governance.
- Discipline Lead: discipline compliance and spatial onboarding.
- Model Author: worksharing execution and governed link placement.
- QA/QC Authority: independent link/coordinate/workset audit.

Observed source labels such as Client BIM Manager, Delegated Coordinator, Model Manager / BIM Lead, Documentation Team Lead, and BIM Support Contact are not promoted as new internal role IDs.

## Tool-specific material not promoted into L4
Revit worksharing and collaboration mechanics and Navisworks federation instructions remain source implementation material. They may be migrated later as L6/L5 tool implementations after the tool-domain architecture is finalized.

## Automation potential
The source package identifies machine-checkable opportunities including coordinate-drift checks, link-workset containment, prohibited workset names, coordination-file geometry checks, link-position verification, and governed link-registry reconciliation. These are candidates for future validation/ZEN implementation and do not become executable authority merely by being listed here.
