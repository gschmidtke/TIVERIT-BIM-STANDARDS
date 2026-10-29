# Confluence Enrichment Harvest Review

## Purpose

This review identifies substantive source material that may add governance, workflow, instruction, registry, exception, verification, or extensibility value beyond what is already normalized in the migration branch.

The objective is not to mirror Confluence page-for-page. The objective is to ensure that no unique source meaning is lost before cutover.

During migration, Confluence remains source authority. All findings below are migration-review findings only. No source page is promoted to canonical authority by inclusion in this review.

## Harvest classification

Each candidate is classified as one of:

- **A — fits existing architecture:** migrate or enrich existing governed objects without structural change.
- **B — generic schema/governance refinement:** source meaning fits the architecture but may justify a reusable schema or lifecycle refinement.
- **C — architecture review required:** source meaning does not fit cleanly and would require curator review before any structural change.
- **DEFER — useful downstream content:** substantive, but not required to close the current migration.

The preferred outcome is A. B is acceptable where the refinement is generic and reusable. C should be rare.

## High-value harvest candidates

### 1. Formal exchange versus transmission

**Source page ID:** `2457714`

**Source maturity:** narrative source module; normative language present.

**Unique substance:**

- Distinguishes information movement from governed delivery.
- Transmission alone does not create delivery, approval, reliance, or authority.
- Formal exchange requires intentional issue, explicit scope, version/traceability, acceptance conditions, and declared purpose.
- Reliance is purpose-bound and does not automatically extend to other uses.
- Exporting, uploading, linking, or synchronizing information does not itself constitute formal exchange.
- Formal exchange is platform-independent at the standards level.

**Existing repository coverage:** partial. S3/S7 already separate production state, submission, acceptance, and permitted use, but the transmission-versus-formal-exchange distinction is not yet expressed as a dedicated, concise requirement set.

**Proposed landing zone:** S7 normative delivery/exchange governance, with cross-references to S2 permitted use and S3 production/CDE state.

**Fit:** **A**.

**Potential migration value:** may help resolve or normalize the still-unresolved S7 validation/delivery reference without creating a parallel delivery model.

---

### 2. Collaboration versus authority

**Source page ID:** `2425347`

**Source maturity:** standalone narrative module.

**Unique substance:**

- Collaboration is continuous; authority is discrete and governed.
- Discussion does not imply approval.
- Agreement in conversation does not constitute acceptance.
- Visibility does not grant permission to use information.
- Responsiveness does not imply responsibility.
- Reviews, feedback, issues, RFIs, chats, meetings, and comments remain production-support mechanisms unless explicitly governed as formal exchange or approval.
- Communication-channel choice does not change governance status.

**Existing repository coverage:** partial. S1 authority doctrine and S5/S7 acceptance boundaries already support this principle, but this source provides a compact cross-channel rule set that could strengthen those objects.

**Proposed landing zone:** S1 authority principles plus S5/S7 cross-reference; avoid creating a separate collaboration authority standard if existing objects can absorb the clauses.

**Fit:** **A**.

---

### 3. Production output versus deliverable

**Source page ID:** `2457722`

**Source maturity:** standalone narrative module.

**Unique substance:**

- Production outputs are not automatically deliverables.
- Availability is not authorization.
- Output maturity must be explicitly declared; visual completeness does not prove maturity.
- Outputs may remain exploratory, informational, coordinated, or validated without being issued.
- Deliverables are issued outputs governed by formal exchange.
- Visual richness does not imply reliability or permission for external/public use.

**Existing repository coverage:** partial. S2/S7 already govern permitted use and delivery states, but the explicit output-versus-deliverable distinction is not strongly isolated.

**Proposed landing zone:** S7 delivery taxonomy and S2 permitted-use linkage; potentially a small S7 requirement family rather than a new object class.

**Fit:** **A**.

---

### 4. Instruction / workflow / process boundary rules

**Source page ID:** `2818184`

**Source maturity:** L4 source standard with explicit normative rules.

**Unique substance:**

