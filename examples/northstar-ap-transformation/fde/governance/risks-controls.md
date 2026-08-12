# Risks and Controls

| ID | Risk/cause | Impact | Severity | Control/mitigation | Owner | Evidence/test | Residual risk | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R-001 | Incorrect classification routes an invoice to the wrong owner | Delay, privacy exposure, or rework | high | Confidence threshold, deterministic routing policy, evidence display, human correction, audit log | Mira Patel | T-003; T-004; UAT-001 | medium | planned |
| R-002 | Automation bypasses payment approval | Unauthorized payment-ready status | critical | AI cannot approve; approval state checked deterministically; negative tests and release gate | Sam Reed | S-004; T-005 | low | planned |
| R-003 | Duplicate invoice is incorrectly cleared | Duplicate payment | critical | Duplicate cases always held for human review; composite-key detection; no autonomous clearance | Sam Reed | S-003; S-004; T-002 | low | planned |
| R-004 | Customer data enters an unapproved model or log | Confidentiality breach | high | De-identified evaluation fixtures, approved endpoint, data-minimizing logs, retention policy | Priya Nair | SEC-001; T-006 | medium | open |
| R-005 | Mailbox/routing change silently drops cases | SLA failure | high | Queue health metrics, reconciliation, canary, rollback to prior mailbox, owner verification | Priya Nair | CHG-001; T-008 | low | planned |
| R-006 | Users reject opaque recommendations | Workaround adoption and shadow process | medium | Evidence-backed explanation, correction action, UAT with Jonah and Mira | Mira Patel | S-003; UAT-001 | low | planned |
