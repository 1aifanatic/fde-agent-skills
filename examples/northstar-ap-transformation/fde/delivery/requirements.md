# Requirements

| ID | Type | Requirement | Owner | Evidence | Acceptance criteria | Priority | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BO-001 | business outcome | Reduce average exception cycle time below 3.0 business days | Mira | S-002 | Four-week post-release measure below target with sample and exclusions documented | must | approved |
| BO-002 | business outcome | Reduce manual triage below 14 hours/week without increasing reopen rate above 8% | Mira | S-002 | Time study and reopen calculation meet both thresholds | must | approved |
| FR-001 | functional | Create one idempotent case for each received invoice | Priya | FS-01 | Duplicate delivery of the same message creates no second active case | must | planned |
| FR-002 | functional/control | Hold suspected duplicates for human review | Sam | S-003; S-004 | Every duplicate fixture is held; no automated payment-ready action is possible | must | approved |
| FR-003 | functional | Evaluate PO, receipt, amount, and completeness rules | Priya | FS-03 | Expected rule outcome matches all approved fixtures | must | planned |
| FR-004 | functional/AI | Recommend category with rationale, confidence, evidence, and model version | Mira | S-003; DEC-002 | UI displays all fields; correction is retained and measurable | must | planned |
| FR-005 | functional/control | Require human review below 0.90 confidence and for conflicting evidence | Sam | DEC-002 | Boundary and conflict tests enter human queue | must | approved |
| FR-006 | functional | Route to the approved accountable owner and start SLA | Mira | FS-05 | Route matches owner matrix; unknown owner goes to triage | must | planned |
| FR-007 | control | Prevent AI from approving payment or altering sensitive master data | Sam | S-004; DEC-003 | Negative tests prove prohibited actions are unavailable | must | approved |
| NFR-001 | observability | Record source IDs, rules/model version, confidence, decision, correction, actor, and timestamp | Priya | S-004 | Every test case produces a complete immutable audit event | must | planned |
| NFR-002 | reliability | Reconcile inbox, active cases, LedgerOne status, and dead-letter queue | Priya | R-005 | No unexplained difference after recovery test | must | planned |
| SEC-001 | security/privacy | Use approved endpoint, least privilege, de-identified evaluation fixtures, and bounded retention | Sam | R-004 | Security assessment and data-handling evidence approved before release | must | open |
| OPS-001 | operations | Alert queue failure within 10 minutes and support rollback to manual queue | Priya | FS-08 | Fault injection produces alert and recovery within acceptance window | must | planned |
| ADP-001 | adoption | Let AP specialists inspect and correct classification before controlled writes | Mira | S-003 | UAT participants complete correction flow and accept usability | should | planned |
