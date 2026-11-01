# Repository Release and Version Governance

Status: migration candidate
Authority: repository governance
Source: curated resolution of STAR-T-GATE Inbox #13 FIND-VER-005
Evaluated against: gschmidtke/TIVERIT-BIM-STANDARDS/main@1f48edce393e6edd80a585df26969cf8ae5830c1

## Purpose

This contract defines how a citable TIVERIT BIM Standards repository release is identified, versioned, validated, and distinguished from ordinary repository history and from versions carried by individual governed objects.

## Three separate version dimensions

TIVERIT shall keep these dimensions distinct:

1. **Repository release version** — identifies an immutable published snapshot of the repository corpus.
2. **Object version** — records the governed revision of an individual canonical object while its stable object `id` remains unchanged.
3. **Migration/status state** — records whether an object is a `migration_candidate`, `draft`, `active`, `deprecated`, `historical`, or `superseded`; status is not a substitute for either repository or object version.

A commit SHA identifies repository history but is not, by itself, a governed release version. A branch name identifies a moving line of work and shall not be cited as an immutable standards release.

## Repository release identity

Repository releases use Semantic Versioning in the form `MAJOR.MINOR.PATCH`, represented by Git tags as `vMAJOR.MINOR.PATCH`.

- **MAJOR** — a released change that can invalidate a consumer's prior governance interpretation, required workflow, machine contract, stable public structure, or compatibility assumption.
- **MINOR** — a backward-compatible governed addition or extension, including new requirements, objects, mappings, tests, or capabilities that do not invalidate existing released meaning.
- **PATCH** — a backward-compatible correction or clarification that does not intentionally change governed meaning or compatibility, including typographical, reference, metadata, rendering, or equivalent maintenance corrections.

If classification is uncertain, the change shall be treated as the higher-impact category until curator review resolves it.

## Pre-cutover rule

The repository is presently in migration and has no published release or tag. No version number is assigned merely by adopting this contract.

Before formal cutover, repository snapshots may be identified by branch and commit SHA for evidence and review, but they are not released standards versions. A first governed release requires an explicit cutover/release decision after the release prerequisites below are satisfied.

A pre-cutover release, if deliberately needed, may use a `0.y.z` version, but creating such a release still requires explicit owner/curator approval. The existence of migration candidates does not automatically create a `0.x` release.

## Release prerequisites

A repository release shall not be published unless:

- the release target is on the canonical release branch;
- repository validation and required conformance checks pass for the exact target commit;
- the release scope and material changes are recorded in `CHANGELOG.md`;
- unresolved findings that materially affect reliance on the release are disclosed rather than hidden;
- generated publication artifacts included in the release are reproducible from the tagged canonical source;
- any required owner or professional decisions for the release scope have been completed;
- the release version has been classified as MAJOR, MINOR, or PATCH under this contract.

A successful CI run is necessary evidence but does not itself authorize a release.

## Release record

A governed release is established by an immutable Git tag `vMAJOR.MINOR.PATCH` pointing to the exact canonical commit and a corresponding published release record. The release record should identify at minimum:

- version and tag;
- target commit SHA;
- publication date;
- release authority/approver;
- summary of governed changes;
- known limitations or unresolved material gaps;
- compatibility or migration notes where applicable;
- links to generated distributions when included.

Tags representing governed releases shall not be moved or reused. If a released snapshot is defective, correct it through a new release version rather than rewriting the prior release.

## Object-version relationship

The existing canonical object envelope permits `version` and `effective_date`. Those fields describe the lifecycle of the individual object, not the repository release that contains it.

An object version may change without requiring every other object to change version. Conversely, a repository release version may advance even when many contained objects retain their existing versions.

An object promoted to `active` must satisfy its schema lifecycle requirements, including `version` and `effective_date`. Inclusion in a repository release does not silently promote a `migration_candidate` or `draft` object to `active`.

## Changelog rule

`CHANGELOG.md` is the human-readable release ledger. Until the first governed release, changes accumulate under `Unreleased`.

Each published release section shall distinguish material categories where present, including breaking governance/compatibility changes, governed additions, corrections, deprecations/supersessions, and known unresolved limitations.

The changelog summarizes change; it does not replace canonical objects, provenance, commit history, or curator dispositions.

## Citation and reliance rule

For reproducible reliance after releases begin, cite the governed release tag/version and, where exact repository state matters, its commit SHA. Do not cite `main` alone as though it were immutable.

During migration before the first governed release, use the exact canonical branch and commit SHA and preserve the migration/cutover qualification.

## Cutover boundary

Formal cutover from Confluence source authority to GitHub authority is a separate owner-governed decision. Creating a tag or release cannot silently perform that cutover.

The first post-cutover governed release must explicitly record that the cutover decision has occurred and identify the authoritative snapshot. Until then, the repository's existing migration authority rules remain in force.

## Reasoning rule

Version answers must first identify which dimension is being asked about: repository release, object revision, or migration/status state. These dimensions must never be collapsed into a single ambiguous "version" value.