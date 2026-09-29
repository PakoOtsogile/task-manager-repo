# Boundary Value Table: calculate_discount

| Variable | Boundary | Just Below | At Boundary | Just Above |
|----------|----------|------------|-------------|------------|
| price | 0 (min) | -0.01 | 0 | 0.01, 1 |
| price | No upper bound | n/a | n/a | n/a |
| is_premium | Boolean | n/a | True / False | n/a |

The specification defines no maximum price, so there is no upper boundary to test.
`10000` is used only as a large-value EP representative (P4), not as a boundary.

`is_premium` has no numeric boundary, but Python treats `1 == True` and `0 == False`.
Those values are tested as boolean edge cases (TC15, TC16, TC17).
