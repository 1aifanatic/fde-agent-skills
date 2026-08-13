# Synthetic Source S-003: AP Specialist Interview

- **Speaker:** Jonah Lee, AP Specialist
- **Interview date:** 2026-08-06
- **Classification:** Synthetic demonstration data

## Actual exception work

- Jonah checks the inbox every two hours and copies invoice identifiers into both LedgerOne and a spreadsheet.
- He classifies exceptions using five informal categories: missing PO, missing receipt, price or quantity mismatch, suspected duplicate, and invalid tax or vendor data.
- Approximate share of exceptions: 34%, 27%, 22%, 9%, and 8%, respectively.
- Missing-PO and missing-receipt cases often loop because the first recipient forwards the email without taking ownership.
- Jonah checks for replies twice daily. After two business days he escalates to Mira.
- Duplicate suspicion and vendor-tax problems always remain under human review.
- The same invoice can appear under filename variants; supplier, invoice number, amount, and date are the reliable duplicate keys.

## Adoption concerns

- A one-click fully autonomous process would be rejected because specialists need to understand why an invoice was routed.
- A useful assistant would propose a category, show the matched evidence, identify the accountable owner, and let Jonah correct the result before any ERP update.
