# Test Results: calculate_discount

Command: `python -m pytest test_calculate_discount.py -v`

## Summary
- Total tests: 17
- Passed: 17
- Failed: 0

| Test | Result | Observation |
|------|--------|-------------|
| TC01-TC08 | Pass | Valid classes behave as specified (20% off for premium, full price otherwise) |
| TC09 | Pass | Negative price accepted and discounted (-10 -> -8) |
| TC10 | Pass | Negative price accepted for regular users (-10 -> -10) |
| TC11 | Pass | `"abc"` raises `TypeError` (Python's own error, no custom validation) |
| TC12 | Pass | `"yes"` gets no discount, because `"yes" == True` is False |
| TC13 | Pass | -0.01 accepted and discounted |
| TC14 | Pass | price 1 -> 0.8 |
| TC15 | Pass | `1` treated as premium (`1 == True`) |
| TC16 | Pass | `0` treated as regular (`0 == False`) |
| TC17 | Pass | `1.0` treated as premium (`1.0 == True`) |

## Issues Revealed

| ID | Issue | Tests | Severity |
|----|-------|-------|----------|
| I1 | No validation of negative prices; the function returns negative "prices" | TC09, TC10, TC13 | Medium |
| I2 | No input type validation; non-numeric price fails with a raw `TypeError` | TC11 | Medium |
| I3 | Non-boolean `is_premium` is silently treated as regular (`"yes"` gets no discount) | TC12 | Low |
| I4 | `is_premium == True` accepts `1` and `1.0` as premium, an unintended side effect of `==` | TC15, TC17 | Low |

## Note
All tests pass because they encode the function's *current* behaviour. The issues
above are validation gaps and unspecified behaviour, not failing tests. The
specification never says what should happen for negative prices or non-boolean
flags, so the expected values in TC09-TC12 are assumptions to be confirmed.
