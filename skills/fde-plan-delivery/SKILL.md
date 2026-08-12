---
name: fde-plan-delivery
description: Turn an approved FDE future-state process into a governed, executable delivery plan with requirements, architecture decisions, backlog, traceability, tests, security, rollout, observability, and release evidence. Use after process redesign, when planning implementation, refining a project backlog, defining acceptance, preparing UiPath delivery, or assessing whether a solution is ready to build or release.
---

# Plan FDE Delivery

Convert approved business design into small verifiable work without fabricating product contracts.

## Confirm the design baseline

1. Read the charter, status, future state, allocation matrix, decisions, risks, approvals, and open knowledge needs.
2. Confirm the current and future states have named approval.
3. Return to `$fde-interview-engagement` or `$fde-reengineer-process` when a gate-critical business decision is missing.
4. Discover the UiPath project before choosing official implementation skills.

**Completion criterion:** Planning begins from an approved baseline with explicit remaining assumptions.

## Define requirements and acceptance

Assign stable IDs to:

- business outcomes;
- functional requirements;
- nonfunctional requirements;
- controls and security requirements;
- operational requirements;
- adoption/training requirements.

Give each requirement an owner, evidence, acceptance criteria, priority, and status. Update `fde/delivery/requirements.md`.

## Design through official owners

Route to the matching official skills:

- SDD/solution: `$uipath-solution`;
- component contract: `$uipath-component-design`;
- project boundaries: `$uipath-project-boundaries`;
- security: `$uipath-solution-security-assessment`;
- observability: `$uipath-observability-design`;
- artifact implementation: the official artifact skill;
- tests: `$uipath-test` or `$uipath-test-driven-automation`;
- repository gates: `$uipath-quality-gates-setup`;
- release evidence: `$uipath-release-readiness`.

Record decisions and produced artifact references in `fde/delivery/architecture.md`; keep current commands and schemas in their official owners.

## Build the delivery plan

Create session-sized backlog items in `fde/delivery/backlog.md`. Each item needs:

```text
ID | outcome | requirement IDs | files/components | dependencies |
acceptance checks | test evidence | risk | rollback/checkpoint | status
```

Order work as thin vertical slices. Establish a red-capable test before high-risk implementation. Separate product behavior from cloud/tenant provisioning.

## Establish traceability

Update `fde/delivery/traceability.md`:

```text
Requirement -> approved process/design -> implementation component ->
test/UAT case -> evidence -> release version
```

Flag orphan requirements, untested components, unsupported controls, and evidence that no longer matches the baseline.

## Plan verification and release

Update test plan, risks/controls, approvals, and runbook with:

- deterministic, integration, evaluation, security, recovery, and UAT coverage;
- environment progression;
- data and access prerequisites;
- deployment approval;
- monitoring and support ownership;
- rollback or compensating actions;
- post-release outcome measurement.

**Completion criterion:** Every critical requirement is owned, implemented by a planned component, verified by a named test, and required by a release gate.

## Finish

Return the executable sequence, critical path, blockers, official skills required, test/evidence gaps, release risks, and next smallest verifiable work item. Do not imply build, test, publish, or deployment occurred unless observed.
