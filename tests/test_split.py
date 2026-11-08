import pytest

from tiptally.split import split_even, split_weighted


def test_even_split_without_tip():
    assert split_even(10000, 4, 0) == [2500, 2500, 2500, 2500]


def test_shares_include_the_tip():
    assert sum(split_even(10000, 4, 10)) == 11000


def test_leftover_cents_go_to_first_payers():
    # 12050 + 10% tip = 13255; 13255 / 4 = 3313 remainder 3
    assert split_even(12050, 4, 10) == [3314, 3314, 3314, 3313]


def test_single_person_pays_everything():
    assert split_even(4599, 1, 20) == [5519]


def test_tip_rounds_half_up():
    # 10% of 1005 is 100.5 cents -> 101
    assert split_even(1005, 1, 10) == [1005 + 101]


def test_tip_rounds_down_below_half():
    # 10% of 1004 is 100.4 cents -> 100
    assert split_even(1004, 1, 10) == [1004 + 100]


def test_zero_total_gives_zero_shares():
    assert split_even(0, 3, 15) == [0, 0, 0]


def test_one_cent_among_three():
    assert split_even(1, 3, 0) == [1, 0, 0]


def test_returns_one_share_per_person():
    assert len(split_even(9999, 7, 12)) == 7


@pytest.mark.parametrize("total", [1, 99, 12345, 100001])
@pytest.mark.parametrize("people", [1, 2, 3, 7])
def test_shares_add_up_and_differ_by_at_most_one_cent(total, people):
    shares = split_even(total, people, 18)
    tip = (total * 18 + 50) // 100
    assert sum(shares) == total + tip
    assert max(shares) - min(shares) <= 1


def test_negative_total_is_rejected():
    with pytest.raises(ValueError):
        split_even(-1, 2, 10)


def test_negative_tip_is_rejected():
    with pytest.raises(ValueError):
        split_even(1000, 2, -5)


def test_weighted_split_follows_the_weights():
    assert split_weighted(10000, [2, 1, 1], 0) == [5000, 2500, 2500]



def test_equal_weights_match_the_even_split():
    for total in (1, 100, 12050, 99999):
        assert split_weighted(total, [1, 1, 1, 1], 15) == split_even(total, 4, 15)


def test_weighted_leftover_goes_to_the_largest_remainder():
    # 100 split 1:2 is 33.33 / 66.67 -> the second payer lost more, so gets the cent
    assert split_weighted(100, [1, 2], 0) == [33, 67]


def test_weighted_ties_go_to_the_first_payer():
    assert split_weighted(100, [1, 1, 1], 0) == [34, 33, 33]


@pytest.mark.parametrize("weights", [[1], [3, 1], [5, 2, 2], [1, 1, 1, 7], [10, 1, 1, 1, 1]])
def test_weighted_shares_add_up(weights):
    shares = split_weighted(12345, weights, 18)
    assert sum(shares) == 12345 + (12345 * 18 + 50) // 100
    assert len(shares) == len(weights)


def test_empty_weights_are_rejected():
    with pytest.raises(ValueError, match="weights must not be empty"):
        split_weighted(1000, [], 10)


def test_zero_weight_is_rejected():
    with pytest.raises(ValueError, match="at least 1"):
        split_weighted(1000, [2, 0], 10)
