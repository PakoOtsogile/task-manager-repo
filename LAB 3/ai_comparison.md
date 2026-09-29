# Manual vs. AI-Generated Test Cases: Comparison

> Replace the "AI output" section with the actual response from your AI assistant
> to the Part F prompt, then re-check the overlap count below.

## AI output (sample from the lab)

Equivalence classes:
- price: valid = positive numbers (> 0); invalid = negative, zero, non-numeric
- is_premium: valid = True, False; invalid = non-boolean

Boundary values for price: -0.01, 0, 0.01, 50, 100, 1000

| price | is_premium | Expected |
|-------|------------|----------|
| 100 | True | 80 |
| 100 | False | 100 |
| 0 | True | 0 |
| -10 | True | Error? |
| 1000 | True | 800 |

## Overlap with my manual tests

| Manual test | Reproduced by AI? |
|-------------|-------------------|
| TC01 (0, True) | Yes |
| TC03 (0.01, True) | Partly: 0.01 listed as a boundary, premium flag not stated |
| TC05 (100, True) | Yes |
| TC06 (100, False) | Yes |
| TC09 (-10, True) | Partly: included, but expected result "Error?" |
| TC13 (-0.01, True) | Partly: -0.01 listed as a boundary, premium flag not stated |
| TC02, TC04, TC07, TC08, TC10, TC11, TC12, TC14, TC15, TC16, TC17 | No |

Reproduced (fully or partly): 6 of 17, about **35%**. Fully matching cases: 3 of 17 (about 18%).

## Comparison

| Criterion | Manual | AI | Verdict |
|-----------|--------|----|---------|
| Valid price classes | P1-P4 (zero, small, normal, large) | Positive numbers only | AI coarser; it lumps positives together |
| Zero price | Valid class P1 | Called invalid | Disagree; the spec does not say. I treat it as valid |
| Invalid price classes | P5 negative, P6 non-numeric | Negative and non-numeric named as classes, but no non-numeric test case | AI named the class but did not turn it into a test |
| `is_premium` classes | B1, B2, B3 | Named non-boolean class, no test values | AI missed concrete cases |
| Boundaries | -0.01, 0, 0.01, 1 | -0.01, 0, 0.01, plus 50 and 1000 | AI similar around 0 |
| Upper bound | None (spec has none) | 1000 | AI invented a limit not in the spec |
| Python `==` quirks | TC15, TC16, TC17 | None | AI missed |
| Expected value for negatives | -8 (current behaviour), flagged as a spec gap | "Error?" | AI flagged the ambiguity but did not resolve it |
| Speed | Slow | Fast | AI |
| Test count | 17 | 5 | Manual |

## What the AI got right
- Recognised the boundary at price = 0 and the -0.01 / 0.01 neighbours
- Correct expected values for standard cases (100 -> 80 / 100)
- Flagged uncertainty over negative prices instead of guessing

## What the AI missed
- Concrete non-numeric and non-boolean test cases (`"abc"`, `"yes"`)
- The `1 == True`, `0 == False` and `1.0 == True` behaviour
- Small and large regular-user cases (TC02, TC04, TC08, TC10)

## What the AI got wrong
- Invented an upper bound (1000) that is not in the specification
- Classified zero as invalid without any basis in the spec

## Conclusion
The AI was useful for quickly producing happy-path cases and spotting the boundary
at zero, but it under-generated invalid and edge cases and hallucinated a maximum
price. About 35% of my manual cases were reproduced, so specification reading and
Python-specific knowledge remain necessary.

## Reflection
**What proportion of my manually designed boundary cases did the AI reproduce, and what did it miss or get wrong?**

The AI reproduced about 35% of my 17 cases (6 fully or partly). It found the boundary
at price = 0 and the -0.01 / 0.01 neighbours, and it correctly hesitated over the
expected result for negative prices. It missed the non-numeric and non-boolean
inputs, the Python `==` behaviour for `1`, `0` and `1.0`, and most regular-user
variants. It also invented a 1000 upper bound that the specification does not
contain, and treated zero as invalid without justification. Its output was a
quick starting point, but every case still needed checking against the spec.
