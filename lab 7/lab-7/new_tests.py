"""Lab 7: new tests written to kill the mutants that survived the combined suite."""
from app import tasks as tasks_module
from app.tasks import add_task


def test_tasks_file_default_name():
    # Kills mutants 1 and 2: other tests monkeypatch TASKS_FILE, so the real default was never checked
    assert tasks_module.TASKS_FILE == "tasks.json"


def test_add_task_stores_given_tags():
    # Kills mutant 13: the "tags" key was never read back
    task = add_task([], "Write report", priority=2, tags=["work", "urgent"])
    assert task["tags"] == ["work", "urgent"]
    assert set(task) == {"id", "title", "priority", "tags", "done"}
