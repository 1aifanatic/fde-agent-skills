# Test Plan

| Test ID | Requirement/risk | Level | Fixture/environment | Expected result | Evidence | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T-001 | FR-001 | deterministic | Duplicate delivery of same synthetic invoice | One active case and one duplicate delivery event | Not run | Priya | planned |
| T-002 | FR-002; R-003 | control/regression | Exact and near-duplicate fixtures | Every suspected duplicate held; no payment-ready action | Not run | Sam | planned |
| T-003 | FR-003 | deterministic/integration | Approved PO, receipt, mismatch fixtures; sandbox | Expected rule result and manual fallback on integration error | Not run | Priya | blocked by KN-007 |
| T-004 | FR-004; FR-005; R-001 | AI evaluation | De-identified labeled exception set | Accuracy threshold defined; evidence/rationale present; low confidence/conflict enters human queue | Not run | Mira | blocked by KN-006 |
| T-005 | FR-007; R-002 | negative/security | Attempt agent approval and sensitive writes | Capability unavailable and request logged/held | Not run | Sam | planned |
| T-006 | NFR-001; SEC-001; R-004 | audit/security | Representative events | Complete audit fields; no unnecessary sensitive content; retention applied | Not run | Priya | planned |
| T-007 | FR-006 | deterministic | Each category plus unknown owner | Correct approved route; unknown owner to triage | Not run | Mira | planned |
| T-008 | OPS-001; CHG-001; R-005 | integration/recovery | Mailbox outage and proposed routing change | Alert within 10 minutes; no case loss; rollback restores prior mailbox | Not run | Priya | planned |
| T-009 | NFR-002 | recovery | Interrupted LedgerOne write and delayed callback | Reconcile actual state before retry; no duplicate status update | Not run | Priya | blocked by KN-007 |
| UAT-001 | ADP-001; BO-001; BO-002 | business UAT | Synthetic end-to-end cases | Jonah and Mira can understand, correct, route, and recover; measurement method accepted | Not run | Mira | planned |
