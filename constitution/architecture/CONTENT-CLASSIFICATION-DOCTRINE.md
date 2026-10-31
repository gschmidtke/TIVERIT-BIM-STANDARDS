# Content Classification Doctrine

## Purpose

This doctrine defines the governance boundaries between standards, workflows, instructions, and descriptive processes in the TIVERIT BIM Standards repository.

Its purpose is to prevent shadow standards, workflow/instruction confusion, uncontrolled how-to sprawl, duplicated authority, and AI-assisted classification drift.

This doctrine governs content classification across all S1–S9 domains and tool-specific implementation material.

## Core rule

**Standards constrain. Workflows coordinate. Instructions execute. Processes explain.**

No governed content class may silently assume the authority or function of another class.

## Standard — normative constraint

A Standard defines an obligation, prohibition, permission, authority boundary, acceptance condition, or other reusable governance rule.

A Standard answers:

> What must, must not, should, or may be true, and under whose authority?

A Standard:

- may define requirements, permissions, prohibitions, authority, evidence expectations, and boundaries;
- should remain tool-neutral unless the governed subject is inherently tool-specific;
- does not become an execution guide merely because a rule will later be implemented by a tool;
- does not prescribe an operational sequence when the real concern is orchestration.

## Workflow — L5 coordination logic

A Workflow coordinates multiple actions, roles, states, and decision points to achieve a defined outcome.

A Workflow answers:

> Who does what, in what order, under which conditions, and what marks entry, decision, escalation, and completion?

A Workflow:

- may coordinate multiple Instructions;
- may span roles, time, systems, and information states;
- may define entry conditions, exit conditions, gates, decision branches, escalation paths, and handoffs;
- should be tool-agnostic at L5 unless a workflow is explicitly scoped to a governed tool environment;
- must not create new normative authority that belongs in a Standard;
- must not collapse into button-click or command-level execution steps.

## Instruction — L6 execution unit

An Instruction is a bounded executable action or tightly bounded execution unit intended to produce a verifiable outcome.

An Instruction answers:

> What exactly is done to achieve this specific result under already-governed conditions?

An Instruction:

- may be tool-specific;
- should have explicit preconditions and a verifiable outcome;
- should be atomic enough that successful execution can be distinguished from failure or indeterminate execution;
- may reference governing Standards and the Workflow that invokes it;
- must not introduce new policy, authority, acceptance criteria, or orchestration logic;
- must not redefine upstream requirements.

The colloquial term **how-to** has no independent governance standing. Governed how-to content is classified as an Instruction when it meets the criteria above.

## Process — descriptive information

A Process is a descriptive explanation of how work commonly or typically occurs.

A Process answers:

> How does this usually work?

A Process:

- is informative rather than prescriptive;
- may explain context, common sequences, background, rationale, or examples;
- may vary between teams or projects;
- does not establish compliance obligations or execution authority;
- must not be treated as a governed substitute for a Standard, Workflow, or Instruction.

If descriptive process material contains mandatory rules, orchestration logic, or executable instructions, those parts must be extracted into their proper governed classes rather than leaving mixed authority inside narrative prose.

## Boundary tests

Use these tests before creating or migrating content:

1. Does the content define obligation, prohibition, permission, authority, or acceptance? → **Standard**.
2. Does it coordinate roles, order, states, decisions, gates, or handoffs? → **Workflow**.
3. Does it tell an actor or tool what bounded action to perform to produce a verifiable outcome? → **Instruction**.
4. Does it explain how work generally happens without creating enforceable obligations? → **Process**.

When one source page contains multiple classes, split the meaning into separate governed objects or informative material. Do not preserve page-level mixing merely because the source combined them.

## Non-overlap rules

- A governed object must not be classified simultaneously as both Workflow and Instruction.
- An Instruction must not create or alter authority.
- A Workflow must not create or alter normative requirements.
- A Process must not be cited as enforceable authority.
- A Standard must not become a substitute for unresolved project purpose or project facts.
- Tool capability, successful execution, or operational precedent must not be promoted into a Standard without curator-governed amendment.

## Layer relationship

The intended stack is:

```text
L4 Standard
normative rule / constraint / authority
        ↓
L5 Workflow
coordination / sequence / roles / gates
        ↓
L6 Instruction
bounded execution / tool action / verifiable result
        ↓
Observed evidence
        ↓
Conformance / validation
```

A Process may describe this stack or its surrounding practice, but it does not occupy a governed execution layer by itself.

## Authoring and migration rule

Source documents may mix rules, workflows, instructions, examples, and explanatory narrative. Migration must classify source meaning rather than replicate source page structure.

When ingesting new content:

- preserve source provenance;
- extract each governed concept to its authoritative home;
- use references instead of duplicating governing truth;
- retain descriptive material as informative where useful;
- preserve unresolved source ambiguity as a gap rather than guessing its class;
- prefer adding governed objects or relationships over changing repository architecture.

## AI-assisted authoring rule

AI systems operating in this repository must classify content before authoring or modifying governed objects.

They must:

- route normative statements to Standards;
- route orchestration logic to Workflows;
- route bounded execution steps to Instructions;
- treat descriptive Processes as informational;
- escalate ambiguous mixed-class content rather than silently blending authority levels;
- never infer that a how-to, example, API action, or successful precedent has normative standing.

## Extensibility principle

New standards content should normally be absorbed by adding or enriching governed objects within these classes.

**Extension by object addition is preferred over extension by structural modification.**

A new top-level architecture, domain, or object family should be introduced only when the new concept cannot be represented faithfully by Standard, Workflow, Instruction, Process/informative material, registry, configuration, or conformance objects and the curator explicitly approves the change.

## Provenance

This doctrine is normalized from Confluence source page ID `2818184` and aligned with the existing repository architecture and reasoning-stack separation.

During migration, Confluence remains source authority. This file is a migration-candidate architectural doctrine until formal cutover.