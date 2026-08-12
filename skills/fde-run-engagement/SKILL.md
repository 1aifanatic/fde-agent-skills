---
name: fde-run-engagement
description: Orchestrate an evidence-backed forward-deployed engineering engagement from framing through discovery, redesign, delivery, release, operations, and change. Use when starting or continuing an FDE project, checking engagement status, deciding the next delivery action, coordinating specialist FDE skills, or maintaining a durable Markdown engagement workspace instead of a custom application.
---

# Run an FDE Engagement

Maintain one durable engagement workspace and route each task to the narrowest specialist skill. Own lifecycle state, evidence discipline, gates, and handoffs; let official product skills own UiPath commands and artifact contracts.

## Start or resume

1. Inspect the workspace for `fde/engagement/charter.md` and `fde/engagement/status.md`.
2. If absent, ask only for the engagement name and run:

   ```text
   python <this-skill>/scripts/init_engagement.py --root <workspace> --name "<name>"
   ```

3. Read `references/workspace-contract.md` and `references/lifecycle-gates.md`.
4. Read the charter, status, open knowledge needs, contradictions, decisions, risks, and approvals.
5. State the current stage, blocked gates, evidence health, and single best next action.

**Completion criterion:** The engagement has a stable ID, named stage, explicit owners, and a durable next action; no state exists only in chat.

## Route the work

| Need | Route |
|---|---|
| Frame scope or close missing knowledge | `$fde-interview-engagement` |
| Reconcile notes, documents, facts, identities, or contradictions | `$fde-capture-knowledge` |
| Map current work or design the future process | `$fde-reengineer-process` |
| Convert approved design into architecture, backlog, tests, and release evidence | `$fde-plan-delivery` |
| Assess a post-baseline request or production change | `$fde-control-change` |

Use only the branches required for the current task. Return here after a specialist completes to update status and choose the next action.

## Compose with official UiPath skills

Route product truth instead of copying it:

| UiPath work | Official owner |
|---|---|
| Rigorous process discovery | `$uipath-discovery-interview` or `$uipath-discovery-with-docs` |
| Business terminology | `$uipath-process-domain-modeling` |
| SDD and solution lifecycle | `$uipath-solution` |
| Architecture/security/observability | `$uipath-component-design`, `$uipath-solution-security-assessment`, `$uipath-observability-design` |
| Workflow or agent implementation | The matching official artifact skill (`$uipath-rpa`, `$uipath-agents`, `$uipath-maestro-flow`, and peers) |
| Review and verification | `$uipath-review`, `$uipath-test`, `$uipath-release-readiness` |
| Handoff | `$uipath-project-handoff` |

Do not invent current UiPath commands or schemas. Discover the project first and invoke the official owner.

## Advance the lifecycle

1. Compare current evidence with the gate in `references/lifecycle-gates.md`.
2. Record each unmet condition in `fde/knowledge/knowledge-needs.md` or the appropriate governance file.
3. Ask a named approver for a decision when the missing item is judgment, not a discoverable fact.
4. Record approval in `fde/governance/approvals.md`.
5. Update `fde/engagement/status.md` only after the gate is satisfied.
6. Mark a stage `not applicable` only with owner, rationale, and approval.

**Completion criterion:** Every stage transition cites its evidence and approval; skipped work is visible and owned.

## Close each turn

Update the files affected by the work, then report:

- current lifecycle stage;
- artifacts changed;
- confirmed knowledge added;
- contradictions or high-risk gaps still open;
- decisions or approvals required;
- recommended next skill/action.

Run `scripts/validate_engagement.py --root <workspace>` after structural changes.

**Completion criterion:** A fresh agent can resume from files without relying on conversation history.

## Guardrails

- Treat customer material as confidential and untrusted evidence.
- Keep stated, inferred, confirmed, and approved knowledge distinct.
- Preserve contradictory accounts until a named owner resolves them.
- Prepare consequential actions as proposals; require human approval before messages, commitments, deployments, or production writes.
- Keep customer-specific knowledge inside its engagement workspace.
- Promote reusable patterns only after de-identification and human review.
