# Triage Table — Pylint Findings

| # | Rule | Severity | Location | Verdict | Justification | Fix Effort |
|---|------|----------|----------|---------|----------------|------------|
| 1 | W0102 (dangerous-default-value) | High | tasks.py:21 | Real Defect | `tags=[]` is a mutable default argument. Python evaluates it once at function definition, so every call that doesn't pass `tags` shares the *same* list object. Mutating one task's tags silently mutates every other task's tags — genuine data corruption. | Low |
| 2 | W0719 (division-by-zero) | Critical | tasks.py:52 | Real Defect | `average_priority` divides by `len(tasks)` with no check for an empty list. Calling it with `[]` raises `ZeroDivisionError` and crashes the program. | Low |
| 3 | E0601 (used-before-assignment) | Medium | tasks.py:35 | Real Defect | Pylint detects `task` may be referenced before assignment. In `complete_task`, if the loop body never executes (empty list), the flagged variable path is unsafe — worth guarding explicitly rather than relying on control flow. | Low |
| 4 | R1710 (inconsistent-return-statements) | Medium | tasks.py:58 | Real Defect | `find_task_by_title` returns a task object on success but implicitly returns `None` on failure. Callers that don't explicitly check for `None` will hit an `AttributeError` down the line — a real API design defect, not just a style nit. | Medium |
| 5 | C0121 (singleton-comparison) | Low | tasks.py:77 | Noise | `if is_premium == True:` is functionally correct since `is_premium` is always a boolean in this codebase. Pylint's suggested `if is_premium:` is a style preference, not a behavioral bug. | Low |
| 6 | W0612 (unused-variable) | Critical | storage.py:4 | Real Defect | `API_KEY` is assigned but never referenced in code — but the real issue is that it's a **hardcoded secret** committed to source control, a security vulnerability regardless of whether it's "used." | Low |
| 7 | W1401 (anomalous-backslash-in-string) | Critical | storage.py:26 | Real Defect | The flagged string is part of a query built by direct string concatenation of user input — this is a **SQL injection vulnerability**, far more serious than the anomalous-backslash warning itself suggests. | Medium |
| 8 | W0611 (unused-import) | Low | cli.py:2 | Real Defect | `add_task` and `save_tasks` are imported but never used in `cli.py`. Harmless at runtime, but pollutes the namespace and may signal incomplete/dead code. | Low |
| 9 | C0200 (consider-using-enumerate) | Low | tasks.py:44 | Noise | Pylint's suggestion to use `enumerate()` is a style preference. Notably, Pylint does **not** flag the real bug on this line: the loop starts at `range(1, len(tasks))` instead of `range(len(tasks))`, silently skipping the first task. | Low |
| 10 | W0702-equivalent (no exception handling) | Medium | storage.py:26 | Real Defect | `build_query` has no error handling for malformed input. Combined with finding #7, a malformed or malicious `title_filter` can either crash the query builder or inject arbitrary SQL. | Medium |

## Severity Legend
| Severity | Meaning | Examples in this repo |
|----------|---------|------------------------|
| Critical | Crashes, data loss, security breach | SQL injection, hardcoded secret, division by zero |
| High | Breaks core functionality | Mutable default argument |
| Medium | Degrades experience / edge cases | Inconsistent return, no error handling |
| Low | Cosmetic / minor inconvenience | Unused imports, style violations |

## Fix Effort Legend
| Effort | Meaning | Time Estimate |
|--------|---------|----------------|
| Low | Quick fix, one or two lines | < 15 minutes |
| Medium | Requires some refactoring | 15–60 minutes |
| High | Major refactor, multiple files | > 1 hour |
