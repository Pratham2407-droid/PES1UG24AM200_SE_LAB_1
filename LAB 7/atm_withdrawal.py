"""Input validation examples for a simple ATM withdrawal application."""

import re


_AMOUNT_PATTERN = re.compile(r"(?:[0-9]+|[0-9]{1,3}(?:,[0-9]{3})+)")
_CARD_PATTERN = re.compile(r"(?:[0-9]{16}|[0-9]{4}(?: [0-9]{4}){3})")


def _require_string(value, field_name):
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be a string")


def notes_needed(amount):
    """Return the number of whole 100-unit notes for a non-negative amount.

    ``amount`` may be an ungrouped integer string (``2500``) or use valid
    thousands separators (``2,500``). Any remainder is dispensed separately.
    """
    _require_string(amount, "amount")
    amount = amount.strip()
    if not _AMOUNT_PATTERN.fullmatch(amount):
        raise ValueError("amount must be a non-negative integer, optionally comma-grouped")
    return int(amount.replace(",", "")) // 100


def mask_card(card_number):
    """Mask a 16-digit card number, accepting digits with or without grouping."""
    _require_string(card_number, "card_number")
    card_number = card_number.strip()
    if not _CARD_PATTERN.fullmatch(card_number):
        raise ValueError("card_number must contain exactly 16 digits")
    digits = card_number.replace(" ", "")
    return "XXXX XXXX XXXX " + digits[-4:]


def average_withdrawal(amounts_csv):
    """Return the floor average of a non-empty CSV list of non-negative integers."""
    _require_string(amounts_csv, "amounts_csv")
    fields = amounts_csv.split(",")
    if not fields or any(not field.strip() for field in fields):
        raise ValueError("amounts_csv must contain one or more integer amounts")

    amounts = []
    for field in fields:
        value = field.strip()
        if not value.isascii() or not value.isdecimal():
            raise ValueError("each withdrawal must be a non-negative integer")
        amounts.append(int(value))
    return sum(amounts) // len(amounts)


def main():
    print("==== Running notes_needed ====")
    user_input = input("Enter an amount (e.g. 2,500): ")
    try:
        result = notes_needed(user_input)
    except (TypeError, ValueError) as error:
        print("Invalid amount:", error)
    else:
        print("Number of 100 Notes:", result)

    print("\n==== Running mask_card ====")
    user_input = input("Enter a card number (e.g. 1234 5678 9012 3456): ")
    try:
        result = mask_card(user_input)
    except (TypeError, ValueError) as error:
        print("Invalid card number:", error)
    else:
        print("Masked Card:", result)

    print("\n==== Running average_withdrawal ====")
    user_input = input("Enter withdrawals as CSV (e.g. 500,1000,2000): ")
    try:
        result = average_withdrawal(user_input)
    except (TypeError, ValueError) as error:
        print("Invalid withdrawals:", error)
    else:
        print("Average Withdrawal:", result)


if __name__ == "__main__":
    main()
