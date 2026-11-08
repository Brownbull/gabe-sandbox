# Active Plan

<!-- status: active -->
<!-- project_type: code -->

## Goal

Weighted splits and currencies without cents

## Context

- **Maturity:** mvp
- **Domain:** Split a restaurant bill and its tip fairly among people, to the cent
- **Created:** 2026-11-07
- **Last Updated:** 2026-11-07

## Phases

| # | Phase | Description | Types | Tier | Complexity | Exec | Review | Commit | Push |
|---|-------|-------------|-------|------|------------|------|--------|--------|------|
| 1 | Even split | Split a bill and its tip evenly, to the cent (what the base already ships) | core-only | mvp | low | ✅ | ✅ | ✅ | ✅ |
| 2 | Weighted split | `split_weighted(total_cents, weights, tip_pct)` and a `--weights 2,1,1` flag, with tests and README | core-only | mvp | med | ⬜ | ⬜ | ⬜ | ⬜ |
| 3 | Currencies by minor unit | 0-decimal (JPY, CLP, KRW, ISK, VND) and 3-decimal (KWD, BHD, OMR, JOD, TND) currencies through a `--currency` flag | core-only | mvp | med | ⬜ | ⬜ | ⬜ | ⬜ |

<!-- Exec is written by /gabe-execute: ⬜ not started, 🔄 in progress, ✅ complete -->
<!-- Review/Commit/Push auto-ticked by /gabe-review, /gabe-commit, /gabe-push -->
<!-- A phase is complete when all status columns are ✅ -->
<!-- /gabe-next routes to the next command based on column state (Exec → Review → Commit → Push → advance phase) -->
<!-- Tier column values: mvp | ent | scale. Read by /gabe-execute (tier-cap) and /gabe-review (TIER_DRIFT finding). -->
<!-- Manual override is fine — edit cells by hand any time (then /gabe-plan update regenerates the PLAN.json mirror) -->

## Phase Details

### Phase 1 — Even split
- **Types:** `core-only`
- **Tier:** mvp
- **Prototype:** no
- **Scope:** tiptally/split.py, tiptally/cli.py, tests/test_split.py, tests/test_cli.py
- **References:** none (first phase)
- **Acceptance:** `python3 -m tiptally 120.50 4 --tip 10` prints four shares and a total that add up to 132.55
- **Checkpoint:** ruff check tiptally tests && python3 -m pytest tests -q
- **Sections considered:** Core
- **Suppressed dimensions:** none (Core is never filtered)
- **Trade-offs accepted:** See DECISIONS.md D2

```yaml
phase: 1
types: [core-only]
phase_tier: mvp
prototype: false
dim_overrides: []
sections_considered: [Core]
suppressed_dims_count: 0
decisions_entry: D2
```

### Phase 2 — Weighted split
- **Types:** `core-only`
- **Tier:** mvp
- **Prototype:** no
- **Scope:** tiptally/split.py, tiptally/cli.py, tests/test_split.py, tests/test_cli.py, README.md
- **References:** `split_even` in tiptally/split.py (same tip rounding and leftover-cent rule); docs/design.md
- **Acceptance:** `python3 -m tiptally 100 3 --tip 10 --weights 2,1,1` prints shares proportional to 2:1:1 that add up to the bill plus tip
- **Checkpoint:** ruff check tiptally tests && python3 -m pytest tests -q
- **Sections considered:** Core
- **Suppressed dimensions:** none (Core is never filtered)
- **Trade-offs accepted:** See DECISIONS.md D3

```yaml
phase: 2
types: [core-only]
phase_tier: mvp
prototype: false
dim_overrides: []
sections_considered: [Core]
suppressed_dims_count: 0
decisions_entry: D3
```

### Phase 3 — Currencies by minor unit
- **Types:** `core-only`
- **Tier:** mvp
- **Prototype:** no
- **Scope:** tiptally/currencies.py, tiptally/split.py, tiptally/cli.py, tests/test_vectors.py, README.md, docs/design.md
- **References:** `split_even` / `split_weighted` in tiptally/split.py; `parse_amount` / `format_amount` in tiptally/cli.py
- **Acceptance:** `python3 -m tiptally 12500 4 --currency JPY` prints whole-yen shares; `--currency KWD` accepts and prints three decimals
- **Checkpoint:** ruff check tiptally tests && python3 -m pytest tests -q
- **Sections considered:** Core
- **Suppressed dimensions:** none (Core is never filtered)
- **Trade-offs accepted:** See DECISIONS.md D4

```yaml
phase: 3
types: [core-only]
phase_tier: mvp
prototype: false
dim_overrides: []
sections_considered: [Core]
suppressed_dims_count: 0
decisions_entry: D4
```

## Current Phase

Phase 1: Even split

## Dependencies

- Phase 2 depends on phase 1 (reuses the tip rounding and the leftover-cent rule).
- Phase 3 depends on phases 1 and 2 (both split functions take the minor unit).

## Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| Weighted shares drift from the even rule when weights are equal | medium | Test that equal weights match `split_even` |
| A wrong minor unit for a currency silently mis-scales every amount | high | Table of the ten currencies checked against ISO 4217; vector tests per currency |

## Notes

All three phases are tier mvp (default pick per U2). Phase 1 is already shipped in the base repo; its Exec/Review/Commit/Push cells were ticked by hand and the PLAN.json mirror regenerated with `scripts/regen-mirror.py`.

## Review Artifacts

- HTML review artifact: none — simple plan / small routine change with no complex decision surface
- Canonical source: `.kdbp/PLAN.md`, `.kdbp/DECISIONS.md`, `.kdbp/LEDGER.md`

## Runtime Evidence Checkpoints

- None: no user-facing runtime phase types (CLI output is covered by tests/test_cli.py).
