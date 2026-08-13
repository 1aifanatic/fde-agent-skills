# Future-State Process

## Design objective

Create an explainable, control-preserving exception flow that reacts immediately, eliminates duplicate entry, routes common cases consistently, and leaves payment authority with people. Version FS-1 is approved for delivery planning, not production.

## Target flow

| Step ID | Step | Actor/system | Inputs | Action/decision | Outputs | Exception/fallback | Control | Metric | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FS-01 | Capture and normalize | Mailbox trigger and normalizer | Email, invoice | Create stable case and normalized identifiers | Case record | Dead-letter queue and alert | Source hash; idempotency | Intake latency | approved design |
| FS-02 | Detect duplicates | Rules service | Supplier, invoice number, amount, date | Compare composite keys | Clear or duplicate hold | Ambiguous match to Jonah | No autonomous duplicate clearance | Precision/recall; false clearance = 0 | approved design |
| FS-03 | Validate PO, receipt, and policy data | Rules/integration layer | Case and LedgerOne data | Apply deterministic match and completeness rules | Matched or exception evidence | Integration failure to manual queue | Read-only until checkpoint | Rule coverage | approved design |
| FS-04 | Recommend category | Classification agent | Exception evidence | Propose category, confidence, rationale, and candidate owner | Recommendation | Low confidence or conflict to Jonah | Model/version log; threshold; correction | Accuracy and correction rate | approved design |
| FS-05 | Route accountable owner | Routing service | Approved category and owner matrix | Send case to named queue/owner and start SLA | Owned case | Unknown owner to triage | Access validation; audit | Correct-owner rate | approved design |
| FS-06 | Resolve exception | Human owner with assistant | Case, evidence, recommendation | Correct source record or supply evidence | Resolution evidence | Dispute/escalation to Mira or Sam | Separation of duties | Resolution time | approved design |
| FS-07 | Apply approval and update ERP | Human approver plus connector | Resolution and approvals | Verify policy; write payment-ready idempotently | LedgerOne status and audit event | Any missing gate remains held | No AI approval; exact approval evidence | Control bypass count | approved design |
| FS-08 | Monitor and improve | Operations dashboard | Events, SLA, corrections, outcomes | Reconcile queues, alert failures, measure targets | Operational evidence | Roll back routing/model to manual queue | Release version and rollback trigger | Cycle, effort, reopen, drift | approved design |

## Current-to-future reconciliation

| Current step | Future disposition | Replacement/owner | Decision/evidence |
| --- | --- | --- | --- |
| CS-01 | automate polling | FS-01 / Priya | S-003; APR-002 |
| CS-02 | eliminate duplicate entry | FS-01 and FS-07 / Priya | S-003; DEC-004 |
| CS-03 | automate deterministic checks | FS-02 and FS-03 / Sam | S-003; S-004 |
| CS-04 | augment classification | FS-04 / Jonah remains accountable for low confidence | S-003; DEC-002 |
| CS-05 | simplify ownership and automate routing | FS-05 / Mira | S-002; S-003 |
| CS-06 | automate timers; retain human escalation | FS-05, FS-06, FS-08 / Mira | S-003 |
| CS-07 | simplify policy; retain human approval | FS-07 / Sam | S-004; DEC-001 |
| CS-08 | automate approved update | FS-07 / Priya with Jonah checkpoint | S-004; DEC-004 |
| EX-04 | retain human decision | FS-02 and FS-06 / Jonah and Sam | DEC-003 |
| EX-05 | retain human-only sensitive change | FS-06 / authorized data owner | DEC-003 |
