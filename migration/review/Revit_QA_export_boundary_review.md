# Revit QA / Monitoring / Export — Source Boundary Review

Status: migration review only; non-canonical.

## Purpose

Capture source-backed authority boundaries for Revit QA/model-health checks and export instructions before creating canonical implementation objects.

## QA/QC source — Confluence page 3735560

The source makes a strong distinction between production quality evidence and authority:

- QC is discipline-led checking during production.
- QA is independent or cross-disciplinary compliance checking.
- QA/QC may evaluate model integrity, information completeness, naming/standards compliance, coordination readiness, and delivery-state alignment.
- QA/QC may generate comments, issue logs, check reports, and compliance summaries.
- Those outputs are evidence, not authorization.
- QA/QC completion or sign-off does not grant approval, permitted reliance, or formal acceptance.
- Formal acceptance occurs through governed exchange mechanisms.

Migration implication: Revit QA instructions should produce evidence consumed by S5/S7 gates; they must not carry independent acceptance authority.

## Monitoring and automation source — Confluence page 3899424

The source classifies monitoring and automation tools as operational aids. Permitted functions include:

- model/data health monitoring;
- standards and parameter compliance checks;
- performance-risk detection;
- pre-QA checks;
- coordination verification;
- repeatable batch operations;
- reports, metrics, logs, and schedule/metadata extraction.

Explicit limitations:

- no creation of authority;
- no approval grant;
- no permitted-reliance grant;
- no governance override;
- no replacement of required human authority decisions.

Any automated action affecting an information container must be traceable, repeatable, auditable, and respect declared states and permitted use.

Migration implication: this is a strong upstream doctrine for future ZEN/validator bindings. Executable checks can produce observations and evidence, but authority remains in governed roles/workflows.

## Navisworks metadata/export source — Confluence page 8159247

Source status: DRAFT, L6 tool-specific implementation under S3/S5.

The page provides high-level use cases and candidate profiles, but many exact values remain TODO:

- exact export view/scope set;
- viewpoint naming/redaction;
- record-NWD qualification;
- ACC paths/version pinning;
- retention and naming;
- plugin/version specifics;
- attribute mapping;
- profile settings;
- responsibility/approval for coordinate checks.

The page explicitly points to Confluence page 8093711, the machine-readable Navisworks Export Settings instruction set, as its governed-values source.

Migration implication: page 8159247 is supporting explanatory L6 guidance. Page 8093711 is the stronger machine-readable execution source, but even that source references a future Export Preset Registry. Exact profile values must therefore remain unresolved until a concrete preset registry/configuration is created through governance.

## Combined execution chain

Source-backed relationship:

1. Tool-independent standards define requirements and authority.
2. Revit/Navisworks L6 instructions define how to perform or inspect governed tasks.
3. Monitoring/automation may execute checks and generate evidence.
4. QA/QC evaluates evidence and readiness.
5. S5/S7 governed gates determine readiness/acceptance according to assigned authority.

A PASS from an automated or QA check is not, by itself, an acceptance decision.

## Candidate future machine interface

Without creating canonical rules yet, the sources support a future pattern of:

- requirement reference;
- check/instruction identifier;
- executor capability;
- observed result;
- evidence artifact;
- verification result;
- authoritative gate/role that may consume the evidence.

This pattern is source-consistent with executable governance while preserving the authority boundary.

## Provenance

Source system: Confluence, space BST.

Primary source page IDs: 3735560, 3899424, 8159247, 8093711.

This review is extraction analysis only and does not promote source drafts, TODO values, settings, or profiles into canonical authority.
