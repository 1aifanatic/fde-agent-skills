# Demonstrated Impact

All measures below are synthetic. Baseline values are fictional source inputs; target values are hypotheses awaiting implementation and production measurement.

## Before the skills

- Engagement context exists in meetings, inboxes, and one person's memory.
- The SOP describes a happy path but omits exception loops and actual ownership.
- “Automate AP exceptions” is too broad to design or test.
- The Controller-approval rule is contradictory across sources.
- AI is treated as one undifferentiated automation mechanism.
- Requirements, tests, controls, and rollout evidence are not connected.
- A routing-change email could be mistaken for permission to edit production.

## After the skills

- A fresh agent can resume from a validated 21-file engagement workspace.
- Five exception families, actual handlers, escalation timing, and controls are explicit.
- Every current step has a future disposition and accountable owner.
- AI is limited to explainable classification and recommendations; payment approval, duplicate suspicion, and sensitive data changes remain human-controlled.
- Requirements trace from evidence and approved design to components, tests, release evidence, and rollback.
- CHG-001 is bounded, authorized for analysis, and held before deployment until UAT and release approval exist.

## Hypothesized operational change

| Measure | Synthetic baseline | Design target | Evidence status |
| --- | ---: | ---: | --- |
| Average exception cycle time | 6.2 business days | Under 3.0 business days | Target; not measured |
| Manual triage effort | 28 hours/week | Under 14 hours/week | Target; not measured |
| Reopen rate | 11% | No more than 8% | Target; not measured |
| Control bypasses | 0 tolerated | 0 | Release gate |
| Explainable routing | Inconsistent manual notes | 100% decision records | Planned acceptance criterion |

## Delivery impact

The important impact is decision quality before code:

1. The team knows which problems are policy, data, deterministic workflow, AI classification, or human accountability.
2. High-risk behavior has explicit stop conditions.
3. The first implementation slice is small and testable.
4. ROI claims remain hypotheses until production evidence exists.
