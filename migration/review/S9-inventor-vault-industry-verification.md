# S9 Inventor / Vault — Industry Verification Record

Status: migration review evidence; non-normative.

Purpose: compare the migrated Inventor/Vault source rules with current Autodesk behavior and relevant international/industry standards. External sources corroborate, constrain, or challenge migration candidates; they do not silently replace source authority or create TIVERIT requirements.

## 1. Inventor → Revit interoperability

### Autodesk evidence

Current Autodesk Inventor 2026 documentation confirms that Inventor can export assemblies to RVT, supports BIM-oriented simplification during export, provides built-in simplification presets including No Simplification, supports placement and included properties, and supports an updating relationship for exported RVT content. Autodesk also distinguishes RVT project/layout exchange from RFA reusable component exchange in its interoperability documentation.

Implication for TIVERIT:

- The source W6.3 RVT/RFA decision gate is technically credible.
- The source principle that manufacturing-level detail should not pollute BIM is aligned with Autodesk guidance.
- The exact TIVERIT export settings remain governed organizational instructions, not Autodesk universal requirements.
- Tool-version behavior must be verified when executing because Autodesk interoperability capabilities change across releases.

Sources:

- Autodesk Inventor 2026 Help — To Export a Model to RVT: https://help.autodesk.com/view/INVNTOR/2026/ENU/?guid=GUID-9F0E010C-2295-4021-BB77-89C119ACDA1A
- Autodesk Support — Inventor 2026 and Revit interoperability associative workflows based on file types: https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Inventor-2026-and-Revit-Interoperability-associative-workflows-based-on-file-types.html

## 2. Vault lifecycle and release governance

### Autodesk evidence

Autodesk Vault documentation confirms that lifecycle definitions use states such as Work in Progress, Review/For Review, and Released, with configurable transition rules, state behavior, security, revision behavior, and audit/history effects. Exact names and transition semantics are configurable.

Implication for TIVERIT:

- The Confluence source model of WIP → review → released is technically supported.
- TIVERIT may normatively define its organizational lifecycle pattern, but must not represent those exact state names as immutable Autodesk defaults.
- Segregation of duties and eligibility for downstream BIM/CDE use are TIVERIT governance decisions, not inherent Vault product behavior.

Sources:

- Autodesk Vault 2026 — Lifecycle Administration: https://help.autodesk.com/cloudhelp/2026/ENU/Vault-Have-You-Tried/files/GUID-A225776F-F9E8-43B7-911F-16800E34E07E.htm
- Autodesk Vault — Lifecycles and States: https://help.autodesk.com/cloudhelp/2025/ENU/Vault-General/files/GUID-63CE799F-5E53-417C-9A6E-3F1987943D83.htm

## 3. Project information management and CDE handoff

ISO 19650-2:2018 remains the published current international standard as of this review, while a second edition is under development. It defines an information-management process for delivery-phase BIM and information exchanges.

Implication for TIVERIT:

- The source distinction between authoring/release state and project information exchange is directionally aligned with ISO 19650 information-management principles.
- Vault release shall not be treated as equivalent to formal project publication, transmission, or acceptance.
- TIVERIT S3/S7 remain the governed project-information and exchange layers.

Source:

- ISO 19650-2:2018: https://www.iso.org/standard/68080.html

## 4. Manufacturing documentation and product definition

Relevant external standards include:

- ISO 129-1:2018 — presentation of dimensions and tolerances.
- ISO 1101:2017 — geometrical tolerancing language.
- ISO 8015:2011 — GPS fundamentals and interpretation principles.
- ISO 5457:1999 — drawing sheet sizes and layout; confirmed current in 2026.
- ISO 5455:1979 — drawing scales; confirmed current in 2025.
- ISO 16792:2021 — digital product definition data practices; a new edition is under development in 2026.
- ASME Y14.5-2018 (R2024) — dimensioning and tolerancing / GD&T for projects using ASME conventions.

Implication for TIVERIT:

The migrated manufacturing-documentation object correctly identifies a standards gap but does not yet contain enough source detail to select one complete ISO/ASME regime. Project, market, contractual, and manufacturing context must determine which external standards are adopted. TIVERIT should reference applicable external standards rather than reproduce licensed normative text.

## 5. Product-data exchange and manufacturing identity

ISO 10303-242:2025 (STEP AP242) covers managed model-based 3D engineering, including parts and assemblies, product configuration, versions and change history, release and approval data, product manufacturing information, dimensional/geometrical tolerances, and long-term product-data management.

Implication for TIVERIT:

- The distinction between manufacturing-object/product identity and BIM project information-container identity is well-founded and should remain explicit.
- STEP/AP242 is a relevant interoperability reference for manufacturing data exchange, but TIVERIT shall not assume every STEP export conforms to AP242 without explicit format/profile evidence.

Source:

- ISO 10303-242:2025: https://www.iso.org/standard/84300.html

## 6. Curator conclusions

1. No external evidence currently contradicts the source-level Inventor/Vault authority model.
2. Autodesk confirms the main technical premises of W6.3, but exact export settings remain governed TIVERIT instructions and require version-aware execution checks.
3. Vault lifecycle concepts are product-supported but configurable; organizational state semantics remain TIVERIT governance.
4. Manufacturing-documentation requirements need a separate standards-selection decision before promotion to active authority.
5. Inventor manufacturing-object identity should not be forced into the current S4 seven-token information-container grammar until the generic identity model is reconciled.
6. External standards are references/evidence only during migration; Confluence remains source authority until formal cutover.
