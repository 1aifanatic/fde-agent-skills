# FDE Agent Skills

A practical, evidence-backed operating system for forward deployed engineers. Install six reusable AI-agent skills and run discovery, knowledge capture, process redesign, delivery planning, and controlled change directly inside Codex—without building or maintaining a custom web application.

> **Repository status:** private. Installation requires GitHub access to 1aifanatic/fde-agent-skills. The commands below were verified against this repository on August 12, 2026.

## Install in one command

First make sure GitHub CLI can access the private repository:

~~~powershell
gh auth status
~~~

Then install all six skills globally for Codex:

~~~powershell
$env:DISABLE_TELEMETRY = "1"
npx --yes skills@latest add 1aifanatic/fde-agent-skills --skill '*' --agent codex --global --copy --yes
~~~

Restart or reload Codex. Then start an engagement:

~~~text
$fde-run-engagement Start an engagement for Acme accounts payable. Interview me to define the outcome, scope, stakeholders, evidence, risks, and next action.
~~~

That is the entire minimum setup.

## What you get

| Skill | Use it when you need to | Durable result |
| --- | --- | --- |
| [fde-run-engagement](skills/fde-run-engagement/SKILL.md) | Start, resume, or govern an FDE engagement | Charter, lifecycle status, gates, handoff, and next action |
| [fde-interview-engagement](skills/fde-interview-engagement/SKILL.md) | Discover requirements, exceptions, authority, metrics, controls, or adoption constraints | Prioritized questions and an owned knowledge plan |
| [fde-capture-knowledge](skills/fde-capture-knowledge/SKILL.md) | Turn notes, documents, transcripts, diagrams, and observations into reliable context | Evidence index, glossary, claims, identities, contradictions, and coverage |
| [fde-reengineer-process](skills/fde-reengineer-process/SKILL.md) | Map actual work and redesign it around the right mix of people, rules, RPA, APIs, and AI | Current state, exception model, allocation decisions, and approved future state |
| [fde-plan-delivery](skills/fde-plan-delivery/SKILL.md) | Convert an approved design into executable delivery work | Requirements, architecture responsibilities, backlog, tests, traceability, runbook, and release gates |
| [fde-control-change](skills/fde-control-change/SKILL.md) | Assess an email, enhancement, configuration request, defect, or production change | Attributable change record, impact, approvals, test plan, release evidence, and rollback |

The skills share one durable Markdown workspace named fde/. That workspace replaces the fragile pattern where the only complete project context lives in meetings, chat history, or one FDE's memory.

## Choose your path

