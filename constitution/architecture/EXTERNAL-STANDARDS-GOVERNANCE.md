# External Standards Governance

Status: migration candidate
Authority: repository governance
Source: curated from STAR-T-GATE Inbox #11
Evaluated against: gschmidtke/TIVERIT-BIM-STANDARDS/main@63dfc33b742de8031c70fa8c9bf643966f946442

## Purpose

This contract defines how TIVERIT may reference external normative standards without copying their protected content or silently transferring external authority into TIVERIT.

## Authority boundary

External standards remain external authority. TIVERIT independently governs its own requirements, implementation doctrine, workflows, controls, evidence, configuration, and conformance artifacts.

The existence of an external standard does not by itself make that standard applicable to a TIVERIT project or make it superior to TIVERIT governance. Applicability must be established by an applicable governing instrument such as law/regulation, contract/appointment, appointing-party information requirements, or explicit project/organizational adoption.

When an applicable higher-authority instrument incorporates a specific external standard and edition, TIVERIT shall not silently resolve a conflict in its own favor. The conflict must be exposed and routed to the appropriate authority.

## Precedence model

For routing potential conflicts, use the following default hierarchy unless the project's governing instruments establish a different lawful order:

1. applicable law and regulation;
2. contract and appointment;
3. appointing-party/client information requirements;
4. external standards explicitly incorporated by an applicable governing instrument;
5. project BEP and other authorized project governance instruments;
6. TIVERIT normative standards;
7. TIVERIT workflows, instructions, configuration, and implementation guidance.

This hierarchy is a routing rule, not a claim that every listed instrument is present or applicable on every project.

## Public reference gateway

A public repository may store only the information needed to identify, route, and assess an external standard lawfully, including standard identity/edition/status, official public locators, lawful clause identifiers, applicability and precedence metadata, independently authored TIVERIT requirements, alignment evidence, and publicly licensed guidance.

The public repository shall not become a substitute for obtaining or lawfully accessing the external publication.

## Copyright and licensed-content boundary

Without a licence that expressly permits the intended use, the repository shall not store substantial protected standard text, systematically reproduce a standard through clause-by-clause paraphrase, encode protected publication content as a substitute dataset or complete rules engine, or redistribute protected tables, figures, definitions, or annex content.

Licensed full-text standards shall not be placed in this public repository. Any future licensed gateway must be private/restricted and must document licence permissions for storage, retrieval, automation, and machine/AI processing before those capabilities are enabled.

## Edition management

External-standard mappings shall identify the part and edition/publication year used for assessment. A generic reference such as `ISO 19650` is insufficient for normative conflict resolution.

Draft stages such as CD, DIS, and FDIS are change-monitoring evidence only unless an authorized governing instrument explicitly adopts them. A newly published edition does not silently rewrite existing TIVERIT mappings; an impact review is required.

## Alignment relationships

Permitted relationship classifications are `implements`, `supports`, `aligned_with`, `partially_aligned_with`, `depends_on`, `more_restrictive_than`, `project_specific_extension_of`, `potential_conflict_with`, `superseded_when_external_requirement_applies`, and `not_yet_verified`.

An alignment claim is informational until its applicability, evidence basis, edition, and curator status are recorded. It does not reproduce or independently create the external requirement.

## Reasoning behavior

When a user asks an external-standard question, identify the standard/part/edition, check official public identity/status, determine project applicability, search TIVERIT for independently governed implementation or verified mapping, use public guidance only as secondary evidence, never invent protected wording, state when authorized clause access is required, and route material unresolved conflicts to curator/project authority.

## Conflict record

A conflict record must identify the TIVERIT object/requirement, external standard and edition, applicable governing instrument where known, the apparent conflict without reproducing protected text, evidence source/date, and disposition authority. Unresolved conflicts remain explicit.

## Security and operational-scope consequence

This gateway permits TIVERIT to register and assess ISO 19650-5 security-minded governance and ISO 19650-3 operational-phase governance without inventing their normative content. It does not itself declare those domains fully implemented by TIVERIT. Scope and implementation remain separate governed decisions.
