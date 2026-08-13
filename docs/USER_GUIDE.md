# FDE Agent Skills User Guide

## Purpose

The FDE Agent Skills suite gives a forward deployed engineer a repeatable engagement method inside an AI coding agent. It focuses the agent on the work that usually determines whether an enterprise AI project succeeds: understanding the business, recovering operational truth, redesigning the process, tracing decisions into delivery, and controlling change.

The suite is an engagement and delivery-control layer. It is not a replacement for domain owners, implementation tools, product-specific skills, security review, UAT, or release authority.

## Why use this suite

### The real bottleneck is context and process design

Modern agents can execute many bounded tasks. Enterprise work remains difficult because:

- every customer has different policies, terminology, ownership, data, systems, and exceptions;
- official documentation usually describes the intended happy path;
- actual work contains queues, informal experts, retries, escalation, reconciliation, and control interpretation;
- stakeholders describe the same process differently;
- automating a bad process can make the bad process faster and harder to govern;
- delivery teams need exact evidence, decisions, requirements, tests, approvals, and rollback—not just a summary.

The suite turns these uncertainties into explicit, owned artifacts.

### The cost of unstructured FDE work

Without a durable operating model, an FDE spends time re-reading documents, reconstructing meeting context, translating between stakeholders, finding the latest decision, repairing ambiguous requirements, and defending against accidental scope or production changes. Knowledge quality declines as the engagement grows.

The suite reduces that coordination load by giving every type of knowledge a stable home and every stage a completion gate.

### What the suite improves

- **Resumability:** another FDE or agent can continue from the repository.
- **Evidence quality:** material claims have source and status.
- **Interview quality:** questions close named gaps and unlock decisions.
- **Design quality:** exceptions and controls shape the future state.
- **Automation judgment:** AI is one mechanism among several, not the default.
- **Delivery quality:** requirements trace into components, tests, evidence, and release.
- **Change safety:** requests are attributable, authorized, reversible, and testable.
- **Honesty:** planned, approved, implemented, released, and measured are distinct states.

## Operating principles

1. **Evidence before confidence.** Summaries help navigation; source-linked claims support decisions.
2. **Exceptions reveal the process.** Map failure paths, manual workarounds, and actual escalation.
3. **Simplify before automating.** Eliminate unnecessary work and settle policy/data ambiguity first.
4. **Use the least risky effective mechanism.** Prefer deterministic rules when behavior is deterministic.
5. **Keep authority human.** The agent proposes; named owners approve consequential decisions and actions.
6. **Make state durable.** No important status, decision, risk, or next action should exist only in chat.
7. **Preserve disagreement.** Contradictory evidence stays visible until a qualified resolver decides.
8. **Measure outcomes after release.** A target or forecast is not observed ROI.

## Skill router

| Current need | Invoke | Completion condition |
| --- | --- | --- |
| New engagement, status, lifecycle, handoff, or next action | $fde-run-engagement | Stable stage, owners, evidence health, blockers, and durable next action |
| Missing business/process/technical/control/support knowledge | $fde-interview-engagement | Every gate-critical gap is answered, evidenced, contradicted with owner, or scheduled |
| New documents, notes, transcripts, diagrams, or conflicting claims | $fde-capture-knowledge | Every material downstream assertion has a source/status or visible gap |
| Current-state map, exceptions, automation allocation, future-state design | $fde-reengineer-process | Every step, exception, control, and ownership change has a disposition |
| Requirements, architecture responsibilities, backlog, tests, release plan | $fde-plan-delivery | Every critical requirement connects to planned implementation and verification |
| Enhancement, defect, email request, routing/config change, production fix | $fde-control-change | Request, authority, impact, approval, evidence, monitoring, and rollback agree |

Start with $fde-run-engagement when unsure. It is the router and lifecycle owner.

## Engagement lifecycle

### Stage 1: Frame

Goal: define why the engagement exists and who can decide.

Capture:

- business problem and desired outcome;
- process boundary and non-goals;
- sponsor, process owner, performers, control owner, technical owner, and support owner;
- baseline and target measures;
- systems of record and constraints;
- available evidence and access;
- timeline, dependencies, and authority.

Do not advance on a slogan such as “automate AP” or “build a support agent.” A bounded engagement has an observable start and end, accountable owners, explicit exclusions, and a testable value hypothesis.

### Stage 2: Discover and capture

Goal: recover the operational truth needed to design safely.

Use interviews and evidence together:

- inspect documents and systems first;
- ask people for authority, lived exceptions, hidden work, preferences, and evidence you cannot access;
- index every source before relying on it;
- extract atomic claims with locators;
- distinguish stated, inferred, confirmed, approved, contradicted, stale, and not-applicable knowledge;
- record identity ambiguity rather than guessing;
- open contradictions that affect scope, control, ownership, routing, architecture, or acceptance.

A good discovery output is not a huge transcript. It is a small set of reliable decisions and a visible plan for consequential unknowns.

### Stage 3: Model the current state