- Instruction = atomic executable action with verifiable outcome.
- Workflow = orchestration of instructions, roles, decisions, entry/exit conditions.
- Process = descriptive, informational explanation; not governed execution authority.
- Standards constrain; workflows coordinate; instructions execute; processes explain.
- How-to content has no independent governance class; it is an instruction when governed.
- Instructions must not introduce policy or orchestration logic.
- Workflows must not become button-click guides.
- A governed object should not simultaneously be classified as both instruction and workflow.
- AI-assisted authoring must preserve these boundaries.

**Existing repository coverage:** strong conceptually, but the boundary tests and explicit non-overlap rules are more precise than the current generic architecture prose.

**Proposed landing zone:** constitution/architecture or repository governance doctrine; optionally validator/schema guidance for type separation.

**Fit:** **A/B**. No new architecture is needed; a generic classification rule may be worth formalizing.

---

### 5. Content lifecycle and normalization governance

**Source page ID:** `3014740`

**Source maturity:** under review / approved-candidate source; not final authority.

**Unique substance:**

- Explicit lifecycle states: draft, under review, approved, superseded, archived.
- Review is collaborative feedback; approval is a formal governance decision.
- Supersession should retain traceability rather than delete history.
- Source-of-truth artifacts and derivative/generated artifacts have different authority.
- Artifacts unable to carry governance metadata should be wrapped by governed containers/references.
- Missing status should not silently imply authority.
- AI should not treat non-approved source content as authoritative.

**Existing repository coverage:** substantial but distributed. Current repository statuses, migration-candidate handling, provenance, generated-output doctrine, and curator authority already implement much of this logic.

**Proposed landing zone:** repository governance / constitutional lifecycle policy; use as source evidence to harden existing lifecycle semantics rather than importing source-specific labels verbatim.

**Fit:** **B**. Generic lifecycle semantics may merit explicit centralization, but no architectural remodeling is justified.

---

### 6. Model progression and authorized use by maturity stage

**Source page ID:** `10551299`

**Source maturity:** draft instruction/production guidance; contains conceptual and example material.

**Unique substance:**

- Treats model progression as planned maturation rather than visual detail alone.
- Defines staged purposes and authorized uses across Concept, Design Development, Coordination, Fabrication, and As-Built.
- Connects stage maturity to minimum geometry/information expectations and responsible parties.
- States that a model must not be used beyond its declared stage and authorized use.
- Introduces information milestone and deliverable-package concepts.

**Existing repository coverage:** partial. S2 LOD/LOI and permitted use exist, but S1 review still records a model-use taxonomy gap.

**Proposed landing zone:** S2 permitted-use / LOD-LOI enrichment, possibly with a separate governed progression registry only if a machine-readable stage model is later curated.

**Fit:** **A** for principle-level enrichment. Stage names and detailed mappings should not be promoted automatically because the source is draft and contains project/tool examples.

**Potential migration value:** candidate source evidence for closing or narrowing `GAP-S1-MODEL-USE-TAXONOMY-01`.

---

### 7. Navisworks federation and coordinate implementation

**Source page ID:** `10944513`

**Source maturity:** draft L6 source with many explicit TODOs.

**Unique substance:**

- One primary federation per coordination scope, with secondary federations only where scope/performance justifies them.
- Governed inclusion/exclusion of source models by lifecycle state.
- Shared/project coordinate intent should be resolved in source models; ad-hoc long-term transforms are discouraged.
- Misalignment triage order: verify source intent, export profile, append settings, then temporary transform only as last resort.
- Temporary transforms should be documented, time-limited, and driven back to source correction.
- Federation segmentation, included-model registry, model identity, and pre-publication federation QC are explicitly linked.
- Federation quality checks include source list/version/time, coordinate frame, benchmark alignment, units/precision, and clash selection-set correctness.

**Existing repository coverage:** partial. S5/S6 and current Navisworks material cover coordination/federation boundaries, but this source contains additional L6 execution detail.

**Proposed landing zone:** Navisworks L6 instruction family under S5/S6 ownership.

