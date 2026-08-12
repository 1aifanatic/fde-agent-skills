"""Validate the structure and minimum resumability of an FDE workspace."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED: dict[str, tuple[str, ...]] = {
    "engagement/charter.md": ("# Engagement Charter", "## Business problem and outcome", "## Scope and non-goals"),
    "engagement/status.md": ("# Engagement Status", "**Engagement ID:**", "**Lifecycle stage:**", "## Next action"),
    "knowledge/evidence-index.md": ("# Evidence Index",),
    "knowledge/glossary.md": ("# Glossary",),
    "knowledge/stakeholders.md": ("# Stakeholders",),
    "knowledge/knowledge-needs.md": ("# Knowledge Needs", "Blocked decision", "Next action"),
    "knowledge/contradictions.md": ("# Contradictions",),
    "process/current-state.md": ("# Current-State Process", "## Exceptions and recovery"),
    "process/automation-allocation.md": ("# Automation Allocation",),
    "process/future-state.md": ("# Future-State Process", "## Current-to-future reconciliation"),
    "delivery/requirements.md": ("# Requirements", "Acceptance criteria"),
    "delivery/architecture.md": ("# Architecture",),
    "delivery/backlog.md": ("# Delivery Backlog", "Acceptance checks"),
    "delivery/traceability.md": ("# Traceability",),
    "delivery/test-plan.md": ("# Test Plan",),
    "delivery/runbook.md": ("# Runbook", "## Recover and roll back"),
    "governance/decisions.md": ("# Decisions",),
    "governance/risks-controls.md": ("# Risks and Controls",),
    "governance/approvals.md": ("# Approvals",),
    "governance/change-log.md": ("# Change Log",),
    "handoff.md": ("# Engagement Handoff", "## Next action"),
}


def validate(root: Path) -> list[dict[str, str]]:
    workspace = root.resolve() / "fde"
    issues: list[dict[str, str]] = []
    for relative, markers in REQUIRED.items():
        path = workspace / relative
        if not path.is_file():
            issues.append({"file": relative, "issue": "missing file"})
            continue
        content = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in content:
                issues.append({"file": relative, "issue": f"missing marker: {marker}"})

    status = workspace / "engagement/status.md"
    if status.is_file():
        content = status.read_text(encoding="utf-8")
        if "**Engagement ID:** Unknown" in content or "**Engagement ID:**\n" in content:
            issues.append({"file": "engagement/status.md", "issue": "engagement ID is not set"})
        if "**Lifecycle stage:** Unknown" in content:
            issues.append({"file": "engagement/status.md", "issue": "lifecycle stage is not set"})
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Project workspace root")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    args = parser.parse_args()

    issues = validate(Path(args.root))
    result = {"valid": not issues, "issues": issues}
    if args.json:
        print(json.dumps(result, indent=2))
    elif issues:
        print(f"FDE workspace invalid: {len(issues)} issue(s)")
        for issue in issues:
            print(f"- {issue['file']}: {issue['issue']}")
    else:
        print("FDE workspace valid")
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
