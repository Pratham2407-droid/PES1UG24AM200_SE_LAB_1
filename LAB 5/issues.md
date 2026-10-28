# Static Analysis Issues

Line numbers below refer to the original `supplier_orders.py`.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Shell command injection | Security - High | 21 | `os.system` builds a shell command using the supplier value, which could allow command injection. | Removed the shell call and used a normal Python notification. |
| SQL injection | Security - Medium | 11 | Supplier and item values were inserted into SQL using string formatting. | Replaced string formatting with parameterized SQL placeholders. |
| Broad exception silently ignored | Reliability - Low | 25-28 | `except Exception: pass` hid database errors and made failures difficult to diagnose. | Removed the broad exception handler so unexpected errors are visible. |
| Global order total and unused argument | Maintainability - Medium | 6, 9-13, 16 | The global total could drift from the database contents, and `remarks` was unused. | Calculate the total from the database and remove the unused argument. |
| Naming, documentation, and formatting problems | Style - Low | 1-35 | Pylint and Flake8 reported missing docstrings, non-snake-case names, long lines, and spacing issues. | Added docstrings, renamed functions, and formatted the code to meet the tools' checks. |

## Verification

After the fixes, Pylint reported **10.00/10**, Bandit reported **zero issues**, and Flake8 reported no issues.