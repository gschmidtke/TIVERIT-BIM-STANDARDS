# Architectural detail annotation — visual reference profile
ID: DETAIL-ANNOTATION-PROPOSAL-20261105-001
Status: Owner-requested curator proposal; not an adopted standard.
Date: 2026-11-05
Contributor: Gottfried Schmidtke (visual reference selection); Zara (extraction and proposed rules).
Baseline: gschmidtke/TIVERIT-BIM-STANDARDS/main@e2cb86712d090b7e558c74c4792b40661f70a04d

## Purpose and success
A reader must be able to identify a component, follow its annotation, distinguish its assembly layers, and locate relevant dimensions and references at the issued paper size without repeatedly consulting a distant legend. Annotation quality is a separate acceptance question from engineering adequacy.

Scope: architectural detail plans and sections. This proposal does not establish construction dimensions, material specifications, code compliance, or technical approval of the pictured assemblies.

## Evidence and authority
The owner supplied five browser screenshots in this conversation on November 5. Several overlap, including duplicate views. They are one visual reference set, not five independent precedents. Authorship and original sheet provenance are unverified. Screenshots are not republished here.

Visible conventions: direct uppercase descriptive labels; horizontal leader landings with angled segments; aligned groups of notes adjacent to details; dimensions arranged outside assemblies where space permits; distinct material hatches; detail titles below views with identifiers and scales; references to other views.

Exact font, paper text height, pen weights, spacing, family names and original sheet scale cannot be recovered reliably from browser pixels. Some source leaders are crowded: those defects are not prescribed.

