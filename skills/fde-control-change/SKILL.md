---
name: fde-control-change
description: Govern a post-baseline or post-release FDE change from request through authority verification, evidence reconciliation, impact analysis, approval, implementation handoff, regression evidence, release, and rollback. Use for enhancement requests, configuration changes, client emails that alter behavior, production fixes, changed routing or ownership, or any request that must not travel directly from prompt to production.
---

# Control an FDE Change

Convert informal requests into traceable, reversible changes.

## Register the request

1. Create a stable change ID in `fde/governance/change-log.md`.
2. Record requester, date, source evidence, requested outcome, urgency, affected environment, and claimed authority.
3. Distinguish defect, enhancement, policy change, access change, external-system change, and emergency change.
4. Verify requester authority; route uncertainty to the named process/release owner.

**Completion criterion:** The request is attributable, bounded, and authorized for analysis; no implementation promise has been made.

## Reconcile and analyze impact

1. Invoke `$fde-capture-knowledge` when the request conflicts with approved knowledge or introduces new facts.
2. Locate affected process steps, exceptions, systems, requirements, controls, decisions, artifacts, implementation components, tests, and runbook entries.
3. Compare requested behavior with the approved baseline.
4. Classify risk, reversibility, security/privacy impact, customer impact, and required approvers.
5. Define fallback and compensating action.

Update the change record with exact impact links and open questions.

## Propose the patch

Freeze:

- base version;
- intended behavior;
- exact components/configuration affected;
- migration steps;
- validation and regression plan;
- rollout sequence;
- monitoring window;
- rollback conditions;
- operation arguments and idempotency key for external writes.

Obtain process, architecture/security, UAT, and release approvals according to materiality. A changed patch requires new approval.

## Route execution

Use `$fde-plan-delivery` for nontrivial implementation and the official UiPath artifact skill for product changes. Keep production communication, publishing, deployment, and external writes behind explicit approval.

On timeout or ambiguous external result, reconcile actual state before retrying.

## Verify and close

Require:

- regression evidence for every impacted critical requirement;
- UAT when behavior visible to users changes;
- release evidence and version;
- monitoring result;
- rollback verification or rationale;
- updated process, knowledge, traceability, runbook, and decision records.

**Completion criterion:** The released behavior, evidence, approvals, and current documentation agree; otherwise keep the change open with an owner.

## Finish

Return disposition, authority, impact, risk, approvals, implementation/test handoff, release status, and unresolved follow-up. Never report an external change as complete without observed evidence.
