"""Splitting logic. All amounts are integer cents; no floats anywhere."""


def split_even(total_cents: int, people: int, tip_pct: int) -> list[int]:
    """Split a bill plus tip evenly, to the cent.

    The tip is ``total_cents * tip_pct / 100`` rounded half up to the cent. The shares
    add up exactly to ``total_cents + tip``; the cents that do not divide evenly go to
    the first payers, one each.
    """
    if total_cents < 0:
        raise ValueError("total must not be negative")
    if tip_pct < 0:
        raise ValueError("tip percentage must not be negative")
    tip_cents = (total_cents * tip_pct + 50) // 100
    grand_total = total_cents + tip_cents
    base, leftover = divmod(grand_total, people)
    return [base + 1 if i < leftover else base for i in range(people)]
