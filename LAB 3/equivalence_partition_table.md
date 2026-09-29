# Equivalence Partition Table: calculate_discount

Specification: "Apply a loyalty discount for premium users." Premium users pay `price * 0.8`; others pay `price`.

| Variable | Class ID | Description | Type | Representative |
|----------|----------|-------------|------|----------------|
| price | P1 | Zero | Valid | 0 |
| price | P2 | Small positive | Valid | 0.01 |
| price | P3 | Normal positive | Valid | 100 |
| price | P4 | Large positive | Valid | 10000 |
| price | P5 | Negative | Invalid | -10 |
| price | P6 | Non-numeric | Invalid | "abc" |
| is_premium | B1 | Premium user (True) | Valid | True |
| is_premium | B2 | Regular user (False) | Valid | False |
| is_premium | B3 | Non-boolean value | Invalid | "yes" |

Note: the specification does not say whether zero or negative prices are valid. I treat zero as valid (a free item) and negative as invalid, and flag both as assumptions.
