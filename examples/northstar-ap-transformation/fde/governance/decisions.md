# Decisions

| ID | Date | Decision | Alternatives | Rationale/evidence | Owner | Effective scope | Supersedes | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DEC-001 | 2026-08-12 | Apply Controller approval to non-PO invoices above USD 10,000; retain PO approval for normal PO-backed invoices | Require Controller on all invoices above threshold | S-004 resolves C-001 and avoids duplicate approval while retaining sensitive-exception review | Sam Reed | FS-1 and requirements | Ambiguous S-001 wording | approved |
| DEC-002 | 2026-08-12 | Use AI only for evidence-backed classification recommendations; auto-route only at confidence >= 0.90 with deterministic policy checks and correction | Fully manual or autonomous end-to-end | S-003 adoption boundary; S-004 authority limit | Mira Patel; Sam Reed | Pilot | None | approved for design |
| DEC-003 | 2026-08-12 | Keep duplicate suspicion, vendor-master, bank-detail, and material tax changes under human review | Agent decision | S-004 | Sam Reed | All environments | None | approved |
| DEC-004 | 2026-08-12 | Keep LedgerOne as the system of record and write only after approved human checkpoints | Replace ERP or parallel database as authority | Charter constraint and S-002 | Mira Patel; Priya Nair | Engagement | None | approved |
