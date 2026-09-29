# Mini Test Plan — REQ-03: Get Pending Tasks

## 1. Scope

This test plan covers the `get_pending_tasks(tasks)` function, which returns all tasks that are not yet done.

## 2. Entry Criteria

- The task list is populated with at least one task.
- Each task has a `done` field (`True`/`False`).
- The function is callable from the test environment.

## 3. Exit Criteria

- All test cases pass.
- No high-severity defects remain open.
- The function returns the correct number of pending tasks.

## 4. Test Cases

| TC ID | Description | Input | Expected Output |
|---|---|---|---|
| TC-05 | Mixed list | `[done=False, done=True, done=False]` | 2 pending tasks |
| TC-06 | Empty list | `[]` | 0 pending tasks |

## 5. Risks

- Off-by-one errors in loop bounds.
- Index errors if the list is empty.
- Incorrect filtering logic.

## 6. Schedule

- Test design: 15 minutes
- Test execution: 5 minutes
- Defect reporting: 10 minutes
