import pytest

from atm_withdrawal import note_breakup, pin_check, withdraw


@pytest.mark.parametrize(
    "balance, amount, account_type, own_bank, expected",
    [
        (5000, 1000, "savings", True, 4000),
        (5000, 1000, "savings", False, 3980),
        (20000, 10000, "savings", False, 9980),
        (20000, 10100, "savings", False, 9870),
        (50000, 25100, "savings", True, "limit exceeded"),
        (1000, 1000, "savings", True, 0),
        (999, 1000, "savings", True, "insufficient funds"),
        (60000, 50000, "current", True, 10000),
    ],
)
def test_withdraw_branches(balance, amount, account_type, own_bank, expected):
    assert withdraw(balance, amount, account_type, own_bank) == expected


@pytest.mark.parametrize(
    "balance, amount, account_type, own_bank",
    [
        (5000, 1000, "unknown", True),
        (5000, 0, "savings", True),
        (5000, 150, "savings", True),
    ],
)
def test_withdraw_error_branches(balance, amount, account_type, own_bank):
    with pytest.raises(ValueError):
        withdraw(balance, amount, account_type, own_bank)


@pytest.mark.parametrize(
    "entered, actual, attempts, expected",
    [
        (1234, 1234, 0, "ok"),
        (1111, 1234, 0, "retry"),
        (1111, 1234, 2, "card blocked"),
        (1234, 1234, 3, "card blocked"),
    ],
)
def test_pin_check_branches(entered, actual, attempts, expected):
    assert pin_check(entered, actual, attempts) == expected


@pytest.mark.parametrize(
    "amount, expected",
    [
        (500, (1, 0, 0)),
        (700, (1, 1, 0)),
        (600, (1, 0, 1)),
        (100, (0, 0, 1)),
    ],
)
def test_note_breakup_branches(amount, expected):
    assert note_breakup(amount) == expected


def test_note_breakup_rejects_non_multiple_of_100():
    with pytest.raises(ValueError):
        note_breakup(101)