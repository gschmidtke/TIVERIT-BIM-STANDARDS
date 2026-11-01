# Contributing to TIVERIT BIM Standards

TIVERIT BIM Standards is publicly readable, but canonical standards content is curator-managed.

## Public contribution route

The canonical public intake route is the **STAR-T-GATE Inbox** described by `STAR-T-GATE.json`. Public submissions are transported by the STAR-T-GATE Inbox Worker and recorded in the `gschmidtke/STAR-T-GATE-INBOX` issue queue as durable, uncurated evidence.

Do not edit canonical repository content directly. Submission through STAR-T-GATE does not create standards authority and does not guarantee promotion.

The repository-local `inbox/**` path is retained only for curator-side staging, recovery, and historical provenance. It is **not the canonical public entry point**.

## How public contributions are handled

1. Submit the observation, proposal, evidence item, review, or candidate change through the STAR-T-GATE Inbox route declared in `STAR-T-GATE.json`.
2. The submission is recorded as uncurated evidence in the STAR-T-GATE Inbox queue.
3. A curator establishes provenance, checks the current governed state, classifies and routes the item, and determines whether normalization or a canonical repository change is justified.
4. Canonical changes are separately validated and promoted under repository governance.

You do not need to understand the repository schemas before contributing. Raw observations and evidence are welcome.

Useful submissions include:

- proposed standards improvements;
- conflicts or contradictions;
- project lessons that may generalize;
- workflow or instruction improvements;
- missing BIM-use, role, registry, exchange, or validation cases;
- external AI reviews;
- implementation evidence;
- failure cases;
- proposed conformance tests;
- examples that expose a gap in the current governance model.

## Repository-local inbox

Material under `inbox/**` remains non-authoritative. It may be used by curators for staging, recovery, or preserving historical provenance, but public contributors should use the STAR-T-GATE Inbox route rather than opening direct contribution PRs against this repository.

Any repository guard or branch rule that permits `inbox/**` changes is a repository permission boundary only; it does not make that path the canonical public intake route and does not create authority for submitted content.

## Contribution rights

By intentionally submitting material through the public STAR-T-GATE Inbox contribution process, you represent that you have the right to submit it and grant TIVERIT permission to review, store, reproduce, normalize, modify, combine, validate, publish, redistribute, and incorporate it into the repository under the license applicable to the destination material, as described in `LICENSE.md`.

Do not submit copyrighted, licensed, proprietary, client, or other third-party material unless you have the rights necessary for that submission and intended use. A citation or observation about an external source is preferable to copying protected source text into public intake.

Submission creates no standards authority and does not guarantee acceptance or promotion.

## Authority boundary

Inbox material is not authoritative merely because it has been submitted or recorded.

The STAR-T-GATE Inbox is an intake and evidence channel. Promotion into standards, workflows, instructions, registries, configurations, schemas, conformance assets, guides, or other canonical areas is performed only through curator review.

Canonical changes remain subject to repository governance, provenance, schema/reference validation, and curator approval.

Repository licensing grants reuse rights where stated; it does not grant canonical write, promotion, approval, certification, or governance authority.

## Safety and privacy

Do not submit:

- credentials, secrets, or tokens;
- private client data you are not authorized to disclose;
- personal information unnecessary to preserve the learning;
- proprietary or licensed material you do not have permission to share;
- project files or other sensitive production artifacts;
- malicious payloads or material intended to compromise reviewers or automation.

The Inbox is an evidence and proposal intake channel, not a code-execution channel.
