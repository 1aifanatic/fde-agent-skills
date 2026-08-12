# Automation Allocation

| Step ID | Current problem | Disposition | Rationale | Risk/control | Human accountability | Evidence | Approval |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CS-01 | Two-hour polling delay | deterministic automation | Mailbox event and attachment capture are rule-based | Reconciliation and dead-letter alert | Priya owns support | S-001; S-003 | APR-002 |
| CS-02 | Duplicate entry | UiPath RPA/API workflow | Normalize once and write through approved LedgerOne contract | Idempotency key; no write until validation | Priya; Jonah corrects failures | S-003 | APR-002 |
| CS-03 | Repetitive matching | deterministic automation | PO, receipt, amount, and duplicate keys have explicit rules | Sensitive cases held | Sam owns controls | S-003; S-004 | APR-002 |
| CS-04 | Informal inconsistent categories | agentic AI with human-in-the-loop | Text and attachment evidence require interpretation; confidence varies | Evidence display; >=0.90 threshold; correction; audit | Jonah confirms low confidence | S-003; DEC-002 | APR-002 |
| CS-05 | Free-text routing and unclear owner | simplify plus deterministic automation | Establish owner matrix, then route by category and source data | Unknown owner falls to triage | Mira owns matrix | S-002; S-003 | APR-002 |
| CS-06 | Manual chasing and hidden waits | deterministic automation plus human escalation | Timers and reminders are rule-based; ownership decisions are human | SLA monitor and escalation | Mira receives escalation | S-003 | APR-002 |
| CS-07 | Conflicting approval interpretation | simplify and deterministic policy check | DEC-001 resolves policy; approval itself remains human | Negative tests; no AI approval | Sam approves controlled cases | S-004; DEC-001 | APR-002 |
| CS-08 | Manual status update | UiPath RPA/API workflow with human checkpoint | Update is deterministic after all gates pass | Approval evidence and idempotent write | Jonah/Mira accountable | S-004; DEC-004 | APR-002 |
| EX-04 | Duplicate suspicion | human-only decision supported by deterministic comparison | Failure impact is critical | Mandatory hold; composite-key evidence | Jonah and Sam | S-003; S-004 | APR-002 |
| EX-05 | Sensitive vendor/tax data | human-only | Authority and data sensitivity prohibit agent writes | Authorized data owner and full audit | Sam | S-004; DEC-003 | APR-002 |
