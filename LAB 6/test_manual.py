"""Manually written tests with exact assertions and edge cases."""
import datetime
import pytest
from app.tasks import find_task_by_title, remove_task

try:
    from app.storage import days_until_due
except ImportError:  
    days_until_due = None

needs_storage = pytest.mark.skipif(days_until_due is None, reason="app.storage not available")


def test_find_task_by_title_returns_correct_task():
    tasks = [{"id": 1, "title": "A"}, {"id": 2, "title": "B"}]
    result = find_task_by_title(tasks, "B")
    assert result is not None
    assert result["id"] == 2
    assert result["title"] == "B"


def test_find_task_by_title_returns_none_when_missing():
    tasks = [{"id": 1, "title": "A"}]
    assert find_task_by_title(tasks, "Z") is None


def test_find_task_by_title_empty_list():
    assert find_task_by_title([], "A") is None


def test_find_task_by_title_returns_first_of_duplicates():
    tasks = [{"id": 1, "title": "A"}, {"id": 2, "title": "A"}]
    assert find_task_by_title(tasks, "A")["id"] == 1


def test_remove_task_removes_correct_task():
    tasks = [{"id": 1, "title": "A"}, {"id": 2, "title": "B"}]
    remove_task(tasks, 1)
    assert len(tasks) == 1
    assert tasks[0]["id"] == 2


def test_remove_task_nonexistent_id():
    tasks = [{"id": 1, "title": "A"}]
    remove_task(tasks, 99)
    assert len(tasks) == 1  


def test_remove_task_empty_list():
    
    tasks = []
    remove_task(tasks, 1)
    assert tasks == []


@needs_storage
def test_days_until_due_future_date():
    future = (datetime.datetime.now() + datetime.timedelta(days=10)).strftime("%Y-%m-%d")
    assert days_until_due(future) == 10


@needs_storage
def test_days_until_due_past_date():
    past = (datetime.datetime.now() - datetime.timedelta(days=5)).strftime("%Y-%m-%d")
    assert days_until_due(past) == -5
