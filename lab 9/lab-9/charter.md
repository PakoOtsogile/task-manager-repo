# Test Charter: Task Manager

## Mission
Explore the task management logic to find bugs related to adding, completing and removing tasks,
the task list, and saving/loading tasks from disk.

## Scope
- Add task (title, priority, tags)
- Complete task and remove task (by id)
- Pending-task list and average priority
- Persistence (`save_tasks` / `load_tasks`, `tasks.json`)
- Out of scope: the web UI (covered by the separate UI session, Part 2 of `session_notes.md`)

## Target
`app/tasks.py` (the functions behind the Task Manager)

## Time-box
- Part 1 (code-level probes): run by script, `probe_session.py`
- Part 2 (UI session): 45 minutes, timed by you

## Heuristics
- SFDIPOT (Structure, Function, Data, Interfaces, Platform, Operations, Time)
- Boundary values
- Error handling and invalid input
- Sequences of operations (add, remove, add)
