"""Create a durable Markdown workspace for one FDE engagement."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


def table(headers: str) -> str:
    columns = [part.strip() for part in headers.split("|")]
    return f"| {' | '.join(columns)} |\n| {' | '.join('---' for _ in columns)} |\n"


def build_files(name: str, engagement_id: str, created: str) -> dict[str, str]:
    files: dict[str, str] = {
        "engagement/charter.md": f"""# Engagement Charter

- **Engagement:** {name}
- **Engagement ID:** {engagement_id}
- **Created:** {created}
- **Sponsor:** Unknown
- **Process owner:** Unknown
- **Delivery owner:** Unknown

## Business problem and outcome

Unknown.

## Scope and non-goals

Unknown.

## Baseline and success measures

Unknown.

## Constraints and assumptions

Unknown.
""",
        "engagement/status.md": f"""# Engagement Status

- **Engagement ID:** {engagement_id}
- **Lifecycle stage:** framing
- **Last updated:** {created}
- **Stage owner:** Unknown

## Gate status

Framing gate is open.

## Critical blockers

- KN-001: Complete engagement framing.

## Next action

Run `$fde-interview-engagement` with the FDE or process owner.

## Recently changed

- Workspace initialized.
""",
        "knowledge/evidence-index.md": "# Evidence Index\n\n" + table("ID | Source | Type | Author/owner | Observed/effective date | Locator | Classification | Status"),
        "knowledge/glossary.md": "# Glossary\n\n" + table("Term | Meaning | Status | Evidence | Owner | Last verified"),
        "knowledge/stakeholders.md": "# Stakeholders\n\n" + table("ID | Person/role | Responsibility | Authority | Process/system | Evidence | Status"),
        "knowledge/knowledge-needs.md": "# Knowledge Needs\n\n" + table("ID | Category | Question or claim | Status | Evidence | Owner/source | Needed by | Blocked decision | Risk | Next action | Last verified") + "| KN-001 | Outcome and scope | Complete engagement framing | unknown |  | Sponsor/process owner | framing | Discovery authorization | high | Interview owner |  |\n",
        "knowledge/contradictions.md": "# Contradictions\n\n" + table("ID | Competing claims/evidence | Impact | Severity | Resolver | Resolution question | Status | Decision"),
        "process/current-state.md": "# Current-State Process\n\n## Boundary\n\nUnknown.\n\n## Normal flow\n\n" + table("Step ID | Step | Performer/owner | Trigger | Inputs | Systems | Rule/action | Outputs | Dependency | Timing/volume | Evidence | Status") + "\n## Exceptions and recovery\n\n" + table("Exception ID | Related step | Condition | Frequency/severity | Actual response | Owner/escalation | Control | Evidence | Status"),
        "process/automation-allocation.md": "# Automation Allocation\n\n" + table("Step ID | Current problem | Disposition | Rationale | Risk/control | Human accountability | Evidence | Approval"),
        "process/future-state.md": "# Future-State Process\n\n## Design objective\n\nUnknown.\n\n## Target flow\n\n" + table("Step ID | Step | Actor/system | Inputs | Action/decision | Outputs | Exception/fallback | Control | Metric | Status") + "\n## Current-to-future reconciliation\n\n" + table("Current step | Future disposition | Replacement/owner | Decision/evidence"),
        "delivery/requirements.md": "# Requirements\n\n" + table("ID | Type | Requirement | Owner | Evidence | Acceptance criteria | Priority | Status"),
        "delivery/architecture.md": "# Architecture\n\n## Context and boundaries\n\nUnknown.\n\n## Components and responsibilities\n\n" + table("Component | Responsibility | Public contract | Owner | Decision/evidence | Status") + "\n## Quality attributes\n\nUnknown.\n",
        "delivery/backlog.md": "# Delivery Backlog\n\n" + table("ID | Outcome | Requirement IDs | Components/files | Dependencies | Acceptance checks | Test evidence | Risk | Rollback/checkpoint | Status"),
        "delivery/traceability.md": "# Traceability\n\n" + table("Requirement | Approved design/process | Implementation | Test/UAT | Evidence | Release version | Status"),
        "delivery/test-plan.md": "# Test Plan\n\n" + table("Test ID | Requirement/risk | Level | Fixture/environment | Expected result | Evidence | Owner | Status"),
        "delivery/runbook.md": "# Runbook\n\n## Deploy and configure\n\nUnknown.\n\n## Monitor and support\n\nUnknown.\n\n## Recover and roll back\n\nUnknown.\n\n## Retain and delete data\n\nUnknown.\n",
        "governance/decisions.md": "# Decisions\n\n" + table("ID | Date | Decision | Alternatives | Rationale/evidence | Owner | Effective scope | Supersedes | Status"),
        "governance/risks-controls.md": "# Risks and Controls\n\n" + table("ID | Risk/cause | Impact | Severity | Control/mitigation | Owner | Evidence/test | Residual risk | Status"),
        "governance/approvals.md": "# Approvals\n\n" + table("ID | Date | Gate/action | Exact baseline/version | Approver/authority | Decision | Conditions | Evidence"),
        "governance/change-log.md": "# Change Log\n\n" + table("ID | Date/requester | Request/source | Authority | Baseline | Impact/risk | Patch/test/rollback | Approvals | Release/evidence | Status"),
        "handoff.md": f"""# Engagement Handoff

## Mission

{name}: framing is not yet complete.

## Current stage and gate

Framing; gate open.

## Confirmed knowledge

None yet.

## Critical gaps and contradictions

- KN-001: Complete engagement framing.

## Approved decisions

None yet.

## Risks and controls

Not assessed.

## Next action

Run `$fde-interview-engagement`.
""",
    }
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Project workspace root")
    parser.add_argument("--name", required=True, help="Engagement name")
    parser.add_argument("--id", dest="engagement_id", help="Stable engagement ID")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    workspace = root / "fde"
    if workspace.exists():
        raise SystemExit(f"Refusing to overwrite existing workspace: {workspace}")

    engagement_id = args.engagement_id or str(uuid4())
    created = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    files = build_files(args.name.strip(), engagement_id, created)

    for relative, content in files.items():
        target = workspace / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content.rstrip() + "\n", encoding="utf-8")

    print(f"Created {len(files)} files in {workspace}")
    print(f"Engagement ID: {engagement_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
