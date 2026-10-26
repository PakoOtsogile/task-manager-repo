# Surviving Mutants Analysis

Tool: mutmut 2.5.1 on `app/tasks.py` (43 mutants). The Lab 4 fixes (DEF-01, DEF-02) were applied first,
because mutmut needs a passing baseline. Suites run: AI-generated (Lab 6 sample), manual (Lab 6),
and combined (`tests/` = AI + manual + Lab 3 + Lab 4 tests).

## Mutation Scores

| Suite | Killed | Survived | Mutation score |
|-------|--------|----------|----------------|
| AI-only | 4 | 39 | 9.3% |
| Manual-only | 5 | 38 | 11.6% |
| Combined | 40 | 3 | 93.0% |
| Combined + new tests | 43 | 0 | 100% |

The AI-only and manual-only scores are low because each suite only tests two functions
(`find_task_by_title`, `remove_task`), so mutants in the other seven functions survive by default.
Compare only the mutants in the functions both suites actually target:

| Function (mutants) | AI-only killed | Manual-only killed |
|--------------------|----------------|--------------------|
| `find_task_by_title` (2) | 2 | 2 |
| `remove_task` (3) | 2 | 3 |

## Surviving Mutants

### In the AI-only suite (target functions)

**Mutant 38** in `remove_task`:
```diff
-        if tasks[i]["id"] == task_id:
+        if tasks[i]["id"] != task_id:
```
Why it survived: the AI test removes id 1 from `[A(id 1), B(id 2)]` and only asserts `len(tasks) == 1`.
The mutant deletes the other task (B), so the length is still 1 and the test passes. The manual test
also checks that the remaining task has id 2 (and a second test removes a nonexistent id and expects
no change), so it fails and kills the mutant.

### In the combined suite (3 survivors)

| ID | Line | Mutation | Why it survived |
|----|------|----------|-----------------|
| 1 | 4 | `TASKS_FILE = "tasks.json"` -> `"XXtasks.jsonXX"` | Persistence tests monkeypatch `TASKS_FILE` to a temp path, so the real value was never checked |
| 2 | 4 | `TASKS_FILE = None` | Same reason |
| 13 | 28 | `"tags": tags` -> `"XXtagsXX": tags` | No test read the `tags` field back |

## New Tests (`new_tests.py`)

- `test_tasks_file_default_name` asserts `TASKS_FILE == "tasks.json"` (kills mutants 1 and 2)
- `test_add_task_stores_given_tags` asserts the exact `tags` value and the exact set of task keys (kills mutant 13)

After adding them (as `tests/test_new_tests.py`), mutmut was re-run on the combined suite: 43 of 43 mutants killed
(`mutation_combined_after_new_tests.txt`).

## Link to Earlier Labs
- The off-by-one mutant from the lab text (`range(len(tasks))` -> `range(1, len(tasks))`) is the same bug as DEF-01
  from Lab 4. With the Lab 4 test TC-05 in the suite, every mutant in `get_pending_tasks` is killed (3 of 3).
- Lab 3's `calculate_discount` tests kill all 4 mutants in that function. Together with Lab 4's
  `average_priority` tests (8 of 8) the combined suite is strong except for the three gaps above.

## Caveats
- `days_until_due` (`app/storage.py`) was not mutated because that file was not available; run
  `mutmut run` with `paths_to_mutate=app/` in your repo to include it.
- 43 mutants is a small sample; scores can change if mutmut is configured to mutate more files.
- The AI suite is the lab's sample, not your assistant's output; re-run if you replace it.
