# Comparison: AI-Generated vs. Manual Tests

Functions under test: `find_task_by_title` and `remove_task` (`app/tasks.py`) and `days_until_due` (`app/storage.py`).

> `days_until_due` tests are written but were **not run** (they skip when `app/storage.py` is missing).
> Run both suites in your repo, then update the rows marked (*) with your numbers.
> The AI suite is the lab's sample; replace it with your assistant's real output and re-measure.

## Measured Results (`app/tasks.py` functions, run here)

| Metric | AI-Only | Manual-Only | Combined |
|--------|---------|-------------|----------|
| Test functions (run / skipped) | 4 (3 / 1) | 9 (7 / 2) | 13 (10 / 3) |
| Assertions (all) | 4 | 12 | 16 |
| Assertions on `tasks.py` functions | 3 | 10 | 13 |
| File coverage, `app/tasks.py` | 41.3% | 41.3% | 41.3% |
| Statement coverage of the 2 target functions | 100% (7/7) | 100% (7/7) | 100% (7/7) |
| Assertion strength | Weak | Strong (exact values) | Strong |
| Edge cases (tasks.py functions) | 1 (title not found) | 5 (missing, empty list, duplicates, nonexistent id, empty remove) | 5 |
| Mutants killed (of 4 hand-made) | 1 (25%) | 4 (100%) | 4 (100%) |
| days_until_due coverage (*) | not measured | not measured | not measured |

File coverage is 41.3% for every suite because the other seven functions in `tasks.py` have no
tests in this lab. Raw output: `coverage_ai.txt`, `coverage_manual.txt`, `coverage_combined.txt`.

## Analysis

1. **Coverage did not separate the suites.** Both reach every statement in the two target
   functions, so a coverage report would rate them the same.
2. **Assertion strength did.** The AI suite's `test_remove_task` only checks `len(tasks) == 1`, so it
   passes even if the wrong task is removed (mutants M1 and M2 survived). The manual suite checks
   which task is left. See `mutant_check.md`.
3. **Edge cases:** the AI suite tested "title not found" but had no empty list, duplicate titles or
   nonexistent id. The manual suite has all three.
4. **Speed:** the AI suite took seconds to produce; the manual suite took longer but is far
   more trustworthy.
5. **Combined** adds nothing over manual on these functions, because the AI cases are a subset
   of the manual ones; its value is only as a quick starting point.

## Verdict
AI generated tests quickly but with weak assertions (checking the size of a list, or `> 0`) and
few edge cases. Manual tests used exact assertions and covered more edge cases. High coverage
did not mean a strong suite: line coverage was identical while the mutant kill rate was
25% vs. 100%.
