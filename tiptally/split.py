"""Splitting logic. All amounts are integer cents; no floats anywhere."""


def _tip_cents(total_cents: int, tip_pct: int) -> int:
    """Tip on a bill, rounded half up to the cent."""
    if total_cents < 0:
        raise ValueError("total must not be negative")
    if tip_pct < 0:
        raise ValueError("tip percentage must not be negative")
    return (total_cents * tip_pct + 50) // 100


def split_even(total_cents: int, people: int, tip_pct: int) -> list[int]:
    """Split a bill plus tip evenly, to the cent.

    The tip is ``total_cents * tip_pct / 100`` rounded half up to the cent. The shares
    add up exactly to ``total_cents + tip``; the cents that do not divide evenly go to
    the first payers, one each.
    """
    tip_cents = _tip_cents(total_cents, tip_pct)
    grand_total = total_cents + tip_cents
    base, leftover = divmod(grand_total, people)
    return [base + 1 if i < leftover else base for i in range(people)]


def split_weighted(total_cents: int, weights: list[int], tip_pct: int) -> list[int]:
    """Split a bill plus tip in proportion to whole-number weights, to the cent.

    Each payer owes ``grand_total * weight / sum(weights)``, rounded down; the cents
    left over go one each to the payers whose exact share lost the most to rounding
    (largest remainder), earlier payers first on a tie. The shares add up exactly to
    ``total_cents + tip``. With equal weights this is the same as ``split_even``.
    """
    if not weights:
        raise ValueError("weights must not be empty")
    if any(weight < 1 for weight in weights):
        raise ValueError("weights must be whole numbers of at least 1")
    grand_total = total_cents + _tip_cents(total_cents, tip_pct)
    weight_sum = sum(weights)
    shares = [grand_total * weight // weight_sum for weight in weights]
    leftover = grand_total - sum(shares)
    by_lost_cents = sorted(
        range(len(weights)), key=lambda i: (-(grand_total * weights[i] % weight_sum), i)
    )
    for i in by_lost_cents[:leftover]:
        shares[i] += 1
    return shares
