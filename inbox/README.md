# Repository-local Inbox

`inbox/` is retained for **curator-side staging, recovery, and historical provenance**. It is not the canonical public contribution entry point.

The canonical public intake route is the **STAR-T-GATE Inbox** declared in `STAR-T-GATE.json`. Public submissions are transported by the STAR-T-GATE Inbox Worker and recorded in the `gschmidtke/STAR-T-GATE-INBOX` issue queue as durable, uncurated evidence.

Content placed here is a proposal, submission, observation, review, evidence item, or candidate change. It is **not canonical authority**.

## Curation lifecycle

```text
STAR-T-GATE public submission
    -> STAR-T-GATE-INBOX evidence record
    -> curator review / routing
    -> optional repository-local staging when needed
    -> classification / normalization
    -> schema / reference / provenance validation
    -> governed promotion when justified
    -> canonical repository content
```

## Rules

- Public contributors should use the STAR-T-GATE Inbox route, not direct repository-local Inbox PRs.
- Repository-local `inbox/**` may be used by curators for staging, recovery, or historical provenance.
- Do not treat Inbox content as an active BIM requirement.
- Do not overwrite canonical IDs from Inbox material.
- Preserve contributor and source provenance.
- Curator review is required before promotion.
- Canonical repository areas are edited only through governed curator workflows.
- A stored or merged Inbox item remains non-authoritative until separately promoted through governance.

See `STAR-T-GATE.json` for the public intake contract, `CONTRIBUTING.md` for contribution guidance, and `CURATION.md` for promotion rules.
