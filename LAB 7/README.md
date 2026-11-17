# Lab 7: Fuzz Testing - ATM Withdrawal

This lab uses Hypothesis to fuzz three input-processing functions and hardens
them against malformed and unexpected input.

## Run

```powershell
python -m pip install -r requirements.txt
python -B -m pytest -p no:cacheprovider -p no:anyio -v test_atm_withdrawal.py
python atm_withdrawal.py
```

Run the commands from this directory. Hypothesis checks generated valid values
against their expected results and feeds arbitrary text and `None` to verify
that invalid input is rejected cleanly with `ValueError` or `TypeError`.

## Input rules

- `notes_needed`: non-negative whole-number strings, either plain digits or
  correctly comma-grouped (for example `2500` or `2,500`). Returns whole 100
  notes; any remainder is not counted as a full note.
- `mask_card`: exactly 16 ASCII digits, with optional spaces between four-digit
  groups. The returned value contains only the last four digits.
- `average_withdrawal`: a non-empty comma-separated list of non-negative whole
  numbers. Returns the floor of the arithmetic mean.

Malformed strings raise `ValueError`; values of the wrong type raise
`TypeError`. The command-line program reports these errors and continues to the
next prompt rather than terminating with a traceback.

## Report

See Lab_7_FuzzTesting_Report.pdf for the fuzz findings, corrected behavior, and test run summary.
