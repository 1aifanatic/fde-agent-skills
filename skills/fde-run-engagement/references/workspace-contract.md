# FDE Engagement Workspace Contract

Use `fde/` as the durable, portable state of one engagement. Chat is transient; these files are the handoff.

## Structure

```text
fde/
|-- engagement/
|   |-- charter.md
|   `-- status.md
|-- knowledge/
|   |-- evidence-index.md
|   |-- glossary.md
|   |-- stakeholders.md
|   |-- knowledge-needs.md
|   `-- contradictions.md
|-- process/
|   |-- current-state.md
|   |-- automation-allocation.md
|   `-- future-state.md
|-- delivery/
|   |-- requirements.md
|   |-- architecture.md
|   |-- backlog.md
|   |-- traceability.md
|   |-- test-plan.md
|   `-- runbook.md
|-- governance/
|   |-- decisions.md
|   |-- risks-controls.md
|   |-- approvals.md
|   `-- change-log.md
`-- handoff.md
```

## Record rules

1. Give durable records stable IDs: `EV-`, `KN-`, `CT-`, `STK-`, `REQ-`, `DEC-`, `RSK-`, `APR-`, `CHG-`, `TST-`, and `ART-`.
2. Preserve source locators: page, slide, row, section, timestamp, file/line, URL, or system record key.
3. Distinguish statuses: `unknown`, `stated`, `evidenced`, `contradicted`, `confirmed`, `approved`, `stale`, `not-applicable`.
4. Date consequential records and name their author/owner.
5. Version approved baselines. Link later records with `supersedes`; retain earlier content.
6. Put customer facts in one engagement only. Link reusable, de-identified patterns rather than copying customer evidence.
7. Keep secrets and unnecessary PII outside the workspace.

## File ownership

| File | Authoritative content |
|---|---|
| charter | scope, outcomes, boundaries, success measures, owners |
| status | lifecycle stage, gate state, next action, blockers |
| evidence index | sources and precise origin metadata |
| glossary | approved and disputed business language |
| stakeholders | people, roles, authority, communication constraints |
| knowledge needs | required knowledge, gaps, owners, blocked decisions |
| contradictions | competing claims and resolutions |
| current state | evidenced human/system process and exceptions |
| allocation | disposition of every current step |
| future state | approved redesigned work and responsibilities |
| requirements | functional, nonfunctional, control, and operational needs |
| architecture | design decisions and official artifact references |
| backlog | session-sized verifiable delivery work |
| traceability | requirement-to-design-to-implementation-to-test-to-release |
| test plan | deterministic, integration, evaluation, security, UAT coverage |
| runbook | deploy, operate, recover, rollback, support |
| decisions | alternatives, decision, rationale, owner, effective date |
| risks/controls | risk, cause, impact, control, owner, evidence |
| approvals | gate/action approvals and exact approved baseline |
| change log | post-baseline request through release/closure |
| handoff | compact current state for a fresh agent or team member |

## Update discipline

Before editing, read the related source file and current status. After editing:

1. add evidence/decision links;
2. update affected knowledge needs and contradictions;
3. flag downstream artifacts made stale;
4. update status and handoff only when the underlying files agree;
5. run the workspace validator after structural changes.

## Completion test

A fresh agent must be able to state the engagement outcome, lifecycle stage, evidence health, critical unknowns, approved decisions, risks, and next action without conversation history.
