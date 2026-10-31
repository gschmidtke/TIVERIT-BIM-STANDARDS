# Curator Record — STAR-T-GATE Inbox #6

**Source:** `gschmidtke/STAR-T-GATE-INBOX#6`  
**Target:** `STANDARDS`  
**Source type:** `gap`  
**Curator disposition:** `held_unresolved`  
**Curator action:** establish governed migration-reconciliation control before further migration batches

## Finding

Inbox #6 identifies a real migration-control gap: the existing Confluence source inventory is not yet proven to be fully reconciled against the current `main` branch of TIVERIT-BIM-STANDARDS.

The issue is not permission to promote all source-side material automatically. It is the absence of a closed-loop reconciliation that gives every inventoried source object an explicit disposition against current `main`.

## Current-main corrections to the source-side audit

The source-side audit compared several areas against the older `build/repository-foundation` branch. Therefore its repo-gap claims must not be adopted verbatim.

Current-main checks already show partial migration in areas including:

- Revit conformance for view templates, worksets, naming, datum coordination, and parameter binding;
- a populated shared-parameter registry;
- ACC onboarding workflow content.

At the same time, current-main checks confirm material holes including:

- no dedicated Navisworks objects found;
- no Inventor-specific objects found;
- no `registries/classification/` path found.

## Curator decision

Do not create one-off RFCs from the stale branch comparison.

Instead, create and maintain a governed migration-reconciliation register. The register is the control surface for determining what is actually missing, partially migrated, superseded, merged, retained as source evidence, intentionally not promoted, or unresolved.

No source object becomes normative solely because it appears in Confluence or Inbox #6.

## Required dispositions

Every inventoried source object must eventually receive exactly one of:

- `migrated`
- `partially_migrated`
- `merged_into_other_object`
- `superseded`
- `source_evidence_only`
- `intentionally_not_promoted`
- `migration_missing`
- `unresolved_source`

## Initial reconciliation priorities

1. Navisworks / S5-S6-S7 coordination and export content — confirmed candidate for `migration_missing` at domain level; object-level source reconciliation required before promotion.
2. Inventor / S9 — confirmed candidate for `migration_missing` at domain level; object-level source reconciliation required before promotion.
3. Classification / S8 — source-side governance exists; current-main registry path is absent; object-level reconciliation required.
4. Revit style-guide content — treat as `partially_migrated` at domain level until source objects are matched to current conformance/standards/configuration objects.
5. Shared parameters — treat as `partially_migrated` at domain level because a registry exists but source completeness is not yet established.
6. ACC governance — treat as `partially_migrated` at domain level because onboarding exists but broader source-side governance must be reconciled.
7. S7 exchanges/lifecycle, BEP engine, and metadata/provenance — `unresolved_source` at domain level until object-by-object reconciliation is performed.

## Completion condition

Migration reconciliation is complete only when every inventoried Confluence source object has an explicit disposition against current `main`, and remaining migration work is generated from that reconciled delta rather than from stale branch comparisons.

Until then, Inbox #6 remains `held_unresolved` as a migration-control dependency.
