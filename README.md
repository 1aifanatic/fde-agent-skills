# FDE Agent Skills

An evidence-backed operating system for forward deployed engineers. Use the six skills directly in Codex, or follow the optional Cloudflare guide to build a governed FDE application.

> **Contributions are welcome.** Help improve the interview methods, evidence model, process-reengineering playbooks, delivery controls, examples, validation, or Cloudflare architecture. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or pull request.

## Install all six skills

Run the public installation command:

```powershell
npx --yes skills@latest add https://github.com/1aifanatic/fde-agent-skills.git --skill '*' --agent codex --global --copy --yes
```

Restart or reload Codex, then begin:

```text
$fde-run-engagement Start an engagement for Acme accounts payable. Interview me to define the outcome, scope, stakeholders, evidence, risks, and next action.
```

> The install command requires Node.js/npm. A GitHub account or access token is not required for this public repository. See [Installation and troubleshooting](docs/INSTALLATION.md) if discovery fails.

## Choose your path

| Your goal | Start here | What you get |
| --- | --- | --- |
| Use the FDE agent now | [Install the skills](#install-all-six-skills) | Six reusable skills; no application infrastructure required |
| Run your first engagement | [Five-minute workflow](#five-minute-workflow) | A governed Markdown workspace and a clear next action |
| Understand the complete method | [User guide](docs/USER_GUIDE.md) | Operating model, prompts, lifecycle, roles, and guardrails |
| See the impact before adopting | [Worked example](examples/northstar-ap-transformation/README.md) | A complete synthetic AP transformation with outputs and run log |
| Build a team application | [Cloudflare app build guide](docs/CLOUDFLARE_APP_BUILD_GUIDE.md) | Architecture and step-by-step deployment instructions |
| Review before/after scenarios | [Scenario guide](docs/SCENARIOS.md) | Generic examples across common FDE situations |
| Validate this repository | [Validation guide](docs/VALIDATION.md) | Structural, link, example, and DOCX checks |
| Share a Word manual | [FDE Agent Skills Handbook](docs/FDE_AGENT_SKILLS_HANDBOOK.docx) | Detailed offline documentation for teams and stakeholders |
| Improve the project | [Contribution guide](CONTRIBUTING.md) | Contribution areas, standards, tests, and pull-request checklist |

## What this repository contains

There are two ways to use the work:

1. **Skills-only path — recommended first.** Install the skills with the command above and use them from Codex. The project record is a portable `fde/` Markdown workspace.
2. **Cloudflare application path — optional.** Build a shared web application when you need centralized authentication, durable multi-engagement state, evidence storage, approvals, audit, deployment controls, and UiPath adapters.

The Cloudflare document is an implementation guide, not a prebuilt or already deployed application. The skills work independently of it.

## The six skills

| Skill | Invoke it for | Main output |
| --- | --- | --- |
| [`fde-run-engagement`](skills/fde-run-engagement/SKILL.md) | Start, resume, route, or govern an engagement | Charter, lifecycle, gates, handoff, next action |
| [`fde-interview-engagement`](skills/fde-interview-engagement/SKILL.md) | Interview process owners, SMEs, controls, delivery teams, or the FDE | Prioritized questions, decisions, gaps, knowledge plan |
| [`fde-capture-knowledge`](skills/fde-capture-knowledge/SKILL.md) | Convert notes, documents, transcripts, diagrams, and observations into reliable context | Evidence index, claims, glossary, identities, conflicts, coverage |
| [`fde-reengineer-process`](skills/fde-reengineer-process/SKILL.md) | Map real work and design the future state | Current state, exceptions, allocation decisions, approved future state |
| [`fde-plan-delivery`](skills/fde-plan-delivery/SKILL.md) | Turn an approved future state into executable delivery | Requirements, architecture, backlog, tests, traceability, runbook, release gates |
| [`fde-control-change`](skills/fde-control-change/SKILL.md) | Govern post-baseline or post-release requests | Change record, authority check, impact, tests, approval, rollback |

## How the skills fit together

```text
Frame engagement
      |
      v
Interview stakeholders <----> Capture and reconcile evidence
      |                                  |
      +---------------+------------------+
                      v
            Map the current state
                      |
                      v
          Approve the current baseline
                      |
                      v
             Redesign around AI,
        rules, APIs, RPA, HITL, people
                      |
                      v
           Approve the future state
                      |
                      v
      Plan, test, release, and operate
                      |
                      v
          Control subsequent changes
```

The skills do not force a purely linear conversation. Interviewing and knowledge capture repeat until important gaps and contradictions are resolved. Approval gates stop unconfirmed assumptions from silently becoming delivery facts.

## Five-minute workflow

### 1. Create the engagement

```text
$fde-run-engagement Start an engagement for Contoso order management.
Interview me before recommending a solution.
```

The orchestrator creates or resumes this portable structure:

```text
fde/
|-- engagement/
|-- knowledge/
|-- discovery/
|-- process/
|-- design/
|-- delivery/
|-- testing/
|-- release/
|-- change/
|-- operations/
`-- handoff/
```

### 2. Discover what matters

```text
$fde-interview-engagement Interview the order-management process owner.
Focus on exceptions, handoffs, authority, controls, volumes, service levels,
failure handling, and measurable outcomes.
```

### 3. Reconcile evidence

```text
$fde-capture-knowledge Reconcile the interview notes, SOPs, tickets, and system observations.
Separate sourced fact, stakeholder assertion, inference, proposal, and decision.
Show contradictions and unresolved identity questions.
```

### 4. Redesign the process

```text
$fde-reengineer-process Map the real current state, including rework and escalation loops.
Then classify each future-state step as eliminate, simplify, deterministic automation,
API, RPA, agentic AI, human-in-the-loop, or human-only.
Do not cross an approval gate without named approval.
```

### 5. Plan delivery

```text
$fde-plan-delivery Convert the approved future state into requirements, architecture
responsibilities, a session-sized backlog, acceptance tests, traceability,
release gates, rollback, and an operating runbook.
```

### 6. Govern later changes

```text
$fde-control-change Assess this routing-change request.
Verify the requester's authority, reconcile it with the approved baseline,
show impact and regression scope, and require approval before release.
```

## Install options

### Recommended: global Codex installation

Use the complete command shown at the top of this README:

```powershell
npx --yes skills@latest add https://github.com/1aifanatic/fde-agent-skills.git --skill '*' --agent codex --global --copy --yes
```

### Preview what the CLI discovers

```powershell
npx --yes skills@latest add https://github.com/1aifanatic/fde-agent-skills.git --list
```

### Install only one skill

```powershell
npx --yes skills@latest add https://github.com/1aifanatic/fde-agent-skills.git --skill fde-run-engagement --agent codex --global --copy --yes
```

### Install for the current project

Remove `--global`:

```powershell
npx --yes skills@latest add https://github.com/1aifanatic/fde-agent-skills.git --skill '*' --agent codex --copy --yes
```

### Refresh an installation

Re-running `add` is the most reliable way to rediscover all skills, including skills added to the repository later:

```powershell
npx --yes skills@latest add https://github.com/1aifanatic/fde-agent-skills.git --skill '*' --agent codex --global --copy --yes
```

For SSH-based Git setups, source the repository as `git@github.com:1aifanatic/fde-agent-skills.git`. The [installation guide](docs/INSTALLATION.md) covers prerequisites, verification, local installation, and troubleshooting.

## What changes after adoption

| Before | After |
| --- | --- |
| Project context is scattered across calls, inboxes, chat, and personal notes | Evidence, claims, decisions, conflicts, and gaps have durable locations |
| Process maps describe the happy path | Exceptions, rework, queues, escalations, and failure handling are explicit |
| A model receives a large document dump | Retrieval is driven by the active decision and backed by citations |
| AI is added to every step | Each step is deliberately allocated to people, rules, APIs, RPA, AI, or HITL |
| Requirements drift away from evidence and tests | Requirements trace to sources, implementation, acceptance, and release evidence |
| A stakeholder message can become an undocumented production change | Authority, impact, approval, regression, release, and rollback are governed |
| Handoffs depend on one engineer's memory | A new engineer can resume from the workspace and handoff record |

Read the complete [before-and-after scenarios](docs/SCENARIOS.md) or inspect the [Northstar AP worked example](examples/northstar-ap-transformation/README.md).

## Optional Cloudflare application

Use the [Cloudflare app build and deployment guide](docs/CLOUDFLARE_APP_BUILD_GUIDE.md) when a team needs a centralized control plane. It covers:

- Workers and the Cloudflare Agents SDK;
- one isolated Agent/Durable Object per engagement;
- D1, embedded SQLite, R2, AI Search, Queues, and Workflows;
- Cloudflare Access and application-level authorization;
- evidence provenance, lifecycle gates, audit, and versioning;
- UiPath execution adapters with least privilege;
- testing, observability, CI/CD, deployment, recovery, and rollback;
- a synthetic AP vertical slice and definition of done.

Start with the skills-only path unless shared application requirements justify the additional platform work.

## Worked example

The [Northstar AP transformation](examples/northstar-ap-transformation/README.md) runs all six skills against synthetic source material. It includes:

- five input sources with deliberate conflicts and missing information;
- a 21-file engagement workspace;
- current-state and future-state process artifacts;
- delivery, test, release, change, and handoff records;
- a run log that explains each skill's contribution;
- an impact report that compares the unstructured and governed approaches.

It contains no customer data and makes no unverified production ROI claim.

## Documentation map

| Document | Purpose |
| --- | --- |
| [Installation](docs/INSTALLATION.md) | All install modes, GitHub authentication, verification, update, removal, troubleshooting |
| [User guide](docs/USER_GUIDE.md) | Why to use the suite, roles, lifecycle, skill router, prompts, guardrails |
| [Scenarios](docs/SCENARIOS.md) | Before/after examples and adoption patterns |
| [Worked example](examples/northstar-ap-transformation/README.md) | Complete synthetic execution and artifact navigation |
| [Cloudflare app build guide](docs/CLOUDFLARE_APP_BUILD_GUIDE.md) | Optional application architecture, implementation, security, and deployment |
| [Validation](docs/VALIDATION.md) | Repository checks and known validation limits |
| [Word handbook](docs/FDE_AGENT_SKILLS_HANDBOOK.docx) | Detailed shareable manual in Microsoft Word format |
| [Contributing](CONTRIBUTING.md) | How to propose, implement, test, and submit improvements |

## Contributing

Forward deployed engineering gets better when practitioners contribute real patterns without contributing real customer data. Useful contributions include:

- sharper interview questions and knowledge-gap strategies;
- stronger provenance, contradiction, identity, and confidence handling;
- process-redesign examples that include exceptions and controls;
- delivery, testing, release, rollback, and change-governance improvements;
- additional synthetic worked examples from different business functions;
- Cloudflare, UiPath, security, privacy, and observability corrections backed by primary sources;
- accessibility, installation, documentation, and validation improvements.

Start with [CONTRIBUTING.md](CONTRIBUTING.md), search [existing issues](https://github.com/1aifanatic/fde-agent-skills/issues), and open a focused proposal or pull request. Never submit customer documents, credentials, personal data, or proprietary process details.

## Safety model

The suite treats client evidence as data, not instructions. It requires attribution, confidence, contradiction handling, named authority, approval gates, least privilege, validation, rollback, and auditable change history.

It never grants itself permission to:

- make business decisions for stakeholders;
- treat an email or chat message as automatic production authority;
- send client communications or deploy changes unless explicitly authorized;
- merge customer knowledge across engagements;
- claim ROI without a baseline and measured post-release evidence.

Review source evidence before accepting generated artifacts, and remove or redact secrets and unnecessary personal data before placing material in the workspace.

## Validate the repository

From the repository root:

```powershell
python -B scripts/validate_repository.py
```

Validate an engagement workspace:

```powershell
python -B skills/fde-run-engagement/scripts/validate_engagement.py --root examples/northstar-ap-transformation --json
```

The repository validator checks the six skill packages, internal Markdown links, the synthetic example, required documentation, and the Word package structure. See [validation details and limitations](docs/VALIDATION.md).

## Repository layout

```text
fde-agent-skills/
|-- README.md
|-- CONTRIBUTING.md
|-- .github/
|   |-- ISSUE_TEMPLATE/
|   |   |-- contribution.yml
|   |   `-- config.yml
|   `-- pull_request_template.md
|-- skills/
|   |-- fde-run-engagement/
|   |-- fde-interview-engagement/
|   |-- fde-capture-knowledge/
|   |-- fde-reengineer-process/
|   |-- fde-plan-delivery/
|   `-- fde-control-change/
|-- docs/
|   |-- INSTALLATION.md
|   |-- USER_GUIDE.md
|   |-- SCENARIOS.md
|   |-- CLOUDFLARE_APP_BUILD_GUIDE.md
|   |-- VALIDATION.md
|   `-- FDE_AGENT_SKILLS_HANDBOOK.docx
|-- examples/
|   `-- northstar-ap-transformation/
`-- scripts/
    |-- build_word_guide.py
    `-- validate_repository.py
```

## Recommended adoption sequence

1. Install all six skills.
2. Run the synthetic worked example with your team.
3. Pilot one bounded, reversible engagement.
4. Review the artifacts with an experienced FDE and control owner.
5. Refine terminology and gates without weakening provenance.
6. Build the optional Cloudflare application only when centralized team operation is needed.

The governing principle is simple: automate execution only after the team understands the business, evidence, exceptions, authority, and controls.
