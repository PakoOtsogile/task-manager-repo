# Hand-Made Mutant Check

Four deliberate bugs were injected into `app/tasks.py` one at a time (original restored after each),
and each suite was run against them. A suite "kills" a mutant if at least one test fails.

| Mutant | Change | AI suite | Manual suite |
|--------|--------|----------|--------------|
| M1 | `remove_task` deletes the last task instead of the matching one (`del tasks[-1]`) | Survived | Killed |
| M2 | `remove_task` condition inverted (`==` to `!=`) | Survived | Killed |
| M3 | `find_task_by_title` returns the last match instead of the first | Survived | Killed |
| M4 | `find_task_by_title` always returns `None` | Killed | Killed |

Killed: AI 1 of 4 (25%), manual 4 of 4 (100%).

Why the AI suite missed M1-M3:
- `test_remove_task` only asserts `len(tasks) == 1`, which is true whether the right or the wrong task was removed.
- `test_find_task_by_title_found` uses unique titles, so "first match" and "last match" look the same.

This is a small hand-made sample, not a full mutation run; it only shows the kind of gap that Lab 7 (mutmut) measures properly.