**Fit:** **A**.

**Migration rule:** migrate durable rules only. Preserve every unresolved tolerance, scope list, owner, folder, and approval field as an explicit gap; do not fill TODOs by inference.

---

### 8. Gap closure and cross-reference governance

**Source page ID:** `2883661`

**Source maturity:** structured migration/review pipeline source.

**Unique substance:**

- One concept should have one authoritative home; other locations should reference it rather than duplicate truth.
- Every documented gap should be closed or explicitly deferred with reason/evidence.
- Reusable gap fields include type, priority, alignment/home decision, resolution route, owner, status, and evidence.
- Resolution routes distinguish authoring in current domain, constitutional reference, cross-reference to another domain, registry creation, and justified deferral.
- Cross-group consistency should explicitly test contradictions, duplicate truth, dependency clarity, and terminology consistency.

**Existing repository coverage:** conceptually strong but not yet centralized as a formal migration closure schema.

**Proposed landing zone:** migration governance and final cutover audit process; potentially enrich the existing conflicts/gaps structures rather than become a normative S1–S9 standard.

**Fit:** **A/B**.

---

### 9. Stable additive data-path evolution

**Source page ID:** `14155787`

**Source maturity:** BEP-engine architecture source.

**Unique substance:**

- Canonical data paths should have one owner.
- Aliases should follow soft deprecation before hard cutover.
- Paths should be semantic, stable, and additive.
- Transforms should consume governed paths rather than invent new paths.
- New paths should declare owner, description, example payload, and version.

**Existing repository coverage:** partially analogous to current identifier/reference governance, but primarily relevant to the future BEP/data engine rather than migration of standards content.

**Proposed landing zone:** post-migration BEP/data-engine architecture.

**Fit:** **DEFER**.

---

### 10. Extensibility / profile-driven architecture

**Source page ID:** `13631492`

**Source maturity:** platform architecture proposal.

**Unique substance:**

- Stable core plus organization/project profile overlays.
- Company/project-specific roles, tools, governance, and LOD mappings should be parameterized rather than hard-coded into the standards architecture.
- Tool/catalog changes should be isolated from core structure.
- Canonical paths should remain stable across engine versions.

**Existing repository coverage:** the current repository already implements the more important abstraction—normative core separated from project-specific facts and tool execution. This source provides useful validation of the extensibility direction but is not itself a migration blocker.

**Proposed landing zone:** architecture design notes / future BEP consumption layer.

**Fit:** **DEFER**.

---

### 11. Tool-specific content normalization lifecycle

**Source page ID:** `6127650`

**Source maturity:** incomplete S9 tool-specific draft; several sections contain blank/incomplete fields.

**Unique substance:**

- Candidate reusable content should be assessed, normalized, assigned lifecycle state/metadata, approved, published, superseded, and retired through governed steps.
- Vendor/project content should not become reusable standard content merely through repeated use.
- Tool-specific content lifecycle should inherit global governance rather than define a parallel lifecycle.

**Existing repository coverage:** global lifecycle principles and S9 tool authority exist; this is a useful specialization pattern for future tool libraries.

**Proposed landing zone:** future S9 tool-specific instruction/workflow content.

**Fit:** **DEFER/A** depending on whether Inventor/library governance is inside the intended migration scope for cutover.

---

### 12. Issue admissibility and metric integrity

**Source page ID:** `2326562`

**Source maturity:** foundational narrative under review; contains normative candidate concepts mixed with broader narrative material.

**Unique substance:**

- An issue implies obligation and therefore requires governance, not merely observation.
- Findings from routine progress/WIP outputs should not automatically become enforceable issues.
- Issue admissibility depends on due scope/context, authorized origin, and explicit obligation context.
- Observations that fail admissibility remain observations and should not contaminate overdue/performance metrics.
- Issue dashboards are meaningful only when they report on admissible issues aligned with declared delivery states.

**Existing repository coverage:** S5 already has issue lifecycle and closure governance, but admissibility before issue creation is not yet strongly isolated.

