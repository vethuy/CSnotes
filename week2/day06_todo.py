"""Week 2 . Day 6 . day06_todo.py - JSON-backed to-do list.

RUN THE PROGRAM:   python week2/day06_todo.py list
                   python week2/day06_todo.py add "read chapter 3"
                   python week2/day06_todo.py done 1
                   python week2/day06_todo.py remove 2
RUN THE CHECKS:    python week2/day06_todo.py --check

REQUIREMENTS
------------
* Storage is week2/data/day06_todos.json, a JSON array of objects:
      [{"id": 1, "text": "read chapter 3", "done": false}]
  The path is fixed and resolved from this file, so the program works from any
  folder. save() creates the data folder when it is missing.
* load(path) returns [] when the file does not exist. A file that exists but
  holds broken JSON raises json.JSONDecodeError - it is not silently replaced.
* Every function except main() returns a value. main(argv) prints and returns
  the exit code: 0 success, 1 usage error or unknown id.
* ids are never reused while a task with a higher id exists:
  new id = max(existing ids, default 0) + 1.
* render([]) returns "" ; otherwise one "[x] <id>. <text>" line per task,
  join with "\\n", no trailing newline.

COMMANDS
--------
    list              print every task, or "No tasks yet."
    add <text>        append with the next id, print "Added <id>"
    done <id>         mark as done, print "Updated <id>"
    remove <id>       delete it, print "Removed <id>"
    <id> not a number or unknown   print "No task with id <what>" (or a usage
                                    line for an unknown command), return 1

ACCEPTANCE - run these six, in this order, from the CSnotes folder.
Delete week2/data/day06_todos.json before you start.

 1  python week2/day06_todo.py list                     -> No tasks yet.
 2  python week2/day06_todo.py add "read chapter"
    python week2/day06_todo.py add "write drills"       -> Added 1 / Added 2
 3  python week2/day06_todo.py list                     -> two "[ ]" lines, 1 then 2
 4  python week2/day06_todo.py done 1
    python week2/day06_todo.py list                     -> "[x] 1. read chapter"
 5  python week2/day06_todo.py remove 2
    python week2/day06_todo.py list                     -> only task 1
 6  python week2/day06_todo.py done 99                  -> No task with id 99, exit 1

Then: python -c "import json;print(json.load(open('week2/data/day06_todos.json')))"
and run every command a second time - the state must survive.
"""

import json
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parent / "data"
TODOS = DATA / "day06_todos.json"


def load(path):
    """Return the task list stored at path, or [] when path does not exist."""
    raise NotImplementedError("load")


def save(path, items):
    """Write items to path as JSON, indent=2, creating the folder if needed."""
    raise NotImplementedError("save")


def add(items, text):
    """Return a new list with text appended, done=False, next free id."""
    raise NotImplementedError("add")


def complete(items, task_id):
    """Return a new list with task_id marked done.

    Raises ValueError("No task with id <task_id>") when the id is unknown.
    """
    raise NotImplementedError("complete")


def remove(items, task_id):
    """Return a new list without task_id.

    Raises ValueError("No task with id <task_id>") when the id is unknown.
    """
    raise NotImplementedError("remove")


def render(items):
    """Return the printable form of items: "[x] 1. text" lines joined by \\n."""
    raise NotImplementedError("render")


def main(argv):
    """Dispatch one command from argv, print the result, return the exit code."""
    raise NotImplementedError("main")


# --------------------------------------------------------------------------
# CHECKS - do not edit below this line
# --------------------------------------------------------------------------
def run_checks():
    # add
    assert add([], "a") == [{"id": 1, "text": "a", "done": False}]
    two = add(add([], "a"), "b")
    assert [task["id"] for task in two] == [1, 2]
    assert add([{"id": 7, "text": "x", "done": True}], "y")[1]["id"] == 8
    original = []
    add(original, "a")
    assert original == [], "add must not modify the list it receives"

    # complete
    tasks = [{"id": 1, "text": "a", "done": False}]
    assert complete(tasks, 1) == [{"id": 1, "text": "a", "done": True}]
    assert tasks[0]["done"] is False, "complete must return a new list"
    try:
        complete(tasks, 99)
    except ValueError as exc:
        assert "99" in str(exc)
    else:
        raise AssertionError("complete must raise ValueError for an unknown id")

    # remove
    tasks = [
        {"id": 1, "text": "a", "done": False},
        {"id": 2, "text": "b", "done": True},
    ]
    assert remove(tasks, 1) == [{"id": 2, "text": "b", "done": True}]
    assert len(tasks) == 2, "remove must return a new list"
    try:
        remove(tasks, 99)
    except ValueError:
        pass
    else:
        raise AssertionError("remove must raise ValueError for an unknown id")

    # render
    assert render([]) == ""
    assert render([{"id": 1, "text": "a", "done": False}]) == "[ ] 1. a"
    assert render([{"id": 2, "text": "b", "done": True}]) == "[x] 2. b"
    assert render(
        [
            {"id": 1, "text": "a", "done": False},
            {"id": 2, "text": "b", "done": True},
        ]
    ) == "[ ] 1. a\n[x] 2. b"

    # load on a missing file
    assert load(DATA / "no_such_todos.json") == []

    print("all checks pass")


if __name__ == "__main__":
    if "--check" in sys.argv[1:]:
        run_checks()
    else:
        sys.exit(main(sys.argv[1:]))
