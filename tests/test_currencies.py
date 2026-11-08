import pytest

from tiptally.currencies import MINOR_UNITS, minor_unit_for


@pytest.mark.parametrize("code", ["JPY", "CLP", "KRW", "ISK", "VND"])
def test_zero_decimal_currencies(code):
    assert minor_unit_for(code) == 0


@pytest.mark.parametrize("code", ["KWD", "BHD", "OMR", "JOD", "TND"])
def test_three_decimal_currencies(code):
    assert minor_unit_for(code) == 3


def test_exactly_ten_currencies():
    assert len(MINOR_UNITS) == 10


def test_lookup_ignores_case():
    assert minor_unit_for("kwd") == 3


def test_unknown_currency_is_rejected():
    with pytest.raises(ValueError, match="unknown currency 'XYZ'"):
        minor_unit_for("XYZ")
