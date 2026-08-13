# Engagement Handoff

## Mission

Reduce AP invoice-exception cycle time and manual triage while preserving LedgerOne, payment controls, human authority, and auditability.

## Current stage and gate

Delivery planning is complete as a design artifact. Implementation, UAT, release, and production measurement remain open.

## Confirmed knowledge

- Synthetic baseline: 1,200 invoices/month; 18% exception rate; 6.2-day average cycle; 28 triage hours/week; 11% reopen rate.
- Jonah Lee is the actual primary exception handler.
- Five exception families account for the current work.
- Non-PO invoices above USD 10,000 require Controller approval; PO-backed invoices normally rely on purchase-order approval.
- AI may assist with classification and routing but may not approve payment or modify vendor/bank data.

## Critical gaps and contradictions

- C-001 is resolved by control policy S-004 and DEC-001.
- Representative de-identified fixtures and the LedgerOne sandbox contract remain missing.
- CHG-001 lacks UAT and production release approval.

## Approved decisions

- DEC-001: Apply the control-policy interpretation for Controller approval.
- DEC-002: Use AI only for evidence-backed classification/recommendation with confidence gating and correction.
- DEC-003: Keep duplicate suspicion and sensitive vendor/tax changes under human review.
- DEC-004: Preserve LedgerOne as system of record.
- APR-002: Future-state baseline FS-1 approved for delivery planning.

## Risks and controls

High risks are payment-control bypass, false duplicate clearance, sensitive-data exposure, and opaque model routing. Controls include human approval, deterministic policy checks, confidence thresholds, immutable decision logs, de-identified evaluation fixtures, and rollback to the manual queue.

## Next action

Implement BL-001 in a sandbox through the official artifact owner. Do not claim deployment or ROI until tests, UAT, approvals, monitoring, and production measurements exist.