**Proposed landing zone:** S5 issue governance / issue registry semantics, with S2/S7 dependency on declared due state and permitted use.

**Fit:** **A**.

---

### 13. Contextual QA/QC layers

**Source page ID:** `2326562`

**Source maturity:** foundational narrative under review.

**Unique substance:**

- QA/QC should first ask whether information is valid for evaluation in its current phase/context, then whether it meets declared expectations.
- Continuous QA/QC produces readiness/health signals rather than acceptance judgments.
- Expectation-based QA/QC compares reality only against formally declared expectations.
- Milestone QA/QC verifies readiness for formal issue/use and is the appropriate place for consequential review outcomes.
- External review should be limited to declared outputs, phase, and explicit expectations.
- Findings outside declared role authority remain observations rather than authoritative QA/QC outcomes.

**Existing repository coverage:** S5 gates and QA/review authority cover parts of this, but the three-layer distinction could sharpen the boundary between monitoring, validation, and acceptance.

**Proposed landing zone:** S5 QA/review doctrine and conformance guidance; do not create a separate QA plane.

**Fit:** **A**.

---

### 14. Interoperability as decodability

**Source page ID:** `2326562`

**Source maturity:** foundational narrative under review.

**Unique substance:**

- Successful technical transfer is not sufficient for interoperability.
- Information crossing a boundary must preserve decodable purpose, status, phase context, limitations, intended use, and responsible recipients.
- Sender responsibility includes encoding intent; receiver responsibility is bounded by declared meaning and should not require inference.
- Incoming requirements are also exchange artifacts and must be decodable before they can safely become executable obligations.
- Material exchange assumptions should be re-declared when phase, context, or responsible party changes.

**Existing repository coverage:** interoperability plane currently focuses on external representations/mappings; this source adds a normative semantic boundary that belongs upstream of those bridges.

**Proposed landing zone:** S7 exchange governance and interoperability architecture doctrine.

**Fit:** **A**.

---

### 15. Handover acceptance and finite defect scope

**Source page ID:** `2326562`

**Source maturity:** foundational narrative under review.

**Unique substance:**

- Handover is a declared exchange/state-transition event, not a gradual fade-out.
- Acceptance is assessed against fitness for declared purpose rather than absolute perfection.
- Acceptance may coexist with a finite, explicit defect list where remaining defects do not invalidate declared purpose.
- Post-handover correction scope should not silently expand into new requirements or reopen production.
- Persistence of information after handover does not imply continued responsibility or continued validity.

**Existing repository coverage:** S7 closeout and acceptance exist, but finite defect-scope and post-handover responsibility boundaries are not yet strongly expressed.

**Proposed landing zone:** S7 handover/closeout requirements and W8.2 workflow enrichment.

**Fit:** **A**.

---

### 16. Automation readiness as governability

**Source page ID:** `2326562`

**Source maturity:** foundational narrative under review.

**Unique substance:**

- Automation readiness depends on explicit, deterministic, machine-legible meaning rather than automation availability.
- Execution-layer volatility should not be mistaken for governed truth.
- Automation should distinguish read from modify authority, remain repeatable/auditable, and preserve human accountability.
- Leadership-facing automated outputs should expose governed signals, not raw execution volatility.
- Information dependent on tribal knowledge or implied context is not automation-ready.

**Existing repository coverage:** strong overlap with S9, conformance, ZEN authority boundaries, and the four-plane architecture; this source provides useful language for readiness criteria.

**Proposed landing zone:** S9 automation governance and maturity/readiness guidance.

**Fit:** **A**.

---

### 17. Training and onboarding as participation readiness

**Source page ID:** `2326562`

**Source maturity:** foundational narrative under review.

**Unique substance:**

- Training is proactive readiness; support is reactive troubleshooting.
- Participation in a governed environment is conditional on suitable readiness, not merely system access or software skill.
- Project-specific induction applies across role/seniority levels.
- Enforcement responsibility belongs with project leadership where staffing/participation authority resides; BIM governance defines readiness requirements but should not silently inherit staffing authority.
- Knowledge should be retrievable and refreshable rather than dependent on memory.

