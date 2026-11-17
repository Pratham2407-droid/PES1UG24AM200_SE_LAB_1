"""Property-based fuzz tests for the ATM input validation functions."""

import pytest
from hypothesis import given, strategies as st

from atm_withdrawal import average_withdrawal, mask_card, notes_needed


@st.composite
def formatted_amounts(draw):
    value = draw(st.integers(min_value=0, max_value=10**30))
    text = str(value)
    if len(text) > 3 and draw(st.booleans()):
        first = len(text) % 3 or 3
        text = text[:first] + "," + ",".join(
            text[index:index + 3] for index in range(first, len(text), 3)
        )
    return value, text


@given(formatted_amounts())
def test_notes_needed_property(generated):
    amount, text = generated
    assert notes_needed(text) == amount // 100


@given(st.one_of(st.text(), st.none()))
def test_notes_needed_arbitrary_input_is_safe(value):
    try:
        result = notes_needed(value)
    except (TypeError, ValueError):
        return
    assert isinstance(result, int)
    assert result >= 0


@given(st.text(alphabet="0123456789", min_size=16, max_size=16))
def test_mask_card_property(digits):
    result = mask_card(digits)
    assert result == "XXXX XXXX XXXX " + digits[-4:]
    assert digits[:12] not in result


@given(st.one_of(st.text(), st.none()))
def test_mask_card_arbitrary_input_is_safe(value):
    try:
        result = mask_card(value)
    except (TypeError, ValueError):
        return
    assert result.startswith("XXXX XXXX XXXX ")
    assert len(result.rsplit(" ", 1)[-1]) == 4


@given(st.lists(st.integers(min_value=0, max_value=10**20), min_size=1, max_size=100))
def test_average_withdrawal_property(amounts):
    csv = ",".join(map(str, amounts))
    assert average_withdrawal(csv) == sum(amounts) // len(amounts)


@given(st.one_of(st.text(), st.none()))
def test_average_withdrawal_arbitrary_input_is_safe(value):
    try:
        result = average_withdrawal(value)
    except (TypeError, ValueError):
        return
    assert isinstance(result, int)
    assert result >= 0


@pytest.mark.parametrize("value", ["", " ", "1,", ",1", "1,,2", "1.5", "-1"])
def test_average_rejects_malformed_csv(value):
    with pytest.raises(ValueError):
        average_withdrawal(value)


@pytest.mark.parametrize("value", ["", "-1", "1,00", "1,,000", "1.00", "+100"])
def test_notes_rejects_malformed_amount(value):
    with pytest.raises(ValueError):
        notes_needed(value)


@pytest.mark.parametrize("value", ["", "123", "123456789012345", "12345678901234567", "abcd 5678 9012 3456"])
def test_mask_rejects_malformed_card(value):
    with pytest.raises(ValueError):
        mask_card(value)


@pytest.mark.parametrize(
    ("function", "value"),
    [(notes_needed, None), (mask_card, None), (average_withdrawal, None)],
)
def test_functions_reject_non_string_values(function, value):
    with pytest.raises(TypeError):
        function(value)
