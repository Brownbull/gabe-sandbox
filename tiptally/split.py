"""Splitting logic. All amounts are integer minor units (cents); no floats anywhere."""

MAX_MINOR_UNIT = 3


def _check_minor_unit(minor_unit: int) -> None:
    if not 0 <= minor_unit <= MAX_MINOR_UNIT:
        raise ValueError(f"minor unit must be between 0 and {MAX_MINOR_UNIT}")


def _tip_cents(total_cents: int, tip_pct: int) -> int:
    """Tip on a bill, rounded half up to the cent."""
    if total_cents < 0:
        raise ValueError("total must not be negative")
    if tip_pct < 0:
        raise ValueError("tip percentage must not be negative")
    return (total_cents * tip_pct + 50) // 100


def split_even(total_cents: int, people: int, tip_pct: int, minor_unit: int = 2) -> list[int]:
    """Split a bill plus tip evenly, to the smallest unit of the currency.

    ``total_cents`` counts minor units: cents for a 2-decimal currency, whole yen for JPY
    (``minor_unit=0``), fils for KWD (``minor_unit=3``).

    The tip is ``total_cents * tip_pct / 100`` rounded half up to the cent. The shares
    add up exactly to ``total_cents + tip``; the cents that do not divide evenly go to
    the first payers, one each.
    """
    _check_minor_unit(minor_unit)
    tip_cents = _tip_cents(total_cents, tip_pct)
    grand_total = total_cents + tip_cents
    base, leftover = divmod(grand_total, people)
    return [base + 1 if i < leftover else base for i in range(people)]


def split_weighted(
    total_cents: int, weights: list[int], tip_pct: int, minor_unit: int = 2
) -> list[int]:
    """Split a bill plus tip in proportion to whole-number weights, to the smallest unit.

    ``total_cents`` counts minor units, as in ``split_even``.

    Each payer owes ``grand_total * weight / sum(weights)``, rounded down; the cents
    left over go one each to the payers whose exact share lost the most to rounding
    (largest remainder), earlier payers first on a tie. The shares add up exactly to
    ``total_cents + tip``. With equal weights this is the same as ``split_even``.
    """
    _check_minor_unit(minor_unit)
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
