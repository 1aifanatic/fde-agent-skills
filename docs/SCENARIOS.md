# Before-and-After Scenarios

These scenarios show how the FDE skills change the quality of an engagement before implementation. All organizations, systems, people, and numbers are fictional.

## Scenario 1: Accounts-payable invoice exceptions

### Before

The request is “use AI to automate AP exceptions.” The team has a 12-page SOP, a shared mailbox, an ERP, and a spreadsheet. The SOP says every invoice above USD 10,000 requires Controller approval. The AP manager says only non-PO invoices above that amount require it. Nobody has documented what happens when an owner ignores the email.

A general agent could summarize the SOP and propose an invoice agent. That would leave a material control contradiction, hide the actual rework loop, and confuse classification with approval.

### Skill flow

1. fde-run-engagement bounds intake through payment-ready and records non-goals.
2. fde-interview-engagement asks the AP manager, actual specialist, Controller, and systems owner different questions.
3. fde-capture-knowledge indexes sources, preserves the approval contradiction, and resolves it through the control policy.
4. fde-reengineer-process maps five exception families, forwarding, waiting, escalation, duplicate entry, and sensitive holds.
5. fde-plan-delivery creates requirements, components, vertical slices, evaluation, recovery, UAT, and traceability.
6. fde-control-change turns a later mailbox-routing email into CHG-001 and stops before unapproved production work.

### After

The design uses rules for duplicate/PO/receipt checks, AI for explainable classification recommendations, human review for low confidence, and human-only authority for duplicate clearance and sensitive data. LedgerOne remains the system of record. The first slice is safe intake and duplicate hold, not an end-to-end autonomous agent.

### Demonstrated effect

- Ambiguous goal becomes measurable boundary and targets.
- A control conflict becomes an approved governing decision.
- Hidden work becomes explicit design input.
- AI scope becomes narrower, evaluable, and safer.
- Backlog and tests are linked to evidence.
- Informal change is governed.

Inspect the [complete worked example](../examples/northstar-ap-transformation/README.md).

## Scenario 2: Customer-support escalation triage

### Before

A SaaS company wants an agent to “handle escalations.” Support, engineering, and customer success each use a different severity definition. Enterprise customers bypass the queue by emailing account executives. The documented SLA starts when a ticket is created, but the actual timer begins when a support lead notices the message.

A quick automation would route by keywords and risk sending contract, security, or outage cases to the wrong team.

### Skill flow

- The interview skill asks who may declare severity, what contractual tiers exist, what evidence confirms an outage, how VIP exceptions work, and what happens after a false escalation.
- Knowledge capture defines incident, escalation, severity, customer impact, and ownership; it opens contradictions across the three severity policies.
- Process reengineering eliminates duplicate intake and creates a deterministic contract/customer lookup.
- AI summarizes evidence and recommends severity; a support lead confirms high-impact cases.
- Delivery planning requires recall/precision evaluation by class, negative security tests, SLA timer semantics, and a fallback manual queue.
- Change control governs new customer tiers and routing rules after release.

### Before and after

| Before | After |
| --- | --- |
| Keyword router | Evidence-backed recommendation plus deterministic contract rules |
| Three severity definitions | Approved glossary and decision |
| SLA starts implicitly | Explicit event and observable timer |
| VIP email bypass | Indexed intake and governed exception |
| No false-escalation recovery | Correction, audit, replay, and manual fallback |
| “Agent handles escalation” | Human authority retained for severity and external communication |

## Scenario 3: Enterprise customer onboarding

### Before

Sales promises a 30-day onboarding. Implementation tracks tasks in a project tool, Security uses a spreadsheet, and the customer sends identity and network details through email. Every onboarding appears unique because terminology, sequencing, and ownership differ.

The temptation is to build an autonomous onboarding agent that chases everyone. The actual problem is unclear prerequisites and inconsistent ownership.

### Skill flow

1. Frame the engagement around time-to-first-value and non-negotiable security gates.
2. Interview Sales, implementation, security, support, and a recently onboarded customer.
3. Capture product/package terminology, account identities, prerequisites, evidence, and contradictions in promised scope.
4. Reengineer the work into a dependency-driven plan:
   - eliminate duplicate intake;
   - normalize package and environment data;
   - automate reminders and evidence validation deterministically;
   - use AI to summarize customer documents and identify likely gaps;
   - require humans for security acceptance, scope tradeoffs, and customer commitments.
5. Plan delivery with prerequisite-state tests, access controls, customer-visible UAT, monitoring, and rollback.
6. Control later scope promises through an attributable change record.

### Before and after

| Before | After |
| --- | --- |
| Every onboarding treated as bespoke | Stable dependency model with explicit variants |
| Sales promise becomes delivery fact | Promise is evidence; authorized baseline is a decision |
| Sensitive data in ad hoc email | Approved intake and retention boundary |
| Manual chasing | Deterministic reminders tied to named dependencies |
| AI “owns onboarding” | AI summarizes; humans own commitments and security |
| Status reconstructed in meetings | Durable stage, blockers, owners, and next action |

## Scenario 4: Finance reconciliation workflow

### Before

A reconciliation team copies files from three banks, matches transactions in spreadsheets, and sends unexplained items to “Chris.” The close calendar requires completion by day three, but nobody agrees whether pending bank corrections count as complete.

A developer proposes automating the spreadsheet and adding an LLM for unmatched rows.

### Skill flow

- Capture the completion definition and identify “Chris” through a deterministic role or account identity.
- Map file timing, formats, duplicate deliveries, match rules, thresholds, close controls, and unresolved-item escalation.
- Separate deterministic matching from judgment:
  - file retrieval and schema validation: deterministic;
  - exact/fuzzy match within approved bounds: rules;
  - narrative explanation draft: AI;
  - write-off, materiality, and close sign-off: human authority.
- Trace every materiality/control requirement to negative tests and release evidence.
- Measure close timing and rework after release rather than claiming savings from the plan.

### Before and after

| Before | After |
| --- | --- |
| “Chris handles exceptions” | Named role, authority, escalation, and backup |
| Spreadsheet is both workflow and evidence | Controlled workflow plus auditable evidence |
| Undefined “complete” | Approved end condition |
| LLM proposed for matching | Deterministic rules first; AI limited to explanation |
| Close-risk discovered late | Control tests and rollback planned before build |

## Scenario 5: Post-release routing change

### Before

A customer emails: “Please send QC reports to the new operations mailbox starting tomorrow.” The requester is known, and the change looks small. An autonomous agent could edit configuration and reply “done.”

The email omits whether the new mailbox is authorized for the data, who monitors it, how historical reports are handled, what test proves success, and how to recover if delivery fails.

### With fde-control-change

The skill:

1. creates a stable change ID;
2. records the request and verifies authority for analysis;
3. compares it to the approved baseline;
4. finds affected process steps, access controls, requirements, configuration, tests, monitoring, and runbook;
5. proposes an exact configuration patch;
6. defines canary, reconciliation, alert, and rollback;
7. obtains data-owner, process-owner, UAT, and release approval as required;
8. reconciles actual state after deployment before closing.

### After

The change may still be simple, but it is no longer invisible. “Small” refers to code size, not operational risk.

## Cross-scenario lesson

The suite's main impact is not producing more documents. It is producing better decisions:

- which facts are reliable;
- which contradictions matter;
- which process is actually being changed;
- which mechanism belongs at each step;
- which human retains authority;
- which evidence is required to build, test, release, operate, and change safely.

That decision quality is what lets a small FDE team go deeper into customers without scaling coordination work linearly.
