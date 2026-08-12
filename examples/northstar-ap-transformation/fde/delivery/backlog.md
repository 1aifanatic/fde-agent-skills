# Delivery Backlog

| ID | Outcome | Requirement IDs | Components/files | Dependencies | Acceptance checks | Test evidence | Risk | Rollback/checkpoint | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BL-001 | Safe case ingestion and duplicate hold | FR-001; FR-002; NFR-001 | C-001; C-002; C-007 | Approved synthetic fixtures | Idempotent intake; every duplicate held; full audit | T-001; T-002 | R-003 | Manual inbox; no ERP write | ready |
| BL-002 | Deterministic match and exception evidence | FR-003; NFR-001 | C-002; C-006 read-only | KN-007 | Rule results match fixtures; read failures enter manual queue | T-003 | R-005 | Disable integration and use current lookup | blocked |
| BL-003 | Explainable classification recommendation | FR-004; FR-005; ADP-001 | C-003; C-005 | KN-006; BL-002 | Required fields visible; low confidence and conflicts go human | T-004; UAT-001 | R-001; R-004; R-006 | Disable model; manual category | blocked |
| BL-004 | Governed routing and SLA | FR-006; OPS-001 | C-004; C-007 | Approved owner matrix; BL-003 | Correct route, unknown-owner fallback, alert and escalation | T-007; T-008 | R-005 | Prior mailbox/manual routing | planned |
| BL-005 | Controlled payment-ready update | FR-007; NFR-002 | C-005; C-006; C-007 | KN-007; BL-001 to BL-004 | No write without approval; idempotent write; reconciliation clean | T-005; T-009 | R-002 | Read-only mode; manual ERP update | blocked |
| BL-006 | Pilot release and measurement | BO-001; BO-002; SEC-001 | All | Tests, security, UAT, release approval | Canary succeeds; monitoring and rollback proven; measures defined | UAT-001; REL-001 | all | Stop pilot; restore manual flow | blocked |
