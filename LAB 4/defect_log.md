# Defect Log — Lab 4

## Defect #1: Off-by-One in `get_pending_tasks`

| Stage | Action | Date | Notes |
|---|---|---|---|
| **New** | Defect discovered during TC-05 execution | Week 4 | First task not returned |
| **Triaged** | Severity: High, Priority: P1 | Week 4 | Breaks core functionality |
| **Assigned** | Assigned to developer | Week 4 | Fix in `tasks.py:44` |
| **Fixed** | Changed `range(1, len(tasks))` to `range(len(tasks))` | Week 4 | Fix committed |
| **Verified** | Re-ran TC-05 → now returns 2 pending tasks | Week 4 | Fix confirmed |
| **Closed** | Defect closed | Week 4 | No regression |

### Defect Summary

- **Defect:** First task is skipped when retrieving pending tasks.
- **Severity:** High
- **Priority:** P1
- **Root cause:** Off-by-one loop range.
- **Fix:** Changed `range(1, len(tasks))` to `range(len(tasks))`.
- **Verification:** TC-05 was re-run and returned 2 pending tasks.
- **Final status:** Closed.

---

## Defect #2: Division by Zero in `average_priority`

| Stage | Action | Date | Notes |
|---|---|---|---|
| **New** | Defect discovered during TC-08 execution | Week 4 | `ZeroDivisionError` on empty list |
| **Triaged** | Severity: Critical, Priority: P0 | Week 4 | Crashes the program |
| **Assigned** | Assigned to developer | Week 4 | Fix in `tasks.py:52` |
| **Fixed** | Added `if not tasks: return 0` | Week 4 | Fix committed |
| **Verified** | Re-ran TC-08 → now returns 0 | Week 4 | Fix confirmed |
| **Closed** | Defect closed | Week 4 | No regression |

### Defect Summary

- **Defect:** Calculating average priority for an empty task list causes a `ZeroDivisionError`.
- **Severity:** Critical
- **Priority:** P0
- **Root cause:** The function attempts division when there are no tasks.
- **Fix:** Added `if not tasks: return 0`.
- **Verification:** TC-08 was re-run and returned 0.
- **Final status:** Closed.
