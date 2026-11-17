"""Hypothesis fuzz tests for the ATM processor functions."""

import pytest
from hypothesis import given, strategies as st

from processor import DAILY_LIMIT, note_breakup, pin_check, withdraw


@given(
    balance=st.integers(min_value=0, max_value=10**9),
    amount=st.integers(min_value=1, max_value=500).map(lambda n: n * 100),
    account=st.sampled_from(tuple(DAILY_LIMIT)),
)
def test_withdraw_respects_limits_balance_and_fees(balance, amount, account):
    result = withdraw(balance, amount, account, True)
    if amount > DAILY_LIMIT[account]:
        assert result == "limit exceeded"
    elif amount > balance:
        assert result == "insufficient funds"
    else:
        assert result == balance - amount


@given(
    balance=st.integers(min_value=0, max_value=10**9),
    amount=st.integers(min_value=1, max_value=500).map(lambda n: n * 100),
)
def test_external_bank_fee_is_applied(balance, amount):
    result = withdraw(balance, amount, "savings", False)
    if amount > DAILY_LIMIT["savings"]:
        assert result == "limit exceeded"
    else:
        fee = 20 + (10 if amount > 10_000 else 0)
        expected = balance - amount - fee if amount + fee <= balance else "insufficient funds"
        assert result == expected


@given(pin=st.integers(min_value=0, max_value=9999), attempts=st.integers(min_value=0, max_value=2))
def test_correct_pin_succeeds_before_lockout(pin, attempts):
    assert pin_check(pin, pin, attempts) == "ok"


@given(
    actual=st.integers(min_value=0, max_value=9999),
    attempts=st.integers(min_value=0, max_value=10**6),
)
def test_wrong_pin_retries_then_blocks(actual, attempts):
    result = pin_check((actual + 1) % 10000, actual, attempts)
    assert result == ("card blocked" if attempts >= 2 else "retry")


@given(amount=st.integers(min_value=0, max_value=10**9).map(lambda n: n * 100))
def test_note_breakup_is_exact_and_non_negative(amount):
    notes = note_breakup(amount)
    assert len(notes) == 3
    assert all(isinstance(count, int) and count >= 0 for count in notes)
    assert sum(count * denomination for count, denomination in zip(notes, (500, 200, 100))) == amount


@pytest.mark.parametrize("value", [None, "100", 100.0, True])
def test_withdraw_rejects_non_integer_balance_and_amount(value):
    with pytest.raises(TypeError):
        withdraw(value, 100, "savings", True)
    with pytest.raises(TypeError):
        withdraw(1000, value, "savings", True)


@pytest.mark.parametrize("amount", [-100, 0, 1, 150, 100.5, None, True])
def test_withdraw_rejects_invalid_amounts(amount):
    if isinstance(amount, (float, type(None), bool)):
        error = TypeError
    else:
        error = ValueError
    with pytest.raises(error):
        withdraw(1000, amount, "savings", True)


@pytest.mark.parametrize("account", [None, "business", "", 1])
def test_withdraw_rejects_unknown_or_wrong_type_accounts(account):
    error = TypeError if not isinstance(account, str) else ValueError
    with pytest.raises(error):
        withdraw(1000, 100, account, True)


@pytest.mark.parametrize("amount", [-100, 1, 150, 100.0, None, True])
def test_note_breakup_rejects_invalid_values(amount):
    error = TypeError if isinstance(amount, (float, type(None), bool)) else ValueError
    with pytest.raises(error):
        note_breakup(amount)


@pytest.mark.parametrize("attempts", [-1, 1.5, None, True])
def test_pin_check_rejects_invalid_attempt_counts(attempts):
    error = TypeError if isinstance(attempts, (float, type(None), bool)) else ValueError
    with pytest.raises(error):
        pin_check(1234, 1234, attempts)


def test_withdraw_daily_limit_boundary_and_fee_boundary():
    assert withdraw(25_000, 25_000, "savings", True) == 0
    assert withdraw(50_000, 50_000, "current", True) == 0
    assert withdraw(10_020, 10_000, "savings", False) == 0
    assert withdraw(10_129, 10_100, "savings", False) == "insufficient funds"


def test_pin_blocks_after_third_failed_attempt():
    assert pin_check(1, 2, 0) == "retry"
    assert pin_check(1, 2, 1) == "retry"
    assert pin_check(1, 2, 2) == "card blocked"
    assert pin_check(1, 2, 3) == "card blocked"
