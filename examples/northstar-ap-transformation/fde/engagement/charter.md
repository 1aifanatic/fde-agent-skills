# Engagement Charter

- **Engagement:** Northstar AP Invoice Exception Transformation
- **Engagement ID:** FDE-DEMO-001
- **Created:** 2026-08-12
- **Sponsor:** Dana Brooks, CFO (fictional)
- **Process owner:** Mira Patel, AP Manager (fictional)
- **Delivery owner:** Priya Nair, Finance Systems Engineer (fictional)

## Business problem and outcome

Northstar's fictional AP team needs to shorten invoice-exception resolution without replacing LedgerOne or weakening payment controls. The design goal is to make intake, classification, ownership, and follow-up reliable while keeping approval and sensitive decisions under human authority.

## Scope and non-goals

**In scope:** invoice arrival at ap@northstar.example through the payment-ready status in LedgerOne; exception classification, routing, evidence, escalation, and operational monitoring.

**Non-goals:** invoice OCR replacement, payment execution, vendor-master modification, bank-detail modification, ERP migration, procurement-policy redesign, and autonomous payment approval.

## Baseline and success measures

| Measure | Synthetic baseline | Target | Evidence |
| --- | ---: | ---: | --- |
| Monthly invoices | 1,200 | Capacity maintained | S-002, Confirmed scope and outcomes |
| Exception rate | 18% / 216 invoices | Observe; no artificial suppression | S-002 |
| Average exception cycle time | 6.2 business days | Under 3.0 business days | S-002 |
| Manual triage effort | 28 hours/week | Under 14 hours/week | S-002 |
| Reopen rate | 11% | No more than 8% | S-002 |
| Duplicate or control bypass | Zero tolerated | Zero | S-004 |

Targets are hypotheses until measured after an approved production release.

## Constraints and assumptions

- Preserve LedgerOne as the system of record.
- AI may classify, summarize, recommend, or route; it may not approve payment or alter sensitive master data.
- Low-confidence results and sensitive exceptions require human review.
- Every automated decision requires auditable evidence and version information.
- All content in this example is synthetic and must not be treated as customer or production evidence.