**Existing repository coverage:** role/onboarding mechanics exist, but this broader readiness doctrine is thin.

**Proposed landing zone:** S1 governance/role enablement plus project onboarding workflow; potentially project-facing rather than a new normative standard family.

**Fit:** **A/DEFER** depending on cutover scope.

---

### 18. Information classification by determinism and authority role

**Source page ID:** `2326562`

**Source maturity:** foundational narrative under review; contains a conceptual classification matrix.

**Unique substance:**

- Information categories differ by determinism, authority, expected storage location, and whether they should exist in authoritative models.
- Governing information, contractual information, geometric/spatial information, transient information, exploratory content, reference/context, approval/status, responsibility/ownership, lifecycle, and derived information have different governance behavior.
- “One source of truth” should not mean forcing all information into the model; deterministic information should live where it remains stable and reusable.

**Existing repository coverage:** S8 governs semantic structure and S3/S7 govern locations/states, but no unified information-category matrix currently joins determinism, authority, carrier, and lifecycle behavior.

**Proposed landing zone:** S8 information-structure enrichment, potentially as a governed classification registry after curator review.

**Fit:** **B**. The concept fits, but converting the source matrix into a canonical registry would be a curator design decision rather than a mechanical migration.

## Consolidated harvest themes

The strongest unique source material now clusters into ten reusable concepts:

1. **Authority is not created by collaboration, visibility, output creation, or file movement.**
2. **Formal exchange is an intentional, purpose-bound governance event distinct from transmission.**
3. **Output maturity and permitted use must be explicitly declared; visual completeness is not evidence of authority.**
4. **Standard / workflow / instruction / process classes require strict non-overlapping governance boundaries.**
5. **Lifecycle, supersession, provenance, and derivative-output authority should be explicit and traceable.**
6. **Migration gaps should have one authoritative home, a resolution route, owner/status/evidence, and explicit deferral when unresolved.**
7. **Issues and QA/QC outcomes require admissibility, declared context, and role authority before they become obligations or metrics.**
8. **Interoperability requires semantic decodability, not merely successful file transfer.**
9. **Handover is a governed state transition with bounded acceptance and finite post-handover correction scope.**
10. **Automation and participation both require readiness conditions; access or technical capability alone is not authority or readiness.**

These themes fit the existing repository architecture without introducing a new S-domain, layer, authority plane, or top-level object family.

## Framework absorption test

Current result from this harvest sample:

- **A / A-dominant:** 12 candidates
- **A/B or B:** 4 candidates
- **DEFER / DEFER-dominant:** 2 candidates
- **C — architecture redesign required:** 0 candidates

This is positive evidence that the current framework can absorb new substantive standards content primarily by object addition, relationship enrichment, and limited generic schema/governance refinement rather than structural remodeling.

## Recommended migration order from this harvest

1. Formal exchange versus transmission (`2457714`).
2. Collaboration versus authority (`2425347`) and output versus deliverable (`2457722`) as a coordinated S1/S3/S7 enrichment pass.
3. Issue admissibility and contextual QA/QC (`2326562`) as an S5 enrichment pass.
4. Instruction/workflow/process boundary standard (`2818184`).
5. Model progression / authorized-use principles (`10551299`).
6. Interoperability decodability and handover acceptance boundaries (`2326562`) as S7 enrichment.
7. Navisworks federation/coordinate durable rules (`10944513`).
8. Automation-readiness language (`2326562`) into S9 where it adds requirements rather than narrative duplication.
9. Lifecycle/governance and gap-closure refinements (`3014740`, `2883661`) during final migration/cutover hardening.
10. Consider the information-determinism matrix (`2326562`) separately as a potential S8 registry design decision.
11. Defer BEP/data-engine, broader training-library, and tool-library architecture material until normative migration is closed unless required by an unresolved forward reference.

## Source hygiene

This review records only neutral Confluence page IDs and normalized descriptions. Source-era names, URLs, examples, and organization-specific identifiers are not reproduced into repository content.
