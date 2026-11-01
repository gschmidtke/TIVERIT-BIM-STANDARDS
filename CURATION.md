# TIVERIT BIM Standards Curation Contract

TIVERIT BIM Standards is publicly readable and accepts external learning through `inbox/**`, while canonical standards content remains curator-managed.

## Core principle

> Raw proposals may enter through the Inbox. Canonical changes occur only after curator review, classification, normalization, provenance checks, validation, and explicit acceptance.

Nothing in `inbox/` is authoritative merely because it exists there or because an Inbox pull request has been merged.

## Curator mode

Canonical repository areas are edited only in curator sessions. The curator may be a human or an AI acting under the repository owner's direction.

The curator must:

1. Read the submission or requested change in context and preserve its actual meaning.
2. Check current standards, workflows, instructions, registries, configurations, schemas, conformance assets, guides, and migration records before creating a new concept.
3. Classify content according to `constitution/architecture/CONTENT-CLASSIFICATION-DOCTRINE.md`.
4. Separate source facts, curator decisions, and unresolved issues.
5. Preserve source and contributor provenance.
6. Prefer extension of existing governed objects over duplication or new top-level architecture.
7. Record conflicts and gaps explicitly rather than silently reconciling them.
8. Run schema/reference validation, executable conformance checks where applicable, and human-readable rendering before considering the curation pass complete.
9. Keep project-specific or client-specific facts out of reusable canonical rules unless deliberately modeled as configurable/project-instance data.
10. Escalate new normative or architectural choices to the repository owner when they are not already established by source authority or an accepted curator decision.
11. Apply the Repository Freshness Gate before asserting that governed content is missing, contradictory, duplicated, or incomplete.

## Repository Freshness Gate

A repository gap or conflict claim is not curator-ready until the evaluator has checked the current canonical repository state during the current analysis session.

For every repository gap analysis, the evaluator must:

1. Resolve the canonical repository and its current default/canonical branch rather than relying on a previously used working branch, cached webpage, prior search result, or remembered repository state.
2. Fetch and record the current canonical branch HEAD commit SHA used as the comparison baseline.
3. Search the current baseline for the candidate concept and for plausible successor identities, including renamed objects, `legacy_ids`, supersession relationships, migration dispositions, forward declarations, merged/normalized objects, and project/configuration boundaries.
4. Distinguish at minimum: `missing`, `migrated_or_renamed`, `superseded`, `partially_migrated`, `forward_declared`, `project_or_configuration_data`, and `unresolved`.
5. Treat a comparison made only against a non-canonical or stale branch as source evidence, not as proof of a current repository gap.
6. Re-run the repository check when canonical HEAD changes materially during a long-running audit before promoting findings into curator decisions.

Every promoted repository-gap record must therefore include an evidence field equivalent to:

```text
evaluated_against: <repository>/<canonical-branch>@<commit-sha>
```

If the canonical repository, branch, or HEAD cannot be established, the result is `indeterminate_stale_or_unresolved_baseline`; the evaluator must not assert that the content is missing.

## Public contribution boundary

External contributors may modify only:

```text
inbox/**
```

Everything else is curator-managed, including:

- `constitution/**`
- `standards/**`
- `workflows/**`
- `instructions/**`
- `configurations/**`
- `registries/**`
- `schemas/**`
- `conformance/**`
- `bridges/**`
- `render/**`
- `guides/**`
- `templates/**`
- `migration/**`
- `scripts/**`
- `.github/**`
- root governance files

## Curation lifecycle

```text
INBOX / SOURCE / OWNER REQUEST
        ↓
TRIAGE
        ↓
FRESHNESS GATE + CURRENT CANONICAL HEAD
        ↓
CONTEXT + DUPLICATE / LEGACY / MIGRATION CHECK
        ↓
CLASSIFY GOVERNED MEANING
        ↓
NORMALIZE + PRESERVE PROVENANCE
        ↓
VALIDATE / TEST
        ↓
CURATOR OR OWNER DECISION
        ↓
CANONICAL CHANGE OR HOLD / REJECT
```

## Authority boundary

The curator manages canonical representation but does not invent missing project facts, contractual authority, professional approvals, or source evidence.

During migration, Confluence remains source authority until formal cutover. GitHub objects marked `migration_candidate` are normalized migration candidates, not yet formally cut-over authority.

After cutover, the accepted GitHub canonical objects become the repository authority according to their governed status and layer.
