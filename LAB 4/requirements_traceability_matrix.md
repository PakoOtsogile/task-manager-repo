# Requirements Traceability Matrix (RTM)

## Requirements

| Requirement ID | Requirement Description |
|---|---|
| REQ-01 | The system shall allow users to add a new task with a title and optional priority |
| REQ-02 | The system shall mark a task as complete by its ID |
| REQ-03 | The system shall return all tasks that are not yet done |
| REQ-04 | The system shall calculate the average priority across all tasks |
| REQ-05 | The system shall apply a 20% discount for premium users |
| REQ-06 | The system shall persist tasks to disk and reload them on startup |

## Test Cases

| Req ID | Test Case ID | Test Description |
|---|---|---|
| REQ-01 | TC-01 | Add a task with title only → task created with default priority 1 |
| REQ-01 | TC-02 | Add a task with title and priority 5 → task created with priority 5 |
| REQ-02 | TC-03 | Complete a task by valid ID → task marked done |
| REQ-02 | TC-04 | Complete a task by invalid ID → returns False |
| REQ-03 | TC-05 | Get pending tasks from mixed list → returns only undone tasks |
| REQ-03 | TC-06 | Get pending tasks from empty list → returns empty list |
| REQ-04 | TC-07 | Calculate average priority of [1, 3, 5] → returns 3.0 |
| REQ-04 | TC-08 | Calculate average priority of empty list → returns 0 (or error?) |
| REQ-05 | TC-09 | Calculate discount for premium user (100) → returns 80 |
| REQ-05 | TC-10 | Calculate discount for regular user (100) → returns 100 |
| REQ-06 | TC-11 | Save tasks to disk, reload → tasks are identical |
| REQ-06 | TC-12 | Load tasks when no file exists → returns empty list |

## Completed RTM

| Requirement ID | Requirement Description | Test Case ID(s) | Test Level | Status |
|---|---|---|---|---|
| REQ-01 | Add a new task | TC-01, TC-02 | Unit | ✅ Pass |
| REQ-02 | Mark task complete | TC-03, TC-04 | Unit | ✅ Pass |
| REQ-03 | Get pending tasks | TC-05, TC-06 | Unit | ⚠️ TC-05 Fails (off-by-one) |
| REQ-04 | Average priority | TC-07, TC-08 | Unit | ⚠️ TC-08 Fails (ZeroDivisionError) |
| REQ-05 | Premium discount | TC-09, TC-10 | Unit | ✅ Pass |
| REQ-06 | Persist tasks to disk | TC-11, TC-12 | Integration | ✅ Pass |

## Traceability Summary

- Total requirements: **6**
- Total test cases: **12**
- Test cases per requirement: **2**
- Requirements covered: **6/6**
