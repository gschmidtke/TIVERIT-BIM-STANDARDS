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
3. Classify content according to the repository content-classification doctrine.
4. Separate source facts, curator decisions, and unresolved issues.
5. Preserve source and contributor provenance.
6. Prefer extension of existing governed objects over duplication or new top-level architecture.
7. Record conflicts and gaps explicitly rather than silently reconciling them.
8. Run repository validation before considering a canonical curation pass complete.
9. Keep project-specific or client-specific facts out of reusable canonical rules unless deliberately modeled as configurable/project-instance data.
10. Escalate new normative or architectural choices to the repository owner when they are not already established by source authority or an accepted curator decision.

## Public contribution boundary

External contributors may modify only:

```text
inbox/**
```

Everything else is curator-managed.

## Curation lifecycle

```text
INBOX / SOURCE / OWNER REQUEST
        ↓
TRIAGE
        ↓
CONTEXT + DUPLICATE CHECK
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

After cutover, accepted GitHub canonical objects become repository authority according to their governed status and layer.
