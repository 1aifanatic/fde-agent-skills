# Runbook

## Deploy and configure

1. Confirm exact approved baseline, release candidate, owners, and environment.
2. Validate mailbox, queue, LedgerOne, model endpoint, least-privilege access, and secrets through official platform owners.
3. Load the approved owner matrix, confidence threshold, policy rules, model version, retention settings, alerts, and rollback configuration.
4. Run deterministic, integration, AI evaluation, security, recovery, and UAT gates.
5. Start with a 10-case canary. Keep manual processing available and prohibit autonomous payment approval.
6. Record release version, approvals, configuration hashes, test evidence, and effective time.

No deployment has occurred in this synthetic example.

## Monitor and support

- Priya owns technical monitoring; Mira owns process outcomes; Sam owns control exceptions.
- Reconcile mailbox intake, active tasks, dead-letter queue, and LedgerOne statuses.
- Alert ingestion or routing failure within 10 minutes.
- Monitor cycle time, queue age, owner accuracy, classifier confidence, correction rate, reopen rate, duplicate holds, control bypass attempts, and manual triage effort.
- Review classifier corrections weekly during pilot and approve any threshold/model change through change control.
- Keep all customer and invoice content subject to approved data handling and retention.

## Recover and roll back

1. Stop new automated routing and LedgerOne writes.
2. Reconcile actual state before retrying any ambiguous operation.
3. Move unresolved cases to the manual triage queue with source evidence intact.
4. Restore the prior routing mailbox and configuration.
5. Verify no case loss, duplicate task, duplicate write, or approval bypass.
6. Record incident, affected case IDs, recovery evidence, owner, and decision to resume.

Rollback triggers include any control bypass, unauthorized access, unexplained reconciliation difference, case loss, critical duplicate false clearance, or sustained queue delay above the approved threshold.

## Retain and delete data

- Retain approved exception evidence and decision logs according to the synthetic seven-year control requirement.
- Keep model prompts/logs data-minimized and within the approved endpoint and retention boundary.
- Use de-identified fixtures for evaluation.
- Delete temporary evaluation exports after approved test evidence is captured.
- Never place credentials, tokens, bank details, or unnecessary personal data in the Markdown workspace.
