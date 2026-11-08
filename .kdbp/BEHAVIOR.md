---
name: tiptally
domain: Split a restaurant bill and its tip fairly among people, to the cent
maturity: mvp
project_type: code
tech: python
created: 2026-11-07
# proof_root: the committed evidence folder evidence-freshness measures — empty = none (the project keeps no runtime-evidence folder)
proof_root:
---

# Project Behavior — tiptally

<!-- The per-project binding file: identity + the commands the gates trust. Written at /gabe-init,
     edited by the HUMAN when the project's tooling changes. Gates NEVER guess a command — they
     bind here first (gate-spec Step 2.0), then package manifests, then language fallbacks. -->

## Verify Commands

<!-- The commands the commit gate and execute's task verification RUN. Author them to your real
     tooling; a checker that cannot fail is non-evidence. -->

- lint: `ruff check tiptally tests`
<!-- types: none — no type checker on this machine (mypy and pyright are absent); left EMPTY on purpose. -->
- types:
- tests: `python3 -m pytest tests -q`
<!-- results_out: not set — the tests command above emits no machine report. To opt in, author a
     reporter flag into the tests command (e.g. --junitxml=tests/results/junit.xml) and add
     `- results_out: tests/results/junit.xml` here; absent, the center renders ⤫ skipped(no reporter). -->

## Critical Paths

<!-- Globs whose changes are hotfix-sensitive: ad-hoc work touching them inherits `proof: test`
     (evidence-doctrine) — a failing-then-passing test, not just a green suite. One glob per line. -->

- `tiptally/split.py`

## Notes

<!-- Anything a session must know before running commands here (env quirks, service deps). -->

- No type checker is installed on this machine (mypy and pyright are absent), so `types` is unbound. Bind it here once one is installed.

# Project Behavior Rules

## B1 — Inventory before proposing (architecture / exploratory questions)

**Trigger phrases:** "can we work on", "should we", "I'm wondering", "explore the possibility", "what do you think about", "how can we approach", "is it possible to". Treat as diagnose-prompts, not build-prompts.

**Mandatory inventory before any proposal:**
1. Read existing project state: `mcp__gabe-kdbp__kdbp_snapshot` FIRST where a server answers (branch · PLAN phase-table states · open PENDING · last LEDGER rows, under 1k tokens) to orient, then the files it does not carry — `.kdbp/PLAN.md` (the phase DETAILS and per-phase records the snapshot summarizes but does not quote), `.kdbp/SCOPE.md` (the phase arc lives in its §Phases), `.kdbp/STRUCTURE.md`, `.kdbp/AUDIT.md` (if present). No server or no `.kdbp/` → read all four as before.
2. Read suite skill(s) being extended: `~/.claude/skills/gabe-*/SKILL.md`
3. Read relevant catalog: `~/.claude/templates/gabe/tier-sections/*.md`
4. If proposing external dep: clone repo, verify license + actual surface (not just README)
5. List what already exists for this question before proposing what's missing — where the project has a command center, `mcp__gabe-map__find` (by name or doc, across entities/endpoints/models/functions/screens) and `mcp__gabe-map__center_overview` (the entity estate in ≤600 tokens) name what is already there; the map is a FLOOR, so `grep -rn` still settles absence

**Proactive suggestions on detection:**
- Suggest user run `/plan` (your `feedback_plan_overrides_auto` rule then enforces wait-for-confirm)
- Offer `/gabe-roast [perspective]` or `/gabe-assess` for adversarial first-pass before plan-text
- If auto-mode active, override it for exploratory Qs — surface inventory + recommendation, wait for user direction

**Self-check before delivery:** "Did I read existing state? Did the user already do this analysis? Am I proposing what already exists under a new name? Did I challenge my first framing?"

**Caveman/terse modes compress output prose only. Reasoning depth is invariant.**

**Why this rule exists:** Past incident (2026-04-24, gastify mockup workflow Q) where shallow first-pass restated work the user had already done in `.kdbp/PLAN.md` + `AUDIT.md` + `STRESS-TEST-SPEC.md`. User flagged as workflow-sustainability concern.