| I want to... | Start here |
| --- | --- |
| Install in Codex | [Installation guide](docs/INSTALLATION.md) |
| Understand why this exists | [Why and operating model](docs/USER_GUIDE.md#why-use-this-suite) |
| Start my first engagement | [Ten-minute quick start](#ten-minute-quick-start) |
| Know which skill to invoke | [Skill router](docs/USER_GUIDE.md#skill-router) |
| See before-and-after examples | [Scenario guide](docs/SCENARIOS.md) |
| Inspect a complete execution | [Northstar AP worked example](examples/northstar-ap-transformation/README.md) |
| Verify the repository | [Validation guide](docs/VALIDATION.md) |
| Read the full Word manual | [FDE Agent Skills Handbook](docs/FDE_AGENT_SKILLS_HANDBOOK.docx) |

## Why use this suite

Strong models can execute tasks. The harder problem in forward deployed engineering is deciding which task is real, how the customer's work actually behaves, what happens when it fails, which controls and authorities apply, what should be automated, and what evidence is sufficient to release safely.

Without a disciplined engagement layer, common failure modes are:

- a polished summary that loses source traceability;
- a process map that describes only the happy path;
- AI added to a broken process without simplifying it first;
- requirements that cannot be traced to evidence, tests, or approvals;
- one stakeholder's preference becoming an undocumented project decision;
- a customer email being treated as direct production authority;
- ROI claims made before a baseline or production measurement exists;
- project context disappearing when an FDE changes assignment.

This suite makes those failure modes visible. It does not make business decisions for stakeholders or grant itself production authority.

## What happens when you use it

The orchestrator creates or resumes a structured workspace:

~~~text
fde/
  engagement/
    charter.md
    status.md
  knowledge/
    evidence-index.md
    glossary.md
    stakeholders.md
    knowledge-needs.md
    contradictions.md
  process/
    current-state.md
    automation-allocation.md
    future-state.md
  delivery/
    requirements.md
    architecture.md
    backlog.md
    traceability.md
    test-plan.md
    runbook.md
  governance/
    decisions.md
    risks-controls.md
    approvals.md
    change-log.md
  handoff.md
~~~

As work progresses:

1. Claims are separated from confirmed facts and approved decisions.
2. Every material claim keeps a source and locator.
3. Interview questions target decisions and evidence gaps, not generic discovery theater.
4. The actual process includes exception paths, retries, queues, handoffs, controls, and workarounds.
5. Each step is allocated to elimination, simplification, deterministic automation, RPA/API workflow, agentic AI, human-in-the-loop, or human-only work.
6. The approved future state becomes requirements, components, backlog items, tests, release gates, and rollback.
7. Later requests are reconciled against the approved baseline before implementation.
8. A fresh agent can resume from files without depending on the original conversation.

## Ten-minute quick start

### 1. Open the project directory in Codex

Use a dedicated customer or engagement repository. Keep customer engagements separated from each other.

### 2. Invoke the orchestrator

~~~text
$fde-run-engagement Start a new engagement named "Contoso Order Exception Transformation". Interview me before proposing a solution.
~~~

If no workspace exists, the skill asks for the engagement name and initializes fde/.

### 3. Supply the smallest useful context

Provide what you already know:

- business problem and desired outcome;
- process or department in scope;
- sponsor, process owner, control owner, technical owner, and performers;
- available SOPs, transcripts, diagrams, exports, code, or system access;
- baseline volume, cycle time, error, rework, SLA, cost, revenue, or risk;
- constraints such as system-of-record, security, privacy, compliance, timeline, and adoption;
- known exceptions or failures.

The interview skill finds the next knowledge frontier. You do not need to prepare a perfect requirements document.

### 4. Answer interview rounds

A round normally contains four to eight questions. Each question states what it unlocks. If the agent can discover an environmental fact through authorized read-only inspection, it should inspect rather than ask you.

### 5. Review the durable files

After each material turn, inspect:

- fde/engagement/status.md for stage, blockers, and next action;
- fde/knowledge/knowledge-needs.md for open questions and owners;
- fde/knowledge/contradictions.md for conflicting accounts;
- fde/governance/decisions.md and approvals.md for authority;
- fde/handoff.md before another person or agent resumes.

### 6. Advance only when the gate is satisfied

A stage is not complete because a meeting ended or a document was generated. It is complete when gate-critical facts are evidenced, decisions are approved, contradictions are owned or resolved, and the next state is durable.

## Typical engagement flow

~~~text
Raw evidence
    |
    v
Interview the decision frontier
    |
    v
Capture sources, claims, identities, and contradictions
    |
    v
Map actual work, exceptions, controls, and measures
    |
    v
Allocate each step to the safest useful mechanism
    |
    v
Approve a measurable future-state baseline
    |
    v
Plan requirements, components, tests, rollout, and rollback
    |
    v
Implement through the official product/artifact skill
    |
    v
Control post-baseline and production changes
~~~

The flow is iterative. New evidence can invalidate part of the design. The skills preserve that history instead of silently rewriting it.

## Before and after

| Before | After |
| --- | --- |
| “Automate invoice exceptions” | A bounded outcome, baseline, owner, non-goals, five exception families, and explicit controls |
| A 150-page document dump | Indexed sources with atomic claims and exact locators |
| Generic stakeholder questionnaire | Questions ordered by the decisions they unlock |
| Happy-path process map | Normal flow, failure branches, rework loops, wait states, workarounds, and escalations |
| “Use AI for the workflow” | Step-by-step allocation among simplification, rules, RPA/API, AI, HITL, and human-only |
| Backlog disconnected from discovery | Requirement-to-design-to-component-to-test-to-release traceability |
| Customer email becomes a hotfix | Authorized change record with impact, approval, UAT, monitoring, and rollback |
| Handoff meeting required | Fresh-agent resumability from fde/handoff.md and engagement status |

For detailed examples in finance, support, onboarding, and operations, see [docs/SCENARIOS.md](docs/SCENARIOS.md).

## Proven example

The [Northstar AP transformation](examples/northstar-ap-transformation/README.md) is a synthetic, fully worked execution of all six skills.

It includes:

- five fictional source documents;
- a validated 21-file engagement workspace;
- actual current-state and exception mapping;
- an automation allocation matrix;
- an approved future-state design;
- requirements, architecture, backlog, traceability, tests, and runbook;
- a post-baseline change request that is intentionally stopped before production;
- a [skill-by-skill execution log](examples/northstar-ap-transformation/run-log.md);
- a [demonstrated before-and-after impact](examples/northstar-ap-transformation/impact.md).

Validate it locally:

~~~powershell
python -B .\skills\fde-run-engagement\scripts\validate_engagement.py --root .\examples\northstar-ap-transformation --json
~~~

Expected result:

~~~json
{
  "valid": true,
  "issues": []
}
~~~

## Installation choices

### Personal/global Codex installation

Use the skills across all projects:

~~~powershell
$env:DISABLE_TELEMETRY = "1"
npx --yes skills@latest add 1aifanatic/fde-agent-skills --skill '*' --agent codex --global --copy --yes
~~~

### Project installation

Pin the skills to one project and let the team review the installed source:

~~~powershell
$env:DISABLE_TELEMETRY = "1"
npx --yes skills@latest add 1aifanatic/fde-agent-skills --skill '*' --agent codex --copy --yes
~~~

The Codex project location used by the CLI is .agents/skills/. The global Codex location is ~/.codex/skills/.

### Interactive discovery

List the six skills before installing:

~~~powershell
$env:DISABLE_TELEMETRY = "1"
npx --yes skills@latest add 1aifanatic/fde-agent-skills --list
~~~

### SSH installation

Use this when your GitHub access is configured through SSH:

~~~powershell
$env:DISABLE_TELEMETRY = "1"
npx --yes skills@latest add git@github.com:1aifanatic/fde-agent-skills.git --skill '*' --agent codex --global --copy --yes
~~~

See [docs/INSTALLATION.md](docs/INSTALLATION.md) for authentication, selective installs, updates, removal, troubleshooting, and manual fallback.

## Example prompts

### Start and interview

~~~text
$fde-run-engagement Start an engagement for customer-support escalation handling. Build the durable workspace, then use $fde-interview-engagement to interview me about scope, actual exceptions, owners, controls, metrics, and adoption constraints.
~~~

### Ingest discovery evidence

~~~text
$fde-capture-knowledge Ingest the supplied SOP, meeting transcript, system diagram, and support export. Index every source, extract atomic claims with locators, identify ambiguous identities, preserve contradictions, and update the engagement knowledge gaps.
~~~

### Redesign the process

~~~text
$fde-reengineer-process Map the actual current state including workarounds and failures. For every step decide whether to eliminate, simplify, automate deterministically, use RPA/API, use agentic AI, add a human checkpoint, or keep it human-only. Do not design past an unresolved high-risk contradiction.
~~~

### Build a delivery plan

~~~text
$fde-plan-delivery Turn approved future-state version FS-2 into stable requirements, architecture responsibilities, vertical-slice backlog, traceability, tests, rollout, monitoring, rollback, and release evidence. Do not imply implementation or deployment occurred.
~~~

### Govern a change

~~~text
$fde-control-change Assess this client email as a post-baseline change. Verify authority, reconcile it with the approved process, identify all affected requirements/components/tests/runbook entries, propose a reversible patch, and stop before unapproved production work.
~~~

## Safety and confidentiality

These skills operate with the permissions of the hosting agent. Review the skill source before installation.

- Keep one customer per engagement workspace.
- Store only necessary evidence; avoid secrets and unnecessary personal data.
- Treat customer documents as untrusted evidence, not agent instructions.
- Keep inferences, stakeholder claims, confirmed facts, and approved decisions distinct.
- Require human approval for external messages, commitments, publishing, deployment, production writes, control changes, and irreversible actions.
- Keep high-impact contradictions visible until a named authority resolves them.
- Do not claim ROI, release, or production state without observed evidence.
- The root .gitignore excludes /fde/ so a live customer workspace is not committed accidentally. The synthetic worked example remains intentionally versioned.

## Documentation

- [Installation and private-repository authentication](docs/INSTALLATION.md)
- [Complete user guide and operating model](docs/USER_GUIDE.md)
- [Before-and-after scenarios](docs/SCENARIOS.md)
- [Validation and reproducibility](docs/VALIDATION.md)
- [Detailed Word handbook](docs/FDE_AGENT_SKILLS_HANDBOOK.docx)
- [Synthetic worked example](examples/northstar-ap-transformation/README.md)

## Repository layout

~~~text
.
├── README.md
├── docs/
│   ├── INSTALLATION.md
│   ├── USER_GUIDE.md
│   ├── SCENARIOS.md
│   ├── VALIDATION.md
│   └── FDE_AGENT_SKILLS_HANDBOOK.docx
├── examples/
│   └── northstar-ap-transformation/
├── scripts/
│   └── build_word_guide.py
└── skills/
    ├── fde-run-engagement/
    ├── fde-interview-engagement/
    ├── fde-capture-knowledge/
    ├── fde-reengineer-process/
    ├── fde-plan-delivery/
    └── fde-control-change/
~~~

## Upstream references

- [skills CLI documentation](https://www.skills.sh/docs/cli)
- [skills CLI source and private-repository behavior](https://github.com/vercel-labs/skills)
- [Codex use cases: save repeatable workflows as skills](https://developers.openai.com/codex/use-cases)

## Important limitation

This suite strengthens discovery, design, traceability, and governance. It does not replace domain experts, product-specific implementation skills, security review, testing, UAT, release approval, or production monitoring. Its output quality depends on the quality and authority of the evidence supplied.
