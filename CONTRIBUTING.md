# Contributing to TIVERIT BIM Standards

TIVERIT BIM Standards is publicly readable, but canonical standards content is curator-managed.

## Public contribution rule

External contributors — human or AI — should add material only under:

```text
inbox/**
```

Do not edit canonical repository content directly.

A repository guard checks external pull requests and rejects changes outside `inbox/**`.

## How to contribute

1. Fork the repository.
2. Add one or more files under:

```text
inbox/<contributor>/<yyyy-mm-dd>-<short-topic>.<ext>
```

3. Open a pull request.
4. The curator reviews, classifies, normalizes, validates, and routes useful material into the governed repository where appropriate.

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

## Contribution rights

By intentionally submitting material through the public Inbox contribution process, you represent that you have the right to submit it and grant TIVERIT permission to review, store, reproduce, normalize, modify, combine, validate, publish, redistribute, and incorporate it into the repository under the license applicable to the destination material, as described in `LICENSE.md`.

Do not submit copyrighted, licensed, proprietary, client, or other third-party material unless you have the rights necessary for that submission and intended use. A citation or observation about an external source is preferable to copying protected source text into the public Inbox.

Submission creates no standards authority and does not guarantee acceptance or promotion.

## Authority boundary

Inbox material is not authoritative merely because it has been submitted or merged.

The public Inbox is an intake channel. Promotion into standards, workflows, instructions, registries, configurations, schemas, conformance assets, guides, or other canonical areas is performed only through curator review.

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
