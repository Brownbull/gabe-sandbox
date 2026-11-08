# Design

## Money is integer cents

Every amount inside `tiptally.split` is an `int` count of cents. Floats never appear.
The command line parses amounts with `Decimal` and converts to cents at the edge
(`tiptally/cli.py`), refusing anything with more than two decimals.

## The tip

`tip = total * tip_pct / 100`, rounded **half up** to the cent. With integers:

```
tip_cents = (total_cents * tip_pct + 50) // 100
```

`10%` of `1005` cents is `100.5`, which becomes `101`. Rounding is on the tip as a whole,
not on each person's share, so the tip is the same however many people split it.

## The shares

The grand total is `total_cents + tip_cents`. It is divided with `divmod(grand_total, people)`
into a base share and a leftover of `0 <= leftover < people` cents. The first `leftover`
payers pay one cent more than the base share, so:

- the shares add up exactly to the grand total, nothing is lost or invented;
- no two shares differ by more than one cent;
- the order is stable: Person 1 always pays the extra cent first.

Example: `12050` cents with a 10% tip is `13255`; `13255 = 4 * 3313 + 3`, so the shares are
`3314, 3314, 3314, 3313`.

### Weighted shares

`split_weighted(total_cents, weights, tip_pct)` uses the same tip and the same grand total.
Each payer's exact share is `grand_total * weight / sum(weights)`. Every share is rounded
down, and the cents left over go one each to the payers whose exact share lost the most to the
rounding (largest remainder); on a tie the earlier payer wins. The remainder is compared as an
integer, `grand_total * weight % sum(weights)`, so there is no float comparison.

With equal weights every remainder is equal, the tie rule gives the extra cents to the first
payers, and the result is identical to `split_even`.

Example: `100` cents split `1:2` is `33.33` and `66.67`; the second payer lost more, so the shares
are `33, 67`.
