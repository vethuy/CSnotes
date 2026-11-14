# Weekend project — `week2/day06_todo.py`

A to-do list that is still there tomorrow. Four commands, one file, JSON on disk.
The scaffold already gives you the file, the seven names, the contracts and the
checks. You write the seven bodies. Nothing else.

**Done when:** `python week2/day06_todo.py --check` prints `all project checks pass`
and the six-command acceptance table below runs clean in a fresh terminal.

---

## Saturday 09:30–12:30 (3 h)

### 09:30–09:40 · Read the scaffold (10 min)

1. Open `week2/day06_todo.py`. Read the header, then the seven stubs.
2. Run it once, exactly as is:

   ```powershell
   cd "C:\Users\User\computer science\CSnotes"
   python week2/day06_todo.py --check
   ```

   It stops on `NotImplementedError("load")`. That traceback is your to-do list.
3. On paper write the order you will fill them in:
   `load → render → add → save → complete → remove → main`.
   `main` last, because until the parts work there is nothing for it to call.

### 09:40–10:00 · `load` and `render` (20 min)

- `load`: `try: json.loads(path.read_text())` / `except FileNotFoundError: return []`.
  Do **not** catch `json.JSONDecodeError` - a broken file must blow up loudly.
- `render`: the empty case first (`"No tasks yet."`), then a loop that builds a
  line per task, then `"\n".join(...)`. Look at `[x]` vs `[ ]` - the space matters.

Checks will still fail, but move on: each run of `--check` must fail **one stub
later** than the run before. That is how you know you are winning.

### 10:00–10:20 · `add` and `save` (20 min)

- `add`: `max((t["id"] for t in items), default=0) + 1`, then return
  `items + [new_task]` - a new list, not `items.append(...)`.
- `save`: `path.parent.mkdir(parents=True, exist_ok=True)`, then
  `path.write_text(json.dumps(items, indent=2), encoding="utf-8")`.
  The `nested/` folder in the check exists to prove you created the parent.

### 10:20–10:40 · `main`, `list` and `add` branches (20 min)

`main` is the only printer. Structure it like this and fill the branches:

```python
def main(argv):
    argv = list(argv)
    path = DATA_PATH
    if "--path" in argv:              # the checks pass --path
        i = argv.index("--path")
        path = Path(argv[i + 1])
        del argv[i:i + 2]
    if not argv:
        print("Unknown command: (none)")
        return 1
    cmd, rest = argv[0], argv[1:]
    try:
        items = load(path)
        if cmd == "list":
            print(render(items))
        elif cmd == "add":
            ...
        else:
            print(f"Unknown command: {cmd}")
            return 1
    except ValueError as exc:
        print(str(exc))
        return 1
    return 0
```

Now the CLI is real:

```powershell
python week2/day06_todo.py list                       # No tasks yet.
python week2/day06_todo.py add "read chapter 3"       # Added 1
python week2/day06_todo.py list                       # [ ] 1. read chapter 3
python week2/day06_todo.py add "write drills"         # Added 2
python week2/day06_todo.py list                       # [ ] 1. ... [ ] 2. ...
```

If `add` prints `Added 1` twice, you forgot `save`.

### 10:55–11:15 · `complete` and `remove` (20 min)

- Both start with a lookup helper that raises:
  `raise ValueError(f"No task with id {n}")`.
- Both return new lists: build a new dict with `dict(task, done=True)` for the
  match, and a list comprehension without it for remove.
- Wire `done` and `remove` into `main`, saving before printing.

```powershell
python week2/day06_todo.py done 1        # Done: read chapter 3
python week2/day06_todo.py list          # [x] 1. ...
python week2/day06_todo.py remove 2      # Removed 2
python week2/day06_todo.py done 99       # No task with id 99
$LASTEXITCODE                            # 1
```

### 11:15–11:45 · Prove it (30 min)

Run the six-command acceptance table **in order, twice each**, then:

1. `python week2/day06_todo.py --check` → `all project checks pass`
2. `python -c "import json;print(json.load(open('week2/data/day06_todos.json')))"` → valid JSON
3. Delete `week2/data/day06_todos.json`; `list` must say `No tasks yet.`, not crash.
4. `python week2/day06_todo.py dance` → `Unknown command: dance`, exit 1.

### 11:45–12:15 · Ship (30 min)

- Short README section: what it is, the four commands, one pasted transcript.
- Add `week2/data/` to the repo (the file is part of the deliverable).
- `git add . ; git commit -m "feat: add JSON-backed to-do CLI" ; git push`
- Open the repo on GitHub and check the README renders.

### 12:15–12:30 · Read your own diff (15 min)

`git diff HEAD~1` - not your memory of it. Write one sentence: what would you
do differently, and what is Week 3's first improvement? Put it in `journal.md`.

---

## Sunday 18:00–19:00 (1 h) — review, not new code

1. **18:00–18:40 · Three questions, written down.**
   - What shipped? Files and commands, not feelings.
   - What confused me most? Name the exact line of the project.
   - What is Week 3's #1 goal?
2. **18:40–18:55 · Tidy and record.**
   - `git log --oneline --since="2026-11-16" | Measure-Object -Line`
   - `git status` must be clean; no `__pycache__`, no scratch files.
   - README week-2 table: one row per practice file with its run command.
   - Fill in the Week-2 review at the bottom of `journal.md`; put Week 3's five
     day-tasks in the tracker.
3. **18:55–19:00 · Commit** `docs: week 2 review and README update`, push.

---

## The bug table (you will meet these)

| Symptom | Cause | Fix |
|---|---|---|
| `add` works, next `list` is empty | saved nowhere | call `save` before printing |
| `ValueError: max() arg is an empty sequence` | no `default=0` | `max(..., default=0)` |
| `TypeError: Object of type PosixPath is not JSON serializable` | `json.dump(path)` | `json.dumps(...)` then `path.write_text(...)` |
| Every task has id 1 | you used `len(items) + 1` and removed one | ids come from `max`, never from length |
| `done 1` marks the first row, not id 1 | index vs id | look the task up by `["id"]` |
| Check fails with "must not change the old list" | used `.append` / `del` | build and return new lists |
| `list` prints `None` | forgot `return` | every function hands a value back |

## If you finish early (not required)

- `list --open` shows only unfinished tasks.
- Sort the rendered lines unfinished-first, then by id.
- `export` command that writes the tasks as CSV — you already did that on Thursday.
