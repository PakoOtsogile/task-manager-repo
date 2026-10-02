"""AI-generated tests (sample from the lab; replace with your assistant's actual output)."""
import pytest
from app.tasks import find_task_by_title, remove_task

try:
    from app.storage import days_until_due
except ImportError: 
    days_until_due = None

needs_storage = pytest.mark.skipif(days_until_due is None, reason="app.storage not available")


def test_find_task_by_title_found():
    tasks = [{"id": 1, "title": "A"}, {"id": 2, "title": "B"}]
    assert find_task_by_title(tasks, "A")["id"] == 1


def test_find_task_by_title_not_found():
    tasks = [{"id": 1, "title": "A"}]
    assert find_task_by_title(tasks, "Z") is None


def test_remove_task():
    tasks = [{"id": 1, "title": "A"}, {"id": 2, "title": "B"}]
    remove_task(tasks, 1)
    assert len(tasks) == 1


@needs_storage
def test_days_until_due():
    result = days_until_due("2030-01-01")
    assert result > 0
