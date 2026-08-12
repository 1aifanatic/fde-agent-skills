---
name: fde-interview-engagement
description: Interview an FDE, process owner, technical SME, control owner, or delivery team to discover the knowledge an engagement requires. Use for project intake, process discovery, stakeholder interviews, unclear requirements, exception discovery, pre-design gap audits, or when an FDE needs a prioritized knowledge-acquisition plan rather than a generic questionnaire.
---

# Interview an FDE Engagement

Run a progressive interview that discovers decisions and missing knowledge without asking for facts already available in evidence.

## Prepare

1. If an `fde/` workspace exists, read its charter, status, evidence index, stakeholders, knowledge needs, contradictions, and decisions.
2. Read `../fde-run-engagement/references/knowledge-taxonomy.md` and `../fde-run-engagement/references/workspace-contract.md`.
3. Inspect available documents, notes, diagrams, code, and systems before asking questions.
4. Select the interview lens:
   - FDE intake and engagement framing;
   - business process owner;
   - process performer/exception handler;
   - application/data SME;
   - risk, security, or control owner;
   - operations/support owner.
5. Convert gaps into a dependency tree: ask only decisions whose prerequisites are already settled.

**Completion criterion:** Every planned question closes a named knowledge gap or unlocks a blocked decision.

## Interview in rounds

Ask the full current frontier in one round, normally 4-8 questions. Format each question:

```text
QUESTION Q1 - Title: Decision or knowledge question, with concrete choices where useful.

RECOMMENDATION: your recommended answer and why.
UNLOCKS: the downstream decision or artifact this answer enables.
```

Wait for answers before computing the next frontier. After each round:

1. separate facts, claims, decisions, assumptions, and preferences;
2. record source and speaker;
3. identify contradictions and ambiguous identities;
4. update answered and newly discovered knowledge needs;
5. recompute the frontier.

Find environmental facts yourself through authorized read-only inspection. Ask the human for decisions, authority, lived exceptions, unwritten work, and evidence you cannot access.

## Probe beyond the golden path

For every process or solution claim, ask:

- What triggers it and what proves completion?
- Who performs, owns, approves, and supports it?
- What inputs, systems, credentials, and data are required?
- What happens when information is missing, late, duplicated, or contradictory?
- Who receives the failure and what do they actually do?
- Which manual workaround is absent from the documented procedure?
- What control must never be bypassed?
- What volume, cycle time, error rate, SLA, and rework exist today?
- What change would users reject even if technically efficient?
- What evidence would make the process owner approve the future state?

Use the complete taxonomy to audit coverage; do not mechanically ask every question.

## Maintain the knowledge plan

For every unresolved item, update `fde/knowledge/knowledge-needs.md` with:

```text
ID | category | question/claim | status | evidence | owner/source |
needed by stage | blocked decision | risk if unknown | next action | last verified
```

Allowed status values: `unknown`, `stated`, `evidenced`, `contradicted`, `confirmed`, `approved`, `stale`, `not-applicable`.

Update stakeholder, glossary, contradiction, decision, risk, and approval files when answers affect them.

**Completion criterion:** Every high-impact branch is either evidenced, decided, explicitly contradicted, or assigned to an owner with a due stage.

## Finish

Return:

- knowledge coverage by taxonomy category;
- decisions settled;
- critical exceptions discovered;
- contradictions requiring resolution;
- evidence still required;
- owners and next interview lens;
- lifecycle gates now unblocked.

Do not declare discovery complete because the question list is empty; declare it complete when every gate-critical knowledge item has a disposition.
