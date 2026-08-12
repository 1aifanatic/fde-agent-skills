# Current-State Process

## Boundary

The process starts when an invoice reaches ap@northstar.example and ends when LedgerOne records payment-ready. Payment execution and vendor-master updates are outside the boundary. Mira Patel is accountable; Jonah Lee performs most exception work.

## Normal flow

| Step ID | Step | Performer/owner | Trigger | Inputs | Systems | Rule/action | Outputs | Dependency | Timing/volume | Evidence | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CS-01 | Monitor inbox | Jonah / Mira | New email | Invoice and attachment | Shared mailbox | Check mailbox every two hours | Candidate invoice | None | 1,200/month; up to 2-hour wait | S-001; S-003 | confirmed |
| CS-02 | Register invoice | Jonah / Mira | Candidate found | Supplier, number, date, amount | LedgerOne; spreadsheet | Re-key identifiers into two systems | ERP record and tracker row | CS-01 | Manual duplicate entry | S-003 | confirmed |
| CS-03 | Match records | Jonah / Mira | ERP record exists | Invoice, PO, receipt | LedgerOne | Compare required fields and approvals | Matched or exception | CS-02 | 18% exception rate | S-001; S-002 | confirmed |
| CS-04 | Classify exception | Jonah / Mira | Match fails | Mismatch details | Spreadsheet; inbox | Choose one of five informal categories | Category | CS-03 | Manual judgment | S-003 | confirmed |
| CS-05 | Route case | Jonah / Mira | Category chosen | Category, requester, PO data | Email | Find likely owner and send free-text email | Ownership request | CS-04 | Frequent forwarding | S-002; S-003 | confirmed |
| CS-06 | Chase and escalate | Jonah / Mira | No response | Email thread, tracker | Email; spreadsheet | Check twice daily; escalate after two business days | Response or manager escalation | CS-05 | Main wait and rework loop | S-003 | confirmed |
| CS-07 | Apply approval control | Jonah / Sam | Data corrected | Invoice type, amount, change type | LedgerOne | Apply PO or non-PO approval and sensitive-exception rules | Approved or held | CS-06 | Policy-dependent | S-004; DEC-001 | approved |
| CS-08 | Mark payment-ready | Jonah / Mira | Checks complete | Corrected record and approval | LedgerOne | Change status and retain evidence | Payment-ready invoice | CS-07 | End condition | S-001; S-004 | approved |

## Exceptions and recovery

| Exception ID | Related step | Condition | Frequency/severity | Actual response | Owner/escalation | Control | Evidence | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EX-01 | CS-03 | Missing purchase order | 34% of exceptions; medium | Email Procurement Operations; cases may be forwarded | Elena; Mira after 2 days | No payment-ready without valid basis | S-002; S-003 | confirmed |
| EX-02 | CS-03 | Missing receipt | 27%; medium | Email requester/receiver and chase | Requester; Mira after 2 days | Receipt or authorized exception required | S-002; S-003 | confirmed |
| EX-03 | CS-03 | Price or quantity mismatch | 22%; high | Procurement and requester reconcile | Elena; Mira | Approved PO change required | S-003; S-004 | confirmed |
| EX-04 | CS-03 | Suspected duplicate | 9%; critical | Hold and manually compare composite keys | Jonah; Sam for ambiguity | No autonomous clearance | S-003; S-004 | approved |
| EX-05 | CS-03 | Invalid tax or vendor data | 8%; high | Hold and send to authorized data owner | Jonah; Sam | Human review; no agent master-data write | S-003; S-004 | approved |
| EX-06 | CS-05 | Recipient forwards without ownership | Common; medium | Jonah finds another recipient and restarts wait | Mira after 2 days | None beyond manual tracker | S-003 | confirmed |
| EX-07 | CS-06 | Reply arrives after case changed | Occasional; medium | Jonah manually reconciles thread and tracker | Mira | Manual review before ERP status change | S-003 inference | inferred |
