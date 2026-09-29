# Test Design Table: calculate_discount

| Test ID | price | is_premium | Expected | Covers | Rationale |
|---------|-------|------------|----------|--------|-----------|
| TC01 | 0 | True | 0 | P1, B1 | Zero price, premium |
| TC02 | 0 | False | 0 | P1, B2 | Zero price, regular |
| TC03 | 0.01 | True | 0.008 | P2, B1 | Small positive, premium |
| TC04 | 0.01 | False | 0.01 | P2, B2 | Small positive, regular |
| TC05 | 100 | True | 80 | P3, B1 | Normal price, premium |
| TC06 | 100 | False | 100 | P3, B2 | Normal price, regular |
| TC07 | 10000 | True | 8000 | P4, B1 | Large price, premium |
| TC08 | 10000 | False | 10000 | P4, B2 | Large price, regular |
| TC09 | -10 | True | -8 | P5, B1 | Negative price (current behaviour) |
| TC10 | -10 | False | -10 | P5, B2 | Negative price (current behaviour) |
| TC11 | "abc" | True | TypeError | P6, B1 | Non-numeric price |
| TC12 | 100 | "yes" | 100 | P3, B3 | Non-boolean, truthy string |
| TC13 | -0.01 | True | -0.008 | BVA | Just below minimum |
| TC14 | 1 | True | 0.8 | BVA | Just above minimum (min + 1) |
| TC15 | 100 | 1 | 80 | Boolean edge | 1 == True in Python |
| TC16 | 100 | 0 | 100 | Boolean edge | 0 == False in Python |
| TC17 | 100 | 1.0 | 80 | Boolean edge | 1.0 == True in Python |

17 test cases, above the minimum of 10. All 9 equivalence classes are covered.
