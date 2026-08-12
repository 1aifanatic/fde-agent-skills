---
name: fde-reengineer-process
description: Map an evidence-backed current-state business process and redesign it across simplification, deterministic automation, UiPath RPA, agentic AI, human-in-the-loop, and human-only work. Use for process mapping, exception analysis, AI suitability, automation allocation, future-state design, adoption analysis, or when a proposed automation risks being layered onto a broken process.
---

# Reengineer an FDE Process

Design from evidence and exceptions, not the documented golden path.

## Gate the work

1. Read the engagement charter, status, knowledge needs, contradictions, evidence index, stakeholders, and risks.
2. Read `../fde-run-engagement/references/lifecycle-gates.md`.
3. Invoke `$fde-interview-engagement` for gate-critical gaps.
4. Invoke `$fde-capture-knowledge` when source reconciliation is incomplete.
5. Stop future-state design until the current-state boundary and high-risk contradictions are owned.

**Completion criterion:** The process boundary, owner, objective, trigger, end condition, and evidence status are explicit.

## Model the current state

For every step record:

```text
ID | name | performer | accountable owner | trigger | inputs | systems |
action/decision rule | outputs | downstream dependency | normal duration |
volume | exceptions | escalation | controls | evidence | confidence/status
```

Trace normal flow and each material exception. Identify rework loops, handoffs, queues, wait states, manual workarounds, control points, duplicate data entry, and undocumented owners.

Use `$uipath-process-domain-modeling` when terms or business concepts are unstable. Use the relevant official UiPath artifact skill only after the process knowledge is ready.

## Challenge the process

For each step ask in order:

1. Can the outcome or step be eliminated?
2. Can policy or data be simplified first?
3. Is the behavior deterministic enough for an API/workflow/RPA implementation?
4. Does it require probabilistic interpretation or judgment suitable for an agent?
5. Which decisions need a human checkpoint?
6. Which step remains human-only because of accountability, empathy, negotiation, physical work, or unacceptable failure impact?

Record the disposition in `fde/process/automation-allocation.md` as:

- eliminate/simplify;
- deterministic automation;
- UiPath RPA/API workflow;
- agentic AI;
- human-in-the-loop;
- human-only.

Justify using volume, variability, data quality, judgment, reversibility, explainability, control obligations, failure severity, adoption cost, and measurable value.

## Design the future state

Update `fde/process/future-state.md` with:

- new sequence and dependencies;
- retained human responsibilities;
- automation/agent responsibilities;
- approval and escalation points;
- source-of-truth systems;
- error recovery and fallback;
- observability and outcome measures;
- adoption/training impact;
- migration assumptions.

Compare current and future states step by step. No current step disappears without a recorded disposition.

**Completion criterion:** Every step, exception, control, and ownership change is accounted for, measurable, and traceable to evidence or an approved decision.

## Finish

Return the current-state risks, automation allocation, future-state value hypothesis, unresolved design decisions, required approvals, and the next official UiPath design skill.
