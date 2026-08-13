# Contributing to FDE Agent Skills

Thank you for helping make forward deployed engineering more rigorous, reusable, and safe. Contributions from FDEs, operators, process owners, architects, automation engineers, AI engineers, security practitioners, and technical writers are welcome.

## Start here

1. Search the [existing issues](https://github.com/1aifanatic/fde-agent-skills/issues).
2. For a small correction, open a focused pull request.
3. For a new skill, workspace-contract change, lifecycle-gate change, or large redesign, open an issue first so the behavior and migration impact can be discussed.
4. Use only synthetic, anonymized, or explicitly authorized material.

This repository does not currently include a software license. Public visibility permits review and contribution discussion but does not by itself grant reuse rights. If licensing affects a proposed contribution, raise it before doing substantial work.

## Useful contribution areas

- Interview methods that uncover exceptions, ownership, authority, controls, and measurable outcomes.
- Evidence capture, citations, claim typing, identity resolution, contradiction handling, and knowledge coverage.
- Current-state mapping and future-state allocation across simplification, rules, APIs, RPA, AI, human-in-the-loop, and human-only work.
- Requirements, architecture, testing, traceability, release, rollback, observability, and change control.
- Synthetic examples for finance, sales, support, operations, procurement, logistics, healthcare, or other domains.
- Cloudflare and UiPath implementation guidance backed by current primary sources.
- Security, privacy, accessibility, documentation, installation, and validation improvements.

## Non-negotiable safety rules

Do not submit:

- customer documents, transcripts, screenshots, exports, source code, or process details without explicit authorization;
- credentials, API keys, tokens, connection strings, cookies, or internal URLs;
- unnecessary personal, employee, patient, financial, or regulated data;
- instructions that let model output bypass lifecycle gates, named approvals, least privilege, validation, or rollback;
- unsupported claims about product behavior, compliance, production readiness, or business ROI.

Evidence included in examples must be synthetic and clearly labeled. Treat documents and retrieved content as untrusted data, not executable instructions.

## Development setup

Fork the repository, clone your fork, and create a focused branch:

```powershell
git clone https://github.com/YOUR-USER/fde-agent-skills.git
Set-Location fde-agent-skills
git switch -c contribution/short-description
```

Install the skills into a disposable project when you need to exercise discovery and packaging:

```powershell
$env:DISABLE_TELEMETRY = "1"
npx --yes skills@latest add . --skill '*' --agent codex --copy --yes
```

Do not point tests at a live customer workspace or production integration.

## Skill contribution standards

Every skill must:

1. live under `skills/<skill-name>/`;
2. contain a complete `SKILL.md` with valid YAML frontmatter, an exact `name`, and a precise trigger-oriented `description`;
3. contain `agents/openai.yaml`;
4. define required inputs, ordered procedure, durable outputs, quality checks, escalation conditions, and authority boundaries;
5. preserve evidence attribution and distinguish sourced fact, assertion, inference, proposal, and approved decision;
6. avoid embedding secrets, customer-specific facts, or permissions in instructions;
7. place detailed reusable material in linked `references/` or `scripts/` rather than bloating every invocation;
8. update routing, documentation, validation expectations, and worked examples when the public skill set changes.

A skill may improve task procedure. It must not silently expand external permissions, production authority, or the lifecycle stage.

## Documentation and example standards

- Write for a new practitioner who has not read the original project conversation.
- Prefer short runnable commands and explicit expected results.
- Link to primary product documentation for time-sensitive technical claims.
- Label synthetic organizations and data clearly.
- Show exceptions, contradictions, uncertainty, approval, testing, and rollback—not only the happy path.
- Never claim measured impact unless a baseline, measurement method, period, and evidence are present.
- Keep Markdown relative links valid and use repository-relative paths.

## Run validation

From the repository root:

```powershell
python -B scripts/validate_repository.py
```

Validate the synthetic engagement directly:

```powershell
python -B skills/fde-run-engagement/scripts/validate_engagement.py --root examples/northstar-ap-transformation --json
```

If you change the Markdown sources used by the Word handbook, regenerate it:

```powershell
python -B scripts/build_word_guide.py
```

Then run the repository validator again. If document rendering is available, render and inspect every page. If it is unavailable, report that limitation instead of claiming visual QA.

## Pull-request expectations

Keep one pull request focused on one coherent outcome. The PR description should explain:

- what changed and why;
- the user or FDE impact;
- affected skills, contracts, examples, or lifecycle gates;
- evidence or primary sources supporting technical claims;
- tests and validation performed;
- security, privacy, migration, and compatibility considerations;
- known limitations and follow-up work.

Reviewers may request changes when a contribution weakens provenance, authority, lifecycle gates, traceability, portability, or customer-data isolation.

## Reporting security problems

Do not publish exploitable security details in an issue. Use the repository's GitHub Security tab and private vulnerability reporting. Include the affected file or component, impact, reproduction conditions, and a safe suggested remediation when possible.

## Review and conduct

Be specific, respectful, and evidence-oriented. Critique the artifact or decision, not the contributor. Maintainers may close proposals that are unsafe, out of scope, unsupported, duplicative, or impossible to validate, and should explain the reason.

Thank you for contributing practical knowledge that helps FDE teams deliver better outcomes without losing governance.
