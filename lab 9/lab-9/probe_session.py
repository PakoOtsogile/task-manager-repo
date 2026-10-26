"""Lab 9: exploratory probe session against app/tasks.py (run from the repo root).

Each probe tries an input an ordinary test would not, and prints what actually happened.
Run: python probe_session.py
"""
import json, os, tempfile, warnings
from app import tasks as t

os.chdir(tempfile.mkdtemp())  # tasks.json is relative to the working directory


def probe(n, idea, title, fn):
    try:
        out = fn()
        print(f"P{n:02d} [{idea}] {title}\n     -> {out!r}")
    except Exception as e:
        print(f"P{n:02d} [{idea}] {title}\n     -> RAISED {type(e).__name__}: {e}")


def add_two_remove_one():
    ts = []
    for name in "ABC":
        t.add_task(ts, name)
    t.remove_task(ts, 2)
    t.add_task(ts, "D")
    return [(x["id"], x["title"]) for x in ts]


def complete_dup_id():
    ts = []
    for name in "ABC":
        t.add_task(ts, name)
    t.remove_task(ts, 2)
    t.add_task(ts, "D")  # gets id 3 again
    t.complete_task(ts, 3)
    return [(x["id"], x["title"], x["done"]) for x in ts]


def shared_tags():
    a = t.add_task([], "a"); a["tags"].append("x")
    b = t.add_task([], "b")
    return b["tags"]


def corrupt_file():
    open("tasks.json", "w").write("{not json")
    return t.load_tasks()


def empty_file():
    open("tasks.json", "w").write("")
    return t.load_tasks()


def non_json_tags():
    return t.save_tasks([{"id": 1, "tags": {"a", "b"}}])


def unclosed_handle():
    t.save_tasks([{"id": 1, "title": "x", "priority": 1, "tags": [], "done": False}])
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        t.load_tasks()
        import gc; gc.collect()
    return [str(x.category.__name__) for x in w]


def unicode_roundtrip():
    data = [{"id": 1, "title": "Café ☕ 日本語", "priority": 1, "tags": [], "done": False}]
    t.save_tasks(data)
    return t.load_tasks() == data


# ---- S: Structure / F: Function ----
probe(1, "F", "add_task with empty title", lambda: t.add_task([], "")["title"])
probe(2, "F", "add_task with whitespace-only title", lambda: t.add_task([], "   ")["title"])
probe(3, "D", "add_task with 1000-character title", lambda: len(t.add_task([], "x" * 1000)["title"]))
probe(4, "D", "add_task with priority -5", lambda: t.add_task([], "a", priority=-5)["priority"])
probe(5, "D", "add_task with priority 'high' (string)", lambda: t.add_task([], "a", priority="high")["priority"])
probe(6, "D", "average_priority after adding a string priority",
      lambda: t.average_priority([t.add_task([], "a", priority=1), t.add_task([], "b", priority="high")]))
probe(7, "D", "add_task with title None", lambda: t.add_task([], None)["title"])
# ---- D: Data / I: Interfaces ----
probe(8, "I", "complete_task with string id '1'",
      lambda: t.complete_task([{"id": 1, "done": False}], "1"))
probe(9, "I", "complete_task with True as id (True == 1)",
      lambda: t.complete_task([{"id": 1, "done": False}], True))
probe(10, "I", "complete_task with float id 1.0",
      lambda: t.complete_task([{"id": 1, "done": False}], 1.0))
probe(11, "F", "remove_task with nonexistent id (silent?)",
      lambda: (lambda ts: (t.remove_task(ts, 99), len(ts)))([{"id": 1}]))
probe(12, "F", "find_task_by_title is case-sensitive",
      lambda: t.find_task_by_title([{"title": "Buy milk"}], "buy milk"))
probe(13, "F", "get_pending_tasks on a task missing the 'done' key",
      lambda: t.get_pending_tasks([{"id": 1}, {"id": 2}]))
probe(14, "F", "average_priority of an empty list", lambda: t.average_priority([]))
probe(15, "F", "get_pending_tasks with exactly one pending task",
      lambda: t.get_pending_tasks([{"id": 1, "done": False}]))
# ---- O: Operations / T: Time ----
probe(16, "O", "ids after add, add, add, remove(2), add", add_two_remove_one)
probe(17, "O", "complete_task(3) when two tasks share id 3", complete_dup_id)
probe(18, "S", "default tags list shared between tasks", shared_tags)
# ---- P: Platform / persistence ----
probe(19, "P", "load_tasks with a corrupt tasks.json", corrupt_file)
probe(20, "P", "load_tasks with an empty tasks.json", empty_file)
probe(21, "P", "save_tasks with a non-JSON value (set) in tags", non_json_tags)
probe(22, "P", "warnings raised by load_tasks (unclosed file)", unclosed_handle)
probe(23, "P", "unicode title survives save/load", unicode_roundtrip)


def failed_save_leaves_file():
    t.save_tasks([{"id": 1, "title": "keep me"}])          # a good file on disk
    try:
        t.save_tasks([{"id": 1, "tags": {"a"}}])           # this save fails part-way
    except TypeError:
        pass
    return open("tasks.json").read()


probe(24, "P", "contents of tasks.json after a FAILED save_tasks (was 'keep me')", failed_save_leaves_file)