Goal: describe the actual work sufficiently to redesign it.

For each step, capture:

- trigger and completion proof;
- performer and accountable owner;
- inputs, systems, credentials, and data;
- rule or judgment;
- outputs and downstream dependencies;
- normal timing and volume;
- exception, recovery, escalation, and control;
- evidence and confidence.

Look for duplicate entry, wait states, forwarding, manual reconciliation, queues, hidden spreadsheets, policy ambiguity, and “Sarah handles it” ownership.

### Stage 4: Reengineer

Goal: design a better operating model rather than attach AI to every step.

Apply the decision ladder to each step:

1. Can the outcome or step be removed?
2. Can policy, ownership, or data be simplified?
3. Is the behavior deterministic enough for a rule, API, workflow, or RPA?
4. Does interpretation require probabilistic AI?
5. Which decisions need a human checkpoint?
6. Which work remains human-only because of accountability, empathy, negotiation, physical action, or unacceptable failure impact?

The approved future state must preserve every current step or explicitly record why it is eliminated, combined, or replaced.

### Stage 5: Plan delivery

Goal: translate approved business design into small verifiable work.

Create:

- stable business, functional, nonfunctional, control, operational, and adoption requirements;
- architecture responsibilities and boundaries;
- thin vertical-slice backlog;
- deterministic, integration, evaluation, security, recovery, and UAT tests;
- requirement-to-design-to-component-to-test-to-release traceability;
- environment progression, monitoring, support, and rollback;
- required approvals and evidence.

Implementation details belong to the official product or artifact owner. The FDE plan names what must be true without inventing current product commands or schemas.

### Stage 6: Implement and verify

Goal: produce tested behavior through the appropriate implementation skill or engineering workflow.

The FDE suite keeps the business baseline, requirement IDs, risks, and evidence requirements stable. Official implementation skills own product-specific files and commands. Update traceability as components and tests become real.

Do not change status from planned to implemented, tested, released, or measured without observed evidence.

### Stage 7: Release and operate

Goal: move an approved, tested version into operation with support and recovery.

Require:

- exact release candidate and approvals;
- successful required tests and UAT;
- least-privilege access and environment readiness;
- monitoring and support owner;
- canary or staged rollout where appropriate;
- rollback or compensating action;
- release evidence and version;
- post-release measurement plan.

### Stage 8: Control change

Goal: prevent informal requests from bypassing the approved baseline.

Every material change records:

- request and source;
- requester and authority;
- exact baseline;
- affected process, requirements, controls, components, tests, runbook, and users;
- proposed patch and risk;
- approval, UAT, monitoring, and rollback;
- actual released state and evidence.

An email can authorize analysis without authorizing production.

## The durable workspace

### Engagement

- **charter.md:** outcome, scope, owners, measures, constraints.
- **status.md:** current stage, gate, blockers, recent changes, one next action.

### Knowledge

- **evidence-index.md:** source catalog and locators.
- **glossary.md:** stable business language.
- **stakeholders.md:** roles, responsibility, authority, and evidence.
- **knowledge-needs.md:** prioritized unknowns, blocked decisions, owners, and due stages.
- **contradictions.md:** competing claims, impact, resolver, and decision.

### Process

- **current-state.md:** normal flow and actual exception/recovery paths.
- **automation-allocation.md:** step-level mechanism decision and accountability.
- **future-state.md:** target flow, controls, measures, fallback, and current-to-future reconciliation.

### Delivery

- **requirements.md:** stable requirements and acceptance.
- **architecture.md:** component responsibilities, contracts, and boundaries.
- **backlog.md:** session-sized vertical slices with tests and rollback.
- **traceability.md:** chain from requirement to release evidence.
- **test-plan.md:** deterministic, integration, AI, security, recovery, and UAT coverage.
- **runbook.md:** deployment, monitoring, support, recovery, rollback, and retention.

### Governance

- **decisions.md:** approved choices and superseded baselines.
- **risks-controls.md:** risk, owner, control, evidence, and residual risk.
- **approvals.md:** exact gate/action and approved version.
- **change-log.md:** post-baseline requests through release or closure.

### Handoff

- **handoff.md:** mission, stage, confirmed knowledge, critical gaps, decisions, risks, and next action.

## Evidence statuses

Use status precisely:

| Status | Meaning |
| --- | --- |
| unknown | Required knowledge is absent |
| stated | A stakeholder or document asserts it |
| evidenced | A source supports it with a locator |
| contradicted | Reliable sources disagree |
| confirmed | Qualified owner verified it |
| approved | Authorized decision-maker accepted it as governing |
| stale | Previously useful knowledge may no longer be current |
| not-applicable | Named owner approved that it does not apply |

Do not collapse stated into approved. Do not resolve a contradiction by deleting the losing claim.

## Interview method

The interview skill works in rounds. Each question contains:

- a concrete knowledge or decision question;
- a recommendation when appropriate;
- the downstream decision or artifact it unlocks.

Useful interview lenses:

