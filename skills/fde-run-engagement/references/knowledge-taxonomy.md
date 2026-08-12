# FDE Knowledge Taxonomy

Use this taxonomy to find consequential unknowns. Do not turn it into a mechanical questionnaire.

## 1. Outcome and scope

- Business problem, desired outcome, baseline, target, and measurement method
- In-scope/out-of-scope processes, regions, products, entities, and time period
- Sponsor, process owner, delivery owner, and decision authority
- Timeline, commercial commitments, dependencies, and non-goals

## 2. Stakeholders and adoption

- Performers, approvers, exception handlers, system owners, control owners, support
- Incentives, pain points, workarounds, adoption risks, training and communication needs
- Authority boundaries and escalation paths

## 3. Current process

- Trigger, completion condition, steps, handoffs, wait states, queues, rework loops
- Inputs, outputs, rules, decisions, ownership, evidence, normal duration
- Documented procedure versus observed or lived behavior

## 4. Exceptions and recovery

- Missing, late, invalid, duplicate, contradictory, and out-of-policy inputs
- Failure recipient, actual recovery work, escalation, retry, fallback, and abandonment
- Frequency, severity, cycle time, control and customer impact

## 5. Systems and integrations

- Systems of record, interfaces, APIs, files, UI automation, batch schedules
- Environments, ownership, authentication, rate/size limits, availability, support
- Existing automations and technical debt

## 6. Data and documents

- Data objects, schemas, identifiers, lineage, quality, retention, residency, classification
- Source of truth, reconciliation, attachment formats, sample data, expected volumes
- PII, financial, health, secret, regulated, or contractual information

## 7. Rules, risks, and controls

- Business rules, approval thresholds, segregation of duties, audit evidence
- Legal, regulatory, privacy, security, AI, and contractual constraints
- Reversibility, explainability, failure severity, fraud/abuse paths

## 8. Volume and performance

- Transaction volume, peaks, seasonality, concurrency, backlog
- Cycle time, touch time, SLA, error rate, rework, availability, cost
- Current measurement source and data confidence

## 9. Future-state allocation

- Eliminate/simplify, deterministic automation, RPA/API, agentic AI, HITL, human-only
- Model/tool boundaries, confidence handling, escalation, fallback, observability
- User experience and retained accountability

## 10. Requirements and architecture

- Functional behavior and acceptance criteria
- Performance, availability, resilience, security, privacy, operability, maintainability
- Project boundaries, reusable components, source control, environments, configuration

## 11. Verification and acceptance

- Golden cases, edge cases, negative/adversarial cases, data fixtures
- Unit, integration, regression, evaluation, security, recovery, UAT evidence
- Named business acceptance and release criteria

## 12. Release and operations

- Deployment authority, cutover, rollback/compensation, monitoring, alerting
- Incident ownership, support model, runbook, retention/deletion, handoff
- Change intake, impact analysis, regression, approval, outcome review

## 13. Value and learning

- Revenue uplift, cost/capacity, cycle time, quality, risk mitigation
- Attribution method, measurement window, counterfactual, adoption
- Reusable pattern criteria and de-identification approval

## Knowledge item contract

Record consequential items with:

```text
ID | category | question or atomic claim | status | evidence/source |
owner | needed-by stage | blocked decision | risk if unknown |
next action | observed/effective/last-verified dates
```

## Coverage gate

Coverage is sufficient when every gate-critical item is evidenced, approved, contradicted with an assigned resolver, or explicitly not applicable. A percentage alone cannot satisfy the gate.
