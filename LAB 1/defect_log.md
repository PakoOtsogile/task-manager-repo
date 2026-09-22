# Lab 1: Manual Defect Log

| ID | File | Line | Description | Suspected Severity |
|----|------|------|-------------|-------------------|
| D01 | app/tasks.py | 44 | `get_pending_tasks` uses `range(1, len(tasks))` — skips index 0, so first task is never checked | High |
| D02 | app/tasks.py | 52 | `average_priority` divides by `len(tasks)` without checking for empty list — ZeroDivisionError | Critical |
| D03 | app/tasks.py | 21 | `add_task` uses mutable default argument `tags=[]` — all tasks share the same list object | High |
| D04 | app/tasks.py | 10 | `load_tasks` opens file without context manager — resource leak on exception | Medium |
| D05 | app/tasks.py | 77 | `calculate_discount` uses `if is_premium == True:` — redundant comparison, `1 == True` applies discount | Low |
| D06 | app/storage.py | 4 | Hardcoded API key `sk-test-1234567890abcdef` — security vulnerability | Critical |
| D07 | app/storage.py | 26 | `build_query` concatenates user input into SQL — SQL injection vulnerability | Critical |
| D08 | app/cli.py | 2 | Unused imports `save_tasks`, `add_task` — wasted namespace | Low |
| D09 | app/tasks.py | 35 | `complete_task` compares `task["id"]` (int) with `task_id` (may be string) — silent failure | Medium |
| D10 | app/tasks.py | 58 | `find_task_by_title` implicitly returns `None` if no match — callers may dereference | Medium |