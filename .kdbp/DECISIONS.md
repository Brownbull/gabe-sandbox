# Architecture Decisions

| # | Date | Decision | Rationale | Alternatives Considered | Status | Review Trigger |
|---|------|----------|-----------|------------------------|--------|----------------|
| D1 | YYYY-MM-DD | [decision] | [why] | [what else was considered] | active | [when to revisit] |

<!-- Status: active / superseded / revisit -->
<!-- BEHAVIOR.md constraints reference decision IDs: "All integrations mocked (ref D1)" -->

## D2 — Phase 1 tier: mvp (2026-11-07)

**Phase:** Even split
**Types:** core-only
**Tier chosen:** mvp
**Prototype:** no
**Reason:** default MVP pick per U2

### Sections rendered
- Core (always)

### Dimensions suppressed (Layer 2 filter)
- none (Core is never filtered)

### Per-dim tier overrides (if any)

```yaml
dim_overrides: []
```

### Δ deferred by tier choice
- Core: Testing edges+fuzz, typed errors with retry, structured logging, interfaces — deferred to a later tier

### Review trigger (when to escalate this phase)
- when the tool is used by a second program rather than from the command line

### Status
- accepted

## D3 — Phase 2 tier: mvp (2026-11-07)

**Phase:** Weighted split
**Types:** core-only
**Tier chosen:** mvp
**Prototype:** no
**Reason:** default MVP pick per U2

### Sections rendered
- Core (always)

### Dimensions suppressed (Layer 2 filter)
- none (Core is never filtered)

### Per-dim tier overrides (if any)

```yaml
dim_overrides: []
```

### Δ deferred by tier choice
- Core: same deferrals as D2

### Review trigger (when to escalate this phase)
- when weights come from outside the process (a file or a service)

### Status
- accepted

## D4 — Phase 3 tier: mvp (2026-11-07)

**Phase:** Currencies by minor unit
**Types:** core-only
**Tier chosen:** mvp
**Prototype:** no
**Reason:** default MVP pick per U2

### Sections rendered
- Core (always)

### Dimensions suppressed (Layer 2 filter)
- none (Core is never filtered)

### Per-dim tier overrides (if any)

```yaml
dim_overrides: []
```

### Δ deferred by tier choice
- Core: same deferrals as D2; a full ISO 4217 table is out of scope (ten currencies only)

### Review trigger (when to escalate this phase)
- when a currency outside the ten is requested

### Status
- accepted
