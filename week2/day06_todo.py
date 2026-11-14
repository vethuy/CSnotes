"""Week 2 project - a to-do CLI that survives between runs.

RUN THE CHECKS
    python week2/day06_todo.py --check

USE IT (from the repo root, C:\\Users\\User\\computer science\\CSnotes)
    python week2/day06_todo.py list
    python week2/day06_todo.py add "read chapter 3"
    python week2/day06_todo.py done 1
    python week2/day06_todo.py remove 2

RULES
 1. Your functions RETURN a value. Only `main` prints. If a function prints,
    the checks cannot see its answer and the program cannot be tested.
 2. `add`, `complete` and `remove` return a NEW list. They must not change the
    list they were given - the checks look for that.
 3. A missing file is an empty list, not an error. Only a broken file is an
    error, and `load` lets that error out.
 4. An unknown task id is a ValueError with the number in the message.
 5. Work in the order given in PROJECT_weekend.md. Run --check after every
    function you finish; do not write all seven and then run it once.

THE POINT
 The whole week in one file: list of dicts in memory, json on disk, id as an
 int, messages as strings, ValueError at the edge, exit code at the top.

LOAD
 Deadline: Sat 21 Nov, 11:45. Yesterday's drills are the parts shelf - steal
 from them, that is not cheating, that is remembering.
"""

import json
import sys
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent / "data" / "day06_todos.json"


# --------------------------------------------------------------------------
# 1. disk
# --------------------------------------------------------------------------
def load(path):
    """Return the list of task dicts stored at path.

    Missing file      -> []          (first run is not an error)
    Broken JSON       -> let json raise; do not swallow it
    """
    raise NotImplementedError("load")


def save(path, items):
    """Write items to path as JSON.

    - indent=2 so the file is readable and diff-friendly
    - create the parent folder if missing (Path.parent.mkdir(parents=True,
      exist_ok=True))
    - return None
    """
    raise NotImplementedError("save")


# --------------------------------------------------------------------------
# 2. the list of dicts
# --------------------------------------------------------------------------
def add(items, text):
    """Return a NEW list with one more task.

    New task: {"id": max existing id + 1 (0 if empty), "text": text,
               "done": False}
    """
    raise NotImplementedError("add")


def complete(items, n):
    """Return a NEW list where the task with id n has done=True.

    Unknown n -> raise ValueError("No task with id 99")   (f-string it)
    """
    raise NotImplementedError("complete")


def remove(items, n):
    """Return a NEW list without the task whose id is n.

    Unknown n -> raise ValueError with the number in the message.
    """
    raise NotImplementedError("remove")


# --------------------------------------------------------------------------
# 3. text out
# --------------------------------------------------------------------------
def render(items):
    """Return the whole list as one string.

    []            -> "No tasks yet."
    two tasks     -> "[ ] 1. read chapter\\n[ ] 2. write drills"
    done task     -> "[x] 1. read chapter"
    """
    raise NotImplementedError("render")


# --------------------------------------------------------------------------
# 4. the front door
# --------------------------------------------------------------------------
def main(argv):
    """Run one command from the command line and return an exit code.

    argv is sys.argv[1:], e.g. ["add", "buy milk"] or ["done", "1"].
    An optional "--path", P overrides DATA_PATH (the checks rely on it).

    list           -> print render(load(path))            return 0
    add TEXT       -> save, print "Added <id>"            return 0
    done N         -> save, print "Done: <text>"          return 0
    remove N       -> save, print "Removed <id>"          return 0
    ValueError     -> print the message                   return 1
    unknown cmd    -> print "Unknown command: <cmd>"      return 1

    main() is the only function allowed to print. It returns, it never calls
    sys.exit - the last two lines of this file do that.
    """
    raise NotImplementedError("main")


# --------------------------------------------------------------------------
# CHECKS - do not edit below this line
# --------------------------------------------------------------------------
def _check():
    import io
    import tempfile
    from contextlib import redirect_stdout

    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "nested" / "todos.json"

        assert load(path) == []
        assert render([]) == "No tasks yet."

        items = add(load(path), "read chapter")
        items = add(items, "write drills")
        assert [t["id"] for t in items] == [1, 2]
        assert all(t["done"] is False for t in items)
        assert items[1]["text"] == "write drills"
        assert render(items) == "[ ] 1. read chapter\n[ ] 2. write drills"

        save(path, items)
        assert path.exists(), "save must create the data folder"
        assert load(path) == items
        assert json.loads(path.read_text(encoding="utf-8")) == items

        done = complete(items, 1)
        assert done[0]["done"] is True
        assert items[0]["done"] is False, "complete must not change the old list"
        assert render(done).splitlines()[0] == "[x] 1. read chapter"

        after = remove(items, 2)
        assert [t["id"] for t in after] == [1]
        assert len(items) == 2, "remove must not change the old list"

        for func in (complete, remove):
            try:
                func(items, 99)
                assert False, f"{func.__name__} must raise ValueError for id 99"
            except ValueError as exc:
                assert "99" in str(exc), f"message must name the id: {exc}"

        buf = io.StringIO()
        with redirect_stdout(buf):
            code = main(["list", "--path", str(path)])
        assert code == 0
        assert buf.getvalue().strip() == "[ ] 1. read chapter\n[ ] 2. write drills"

        buf = io.StringIO()
        with redirect_stdout(buf):
            code = main(["done", "99", "--path", str(path)])
        assert code == 1, "a bad id is a program failure, so the code is 1"
        assert "99" in buf.getvalue()

        buf = io.StringIO()
        with redirect_stdout(buf):
            code = main(["dance", "--path", str(path)])
        assert code == 1

    print("all project checks pass")


if __name__ == "__main__":
    if sys.argv[1:] == ["--check"]:
        _check()
    else:
        sys.exit(main(sys.argv[1:]))
