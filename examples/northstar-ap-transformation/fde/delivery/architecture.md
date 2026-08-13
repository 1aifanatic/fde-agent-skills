# Architecture

## Context and boundaries

The planned solution sits above existing systems. LedgerOne remains authoritative; the mailbox is an intake channel; human work is presented through a governed task surface. This artifact defines responsibilities only and intentionally does not invent a UiPath schema or current product command.

## Components and responsibilities

| Component | Responsibility | Public contract | Owner | Decision/evidence | Status |
| --- | --- | --- | --- | --- | --- |
| C-001 Intake adapter | Receive email and create stable idempotent case | Invoice-received event with source hash | Priya | FS-01; FR-001 | planned |
| C-002 Normalizer and rules | Normalize identifiers; evaluate duplicate, PO, receipt, and policy rules | Case evidence and rule result | Priya / Sam controls | FS-02; FS-03 | planned |
| C-003 Classification agent | Recommend category, confidence, rationale, evidence, and candidate owner | Recommendation; no approval or direct sensitive write | Mira | DEC-002; FR-004 | planned |
| C-004 Routing and SLA | Apply approved owner matrix, start timers, and escalate | Owned task and routing audit | Mira | FS-05; FR-006 | planned |
| C-005 Human task surface | Show evidence; capture correction, decision, and approval | Human outcome with actor and timestamp | Jonah / Sam | S-003; FR-005; FR-007 | planned |
| C-006 LedgerOne connector | Read match data and perform idempotent payment-ready update after gates | Approved status-write command | Priya | DEC-004; KN-007 | blocked |
| C-007 Audit and observability | Store decision events, reconcile queues, metrics, alerts, and release version | Searchable immutable events and dashboards | Priya | NFR-001; NFR-002; OPS-001 | planned |

## Quality attributes

- **Safety:** prohibited actions are absent from agent capabilities; sensitive cases stay human-controlled.
- **Reliability:** ingestion and writes are idempotent; queues reconcile; failures have a manual fallback.
- **Explainability:** every AI recommendation carries evidence, confidence, and model version.
- **Security:** least privilege, approved endpoint, de-identified evaluation data, bounded retention.
- **Operability:** dashboards, alerts, runbook, rollback, correction monitoring, and named support owner.
- **Adoption:** the future state preserves visible specialist judgment rather than hiding it behind a one-step interface.
