# Repository Governance

## Authority model

During migration, Confluence remains the source authority. GitHub contains migration candidates and validated canonical objects until formal cutover.

After cutover, the canonical GitHub corpus becomes the governing source of truth.

## Public contribution model

This repository separates public contribution from canonical authority.

- `inbox/` is the public proposal surface.
- Canonical content is curator-controlled.
- Public contributors may propose additions or changes through `inbox/` and pull requests.
- Public contribution does not directly alter governed standards.
- Promotion from `inbox/` into canonical content requires curator review, validation, provenance checks, and an explicit governed change.

## Curator boundary

The following areas are curator-controlled:

- `constitution/`
- `standards/`
- `workflows/`
- `instructions/`
- `configurations/`
- `registries/`
- `modules/`
- `engine/`
- `schemas/`
- `provenance/`
- `migration/`
- `archive/`
- `dist/`

Only curator sessions should modify or promote content in these areas once the repository enters governed operation.

## Namespace policy

Canonical identifiers use `TIVERIT` exclusively.

Historical traceability is preserved through neutral source metadata such as Confluence page IDs, versions, and source links. Retired organization naming is not stored in repository content.

## L1-L7 governance layers

- L1 — external authority and reference standards
- L2 — doctrine and constitutional principles
- L3 — architecture, charters, and structural definitions
- L4 — governed normative standards
- L5 — executable workflows and processes
- L6 — tool and user instructions
- L7 — configurations, presets, and machine payloads

## S1-S9 modules

S1-S9 remain semantic classifications and may be multi-valued. They are not treated as exclusive folder ownership.
