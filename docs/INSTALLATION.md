# Installation Guide

This guide installs the private 1aifanatic/fde-agent-skills repository through the open skills CLI. The repository contains six independent skills that are discovered from their SKILL.md files.

## Fast path for Codex

### Prerequisites

Confirm these commands work:

~~~powershell
node --version
npx --version
git --version
gh --version
gh auth status
~~~

The GitHub account reported by gh auth status must have read access to the private repository.

### Install all skills globally

Use this for an FDE who wants the suite available in every Codex workspace:

~~~powershell
$env:DISABLE_TELEMETRY = "1"
npx --yes skills@latest add 1aifanatic/fde-agent-skills --skill '*' --agent codex --global --copy --yes
~~~

What each option means:

| Option | Effect |
| --- | --- |
| npx --yes | Downloads/runs the CLI package without the npm confirmation prompt |
| skills@latest | Uses the current released skills CLI |
| add 1aifanatic/fde-agent-skills | Reads the private GitHub repository |
| --skill '*' | Selects all six discovered skills |
| --agent codex | Installs only for Codex |
| --global | Installs for the current user rather than one project |
| --copy | Copies each skill instead of depending on symlink support |
| --yes | Skips interactive CLI confirmations |
| DISABLE_TELEMETRY | Disables skills CLI telemetry for this shell |

The global Codex destination is ~/.codex/skills/.

### Install into one project

Run from the project root:

~~~powershell
$env:DISABLE_TELEMETRY = "1"
npx --yes skills@latest add 1aifanatic/fde-agent-skills --skill '*' --agent codex --copy --yes
~~~

The project destination is .agents/skills/. Project installation is useful when the project should pin, review, and share the skill source with the delivery team.

### Reload Codex

Restart or reload Codex after installation so the new skill metadata is discovered. Start a fresh prompt with:

~~~text
$fde-run-engagement Start an FDE engagement and interview me to establish the charter.
~~~

## Private-repository authentication

The skills CLI supports private repositories by using existing Git, GitHub CLI, or SSH authentication.

### GitHub CLI authentication

Recommended on developer machines:

~~~powershell
gh auth login
gh auth status
gh repo view 1aifanatic/fde-agent-skills
~~~

Do not paste tokens into the install command. The CLI can use the authenticated GitHub CLI path without printing or copying the credential.

### SSH authentication

Use the SSH URL when SSH keys are already authorized:

~~~powershell
ssh -T git@github.com
$env:DISABLE_TELEMETRY = "1"
npx --yes skills@latest add git@github.com:1aifanatic/fde-agent-skills.git --skill '*' --agent codex --global --copy --yes
~~~

### Explicit environment token

For a CI worker that cannot use gh or SSH, supply a short-lived, least-privilege token through the secret manager:

~~~powershell
$env:GITHUB_TOKEN = $env:FDE_SKILLS_READ_TOKEN
$env:DISABLE_TELEMETRY = "1"
npx --yes skills@latest add 1aifanatic/fde-agent-skills --skill '*' --agent codex --copy --yes
Remove-Item Env:GITHUB_TOKEN
~~~

Never commit a token, place it in README output, or echo it in logs.

## Discover before installing

List what the CLI finds:

~~~powershell
$env:DISABLE_TELEMETRY = "1"
npx --yes skills@latest add 1aifanatic/fde-agent-skills --list
~~~

Expected skill names:

1. fde-capture-knowledge
2. fde-control-change
3. fde-interview-engagement
4. fde-plan-delivery
5. fde-reengineer-process
6. fde-run-engagement

The repository was smoke-tested with this command. The CLI found all six skills and copied their scripts, references, and metadata.

## Install selected skills

The suite is designed to work together, so installing all six is recommended. For an advanced, bounded use case:

~~~powershell
$env:DISABLE_TELEMETRY = "1"
npx --yes skills@latest add 1aifanatic/fde-agent-skills --skill fde-interview-engagement --skill fde-capture-knowledge --agent codex --global --copy --yes
~~~

Important dependency guidance:

