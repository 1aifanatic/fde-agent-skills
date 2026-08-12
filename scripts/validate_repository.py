from __future__ import annotations

import json
import re
import subprocess
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = {
    "fde-run-engagement",
    "fde-interview-engagement",
    "fde-capture-knowledge",
    "fde-reengineer-process",
    "fde-plan-delivery",
    "fde-control-change",
}
EXPECTED_DOCS = {
    ROOT / "README.md",
    ROOT / "docs" / "INSTALLATION.md",
    ROOT / "docs" / "USER_GUIDE.md",
    ROOT / "docs" / "SCENARIOS.md",
    ROOT / "docs" / "VALIDATION.md",
    ROOT / "docs" / "FDE_AGENT_SKILLS_HANDBOOK.docx",
}
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def validate_skills(errors: list[str]) -> None:
    skill_root = ROOT / "skills"
    discovered = {path.name for path in skill_root.iterdir() if path.is_dir() and (path / "SKILL.md").is_file()}
    require(discovered == EXPECTED_SKILLS, f"skill set mismatch: {sorted(discovered)}", errors)

    for name in sorted(EXPECTED_SKILLS):
        text = (skill_root / name / "SKILL.md").read_text(encoding="utf-8")
        require(text.startswith("---\n"), f"{name}: missing YAML frontmatter", errors)
        require(f"\nname: {name}\n" in text, f"{name}: frontmatter name mismatch", errors)
        require("\ndescription:" in text, f"{name}: missing description", errors)
        require((skill_root / name / "agents" / "openai.yaml").is_file(), f"{name}: missing agents/openai.yaml", errors)


def validate_links(errors: list[str]) -> None:
    markdown_files = list(ROOT.glob("*.md")) + list((ROOT / "docs").glob("*.md"))
    markdown_files += list((ROOT / "examples").rglob("*.md"))

    for markdown in markdown_files:
        text = markdown.read_text(encoding="utf-8")
        for target in LINK_PATTERN.findall(text):
            target = target.strip()
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path_text = target.split("#", 1)[0]
            if not path_text:
                continue
            resolved = (markdown.parent / path_text).resolve()
            require(resolved.exists(), f"{markdown.relative_to(ROOT)}: broken link {target}", errors)


def validate_example(errors: list[str]) -> None:
    validator = ROOT / "skills" / "fde-run-engagement" / "scripts" / "validate_engagement.py"
    example = ROOT / "examples" / "northstar-ap-transformation"
    result = subprocess.run(
        [sys.executable, "-B", str(validator), "--root", str(example), "--json"],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    require(result.returncode == 0, f"example validator failed: {result.stdout}{result.stderr}", errors)
    if result.returncode == 0:
        payload = json.loads(result.stdout)
        require(payload.get("valid") is True, f"example workspace reported invalid: {payload}", errors)

    inputs = list((example / "inputs").glob("*.md"))
    require(len(inputs) == 5, f"expected 5 synthetic input sources, found {len(inputs)}", errors)
    require((example / "run-log.md").is_file(), "worked example missing run-log.md", errors)
    require((example / "impact.md").is_file(), "worked example missing impact.md", errors)


def validate_docs(errors: list[str]) -> None:
    for path in sorted(EXPECTED_DOCS):
        require(path.is_file(), f"missing documentation artifact: {path.relative_to(ROOT)}", errors)

    handbook = ROOT / "docs" / "FDE_AGENT_SKILLS_HANDBOOK.docx"
    if handbook.is_file():
        try:
            with zipfile.ZipFile(handbook) as archive:
                require(archive.testzip() is None, "handbook DOCX contains a corrupt ZIP member", errors)
                names = set(archive.namelist())
                require("word/document.xml" in names, "handbook missing word/document.xml", errors)
                require("word/styles.xml" in names, "handbook missing word/styles.xml", errors)
        except zipfile.BadZipFile:
            errors.append("handbook is not a valid DOCX/ZIP package")


def main() -> int:
    errors: list[str] = []
    validate_skills(errors)
    validate_links(errors)
    validate_example(errors)
    validate_docs(errors)

    if errors:
        print(f"Repository validation failed with {len(errors)} issue(s):")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository validation passed")
    print("- 6 expected skills discovered")
    print("- Markdown relative links resolve")
    print("- synthetic 21-file engagement workspace is valid")
    print("- Word handbook package is structurally valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
