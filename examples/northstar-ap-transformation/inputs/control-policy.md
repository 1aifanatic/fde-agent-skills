# Synthetic Source S-004: Payment Control Policy Extract

- **Owner:** Sam Reed, Controller
- **Effective date:** 2026-03-01
- **Classification:** Synthetic demonstration data

## Policy

- Non-PO invoices above USD 10,000 require Controller approval.
- PO-backed invoices rely on the purchase-order approval chain unless an exception changes supplier, amount, bank details, tax treatment, or payment terms.
- Duplicate suspicion, vendor-master changes, and bank-detail changes require manual review.
- AI may classify, summarize, recommend, or route. AI may not approve payment, change vendor master data, or override a control.
- Every automated decision must record the input identifiers, rule or model version, confidence when applicable, outcome, human correction, and timestamp.
- A release affecting payment routing requires process-owner, control-owner, UAT, and release approval.