Related sources previously reviewed:
- [BST Annotation Standards, page 5799975](https://tiveritllc.atlassian.net/wiki/spaces/BST/pages/5799975): controlled types, readability, left alignment, consistent dimensions and data-driven tags/keynotes; exact style values remain unresolved.
- [BST QA checklist, page 6422564](https://tiveritllc.atlassian.net/wiki/spaces/BST/pages/6422564): aligned note stacks, avoid crossing leaders, clearances and print checks; source is draft.
- [BST Sheet and Titleblock Standards, page 6357066](https://tiveritllc.atlassian.net/wiki/spaces/BST/pages/6357066): cohesive composition and associated annotations.
- Existing repository instruction: TIVERIT-BIM-INS-REVIT-ANNOTATION-001 (migration_candidate).
- Existing sheet curation: curation/CONFLUENCE-SHEET-STANDARDS-001.md.

Existing source controls remain distinct from this proposed detail-specific appearance profile. Confluence remains source authority during migration. No source TODO or screenshot observation is promoted by this document alone.

## Proposed reusable rules
The requirement language below defines the candidate standard, pending acceptance.

| ID | Candidate requirement | Evidence / rationale |
|---|---|---|
| DA-01 | Use direct descriptive local notes as the default for junction-specific information. Controlled keynotes remain permitted for repeated specifications or when required by the project. A remote numbered legend must not be the only explanation of a critical junction. | Visual reference; proposed local-note preference, compatible with governed keynotes. |
| DA-02 | Place notes in coherent groups adjacent to their detail. Align each group's text to a common left margin and keep text horizontal. Use consistent spacing between note bounding boxes, allowing multiline notes room. | Visual reference and Confluence alignment guidance. |
| DA-03 | Use a horizontal landing next to the text and a simple leader to the target, normally with one elbow. Route from the nearest appropriate side of the text. Do not force a fixed angle when it produces ambiguity or crossings. | Visual reference; routing refinement proposed. |
| DA-04 | Leaders must not cross other leaders or pass through text, dimensions, titles or reference symbols. Order notes to match target order and use the nearest suitable note zone. If congestion remains, split or enlarge the view. | Confluence QA plus proposed remedy. |
| DA-05 | Terminate each leader unambiguously on its intended component, surface or layer. For very thin layers, use an enlargement when the target cannot be distinguished at print size. Multiple leaders from one note are permitted only for identical requirements. | Proposed semantic acceptance rule. |
| DA-06 | Use one controlled leader/arrowhead style per annotation role. Leaders and hatch must remain visually subordinate to cut geometry while remaining legible. Avoid routing through unrelated assemblies when an exterior route is available. | Consistency source; proposed hierarchy. |
| DA-07 | Use concise uppercase local labels for this profile, with controlled abbreviations. State material/component plus applicable size, finish or connection requirement only when confirmed. Longer explanations belong in local general notes or referenced specifications. Preserve exact identifiers and case-sensitive codes. | Visual reference; uppercase is a proposed profile choice, not universal authority. |
| DA-08 | Place dimensions in a distinct lane where practicable: local/component dimensions nearer the assembly, overall dimensions farther out. Keep text and witness lines readable. Avoid redundant/conflicting dimensions; follow governed units and precision. Do not replace measured values with deceptive text overrides. | Visual reference and existing dimension controls. |
| DA-09 | Distinguish cut outlines, projection/beyond lines, hidden/overhead lines, hatch and annotation consistently. Hatch must identify material without obscuring layers or leaders. Information must remain intelligible in monochrome when that is the delivery mode. | Visual reference and print QA. |
| DA-10 | Locate the title consistently below the view, with detail identifier and scale. View references must resolve to their target detail and sheet. Use governed title and reference types; do not manually imitate references that can be associated. | Visual reference and existing sheet/tag controls. |
| DA-11 | Keep unresolved assumptions and review status distinguishable from construction requirements. Do not overload local component labels with long design commentary or provenance codes; retain that information in an associated review record. | Proposed separation of drawing content and review evidence. |
| DA-12 | Verify the exported detail at its intended paper size and scale. Acceptance requires legible text, distinguishable targets, no collisions, resolved references and coherent hierarchy. Model/API success alone is insufficient. | Existing QA principle, made detail-specific. |

## Proposed paper-space profile — trial values only
These are new trial settings, not measurements extracted from screenshots and not existing approved Confluence values. A governed project profile takes precedence. Check the exported PDF before adopting these settings.

| Property | Initial trial value |
|---|---|
| Local note and dimension text height | 2.5 mm |
| Detail title text height | 3.5 mm |
| Clear vertical gap between note bounding boxes | at least 2 mm |
| Clear text-to-unrelated-graphics gap | at least 2 mm |
| Horizontal leader landing | 6 mm nominal; adjust for routing |
| First dimension lane offset from geometry | 10 mm nominal |
| Spacing between dimension lanes | 7 mm nominal |
| Leader pen weight | 0.18 mm trial |
| Cut outline pen weight | 0.35 mm trial; stronger major boundaries if needed |

Use a controlled, readable font already available in the project. These values do not assign Revit pen numbers: pen-number-to-output-width mapping depends on the template. Gaps are measured between actual plotted bounding boxes, not text insertion points. No fixed maximum note count is imposed; readability and target ambiguity govern splitting.

## Verification and machine-readable interpretation
Each rule ID is stable within this proposal. A later implementation should record:
- rule_id, detail_id, profile_id and profile_version;
- note_id, target_element_or_detail_component_id, leader endpoint and text bounding box;
- measurement coordinate system and paper scale;
- check_result: pass / fail / indeterminate / not_applicable;
- evidence reference, checker and documented exception where relevant.

Geometric checks can assist with bounding-box collisions, leader intersections, alignment, paper gaps, type inventory and broken references. Exclude shared endpoints belonging to a legitimate multi-leader note from crossing counts. A geometric PASS cannot prove that a leader names the correct layer or that a construction specification is correct; those need human/assisted semantic review. Do not infer missing targets from pixel proximity alone.

Acceptance evidence:
1. Exported PDF at intended sheet size, reviewed at actual print size.
2. Detail crops showing local note stacks, targets, dimensions and titles.
3. Annotation type inventory and measured paper-space profile.
4. Rule results identifying failures and indeterminate checks explicitly.
5. Reviewer confirmation of target correctness; unresolved technical design remains separately listed.

## Application to the ADU eave trial
Apply the proposed local-note layout to DET-01 and the existing enlarged views. Keep long rationale and assumption registers outside the component annotation zone. Replace the distant number-only dependency with clear local component labels where feasible; retain governed keynotes if useful. Separate edge, bearing and blocking conditions when their leaders cannot be routed clearly together. Do not change the assembly merely to improve its annotation.

This is an application brief, not confirmation that any model or PDF has been revised.

## Classification and promotion
- DA rules: proposed tool-neutral standard constraints.
- Trial dimensions and typography: proposed configurable appearance profile.
- Layout and Revit production techniques: downstream instruction/ARPL work, not new standards authority.
- Print and semantic checks: proposed conformance evidence.

Extend the existing annotation instruction and sheet-documentation relationships when accepted; do not create a competing annotation authority. Exact appearance choices require owner acceptance under AGENTS.md and CURATION.md. This staged proposal can be reviewed before canonical schema/reference/conformance integration. No canonical completion or validation claim is made.
