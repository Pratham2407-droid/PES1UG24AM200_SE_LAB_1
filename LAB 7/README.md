# Lab 7: Fuzz Testing - ATM Withdrawal

This submission follows the handout's three deliverables: a screenshot report, a fixed Python application, and Hypothesis tests. The ATM application keeps the `withdraw`, `pin_check`, and `note_breakup` functions from the assigned Lab 6 topic.

## Install and run

```powershell
python -m pip install -r requirements.txt
python processor.py
python -m pytest -v test_processor.py
```

`test_processor.py` includes generated properties, malformed-input checks, and boundary checks for balances, daily limits, fees, PIN lockout, and note breakdown. The report includes the original-version fuzz failure, fixed application run, and passing test output.