- sponsor/FDE intake;
- process owner;
- actual performer and exception handler;
- application/data SME;
- risk/security/control owner;
- operations/support owner.

The agent should discover environmental facts through authorized read-only inspection. Human time should focus on authority, lived behavior, judgment, exceptions, evidence unavailable to the agent, and adoption boundaries.

## Automation allocation

Use these dispositions:

| Disposition | Appropriate when | Typical controls |
| --- | --- | --- |
| Eliminate/simplify | Work exists because of duplicate policy, unclear ownership, or avoidable data friction | Owner approval and updated procedure |
| Deterministic automation | Inputs and rules are stable and testable | Idempotency, negative tests, reconciliation |
| RPA/API workflow | Existing UI/API must be driven reliably | Credentials, retry, selectors/contracts, rollback |
| Agentic AI | Interpretation or synthesis is probabilistic and valuable | Evidence, confidence, evals, versioning, HITL |
| Human-in-the-loop | A person must verify or approve a recommendation | Clear authority, correction, audit |
| Human-only | Accountability, empathy, negotiation, physical work, or failure impact dominates | Training, procedure, escalation |

AI suitability is not “can a model produce an answer?” It is whether the answer can be evaluated, controlled, reversed, explained, monitored, and accepted at the required risk level.

## Recommended interaction pattern

At the end of every meaningful turn, ask the agent to report:

1. current lifecycle stage;
2. artifacts changed;
3. confirmed knowledge added;
4. contradictions and high-risk gaps;
5. decisions and approvals required;
6. next skill and smallest verifiable action.

Then review the files, not only the prose response.

## Collaboration with product skills

The FDE suite should route product truth to the official implementation owner. For UiPath, use the relevant official discovery, domain, solution, component, security, observability, artifact, test, release-readiness, and handoff skill.

The division of responsibility is:

- FDE skills own business evidence, process design, delivery intent, gates, and traceability.
- Product skills own current product commands, schemas, file contracts, builds, deployments, and platform evidence.

This keeps engagement knowledge stable while product tooling evolves.

## Common mistakes

### Uploading everything and asking for a summary

A summary can hide missing evidence and contradictions. Index sources, capture atomic claims, and ask what decision each claim supports.

### Designing after one process-owner interview

Process owners know policy and outcomes; performers know actual retries, workarounds, and failure handling. Interview both, plus control and technical owners.

### Treating every step as AI

Start with elimination and simplification. Use deterministic automation for deterministic rules. Reserve AI for interpretation that has an evaluation and control story.

### Replacing the system of record

Most enterprises have already invested deeply in ERP, CRM, HRIS, or ticketing systems. Build above the system of record unless migration is explicitly approved.

### Claiming implementation from a plan

A requirement or architecture artifact is not running software. Preserve status boundaries.

### Letting a client message alter production directly

Register it as a change. Verify authority and impact. Require a patch, tests, approval, monitoring, and rollback.

## Prompt library

### Engagement framing

~~~text
$fde-run-engagement Start a new engagement. Ask me the smallest set of questions needed to establish outcome, boundary, owners, evidence, baseline, constraints, and discovery authority. Create durable state after I answer.
~~~

### Performer interview

~~~text
$fde-interview-engagement Interview the person who actually handles exceptions. Focus on triggers, hidden work, handoffs, retries, escalation, controls, volume, timing, and what they would reject in a future design.
~~~

### Knowledge ingestion

~~~text
$fde-capture-knowledge Ingest these materials. Create stable source IDs and locators, extract atomic claims, resolve identities cautiously, open contradictions, and identify downstream artifacts that new evidence invalidates.
~~~

### Process redesign

~~~text
$fde-reengineer-process Build the current state from evidence, including every material exception. Challenge each step in order: eliminate, simplify, deterministic automation, RPA/API, AI, HITL, or human-only. Preserve controls and adoption.
~~~

### Delivery planning

~~~text
$fde-plan-delivery Convert the approved future state into stable requirements, component responsibilities, vertical slices, tests, traceability, rollout, operations, and rollback. Show the critical path and evidence gaps.
~~~

### Change control

~~~text
$fde-control-change Register this request, verify authority, compare it with the approved baseline, find every affected artifact, define an exact reversible patch and regression plan, and stop at the current approval boundary.
~~~

## Expected results and limitations

### Expected results

- higher-quality project context;
- fewer unowned unknowns;
- visible contradictions and authority;
- safer automation allocation;
- smaller delivery slices;
- clearer test and release evidence;
- reliable handoff and resumption;
- controlled post-release change.

### Limitations

- The agent cannot know what was never supplied, observed, or authorized.
- A well-structured false claim is still false; evidence and human review matter.
- The suite does not run production systems by itself.
- Generic templates must be adapted to actual policy, regulation, architecture, and product contracts.
- A target is not realized value until measured after release.
- Customer confidentiality obligations still govern the workspace.

## Next step

Install the suite, open one bounded engagement, invoke $fde-run-engagement, and let the interview skill establish a reliable frontier before anyone proposes an implementation.
