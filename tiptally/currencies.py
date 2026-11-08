"""Minor units (digits after the decimal point) of the currencies tiptally knows.

Source: ISO 4217. Amounts inside tiptally are integer counts of the minor unit:
1 JPY is 1, 1 KWD is 1000 fils.
"""

MINOR_UNITS: dict[str, int] = {
    # 0 decimals
    "JPY": 0,  # Japanese yen
    "CLP": 0,  # Chilean peso
    "KRW": 0,  # South Korean won
    "ISK": 0,  # Icelandic krona
    "VND": 0,  # Vietnamese dong
    # 3 decimals
    "KWD": 3,  # Kuwaiti dinar
    "BHD": 3,  # Bahraini dinar
    "OMR": 3,  # Omani rial
    "JOD": 3,  # Jordanian dinar
    "TND": 3,  # Tunisian dinar
}

DEFAULT_MINOR_UNIT = 2


def minor_unit_for(code: str) -> int:
    """Return how many decimals the currency ``code`` has (case-insensitive)."""
    try:
        return MINOR_UNITS[code.upper()]
    except KeyError:
        known = ", ".join(sorted(MINOR_UNITS))
        raise ValueError(f"unknown currency {code!r}; known currencies: {known}") from None
