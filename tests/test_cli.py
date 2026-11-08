import subprocess
import sys

import pytest

from tiptally.cli import format_amount, main, parse_amount


def test_prints_one_line_per_person_and_a_total(capsys):
    assert main(["120.50", "4", "--tip", "10"]) == 0
    lines = capsys.readouterr().out.splitlines()
    assert lines == [
        "Person 1: 33.14",
        "Person 2: 33.14",
        "Person 3: 33.14",
        "Person 4: 33.13",
        "Total: 132.55 (tip 12.05)",
    ]


def test_tip_defaults_to_zero(capsys):
    main(["100", "2"])
    assert capsys.readouterr().out.splitlines()[-1] == "Total: 100.00 (tip 0.00)"


def test_parse_amount_accepts_one_decimal():
    assert parse_amount("7.5") == 750


def test_parse_amount_accepts_whole_numbers():
    assert parse_amount("42") == 4200


def test_parse_amount_rejects_three_decimals():
    with pytest.raises(ValueError):
        parse_amount("1.005")


def test_parse_amount_rejects_negative():
    with pytest.raises(ValueError):
        parse_amount("-5")


def test_parse_amount_rejects_text():
    with pytest.raises(ValueError):
        parse_amount("abc")


def test_format_amount_pads_cents():
    assert format_amount(1205) == "12.05"
    assert format_amount(5) == "0.05"


def test_bad_amount_exits_with_usage_error(capsys):
    with pytest.raises(SystemExit) as exc:
        main(["abc", "2"])
    assert exc.value.code == 2
    assert "not a valid amount" in capsys.readouterr().err


def test_module_entry_point():
    result = subprocess.run(
        [sys.executable, "-m", "tiptally", "120.50", "4", "--tip", "10"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout.splitlines()[0] == "Person 1: 33.14"
