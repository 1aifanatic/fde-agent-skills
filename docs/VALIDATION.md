# Validation and Reproducibility

This repository is designed to be independently inspected and reproduced. The checks below distinguish structure, installation, example behavior, document integrity, and production claims.

## One-command repository check

From the repository root:

~~~powershell
python -B .\scripts\validate_repository.py
~~~

Expected result:

~~~text
Repository validation passed
- 6 expected skills discovered
- Markdown relative links resolve
- synthetic 21-file engagement workspace is valid
- Word handbook package is structurally valid
~~~

The validator checks:

- the exact six skill directories and metadata files;
- skill frontmatter names and descriptions;
- all relative links in README, docs, and examples;
- the worked example through the orchestrator validator;
- five synthetic source inputs plus execution and impact logs;
- the Word handbook as an uncorrupted Office Open XML package.

## Skill validation

Run the Codex skill-creator validator against every skill:

~~~powershell
$validator = "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py"
Get-ChildItem -LiteralPath .\skills -Directory | Sort-Object Name | ForEach-Object {
  python $validator $_.FullName
}
~~~

Expected result: each of the six skills reports Skill is valid!.

## Public npx installation smoke test

### Tested environment

- Date: August 12, 2026
- Platform: Windows
- Node: v24.18.0
- npm: 11.8.0
- skills CLI: 1.5.22
- Repository: public 1aifanatic/fde-agent-skills
- Authentication: none required for HTTPS installation
- Telemetry: disabled
- Installation scope: isolated temporary project
- Target agent: Codex
- Method: copy

### Discovery command

~~~powershell
$env:DISABLE_TELEMETRY = "1"
npx --yes skills@latest add https://github.com/1aifanatic/fde-agent-skills.git --list
~~~

Observed result: the CLI cloned the repository and found exactly six skills.

### Installation command

~~~powershell
$env:DISABLE_TELEMETRY = "1"
npx --yes skills@latest add https://github.com/1aifanatic/fde-agent-skills.git --skill '*' --agent codex --copy --yes
~~~

Observed result: six skills installed under .agents/skills/. The installed tree included:

- all six SKILL.md files;
- all six agents/openai.yaml files;
- fde-run-engagement reference files;
- fde-run-engagement initialization and validation scripts.

This proves repository discovery and project-scope copy installation. The documented --global option is upstream CLI behavior and changes only the installation scope.

## Worked example validation

Run:

~~~powershell
python -B .\skills\fde-run-engagement\scripts\validate_engagement.py --root .\examples\northstar-ap-transformation --json
~~~

Observed result:

~~~json
{
  "valid": true,
  "issues": []
}
~~~

The example contains the 21 required workspace files and runs all six skill responsibilities:

1. engagement orchestration;
2. gap-driven interview;
3. source normalization and contradiction reconciliation;
4. current/future process redesign and allocation;
5. delivery planning and traceability;
6. post-baseline change control.

Review [the execution log](../examples/northstar-ap-transformation/run-log.md) to see the inputs, actions, outputs, and limitations for each skill.

## Word handbook generation

Build the handbook:

~~~powershell
python -B .\scripts\build_word_guide.py
~~~

Output:

~~~text
docs/FDE_AGENT_SKILLS_HANDBOOK.docx
~~~

The builder reads the maintained Markdown documentation and worked-example summaries, applies a compact reference-guide design, creates real heading styles and list styles, uses fixed Word table geometry, adds navigation-friendly hierarchy, and writes document metadata.

### Structural audits performed

The generated handbook passed:

- DOCX ZIP/package integrity;
- python-docx reopen;
- one-section US Letter portrait geometry;
- one-inch margins;
- heading hierarchy audit with no level jumps;
- accessibility audit with zero high, medium, or low findings;
- exact table geometry for all eight tables;
- matching table width, indent, grid, and cell widths;
- no fixed row heights;
- source link and document-part checks.

The table-geometry audit reported 9360 DXA width and matching grid/cell totals for every table.

### Visual-render limitation

The environment did not have LibreOffice or pdftoppm. Two hidden Microsoft Word automation exports timed out without producing a PDF, so a page-image render review could not be completed. The Word processes created by those attempts were terminated after the timeout, and the handbook was rebuilt and structurally re-audited.

The document should receive a final human visual review in Microsoft Word before external distribution. This repository does not claim that a PNG render gate passed.

## Credential and privacy scan

Before publishing, scan for common credential patterns:

~~~powershell
rg -n --hidden --glob '!.git/**' --pcre2 "gho_[A-Za-z0-9]+|ghp_[A-Za-z0-9]+|github_pat_[A-Za-z0-9_]+|sk-[A-Za-z0-9_-]{20,}|BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY" .
~~~

Expected result: no matches.

The synthetic example uses example-domain email addresses and fictional identities. A live root-level fde/ workspace is ignored by Git to reduce accidental customer-evidence commits.

## What these validations do not prove

They do not prove:

- model accuracy on real customer data;
- compatibility with a particular ERP, CRM, or UiPath tenant;
- security, privacy, or regulatory approval;
- implementation, UAT, release, production operation, or ROI;
- correctness of evidence supplied by a customer.

Those claims require engagement-specific evidence and the named human approval gates.

## Release checklist

Before publishing a change to this repository:

1. Run all six quick validators.
2. Run scripts/validate_repository.py.
3. Validate the worked example.
4. Rebuild the Word handbook after documentation changes.
5. Run the Word structural and accessibility audits.
6. Run the credential scan.
7. Inspect git diff and staged scope.
8. Commit and push intentionally.
9. Verify the remote branch and commit hash.
