"""Validated ATM withdrawal operations for Lab 7 fuzz testing."""

DAILY_LIMIT = {"savings": 25_000, "current": 50_000}


def _require_int(value, name):
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def withdraw(balance, amount, account_type, own_bank):
    """Withdraw a valid amount, returning a balance or an ATM status string."""
    _require_int(balance, "balance")
    _require_int(amount, "amount")
    if balance < 0:
        raise ValueError("balance cannot be negative")
    if amount <= 0 or amount % 100:
        raise ValueError("amount must be a positive multiple of 100")
    if not isinstance(account_type, str):
        raise TypeError("account_type must be a string")
    if account_type not in DAILY_LIMIT:
        raise ValueError("unknown account")
    if not isinstance(own_bank, bool):
        raise TypeError("own_bank must be a boolean")

    if amount > DAILY_LIMIT[account_type]:
        return "limit exceeded"
    fee = 0 if own_bank else 20 + (10 if amount > 10_000 else 0)
    if amount + fee > balance:
        return "insufficient funds"
    return balance - amount - fee


def pin_check(entered, actual, attempts):
    """Check a four-digit PIN and safely enforce the three-attempt lockout."""
    _require_int(entered, "entered PIN")
    _require_int(actual, "actual PIN")
    _require_int(attempts, "attempts")
    if not 0 <= entered <= 9999 or not 0 <= actual <= 9999:
        raise ValueError("PINs must be between 0000 and 9999")
    if attempts < 0:
        raise ValueError("attempts cannot be negative")
    if attempts >= 3:
        return "card blocked"
    if entered == actual:
        return "ok"
    if attempts >= 2:
        return "card blocked"
    return "retry"


def note_breakup(amount):
    """Return counts of 500, 200, and 100-unit notes for a valid amount."""
    _require_int(amount, "amount")
    if amount < 0 or amount % 100:
        raise ValueError("amount must be a non-negative multiple of 100")
    notes_500, remaining = divmod(amount, 500)
    notes_200, remaining = divmod(remaining, 200)
    notes_100 = remaining // 100
    return notes_500, notes_200, notes_100


def main():
    """Run a small deterministic example of the three ATM operations."""
    print("ATM withdrawal demonstration")
    print("withdraw(5000, 1000, 'savings', True):", withdraw(5000, 1000, "savings", True))
    print("pin_check(1234, 1234, 0):", pin_check(1234, 1234, 0))
    print("note_breakup(1800):", note_breakup(1800))


if __name__ == "__main__":
    main()