- fde-run-engagement routes work to all five specialist skills.
- Specialist skills reference the orchestrator's shared taxonomy and workspace contract.
- Install all six unless you intentionally manage those dependencies another way.

## Verify installation

List global Codex skills:

~~~powershell
npx --yes skills@latest list --global --agent codex
~~~

Confirm the files directly if needed:

~~~powershell
Get-ChildItem "$env:USERPROFILE\.codex\skills" -Directory |
  Where-Object Name -Like "fde-*" |
  Select-Object Name
~~~

For a project install:

~~~powershell
Get-ChildItem ".\.agents\skills" -Directory |
  Where-Object Name -Like "fde-*" |
  Select-Object Name
~~~

Then invoke one skill in Codex. Discovery is complete when the skill appears and follows its workflow.

## Update

Update installed global skills:

~~~powershell
$env:DISABLE_TELEMETRY = "1"
npx --yes skills@latest update --global --yes
~~~

Update a project installation:

~~~powershell
$env:DISABLE_TELEMETRY = "1"
npx --yes skills@latest update --project --yes
~~~

If the repository later adds a new skill, rerun the original add command with --skill '*' because update refreshes already tracked skills and may not add a newly introduced skill.

## Remove

Remove the suite interactively:

~~~powershell
npx --yes skills@latest remove --global
~~~

Or name all six:

~~~powershell
npx --yes skills@latest remove --global fde-run-engagement fde-interview-engagement fde-capture-knowledge fde-reengineer-process fde-plan-delivery fde-control-change
~~~

Removal deletes installed skill packages. It should not delete a project's fde/ engagement workspace, but review the prompt and back up customer records according to your governance policy.

## Copy versus symlink

The CLI can install through a canonical copy plus symlinks or through independent copies.

- Use --copy for the most predictable Windows and enterprise installation.
- Use interactive symlink mode when a single local source of truth is valuable and symlinks are supported.
- Use project copy mode when the team wants installed files visible and reviewable inside the repository.

Updates should still be performed through the skills CLI so the source lock and installed copies remain consistent.

## Telemetry and private repositories

The upstream CLI documents that GitHub repository and skill identifiers are sent only when GitHub confirms the repository is public. This repository is private. This guide still sets DISABLE_TELEMETRY=1 as a conservative default.

Official sources:

- https://www.skills.sh/docs/cli
- https://github.com/vercel-labs/skills

## Troubleshooting

### Repository cannot be found

Check access independently:

~~~powershell
gh auth status
gh repo view 1aifanatic/fde-agent-skills
git ls-remote https://github.com/1aifanatic/fde-agent-skills.git
~~~

If HTTPS fails but SSH is configured, use the SSH installation command.

### No agent detected

Specify Codex explicitly:

~~~powershell
npx --yes skills@latest add 1aifanatic/fde-agent-skills --skill '*' --agent codex --copy --yes
~~~

### Skills installed but not visible

1. Confirm the destination contains all six directories.
2. Confirm every directory contains SKILL.md.
3. Restart or reload Codex.
4. Start a new turn and explicitly invoke $fde-run-engagement.
5. Check for another older skill directory with the same name.

### Scripts or references are missing

Install from the repository root and use the current skills CLI. The verified package contains the orchestrator's scripts and references as well as all SKILL.md files.

### Global install permission issue

Use project scope by omitting --global, or fix ownership of the user-level Codex skill directory. Do not run the installer as an administrator merely to bypass a path problem without understanding the effect.

### Symlink creation fails on Windows

Add --copy, as shown in the recommended command.

### Existing skill blocks installation

Review whether the existing directory contains user changes. Back it up, remove it intentionally through the CLI, and reinstall. Do not overwrite unknown local work silently.

### CI installation

Use a secret-managed read token, project scope, --copy, --yes, and disabled telemetry. Review the installed skill source during the build, and avoid persisting credentials in artifacts or logs.

## Manual fallback

If npx is unavailable, clone the repository with existing Git credentials and copy the six directories under skills/ into ~/.codex/skills/. Keep the six siblings together because specialist skills reference the orchestrator's shared resources through relative paths.

The npx path is preferred because it handles discovery, agent-specific destinations, installation scope, and updates consistently.
