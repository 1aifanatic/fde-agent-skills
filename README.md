# FDE Agent Skills

An evidence-backed skill suite for forward deployed engineers. The suite guides an engagement from discovery through process redesign, delivery planning, release, and controlled post-release change without requiring a dedicated web application.

## Included skills

| Skill | Purpose |
| --- | --- |
| `fde-run-engagement` | Orchestrates the complete FDE lifecycle and maintains the engagement workspace. |
| `fde-interview-engagement` | Interviews process owners, SMEs, control owners, and delivery teams to uncover required knowledge. |
| `fde-capture-knowledge` | Converts notes, documents, transcripts, and observations into evidence-backed engagement knowledge. |
| `fde-reengineer-process` | Maps the current state and designs a governed future state across people, deterministic automation, RPA, and AI. |
| `fde-plan-delivery` | Turns an approved future state into requirements, architecture decisions, backlog items, tests, rollout, and support plans. |
| `fde-control-change` | Governs post-baseline and post-release changes through authority checks, impact analysis, approval, validation, and audit history. |

## Install

Copy the six directories under `skills/` into your Codex skills directory:

```text
%CODEX_HOME%\skills\
```

If `CODEX_HOME` is not set, the usual Windows location is:

```text
%USERPROFILE%\.codex\skills\
```

Restart or reload Codex so the new skills are discovered.

## Start an engagement

Invoke the orchestrator in Codex:

```text
$fde-run-engagement
```

Provide the client or program name, target business area, intended outcome, known stakeholders, available evidence, constraints, and desired timeline. The skill initializes a durable Markdown workspace under `fde/`, identifies gaps, and routes work to the specialist skills.

You can also invoke a specialist directly, for example:

```text
$fde-interview-engagement interview the accounts-payable process owner and identify the evidence required to redesign invoice exception handling
```

## Validate the suite

Run the Codex skill validator against each directory:

```powershell
$validator = "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py"
Get-ChildItem -LiteralPath .\skills -Directory | ForEach-Object {
    python $validator $_.FullName
}
```

The orchestrator also includes workspace utilities:

```powershell
python .\skills\fde-run-engagement\scripts\init_engagement.py --help
python .\skills\fde-run-engagement\scripts\validate_engagement.py --help
```

## Design principles

- Treat source evidence, stakeholder claims, assumptions, decisions, and unresolved gaps as different things.
- Capture exception paths, handoffs, controls, and operational reality—not only the documented happy path.
- Redesign the process before selecting an automation mechanism.
- Keep high-risk or judgment-heavy work under explicit human authority.
- Preserve traceability from business outcomes through requirements, implementation, tests, release evidence, and change history.
- Deploy on top of the customer's existing systems of record unless migration is an explicit, approved part of the engagement.

## Repository layout

```text
skills/
  fde-run-engagement/
  fde-interview-engagement/
  fde-capture-knowledge/
  fde-reengineer-process/
  fde-plan-delivery/
  fde-control-change/
```

The specialist skills reference the orchestrator's shared taxonomy, lifecycle gates, and workspace contract using relative paths, so keep the six directories together.
