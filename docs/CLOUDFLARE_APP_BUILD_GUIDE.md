# FDE Agent: Step-by-Step Build and Cloudflare Deployment Guide

| Guide property | Value |
| --- | --- |
| Status | Implementation guide, not an implementation |
| Last platform verification | 2026-08-12 |
| Initial vertical slice | Synthetic accounts-payable invoice exception resolution |
| Primary runtime | Cloudflare Workers + Cloudflare Agents SDK (TypeScript) |
| Enterprise execution adapter | UiPath Automation Cloud / Orchestrator |

## Guide map

This is the optional application path. If you only want to use the FDE method inside Codex, return to the [README install command](../README.md#install-all-six-skills); no Cloudflare application is required.

| Goal | Go to |
| --- | --- |
| Understand the platform shape | [Target architecture](#2-target-architecture) |
| Review the non-bypassable controls | [Trust invariants](#3-trust-invariants) |
| See the proposed code layout | [Repository structure](#4-recommended-repository-structure) |
| Model evidence, claims, people, process, and traceability | [Domain model](#5-domain-model) |
| Understand lifecycle approvals | [Lifecycle and gates](#6-lifecycle-and-gates) |
| Start building | [Step-by-step implementation](#8-step-by-step-implementation) |
| Configure Cloudflare resources | [Cloudflare configuration](#10-cloudflare-configuration) |
| Implement identity and authorization | [Authentication and authorization](#11-authentication-and-authorization) |
| Deploy and roll back | [Deployment sequence](#12-deployment-sequence) |
| Add GitHub delivery automation | [CI/CD](#13-cicd) |
| Prove release readiness | [Evaluation and release gates](#9-evaluation-and-release-gates) |
| Verify platform assumptions | [Primary source index](#19-primary-source-index) |

Recommended reading order for a first implementation: Sections 1-3, Step 0 and Step 1, Steps 2-16 in order, then Sections 9-17 before any production release.

## 1. Read this first

This guide describes how to build a Forward Deployed Engineer (FDE) agent that helps a delivery team:

1. ingest and reconcile customer evidence;
2. discover the real current-state process, including exceptions;
3. redesign work across deterministic automation, RPA, agentic AI, human-in-the-loop, and human-only steps;
4. produce traceable solution and test artifacts;
5. perform only approved, governed external actions; and
6. manage post-release changes without a prompt-to-production path.

The central runtime should be **Cloudflare-native TypeScript**, not a Python LangGraph service placed awkwardly behind Cloudflare. Cloudflare's Agents SDK already supplies durable agent identity, per-instance SQLite storage, real-time connections, scheduling, recovery, and workflow integration. Each engagement can therefore be one isolated Agent/Durable Object instance. See [Cloudflare Agents](https://developers.cloudflare.com/agents/) and the [Agents API](https://developers.cloudflare.com/agents/runtime/agents-api/).

> **Architecture change:** the Cloudflare-deployment requirement supersedes the earlier assumption that a UiPath Python/LangGraph agent would be the central orchestrator. Keeping LangGraph central would produce a hybrid deployment with a second Python runtime. This guide instead makes Cloudflare the control plane and keeps UiPath behind governed adapters.

UiPath remains the execution system for RPA, Maestro, coded agents, Action Center, and Orchestrator processes. The Cloudflare agent calls UiPath through narrow, approval-controlled adapters. If a specialized Python/LangGraph UiPath coded agent is useful later, deploy it to UiPath and invoke it as an Orchestrator process; do not make it the Cloudflare control plane.

### Non-goals for the first release

- No autonomous client email, Slack, or Teams communication.
- No production deployment without named human approval.
- No live ERP, mailbox, or financial-system connection in the synthetic MVP.
- No model fine-tuning or reinforcement learning.
- No arbitrary model-generated code execution.
- No shared cross-customer memory.
- No polished multi-tenant SaaS administration layer.
- No claim of business ROI before a real baseline and post-release measurement exist.

## 2. Target architecture

```text
FDE / approver browser
        |
        v
Cloudflare Access (SSO, deny by default)
        |
        v
Cloudflare Worker + minimal web UI
        |
        +--> D1: engagement directory and authorization index
        |
        +--> FdeEngagementAgent Durable Object (one opaque ID per engagement)
        |       |
        |       +--> embedded SQLite: graph, lifecycle, versions, audit
        |       +--> Agent skills: phase-specific delivery playbooks
        |       +--> Cloudflare Workflows: durable approvals and writes
        |
        +--> R2: immutable source evidence and generated artifacts
        +--> AI Search: evidence retrieval with engagement filters
        +--> Queues: asynchronous ingestion, extraction, and indexing
        +--> AI Gateway / model provider: governed inference
        |
        +--> UiPath adapter (OAuth, least privilege)
                +--> read Orchestrator state
                +--> start an approved process/job
                +--> optionally mirror approvals to Action Center
```

### Cloudflare component responsibilities

| Component | Responsibility | Must not become |
|---|---|---|
| Worker | HTTP API, routing, authentication, static UI | The durable engagement database |
| Agent/Durable Object | One engagement's authoritative state and coordination | A cross-customer singleton |
| Durable Object SQLite | Typed graph, versions, gates, audit events | Raw-document blob storage |
| D1 | Engagement directory, user-role mappings, deployment metadata | The detailed customer knowledge graph |
| R2 | Immutable evidence and versioned generated artifacts | A public bucket |
| AI Search | Retrieval over approved/indexable evidence | The source of truth |
| Queues | Background ingestion and extraction | A place to send large document bodies |
| Workflows | Long-running gates, retries, and consequential operations | An unreviewed model tool |
| AI Gateway | Provider routing, observability, optional DLP | An unquestioned compliance boundary |
| Cloudflare Access | Workforce SSO and coarse application access | The only authorization check in the app |
| UiPath | Governed automation execution and human work | The FDE agent's engagement memory |

Cloudflare documents SQLite-backed Durable Objects as the recommended storage backend for new Agent classes. New projects should use the declarative `exports` configuration rather than legacy Durable Object migrations. See [Agents configuration](https://developers.cloudflare.com/agents/runtime/operations/configuration/) and [Durable Objects](https://developers.cloudflare.com/durable-objects/).

## 3. Trust invariants

Implement these rules in deterministic code. Do not rely on a system prompt to enforce them.

1. **The model never writes authoritative records directly.** It produces a `ProposedPatch`.
2. **Every material claim has provenance.** A claim points to one or more immutable evidence spans.
3. **Contradictions are records, not prose.** They remain open until a named person resolves them.
4. **Approved baselines are immutable.** Changes create new versions linked by `supersedes`.
5. **Stage transitions are policy decisions.** The model may recommend; deterministic gate code decides.
6. **Write tools are never ordinary chat tools.** They execute only inside an approved Workflow.
7. **Approval freezes the operation.** Approvers see the exact action, arguments, impact, and hash that will execute.
8. **Retries reconcile external state first.** A timeout never means "run it again and hope."
9. **Customer and engagement IDs are mandatory filters.** Missing scope is an error, never "all records."
10. **Retrieved documents are untrusted data.** Instructions inside evidence cannot change agent policy or tool authority.
11. **Human overrides are allowed but audited.** Store actor, rationale, date, and affected risks.
12. **Secrets never enter prompts, artifacts, logs, or source control.**

## 4. Recommended repository structure

Create this structure gradually; do not generate empty architecture for its own sake.

```text
fde-agent/
|-- src/
|   |-- server.ts                    # Worker entry and authenticated routing
|   |-- agent/
|   |   |-- fde-engagement-agent.ts
|   |   |-- command-router.ts
|   |   `-- system-policy.ts
|   |-- domain/
|   |   |-- schemas.ts               # Zod schemas and TypeScript types
|   |   |-- lifecycle.ts
|   |   |-- graph.ts
|   |   |-- provenance.ts
|   |   `-- policies.ts
|   |-- storage/
|   |   |-- engagement-store.ts      # interface
|   |   |-- durable-object-store.ts
|   |   |-- evidence-store.ts        # R2 interface
|   |   |-- search-store.ts          # AI Search interface
|   |   `-- registry-store.ts        # D1 interface
|   |-- ingestion/
|   |   |-- upload.ts
|   |   |-- normalize.ts
|   |   |-- extract-claims.ts
|   |   `-- queue-consumer.ts
|   |-- workflows/
|   |   |-- approval-workflow.ts
|   |   |-- external-operation.ts
|   |   `-- change-request.ts
|   |-- adapters/
|   |   |-- model.ts
|   |   |-- uipath.ts
|   |   `-- identity.ts
|   |-- artifacts/
|   |   |-- current-state.ts
|   |   |-- future-state.ts
|   |   |-- traceability.ts
|   |   `-- render-markdown.ts
|   `-- skills/
|       |-- engagement-intake/SKILL.md
|       |-- evidence-analysis/SKILL.md
|       |-- discovery/SKILL.md
|       |-- process-modeling/SKILL.md
|       |-- process-redesign/SKILL.md
|       |-- uipath-solution-design/SKILL.md
|       |-- test-design/SKILL.md
|       |-- release-readiness/SKILL.md
|       `-- change-management/SKILL.md
|-- public/                         # minimal chat and structured review UI
|-- migrations/                     # D1 registry migrations
|-- test/
|   |-- unit/
|   |-- integration/
|   |-- security/
|   `-- fixtures/ap-exceptions/
|-- evaluations/
|   |-- cases/
|   |-- expected/
|   |-- evaluators/
|   `-- thresholds.json
|-- docs/
|   |-- adr/
|   |-- schemas/
|   |-- threat-model.md
|   `-- runbook.md
|-- wrangler.jsonc
|-- vitest.config.mts
|-- package.json
`-- tsconfig.json
```

Cloudflare Agent Skills can load task-specific instructions without placing the whole library in every prompt, but the feature and especially skill script execution are documented as experimental. Put stable delivery knowledge in Markdown skills, isolate the registry behind your own interface, and keep security/lifecycle enforcement in normal TypeScript. See [Agent Skills](https://developers.cloudflare.com/agents/runtime/execution/agent-skills/).

## 5. Domain model

### 5.1 Node types

Start with these graph node types:

- `person`
- `role`
- `team`
- `process`
- `process_step`
- `system`
- `data_object`
- `business_rule`
- `exception`
- `control`
- `metric`
- `requirement`
- `risk`
- `decision`
- `artifact`
- `test`
- `change_request`

### 5.2 Edge types

Start with these directed relationships:

- `owns`
- `performs`
- `depends_on`
- `precedes`
- `uses`
- `reads`
- `writes`
- `produces`
- `triggers`
- `exception_to`
- `governed_by`
- `mitigates`
- `satisfies`
- `implemented_by`
- `verified_by`
- `approved_by`
- `conflicts_with`
- `supersedes`

### 5.3 Required record families

Use normalized SQLite tables rather than one giant JSON document:

| Table | Purpose |
|---|---|
| `engagement` | Scope, status, owners, schema version, success measures |
| `evidence_source` | Immutable R2 object reference, checksum, origin, classification |
| `evidence_span` | Page/slide/row/time range and normalized text reference |
| `claim` | Atomic assertion, status, confidence category, effective dates |
| `claim_evidence` | Many-to-many provenance links |
| `entity` | Typed graph node with stable ID and lifecycle status |
| `entity_alias` | Names and identifiers used for identity resolution |
| `edge` | Typed directed relationship |
| `contradiction` | Conflicting claims, impact, owner, resolution |
| `requirement` | Functional/nonfunctional requirement and acceptance criteria |
| `decision` | Decision, alternatives, rationale, owner, effective date |
| `approval` | Gate/action approval and frozen payload hash |
| `artifact` | Versioned generated deliverable stored in R2 |
| `trace_link` | Requirement-to-design-to-implementation-to-test evidence |
| `change_request` | Proposed post-baseline change and impact |
| `tool_operation` | Idempotency key, frozen arguments, external result/status |
| `audit_event` | Append-only actor/action/object/version event |

Every mutable business table should include at least:

```text
id, engagement_id, version, status, created_at, created_by,
updated_at, schema_version, supersedes_id
```

Material assertions also require `source_kind`, provenance links, and effective/observed dates. Avoid using a model-generated floating-point confidence score as a gate. Use categories such as `stated`, `observed`, `inferred`, `confirmed`, and `approved`.

### 5.4 Proposed patch contract

Require the model to produce a schema-validated object like:

```json
{
  "engagementId": "opaque-uuid",
  "baseVersion": 17,
  "intent": "record_discovery_findings",
  "operations": [
    {
      "op": "add_claim",
      "value": { "text": "...", "status": "stated" },
      "evidenceSpanIds": ["span-123"]
    }
  ],
  "preconditions": ["engagement.stage == discovery"],
  "materiality": "medium",
  "risks": [],
  "rationale": "..."
}
```

The commit path is:

```text
model proposal -> Zod validation -> authorization -> lifecycle policy ->
provenance checks -> graph constraint checks -> approval if required ->
single SQLite transaction -> audit event -> artifact invalidation
```

## 6. Lifecycle and gates

Represent the lifecycle as an explicit state machine:

```text
framing
  -> discovery
  -> current_state_review
  -> current_state_approved
  -> future_state_design
  -> future_state_approved
  -> solution_design
  -> build
  -> verification
  -> uat
  -> release_review
  -> released
  -> operating
  -> change_review (loop back through affected stages)
```

Each transition has a deterministic gate. Example gate requirements:

| Transition | Minimum evidence |
|---|---|
| framing -> discovery | charter, process owner, objective, boundary, baseline plan |
| discovery -> current-state review | stakeholder map, evidence inventory, open gaps, exception inventory |
| current-state review -> approved | process-owner approval, no unresolved critical contradiction |
| future-state design -> approved | allocation matrix, risk/control analysis, target metrics |
| solution design -> build | architecture approval, NFRs, security decision, traceability initialized |
| verification -> UAT | automated tests pass, critical requirements traced |
| UAT -> release review | business acceptance and unresolved-defect decision |
| release review -> released | named release approval, rollback verified, runbook present |

A stage may be marked `not_applicable` only with a named approver and justification. It is never silently skipped.

## 7. Command vocabulary

Support conversational language, but route it to explicit intents:

```text
start engagement
ingest evidence
show evidence
show gaps
show contradictions
prepare interview
record findings
validate current state
classify automation
propose future state
design UiPath solution
generate engagement package
show traceability
run evaluations
prepare approval
show pending approvals
request change
analyze change impact
show status
create handoff
```

If the intent is ambiguous or would change lifecycle stage, ask for confirmation. Query commands may run directly. Mutating commands produce patches. Consequential tools produce approval requests.

## 8. Step-by-step implementation

### Step 0 - Write architecture decisions before code

Create these ADRs:

1. `ADR-001-cloudflare-native-runtime.md`
2. `ADR-002-agent-instance-per-engagement.md`
3. `ADR-003-evidence-backed-typed-graph.md`
4. `ADR-004-model-proposes-code-commits.md`
5. `ADR-005-workflow-gated-external-writes.md`
6. `ADR-006-uipath-as-execution-adapter.md`

For each ADR record context, decision, rejected options, consequences, and reversal conditions.

**Exit criterion:** another engineer can explain where state lives, who may mutate it, and why Cloudflare rather than LangGraph is the central runtime.

### Step 1 - Scaffold the Cloudflare Agents project

Prerequisites: a supported Node.js LTS release, npm, a Cloudflare account, and permission to create the resources named later in this guide. From the parent directory, run:

```powershell
npm create cloudflare@latest fde-agent -- --template cloudflare/agents-starter
Set-Location fde-agent
npm install
npm install zod
npm install --save-dev vitest@^4.1.0 @cloudflare/vitest-pool-workers tsx
```

The official starter includes streaming chat, server/client tools, approvals, and scheduling. Cloudflare's current starter and configuration are documented in [Cloudflare Agents](https://developers.cloudflare.com/agents/) and [Agents configuration](https://developers.cloudflare.com/agents/runtime/operations/configuration/).

Add scripts equivalent to:

```json
{
  "scripts": {
    "dev": "vite dev",
    "typecheck": "tsc --noEmit",
    "test": "vitest run",
    "test:watch": "vitest",
    "eval": "tsx evaluations/run.ts",
    "deploy:dry": "wrangler deploy --dry-run"
  }
}
```

Pin all direct dependencies. Commit the lockfile. Use a supported Node LTS line consistently in local development and CI.

**Tests:** run the starter test and local server.

**Exit criterion:** `npm run typecheck`, `npm test`, and `npm run dev` succeed before FDE logic is added.

### Step 2 - Create the synthetic AP golden fixture first

Before implementing agent behavior, create authorized synthetic evidence:

- 10 invoices with normal and exceptional cases;
- matching and mismatching purchase orders;
- goods-receipt records;
- AP policy document;
- approval matrix;
- ERP field dictionary;
- meeting transcript with two conflicting descriptions;
- email that uses an ambiguous employee alias;
- undocumented escalation to a second process owner;
- one malicious document containing prompt-injection instructions;
- current KPI baseline and target;
- expected graph, contradictions, exceptions, requirements, future state, and tests.

Seed at least these critical exceptions:

1. invoice/PO amount mismatch;
2. duplicate invoice;
3. missing goods receipt;
4. supplier master-data discrepancy;
5. approval threshold exceeded;
6. tax discrepancy;
7. emergency/manual payment route;
8. ambiguous process ownership.

Write failing tests for the expected entities, edges, contradictions, and exceptions before extraction logic.

**Exit criterion:** the fixture has an expert-authored answer key independent of model output.

### Step 3 - Define Zod schemas and deterministic policies

Implement schemas for all record families, commands, patches, approvals, external operations, and artifacts. Disallow unknown fields for authoritative writes.

Implement pure policy functions:

- `authorize(actor, action, resource)`
- `validateTransition(from, to, evidence)`
- `validateProvenance(patch)`
- `validateGraphConstraints(patch)`
- `classifyMateriality(patch)`
- `requiresApproval(operation)`
- `validateFrozenApproval(approval, operationHash)`

Test them without a model, Cloudflare account, or UiPath tenant.

**Exit criterion:** unauthorized writes, missing provenance, invalid transitions, stale base versions, and unknown fields all fail deterministically.

### Step 4 - Build per-engagement storage in the Agent Durable Object

Create `FdeEngagementAgent` as the only owner of detailed engagement state. Address instances by an opaque UUID, not customer name or email. Cloudflare routes the same instance name back to the same durable Agent instance, and each Agent exposes embedded SQLite through `this.sql`; see the [Agents API](https://developers.cloudflare.com/agents/runtime/agents-api/).

In `onStart`, apply numbered, idempotent SQLite schema migrations. Maintain a `schema_meta` table. Use transactions for patch commits and append the `audit_event` in the same transaction.

Do not store full documents or secrets in Agent SQLite. Store R2 references and content hashes.

**Tests:** concurrent patch conflict, stale version, transaction rollback, idempotent migration, audit append, and reload after hibernation.

**Exit criterion:** restarting the local runtime preserves the engagement and cannot partially commit a patch.

### Step 5 - Add D1 only for the directory and authorization index

Create a D1 database:

```powershell
npx wrangler d1 create fde-registry-dev
npx wrangler d1 migrations create fde-registry-dev init-registry
npx wrangler d1 migrations apply fde-registry-dev --local
```

Use D1 tables such as:

- `engagement_registry(engagement_id, agent_instance_id, status, created_at)`
- `principal_role(principal_id, engagement_id, role, valid_from, valid_to)`
- `deployment_config(key, nonsecret_value, version)`

Use foreign keys and indexes for authorization lookup. Cloudflare documents D1 migrations as versioned SQL files and supports foreign keys through SQLite semantics; see [D1 migrations](https://developers.cloudflare.com/d1/reference/migrations/) and [querying D1](https://developers.cloudflare.com/d1/best-practices/query-d1/).

**Exit criterion:** D1 can list engagements a principal may access without containing the engagement's evidence graph.

### Step 6 - Add immutable evidence storage in R2

Create a private bucket:

```powershell
npx wrangler r2 bucket create fde-evidence-dev
```

Use content-addressed keys:

```text
engagements/<engagement-id>/evidence/<sha256>/<sanitized-filename>
engagements/<engagement-id>/normalized/<source-id>/<version>.json
engagements/<engagement-id>/artifacts/<artifact-id>/<version>/<filename>
```

On upload:

1. authenticate and authorize the user;
2. stream the file while computing SHA-256;
3. reject disallowed type/size;
4. malware-scan through an approved service if required;
5. store with classification and engagement metadata;
6. create the `evidence_source` record;
7. enqueue only an R2 pointer and IDs, not the document bytes.

Never overwrite evidence objects. Generated artifacts are versioned. R2 bindings support checksums, conditional operations, and custom metadata; see the [R2 Workers API](https://developers.cloudflare.com/r2/api/workers/workers-api-reference/). Configure lifecycle rules only after retention requirements are approved; see [R2 object lifecycles](https://developers.cloudflare.com/r2/buckets/object-lifecycles/).

**Exit criterion:** duplicate uploads are detected by hash and original evidence remains immutable.

### Step 7 - Build asynchronous ingestion with Queues

Create a queue and dead-letter queue:

```powershell
npx wrangler queues create fde-ingestion-dev
npx wrangler queues create fde-ingestion-dlq-dev
```

The consumer should:

1. load the R2 object by immutable key;
2. normalize supported formats;
3. create stable page/slide/row/time-based spans;
4. extract candidate claims and entities using a schema-bound model call;
5. store a proposed patch, not committed truth;
6. run deterministic validation;
7. commit only allowed low-risk records or send material changes to review;
8. mark indexing status and emit audit events.

Make every stage idempotent by `source_id + content_hash + extractor_version`. Configure bounded retries and a DLQ. Without a DLQ, messages that exceed the retry limit can be deleted; see [Cloudflare Queues retries](https://developers.cloudflare.com/queues/configuration/batching-retries/) and [dead-letter queues](https://developers.cloudflare.com/queues/configuration/dead-letter-queues/).

**Exit criterion:** poison evidence reaches the DLQ, retrying a completed message creates no duplicate records, and queue messages contain no raw document body.

### Step 8 - Add AI Search as retrieval, not truth

Create an AI Search instance over the R2 bucket:

```powershell
npx wrangler ai-search create fde-evidence-dev --type r2 --source fde-evidence-dev
npx wrangler ai-search stats fde-evidence-dev
```

Bind the AI Search namespace in the Worker. AI Search can index R2 content and supports metadata filtering. See [AI Search CLI](https://developers.cloudflare.com/ai-search/get-started/wrangler/), [R2 as a data source](https://developers.cloudflare.com/ai-search/configuration/data-source/r2/), and [retrieval filtering](https://developers.cloudflare.com/ai-search/configuration/retrieval/filtering/).

AI Search is currently labeled Beta in Cloudflare's documentation. Keep it behind the `SearchStore` interface, verify plan/region/retention suitability with the customer, and retain the ability to substitute Vectorize or another approved search service without changing the engagement domain model.

Every query must filter by at least customer/deployment boundary and `engagement_id`. Retrieval results must return source IDs and span metadata. The agent may answer "insufficient evidence"; it may not fill gaps from general model knowledge while presenting them as customer facts.

Provide a fake `SearchStore` in unit tests because remote AI Search does not run in the local Worker simulation; the official Workers binding uses `remote: true` for local proxying when integration testing. See [AI Search Workers binding](https://developers.cloudflare.com/ai-search/get-started/workers/).

**Exit criterion:** a test querying engagement A can never receive a result tagged only for engagement B.

### Step 9 - Implement the engagement graph and discovery loop

Implement these deterministic graph operations:

- create/update entity through a proposed patch;
- add typed edge;
- resolve or split alias;
- find unowned steps;
- find dependency cycles;
- find steps without inputs/outputs;
- find requirements without tests;
- find exceptions without owners/controls;
- compare stated versus observed claims;
- calculate impacted nodes for a change request.

The discovery planner ranks unanswered questions by:

```text
priority = downstream_decisions_blocked * impact * risk * uncertainty
```

Ask a small coherent batch and state why each answer matters. Never ask the user for a fact already present in evidence or obtainable through an authorized read tool.

**Exit criterion:** the synthetic fixture produces the expected missing owner, identity ambiguity, contradiction, and critical exception questions.

### Step 10 - Add specialist skills without delegating authority

Create one concise `SKILL.md` for each phase. A skill should contain:

- when it applies;
- required inputs;
- ordered procedure;
- expected structured output;
- quality checks;
- escalation conditions;
- linked templates or references.

Do not include security policy, authorization logic, or lifecycle transition rules only in skills. Those remain always-on deterministic code. Do not enable experimental skill script execution in the MVP.

**Exit criterion:** loading one specialist skill changes task procedure but cannot expand tool permissions or bypass a gate.

### Step 11 - Implement current-state and future-state design

For every process step capture:

- actor and accountable owner;
- trigger;
- required inputs and source systems;
- action and decision rule;
- outputs and downstream consumers;
- normal path;
- exceptions and escalation;
- volume, cycle time, rework, failure rate;
- controls and evidence;
- pain points and current cost/risk.

Classify the future disposition of each step as:

1. eliminate/simplify;
2. deterministic automation;
3. UiPath RPA or API workflow;
4. agentic AI;
5. human-in-the-loop;
6. human-only.

The classification must cite variability, judgment, data quality, reversibility, explainability, compliance impact, failure severity, volume, and measurable value.

**Exit criterion:** every current step has a future disposition or an explicit unresolved decision; no step disappears silently.

### Step 12 - Generate the engagement package

Generate both human-readable Markdown and validated machine-readable JSON for:

- engagement charter and success measures;
- evidence inventory;
- stakeholder map and RACI;
- domain glossary;
- current-state process and exception map;
- contradictions and open questions;
- requirements and NFRs;
- automation-allocation matrix;
- future-state process;
- UiPath solution architecture;
- risk/control register;
- traceability matrix;
- implementation backlog;
- test/UAT plan;
- ROI baseline and measurement plan;
- release runbook and decision log.

Each artifact includes `artifact_id`, version, engagement baseline version, prompt/policy version, evidence IDs, generator version, and approval status. Store rendered artifacts in R2 and metadata in SQLite.

**Exit criterion:** changing a requirement invalidates or flags every dependent design, implementation, test, and artifact through `trace_link` records.

### Step 13 - Implement durable human approval

Use a Cloudflare Workflow for every material stage transition and consequential tool operation. `waitForApproval()` can durably pause a Workflow without keeping the Agent running; see [human-in-the-loop patterns](https://developers.cloudflare.com/agents/concepts/agentic-patterns/human-in-the-loop/) and [Agents with Workflows](https://developers.cloudflare.com/agents/concepts/workflows/).

The approval request must display:

- requester and approver role;
- exact frozen operation and arguments;
- payload hash and base version;
- cited evidence;
- requirements and components affected;
- security/financial/business impact;
- validation and test results;
- rollback plan;
- expiry and escalation behavior.

After approval, the Workflow revalidates the actor, hash, base version, and external preconditions before executing. Use `step.do()` for the external write and a stable idempotency key. Record rejection, timeout, and cancellation.

For high-risk operations, require separation of duties: requester cannot be sole approver.

**Exit criterion:** modifying one argument after approval invalidates the approval and prevents execution.

### Step 14 - Build the UiPath adapter

Start with a fake adapter, then read-only sandbox calls, then approved writes.

Define an interface similar to:

```text
listProcesses(folder): ProcessSummary[]
getJob(jobId): JobStatus
getAction(actionId): ActionStatus
proposeStartProcess(process, input): ExternalOperation
executeApprovedOperation(frozenOperation): ExternalResult
```

#### UiPath authentication

For a server-to-server integration, register a confidential external application in the customer's UiPath organization, grant only required application scopes, and assign the app only to the intended tenant/folder and role. UiPath distinguishes user scopes from application scopes and recommends least privilege. See [managing external OAuth applications](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/managing-external-applications) and [fine-grained confidential-app access](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/configuring-access-for-external-apps).

Use user-scope authorization when the action must occur in a user context or when a UiPath Integration Service capability does not support client credentials. UiPath documents the scope and folder-routing behavior, including `OR.Default`, `OR.Execution`, `OR.Jobs`, and the folder-key requirements, in [authenticating an external application](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/authenticating-with-an-external-application).

Store credentials only as Cloudflare secrets:

```powershell
npx wrangler secret put UIPATH_CLIENT_ID --env staging
npx wrangler secret put UIPATH_CLIENT_SECRET --env staging
npx wrangler secret put UIPATH_BASE_URL --env staging
npx wrangler secret put UIPATH_FOLDER_KEY --env staging
```

Never expose a raw "start any process" model tool. The model proposes a named, allowlisted process invocation; a Workflow approves and executes the frozen call. If a request times out, query Orchestrator/job state before retrying. UiPath processes can be started through supported Orchestrator APIs, and a deployed coded agent also registers as an Orchestrator process; see [managing jobs](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-jobs) and [UiPath coded agents](https://uipath.github.io/uipath-python/core/agents/).

If the customer requires Action Center as the approval interface, create or retrieve an external task and resume the Cloudflare Workflow from the completed task event. Choose one authoritative approval record and link the mirror; do not create two independent approvals. See [UiPath external tasks](https://docs.uipath.com/action-center/automation-cloud/latest/user-guide/create-external-task).

**Exit criterion:** the fake adapter passes all lifecycle tests; sandbox reads are scope-limited; a write cannot run without a matching, unexpired approval.

### Step 15 - Build the minimum operator UI

Keep the UI small but structured. Include:

1. chat/command surface;
2. lifecycle stage and blocked gates;
3. evidence browser with citations;
4. graph/entity view;
5. contradictions and open questions;
6. artifact versions and diffs;
7. pending approvals;
8. evaluation results;
9. change-impact view.

Use same-origin HTTP-only authentication cookies where possible. Cloudflare warns that cross-origin WebSocket connections cannot send arbitrary authorization headers; if cross-origin is unavoidable, use a short-lived scoped signed token, never a raw secret. See [Agents cross-domain authentication](https://developers.cloudflare.com/agents/runtime/operations/cross-domain-authentication/).

**Exit criterion:** an auditor can understand why a recommendation exists without reading raw chat history.

### Step 16 - Add model routing and privacy controls

Put model access behind a `ModelAdapter`. Start with one qualified model and one deterministic fallback behavior. Cloudflare Agents can use Workers AI or external providers through the AI SDK, and AI Gateway can route providers; see [using AI models](https://developers.cloudflare.com/agents/runtime/operations/using-ai-models/).

Version:

- model/provider;
- system policy;
- skill version;
- extraction prompt;
- output schema;
- evaluator configuration.

Review AI Gateway logging before using customer data. Gateway logs may include prompts and responses by default. Disable or minimize content logging when policy requires it. If available for the customer's plan, configure DLP for both prompt and response inspection, understanding that response DLP can buffer streaming output. See [AI Gateway logging](https://developers.cloudflare.com/ai-gateway/observability/logging/) and [AI Gateway DLP](https://developers.cloudflare.com/ai-gateway/features/dlp/).

**Exit criterion:** switching model versions runs the full evaluation suite and cannot silently change production behavior.

## 9. Evaluation and release gates

### 9.1 Test layers

Use Cloudflare's Workers Vitest pool for Agent and Durable Object integration tests; see [testing Cloudflare Agents](https://developers.cloudflare.com/agents/getting-started/testing-your-agent/).

Implement:

1. schema and policy unit tests;
2. lifecycle transition tests;
3. graph constraint tests;
4. storage and transactional tests;
5. golden AP extraction and reasoning cases;
6. contradictory/incomplete evidence cases;
7. identity ambiguity cases;
8. prompt-injection cases;
9. cross-engagement isolation cases;
10. approval tampering and replay cases;
11. queue retry/DLQ cases;
12. UiPath timeout/reconciliation cases;
13. end-to-end lifecycle tests;
14. expert human review.

LLM judges may assist with semantic comparison, but they cannot be the only release authority. Prefer deterministic checks and expert-authored expected records.

### 9.2 Initial blocking thresholds

- 0 cross-engagement leaks.
- 0 unauthorized consequential actions.
- 100% enforcement of mandatory approvals.
- 100% schema-valid committed records.
- 100% source linkage for material factual claims.
- 100% detection of seeded high-impact contradictions.
- At least 95% recall for seeded critical exceptions.
- At least 95% requirement-to-design-to-test traceability.
- 0 unresolved critical security findings.
- Successful recovery for every tested interrupted write.

### 9.3 Human benchmark

An experienced FDE should independently review or build the same AP engagement package. Compare:

- critical exceptions found;
- unsupported claims;
- completeness and usefulness;
- preparation time;
- artifact maintenance time;
- rework required;
- safety and traceability.

The pilot target is at least 30% less FDE preparation/maintenance time with no reduction in expert-rated quality and no critical safety violation.

## 10. Cloudflare configuration

Use a `wrangler.jsonc` skeleton like the following and replace every placeholder. Keep development, staging, and production resources separate. Durable Object bindings and other non-inherited configuration must be repeated for each Wrangler environment; see [Durable Object environments](https://developers.cloudflare.com/durable-objects/reference/environments/).

```jsonc
{
  "$schema": "./node_modules/wrangler/config-schema.json",
  "name": "fde-agent",
  "main": "src/server.ts",
  "compatibility_date": "2026-08-12",
  "compatibility_flags": ["nodejs_compat"],

  "assets": {
    "directory": "public",
    "binding": "ASSETS"
  },

  "durable_objects": {
    "bindings": [
      { "name": "FDE_AGENT", "class_name": "FdeEngagementAgent" }
    ]
  },
  "exports": {
    "FdeEngagementAgent": {
      "type": "durable-object",
      "storage": "sqlite"
    }
  },

  "d1_databases": [
    {
      "binding": "REGISTRY_DB",
      "database_name": "fde-registry-dev",
      "database_id": "<D1_DATABASE_ID>",
      "migrations_dir": "migrations"
    }
  ],

  "r2_buckets": [
    { "binding": "EVIDENCE_BUCKET", "bucket_name": "fde-evidence-dev" }
  ],

  "ai_search_namespaces": [
    { "binding": "AI_SEARCH", "namespace": "default", "remote": true }
  ],

  "queues": {
    "producers": [
      { "binding": "INGESTION_QUEUE", "queue": "fde-ingestion-dev" }
    ],
    "consumers": [
      {
        "queue": "fde-ingestion-dev",
        "dead_letter_queue": "fde-ingestion-dlq-dev",
        "max_batch_size": 5,
        "max_batch_timeout": 10,
        "max_retries": 3
      }
    ]
  },

  "workflows": [
    {
      "name": "fde-approval-dev",
      "binding": "APPROVAL_WORKFLOW",
      "class_name": "ApprovalWorkflow"
    }
  ],

  "ai": { "binding": "AI" },

  "vars": {
    "ENVIRONMENT": "development",
    "AI_SEARCH_INSTANCE": "fde-evidence-dev"
  },

  "secrets": {
    "required": [
      "UIPATH_CLIENT_ID",
      "UIPATH_CLIENT_SECRET",
      "UIPATH_BASE_URL",
      "UIPATH_FOLDER_KEY"
    ]
  },

  "observability": {
    "enabled": true,
    "logs": { "enabled": true, "head_sampling_rate": 1 },
    "traces": { "enabled": true, "head_sampling_rate": 1 }
  }
}
```

Generate binding types after any configuration change:

```powershell
npx wrangler types
```

Cloudflare recommends `nodejs_compat` for Agents and supports declarative SQLite Agent exports, R2/D1/AI bindings, required secrets, and observability in Wrangler configuration; see [Wrangler configuration](https://developers.cloudflare.com/workers/wrangler/configuration/) and [Agents configuration](https://developers.cloudflare.com/agents/runtime/operations/configuration/).

Do not use 100% log/trace sampling indefinitely in a high-volume production system. Start high in a synthetic pilot, redact business content, then set a reviewed sampling/retention policy. Workers tracing automatically covers fetch, binding, and handler operations when enabled; see [Workers traces](https://developers.cloudflare.com/workers/observability/traces/).

## 11. Authentication and authorization

### 11.1 Protect the application with Cloudflare Access

1. Put the Worker on a customer-specific custom domain.
2. In Cloudflare Zero Trust, create an Access application for that hostname.
3. Configure the customer's identity provider.
4. Set a deny-by-default policy.
5. Allow only approved delivery and customer groups.
6. Require MFA or device posture if the customer requires it.
7. Validate the `Cf-Access-Jwt-Assertion` signature, issuer, audience, and expiry in the Worker.
8. Map the verified identity to application roles in D1.

Cloudflare documents the Access JWT header and signing-key validation in [Validate JWTs](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/). Access authentication does not replace per-engagement authorization.

### 11.2 Initial roles

- `fde_contributor`
- `delivery_approver`
- `customer_process_approver`
- `security_approver`
- `release_approver`
- `auditor`
- `platform_admin`

Use explicit permission mappings. Editing permission never implies approval permission.

## 12. Deployment sequence

### 12.1 Local development

```powershell
npm ci
npx wrangler types
npm run typecheck
npm test
npm run eval
npm run dev
```

Local Durable Object state is persisted under `.wrangler/state`; Cloudflare documents how to inspect or clear it in [Agents configuration](https://developers.cloudflare.com/agents/runtime/operations/configuration/). Do not point routine local tests at production R2, D1, AI Search, or UiPath.

### 12.2 Create isolated staging resources

Use distinct names, for example:

```powershell
npx wrangler d1 create fde-registry-staging
npx wrangler r2 bucket create fde-evidence-staging
npx wrangler queues create fde-ingestion-staging
npx wrangler queues create fde-ingestion-dlq-staging
npx wrangler ai-search create fde-evidence-staging --type r2 --source fde-evidence-staging
```

Copy the generated resource IDs into the staging environment configuration. Apply D1 migrations explicitly:

```powershell
npx wrangler d1 migrations apply fde-registry-staging --remote
```

Configure staging secrets one at a time with `wrangler secret put`. Never place secret values in `wrangler.jsonc` or GitHub variables visible to pull requests.

### 12.3 Dry run and staging deploy

```powershell
npx wrangler deploy --dry-run --env staging
npx wrangler deploy --env staging
npx wrangler tail --env staging
```

Run smoke tests using only synthetic data. Verify Access, WebSocket/chat reconnect, evidence ingestion, queue completion, approval wait/resume, audit records, and the fake or sandbox UiPath adapter.

### 12.4 Production resources

Create a separate customer-dedicated production Worker and separate D1, R2, AI Search, Queues, Workflows, secrets, domain, and Access policy. Do not use a shared provider-wide evidence bucket.

Before deployment:

1. approve data residency and retention;
2. approve AI provider/logging/DLP settings;
3. validate least-privilege UiPath scopes and folder assignment;
4. export/backup required state;
5. rehearse rollback;
6. pass all blocking evaluations;
7. obtain named release approval.

Upload a version without immediately promoting it:

```powershell
npx wrangler versions upload --env production
```

Review the preview, then deploy the approved version. Cloudflare supports uploaded versions and gradual deployment through Wrangler; see [Agents deployment configuration](https://developers.cloudflare.com/agents/runtime/operations/configuration/).

### 12.5 Rollback

For a code-only regression:

```powershell
npx wrangler rollback --env production
```

Worker rollback does not roll back D1, Durable Object SQLite, R2, Queues, or external UiPath state. Cloudflare warns that resource/binding and schema changes can prevent or break code rollback; see [Workers rollbacks](https://developers.cloudflare.com/workers/versions-and-deployments/rollbacks/).

Therefore use expand/contract schema migrations:

1. deploy backward-compatible schema additions;
2. deploy code that can read old and new forms;
3. backfill with an idempotent job;
4. switch writes;
5. verify;
6. remove old fields only in a later release.

Every UiPath operation needs a documented compensating action. A job already started cannot be "rolled back" merely by reverting Worker code.

## 13. CI/CD

Pull requests should run:

```text
npm ci
npm run typecheck
npm test
npm run eval
npx wrangler deploy --dry-run
```

Protect `main`. Require review for policy, schema, skills, prompts, model configuration, resource bindings, and migrations.

A minimal GitHub Actions deployment uses scoped `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID` secrets with Cloudflare's Wrangler action. Cloudflare recommends restricting the token to the required account and never storing it in the repository; see [Cloudflare GitHub Actions](https://developers.cloudflare.com/workers/ci-cd/external-cicd/github-actions/).

```yaml
name: Deploy staging
on:
  push:
    branches: [main]

jobs:
  verify-and-deploy:
    runs-on: ubuntu-latest
    timeout-minutes: 60
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-node@v6
        with:
          node-version-file: .nvmrc
          cache: npm
      - run: npm ci
      - run: npm run typecheck
      - run: npm test
      - run: npm run eval
      - name: Deploy staging
        uses: cloudflare/wrangler-action@v3
        with:
          apiToken: ${{ secrets.CLOUDFLARE_API_TOKEN }}
          accountId: ${{ secrets.CLOUDFLARE_ACCOUNT_ID }}
          command: deploy --env staging
```

Production promotion should be a separate protected workflow requiring environment approval. Do not auto-deploy production on every merge.

## 14. Observability and operations

Every material operation should log structured, redacted metadata:

- engagement ID;
- actor ID and role;
- command intent;
- lifecycle stage;
- model, prompt, schema, and skill version;
- retrieved evidence IDs, not raw evidence text;
- proposed and committed patch IDs;
- tool operation and idempotency key;
- approval ID and approver;
- validation/evaluation outcome;
- latency, token usage, and estimated cost;
- failure or escalation reason.

Create alerts for:

- repeated authorization failures;
- cross-engagement filter violations;
- queue/DLQ growth;
- approval bypass attempts;
- repeated UiPath timeouts;
- schema migration failure;
- sudden retrieval miss rate;
- evaluation regression;
- abnormal token or cost growth.

Never log secrets, full documents, full prompts containing customer material, or model responses containing sensitive records unless a reviewed policy explicitly allows it.

## 15. Required security tests

Before a customer pilot, test:

1. prompt injection embedded in PDF/email/transcript;
2. evidence that attempts to rename or invoke a tool;
3. user with access to engagement A requesting engagement B;
4. guessed Agent instance IDs;
5. replayed approval request;
6. approval payload modified after signature/hash;
7. stale lifecycle baseline;
8. malicious filename and MIME mismatch;
9. oversized upload and decompression bomb;
10. poisoned extraction result;
11. OAuth secret exposure attempts;
12. excessive UiPath scopes;
13. external timeout followed by duplicate invocation;
14. audit-log tampering attempt;
15. retention/deletion verification across SQLite, D1, R2, AI Search, and caches.

Maintain a threat model covering cross-customer leakage, prompt injection, poisoned evidence, identity confusion, unauthorized change requests, dependency compromise, approval bypass, replay, insecure generated artifacts, and unsafe rollback.

## 16. MVP demonstration script

The first release is complete only when this walkthrough runs repeatedly:

1. An FDE creates an isolated AP engagement.
2. The FDE uploads synthetic documents and conflicting notes.
3. The queue normalizes/indexes the evidence idempotently.
4. The Agent creates proposed claims, entities, and edges with citations.
5. Deterministic validation rejects the malicious document's instructions.
6. The Agent identifies ambiguous identity, missing ownership, and critical exceptions.
7. It produces ranked interview questions.
8. Confirmed answers create a new version without erasing prior statements.
9. A customer process owner approves the current-state baseline.
10. The Agent classifies steps across simplification, RPA, AI, HITL, and human-only.
11. It produces the future state, UiPath architecture, backlog, tests, and traceability.
12. An unauthorized release request is blocked.
13. An authorized sandbox UiPath operation executes once through a Workflow.
14. A post-release routing change produces impact analysis and regression tests.
15. The approved change is versioned, audited, and reversible.

## 17. Definition of done

Do not call the MVP complete until:

- the full demonstration passes from a clean environment;
- all required artifacts are generated and schema-valid;
- blocking evaluation thresholds pass;
- an experienced FDE reviews the output;
- interruption, retry, recovery, and rollback are demonstrated;
- Access and per-engagement authorization are tested;
- no critical security findings remain;
- installation, configuration, retention, deletion, support, and recovery are documented;
- customer data export is documented in open formats;
- known limitations and non-goals are visible to operators.

## 18. What to build after the MVP

Only after the vertical slice passes:

1. add read-only Outlook/Slack/Teams/document connectors;
2. add UiPath Action Center mirroring if required;
3. add more business-process fixtures;
4. add reusable de-identified pattern promotion with human curation;
5. improve visual process/graph review;
6. add customer-specific deployment automation/IaC;
7. add carefully scoped subagents for bounded research or validation;
8. consider model adaptation only after a measured failure corpus proves orchestration and retrieval are insufficient.

## 19. Primary source index

### Cloudflare

- [Cloudflare Agents overview](https://developers.cloudflare.com/agents/)
- [Agents API](https://developers.cloudflare.com/agents/runtime/agents-api/)
- [Agents configuration and deployment](https://developers.cloudflare.com/agents/runtime/operations/configuration/)
- [Testing Agents](https://developers.cloudflare.com/agents/getting-started/testing-your-agent/)
- [Human-in-the-loop patterns](https://developers.cloudflare.com/agents/concepts/agentic-patterns/human-in-the-loop/)
- [Agents with Workflows](https://developers.cloudflare.com/agents/concepts/workflows/)
- [Agent Skills](https://developers.cloudflare.com/agents/runtime/execution/agent-skills/)
- [Durable Objects](https://developers.cloudflare.com/durable-objects/)
- [D1 migrations](https://developers.cloudflare.com/d1/reference/migrations/)
- [R2 Workers API](https://developers.cloudflare.com/r2/api/workers/workers-api-reference/)
- [AI Search](https://developers.cloudflare.com/ai-search/get-started/)
- [Queues](https://developers.cloudflare.com/queues/)
- [Access JWT validation](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/)
- [Workers observability](https://developers.cloudflare.com/workers/observability/)
- [Workers GitHub Actions](https://developers.cloudflare.com/workers/ci-cd/external-cicd/github-actions/)
- [Workers rollbacks](https://developers.cloudflare.com/workers/versions-and-deployments/rollbacks/)

### UiPath

- [Managing external OAuth applications](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/managing-external-applications)
- [Fine-grained confidential-app access](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/configuring-access-for-external-apps)
- [Authenticating an external application](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/authenticating-with-an-external-application)
- [Managing Orchestrator jobs](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-jobs)
- [UiPath coded agents](https://uipath.github.io/uipath-python/core/agents/)
- [UiPath process SDK](https://uipath.github.io/uipath-python/core/processes/)
- [UiPath task SDK](https://uipath.github.io/uipath-python/core/tasks/)
- [Action Center external tasks](https://docs.uipath.com/action-center/automation-cloud/latest/user-guide/create-external-task)
