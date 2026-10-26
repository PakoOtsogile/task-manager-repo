# Lab 7: Mutation Testing & Suite Effectiveness

## Completed By
- Student ID: <your ID>
- Date: <today's date>

## What I Did
1. Installed mutmut 2.5.1 and configured it (`setup.cfg`) to mutate `app/tasks.py` (43 mutants)
2. Applied the Lab 4 fixes first, since mutmut needs a passing baseline
3. Ran mutation testing against three suites: AI-only, manual-only and combined
4. Analysed the surviving mutants and wrote tests to kill them (`new_tests.py`)
5. Re-ran the combined suite: 43 of 43 mutants killed

## Results

| Suite | Mutation score | Line coverage of `tasks.py` |
|-------|---------------|------------------------------|
| AI-only | 9.3% (4/43) | 40% |
| Manual-only | 11.6% (5/43) | 40% |
| Combined | 93.0% (40/43) | 100% |
| Combined + new tests | 100% (43/43) | 100% |

## Gap Analysis
- The combined suite reached **100% line coverage but only a 93% mutation score**. Every line ran, yet
  three mutants (the `TASKS_FILE` constant and the `tags` key) still went undetected, because no assertion checked them.
  Coverage shows code was executed, not that results were verified.
- The AI-only and manual-only scores are low mainly because they only test two functions; on those
  two functions the AI suite killed 4 of 5 mutants and the manual suite 5 of 5. The AI suite missed an
  inverted condition in `remove_task` because it only checked `len(tasks) == 1`.

## Notes
- The lab text uses `mutmut run --tests-dir=...`, which is not a flag in mutmut 2.x. I used
  `--runner "python -m pytest -x -q <suite>"` and `tests_dir` in `setup.cfg`.
- `days_until_due` (`app/storage.py`) was not included because I did not have the file.
- To reproduce: copy `new_tests.py` into your tests folder as `test_new_tests.py` (pytest only collects `test_*.py`),
  then run `mutmut run --runner "python -m pytest -x -q tests/"`.

## Files
- `mutation_ai.txt`, `mutation_manual.txt`, `mutation_combined.txt`, `mutation_combined_after_new_tests.txt`
- `surviving_mutants_analysis.md`, `new_tests.py`, `setup.cfg`
