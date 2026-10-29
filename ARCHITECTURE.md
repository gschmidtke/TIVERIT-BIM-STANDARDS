# TIVERIT BIM Standards Repository Architecture

## Object-oriented repository

The repository does not reproduce the Confluence page tree. Canonical content is organized by governance function and object type.

```text
constitution/      L1-L3 authority, doctrine, architecture
standards/         L4 governed normative standards
workflows/         L5 executable workflows/processes
instructions/      L6 tool and user instructions
configurations/    L7 presets and machine payloads
registries/        governed controlled vocabularies and indexes
modules/           S1-S9 semantic module manifests
engine/            automation engines that consume governed data
schemas/           JSON Schema definitions
provenance/        immutable source traceability
migration/         migration mappings, gaps, and review artifacts
archive/           non-canonical historical material
dist/              generated distributions and documentation
inbox/             public proposal/contribution surface
```

## Layer model

The L1-L7 layer is a governance coordinate carried by each object. It is not merely a folder location.

## Module model

S1-S9 are semantic coordinates. An object may belong to multiple modules. Module membership is therefore stored as metadata rather than inferred exclusively from file paths.

## Canonical object envelope

Canonical JSON objects share a common envelope defined by `schemas/base-object.schema.json`:

- `id`
- `legacy_ids`
- `type`
- `title`
- `status`
- `version`
- `effective_date`
- `supersedes`
- `superseded_by`
- `authority`
- `layer`
- `modules`
- `scope`
- `relationships`
- `verification`
- `provenance`

Object identity and object version are separate dimensions. The stable `id` persists across governed revisions. `version` records the governed content revision, while `effective_date` records when that revision becomes authoritative. Migration candidates and drafts may omit those lifecycle values while source reconciliation is incomplete; an object cannot be promoted to `active` unless both `version` and `effective_date` are present and valid.

## Reference integrity

Canonical-looking cross-references are validated against IDs present in the repository. References to governed objects that are not yet migrated must be declared individually in `migration/reference-forward-declarations.json` with a rationale. Wildcard exemptions are not permitted. When a referenced object is migrated or a stale source reference is repaired, its forward declaration must be removed.

## Migration rule

Confluence remains source authority during migration. GitHub objects are `migration_candidate` until reviewed and promoted.

Canonical identifiers use `TIVERIT` exclusively. Historical traceability is retained through neutral source metadata such as Confluence page IDs, versions, and source links.
