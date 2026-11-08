"""Command-line interface: ``python3 -m tiptally 120.50 4 --tip 10``."""

import argparse
from decimal import Decimal, InvalidOperation

from tiptally.split import split_even, split_weighted


def parse_amount(text: str) -> int:
    """Parse a decimal amount such as ``120.50`` into whole cents."""
    try:
        value = Decimal(text)
    except InvalidOperation:
        raise ValueError(f"not a valid amount: {text!r}") from None
    if not value.is_finite() or value < 0:
        raise ValueError(f"amount must be a non-negative number: {text!r}")
    cents = value * 100
    if cents != cents.to_integral_value():
        raise ValueError(f"amount has more than two decimals: {text!r}")
    return int(cents)


def format_amount(cents: int) -> str:
    """Format whole cents as ``units.cc``."""
    units, rest = divmod(cents, 100)
    return f"{units}.{rest:02d}"


def parse_weights(text: str) -> list[int]:
    """Parse ``2,1,1`` into ``[2, 1, 1]``."""
    try:
        return [int(part) for part in text.split(",")]
    except ValueError:
        raise ValueError(f"weights must be whole numbers separated by commas: {text!r}") from None


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="tiptally",
        description="Split a restaurant bill and its tip among people, to the cent.",
    )
    parser.add_argument("amount", help="bill total before tip, for example 120.50")
    parser.add_argument("people", type=int, help="how many people share the bill")
    parser.add_argument(
        "--tip", type=int, default=0, metavar="PCT", help="tip percentage (default: 0)"
    )
    parser.add_argument(
        "--weights",
        metavar="W1,W2,...",
        help="split in proportion to these whole-number weights, one per person (e.g. 2,1,1)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        total_cents = parse_amount(args.amount)
        if args.weights is None:
            shares = split_even(total_cents, args.people, args.tip)
        else:
            weights = parse_weights(args.weights)
            if len(weights) != args.people:
                raise ValueError(f"expected {args.people} weights, got {len(weights)}")
            shares = split_weighted(total_cents, weights, args.tip)
    except ValueError as exc:
        parser.error(str(exc))
    for number, share in enumerate(shares, start=1):
        print(f"Person {number}: {format_amount(share)}")
    grand_total = sum(shares)
    print(f"Total: {format_amount(grand_total)} (tip {format_amount(grand_total - total_cents)})")
    return 0
