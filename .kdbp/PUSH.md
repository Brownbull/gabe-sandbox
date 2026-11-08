# Push Configuration

Managed by `/gabe-push`. First run writes this file; every run after reads it.
Edit values directly or rerun `/gabe-push --reconfigure` to redo the interview.

## Defaults

| Setting | Value |
|---------|-------|
| remote | origin |
| default_env | staging |
| pr_template | none |

## Notes

- **Setup 2026-11-08:** deploy pattern [2] staging-then-prod; CI github-actions (`.github/workflows/ci.yml`); default_env staging, so production is named on purpose (`/gabe-push production`).

## Environments

<!-- One block per env. `/gabe-push <name>` targets the env named below. -->
<!-- `/gabe-push` (no arg) targets default_env. -->

### staging

| Setting | Value |
|---------|-------|
| target_branch | staging |
| promote_from | — |
| ci | github-actions |
| branch_cleanup | never |

### production

| Setting | Value |
|---------|-------|
| target_branch | main |
| promote_from | staging |
| promotion_mode | direct |
| ci | github-actions |
| branch_cleanup | ask |

## Remote branch policy

| Setting | Value |
|---------|-------|
| known_branches | main, staging |
| on_extra | prompt |

## Decisions log

| Branch | Action | Decided | Notes |
|--------|--------|---------|-------|
