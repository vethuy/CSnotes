# Journal

One entry a night, newest at the bottom, under a week heading. Three parts, in
this order, blank line between: **Shipped**, **Bug** (or **Optimization** when
nothing broke), **Learned**. The week-closing entry is a review.before editing
this file. Look Format definition: `CSstudy\RULES-BUILDFORMAT.md` §2.3.

---

## Week 1 — 9–15 Nov 2026

### Day 1 — 2026-11-07 · fizzbuzz, `range`, `continue`

**Shipped:** `week1/day01_fizzbuzz.py`; reading lab 1 (`week1/day01_reading1.py`) **1/1**.

**Bug:** Traced `range(1, 6)` as ending at 6 — it is half-open (1–5), so the odd sum is `(n+1)**2/4`, not `(1+n)*n/4`.

**Learned:**
- `continue` skips the rest of one iteration, not the loop.
- A function should `return` and let the caller print.
- `range` excludes its stop value, so `range(1, 6)` walks 1–5.

### Day 2 — 2026-11-08 · grade calculator, `elif` chains

**Shipped:** `week1/day02_grade_calculator.py`.

**Bug:** The `elif` chain repeated conditions already ruled out, and the `except` printed `score` before it existed → `UnboundLocalError` on `abc`.

**Learned:**
- An `elif` already carries the negation of every branch above it.
- `except ValueError` catches only that class.
- Return `None` for "no grade" — `'reject'` is a truthy string.

### Day 3 — 2026-11-09 · temperature converter, validation

**Shipped:** `week1/day03_temperature.py`.

**Bug:** `mode(user)` got the string `"1"` instead of `1` (`"1" == 1` is `False`) and the program exited silently, and a `None` from the error branch reached the arithmetic.

**Learned:**
- `try` does not prevent the raise; it stops the raise ending the program.
- A failed `int()` aborts before assigning, so the name never exists.
- Keep the value a validator returns — `check_float(c)`'s result was thrown away.

### Day 4 — 2026-11-10 · leap year, bool vs string

**Shipped:** `week1/day04_leap_year.py`.

**Bug:** `is_leap` returned the strings `'True'`/`'False'`; output looked identical, but `bool('False')` is `True`, so `if is_leap(1900):` took the wrong branch.

**Learned:**
- A value's type is not its printout — check `type()`/`repr()`.
- `if X: return True` / `else: return False` is just `return X`.
- Keep decide (`True`/`False`) separate from render (words).

### Day 5 — 2026-11-11 · `datetime` internals

**Shipped:** `week1/day05_days_between.py`; reading lab 2 (`week1/day05_reading2.py`) **4/5**.

**Optimization:** Drop `main(0)`'s counter for `while len(dates) < 2`, and make `parse_date` return a date instead of printing it.

**Learned:**
- A date is a number in a costume — `d2 - d1` → `timedelta`, `.days` → `int`.
- `_DAYS_BEFORE_MONTH` is a non-leap table; the Feb 29 day is added at lookup when `month > 2`.
- `if __name__ == "__main__":` is a launch switch — `__name__` is `"__main__"` only when the file runs directly.

### Day 6 — 2026-11-13 · polish and Caesar cipher

**Shipped:** re-asks and validation on `week1/day01`–`day05`; reading lab 3 (`week1/day06_reading3.py`) **5/5**.

**Bug:** `day02` called `grade(a)` with the raw string instead of `grade(score)` → `TypeError` on valid input only; `day05` imported `datetime` but used `date.fromisoformat` → `NameError`, which `except ValueError` does not catch.

**Learned:**
- A validator is only as strict as the type it parses into — `datetime` accepts `2026-11-09 23:00`, `date` rejects it.
- `encode` builds a new string because strings are immutable, and `% 26` wraps any number back into a letter.
- `decode` is one line because `-shift` travels through the same `% 26` — Python's modulo is never negative.

### Week 1 review — 2026-11-13

- **What shipped this week?** 5 programs — `day01_fizzbuzz.py`, `day02_grade_calculator.py`, `day03_temperature.py`, `day04_leap_year.py`, `day05_days_between.py` — plus 3 reading labs **10/11**.
- **What confused me most this week?** Day 5: `_days_before_month(month, year)` and `+ (month > 2 and _is_leap(year))` — the `datetime` module-level loop needed outside sources.
- **What is the #1 goal for Week 2?** Finish the tasks on time.

---

## Week 2 — 16–22 Nov 2026

### Day 1 — 2026-11-15 · `second_largest`, `rotate_left`, `remove_duplicates`

**Shipped:** `week2/day01_drill01.py` prints `all drills pass`; reading lab 1 `week2/day01_readinglab1.py` **4/4**.

**Bug:** `second_largest` guards on `len(nums) <= 2` when the contract is fewer than two distinct values, so `[1, 2]` returns `None` and `[9, 9, 9]` returns `9` — both outside the check block.

**Learned:**
- The check block is a sample and the docstring is the spec — write the `[1, 2]` and `[9, 9, 9]` asserts yourself.
- A `raise NotImplementedError` left after a `return` can never run — it is a comment pretending to be a guard.
- `total / len(nums)` is true division: `6 / 3` is `2.0`, and `2.0 == 2` is `True`.

### Day 2 — 2026-11-16 · `sorted` keys and ties

**Shipped:** `week2/day02_drill02.py` prints `all drills pass`; reading lab 2 `week2/day02_readinglab2.py` **2/4**.

**Bug:** `counts.items` without `()` sorted a method object (`TypeError: 'builtin_function_or_method' object is not iterable`), `pair += (i, counts[i],)` flattened the pairs, and `sorted(...)` was never assigned, so `top_n` fell through to `raise NotImplementedError`.

**Learned:**
- A key function is a ruler — `sorted` compares what the key returns and returns the original items, so `(-x[1], x[0])` means count descending, word ascending.
- `reverse=True` flips the comparison, not the finished list — equal keys are never compared, so stability keeps their arrival order.
- `get(k, default)` returns the default and never writes to the dict.

### Day 3 — 2026-11-16 · set algebra, hash order

**Shipped:** `week2/day03_drill03.py` prints `all drills pass`; reading lab 3 `week2/day03_readinglab3.py` **3/4**.

**Bug:** `set={}` was an empty dict, so `.add` died with `AttributeError: 'dict' object has no attribute 'add'`; then `set.add('word')` called the method on the built-in type and passed the literal string → `TypeError: descriptor 'add' for 'set' objects doesn't apply to a 'str' object`.

**Learned:**
- `{}` is a dict and Python has no empty-set literal, so a set starts life as `set()`.
- A set operator hands back a set, and `sorted()` is the only step that turns it into the ordered list.
- `set([3, 1, 2, 1])` removes duplicates at construction — `list()` only wraps what is already there.

### Day 4 — 2026-11-17 · files and `csv.DictReader`

**Shipped:** `week2/day04_drill04.py` prints `all drills pass`; reading lab 4 `week2/day04_readinglab4.py` **1/4**.

**Bug:** `float = []` shadowed the builtin (`TypeError: 'list' object is not callable`), and `if line != '' or line[0] != '#'` indexed `''` (`IndexError: string index out of range`); `longest_line` mixed words with lengths (`TypeError: '>' not supported between instances of 'int' and 'str'`), and a module-level `raise NotImplementedError` killed the file on import.

**Learned:**
- Never name a variable after a function you still have to call — the local wins for the whole function, even on lines above the assignment.
- Filter before you convert: strip, test blank, test `#`, then `float(line)` inside a `try`.
- `csv.DictReader` gives a dict per row keyed by the header — a short row fills `restval`, a long row hides surplus under `restkey`.

### Day 5 — 2026-11-18 · `json.loads` and validation

**Shipped:** `week2/day05_drill05.py` prints `all drills pass`; reading lab 5 `week2/day05_readinglab5.py` **3/5**.

**Bug:** `raise a` tried to raise the float (`TypeError: exceptions must derive from BaseException`), then the rewritten `except` built its message from the unassigned `a` (`UnboundLocalError`). `if i.strip == "":` compared the method object, so the skip never fired and `tally("")` returned `(0, [''])`.

**Learned:**
- `raise` wants an exception object built from names that exist on the failing path — `text`, not the conversion result that just failed.
- `s.strip` is the method and `s.strip()` is its result — a missing `()` makes a comparison that is always false.
- `JSONDecodeError` subclasses `ValueError` (`json/decoder.py:353`), and its `lineno`/`colno` are 1-based.

### Day 6 — 2026-11-20 · to-do CLI

**Shipped:** `week2/day06_todo.py` — `load`, `save`, `add`, `complete`, `remove`, `render`, `main(argv)`; `python week2/day06_todo.py --check` prints `all project checks pass`.

**Bug:** `main` first called `complete(argv)` with the whole argument list (`TypeError: complete() missing 1 required positional argument: 'n'`), then passed the id as the string `"1"` while `complete` compares it to an `int` — `1 == "1"` is `False`, so an existing task answered `No task with id 1`; the check only tries id `99`, which does not exist.

**Learned:**
- The check block is a sample and the docstring is the spec.
- The `try/except ValueError` wall turns a `raise` into `print(str(exc)); return 1` instead of a traceback.
- An argument parsed twice is an argument parsed wrong once.

### Week 2 practice — 2026-11-21 · five functions, docstrings as spec

**Shipped:** `week2/Week2_practice.py` — `compress_runs`, `group_by_length`, `missing_from`, `word_counts`, `parse_config`; the 25 asserts in the check block were verified one at a time.

**Bug:** Every docstring was written under its body, so all five `__doc__` were `None` and the five `raise NotImplementedError` lines could never run; `missing_from` returned `sorted(...)`, so `(["c", "a"], [])` gave `['a', 'c']` where the contract asks for first's order.

**Learned:**
- The docstring is the spec and the check block is a sample — a docstring goes directly under `def`.
- A function whose answer is "in this order" must build that order, because `sorted` answers a different question.
- A sample that never varies its input catches nothing — the check only fed alphabetical input.

### Week 2 review — 2026-11-21

- **What shipped this week?** 5 drills — `week2/day01_drill01.py` to `week2/day05_drill05.py`, 15 functions, each `all drills pass` — 5 reading labs **13/21** (4/4, 2/4, 3/4, 1/4, 3/5), `week2/day06_todo.py` (`python week2/day06_todo.py --check` → `all project checks pass`), `week2/Week2_practice.py` (5 functions, 25 asserts), README week-2 table, 9 commits (15–21 Nov).
- **What confused me most this week?** Code I did not write: the lab predictions scored 13/21, worst on `csv.DictReader` (1/4) — a short row filling `restval` and a long row hiding its surplus under `restkey`, which only made sense after I ran it.
- **What is the #1 goal for Week 3?** — keep going and finish on time.

---

## Week 3 — 23–29 Nov 2026

### Day 1 — 2026-11-22 · defaults, keywords, a clean return

**Shipped:** `week3/day01_drill01.py` prints `all drills pass`; reading lab 1 `week3/day01_readinglab1.py` **3/5**.

**Bug:** `merge_prefs` opened with `if user == {}: return base` (`week3/day01_drill01.py:73`), so an empty `user` handed back the caller's own dict and `merge_prefs({})` returned `None` — both against the docstring; deleting the branch and always copying `base` then updating from `user` fixed it. The check block never saw it, because it never calls `merge_prefs` with an empty `user`.

**Learned:**
- A name is local because the body assigns to it, not because you read a global — `write_label` shadows the module's `label`, and `bump`'s `count = count + 1` reads a local that does not exist yet (`UnboundLocalError`).
- A default list is built once at `def`, so every call mutates the same object: `add_tag('b')` returns `['a', 'b']`.
- The docstring is the spec and the check block is a sample — a branch that returns the argument itself is the bug the asserts cannot see.

### Day 2 — 2026-11-22 · modules, imports, a hidden default

**Shipped:** `week3/day02_drill02.py` prints `all drills pass`; reading lab 2 `week3/day02_readinglab2.py` **3/5**.

**Bug:** `simplify` returned floats — `(3.0, 4.0)` — because it divided with `/` (`week3/day02_drill02.py:33`) while the docstring asks for ints; every assert still passed, since `3.0 == 3`, and `//` fixed it. In `is_palindrome`, `final[::1]` copied the string forward instead of reversing it, so the function answered `True` for every input — the first check that noticed was `is_palindrome("hello") is False`, the first one expecting `False`.

**Learned:**
- `s.split(None)` splits on any run of whitespace and drops the empty pieces, which is why `capwords("hello   world")` keeps one space and `capwords("  spam  ")` loses both ends — the surprise is the *missing* `sep` argument, not `sep or ' '`.
- In a slice the step is the direction — `[::-1]` walks backwards, `[::1]` is a copy — and five asserts that all expect `True` cannot tell a working palindrome check from one that says `True` to everything.
- `x.method` is the function and `x.method()` is its result; `.casefold` without the parens left a method object, and slicing it raised `TypeError: 'builtin_function_or_method' object is not subscriptable`.

### Day 3 — 2026-11-23 · pure functions, `sorted` on a copy

**Shipped:** `week3/day03_drill03.py` prints `all drills pass`; reading lab 3 `week3/day03_readinglab3.py` **4/5**.

**Optimization:** read the cited stdlib lines before predicting — `Lib\statistics.py:637` had the exact message `no median for empty data`, and the one I took from the internet was wrong.

**Learned:**
- `sorted(x)` returns a new list in ascending order, while `x.sort()` returns `None` and reorders the caller's list — that one choice is what makes `median` pure.
- `StatisticsError` is a `ValueError` subclass, so `except ValueError` catches it, and `median([])` raises it as `no median for empty data`.
- `items + extra` and a list comprehension already build a new list, so `append_all` and `with_tax` were one expression, not an accumulator loop.

### Day 4 — 2026-11-23 · tests as specs, boundaries, one green lie

**Shipped:** `week3/day04_drill04.py` prints `all drills pass`; reading lab 4 `week3/day04_readinglab4.py` **5/5**.

**Bug:** `parse_bool("maybe")` raised `ValueError(text, 'is not a boolean express')` — two arguments, so `str(exc)` was the tuple repr `"('maybe', 'is not a boolean express')"`, not a sentence; one f-string fixed it. `grade(101)`'s message was `101is not a acceptable score` — the f-string glued the score to the words — and no assert could see it, because the check only asks for `ValueError`.

**Learned:**
- `ValueError(a, b)` stores two arguments and `str(exc)` shows the tuple, so a message is built by joining inside the call, not by passing the parts.
- A test is only as strict as its expected value: `chunk("abcd", 2) == ["ab", "cd"]` passes because the expectation was copied from the output, not from the docstring — the pieces are `str`, and only a test that demands a `list` would have failed.
- Q: which of the five tests passes for the wrong reason? A: `test_chunk_string` — slicing a `str` yields `str`, so a stricter test would assert every chunk is a `list`, or that `chunk("abcd", 2)` raises, since the docstring says `items` is a list.

### Day 5 — 2026-11-24 · three bugs that run, one traceback walk

**Shipped:** `week3/day05_drill05.py` prints `all drills pass`; reading lab 5 `week3/day05_readinglab5.py` **5/5**.

**Bug:** `running_total` returned the caller's list because `out = nums` copied the name and not the list, and `list(nums)` fixed it; `bump` raised `UnboundLocalError: cannot access local variable 'count' where it is not associated with a value` because its `count = count + 1` made the name local, and `nonlocal count` moved it one scope out; `add_label`'s default `[]` was built once at `def` time, so the second no-arg call returned `['a', 'b']`, and a `None` sentinel plus a copy fixed it.

**Learned:**
- A function assigns a name for its whole body — `count = count + 1` inside `bump` made `count` local before the first line ran, so the read raised `UnboundLocalError` — and `nonlocal` is the compile-time promise that the name belongs to the enclosing function.
- Default arguments are evaluated once when the `def` runs and live on `add_label.__defaults__`, so a mutable default is one object shared by every call that omits it; `None` plus a fresh list inside is the fix.
- Q: `best` is the function you call, but which function does the traceback blame? A: `parse_line` — walking `exc.__traceback__` to `tb_next is None` leaves the innermost frame, and its `tb_frame.f_code.co_name` and `tb_lineno` name the line where the value went bad (`:19` unpack, `:20` `int()`).

### Day 6 — 2026-11-25 · to-do data as pure functions, ten tests

**Shipped:** `week3/day06_tools.py` (seven functions, `new_id` … `parse_command`) and `week3/day06_test_tools.py`; `python -m pytest week3/day06_test_tools.py` → `10 passed`.

**Bug:** `parse_command(["done"])` raises `IndexError: list index out of range` at `week3/day06_tools.py:164` — `argv[1]` is read before it is known to exist, while the docstring asks for `ValueError` on a missing id.

**Learned:**
- `list(tasks)` copies the outer list only, so `target['done'] = True` edited the caller's task; `{**i, 'done': True}` built the new dict the returned list needed.
- `type("3") == int` is `False` — words from the command line are always `str`, so "a whole number" is proved by `int()` inside a `try`, not by a type test.
- Q: why did the `add` test pass while returning only the first word? A: it typed one word, so `' '.join(argv[1:])` was never exercised.

### Week 3 review — 2026-11-25

- **What shipped this week?** 5 drills — `week3/day01_drill01.py` to `week3/day05_drill05.py`, 15 functions, each `all drills pass` — 5 reading labs **20/25** (3/5, 3/5, 4/5, 5/5, 5/5), `week3/day06_tools.py` + `week3/day06_test_tools.py` (`10 passed`), the README week-3 tables, and 6 journal entries (22–25 Nov). The day-6 pair is not committed yet, so the `week03` branch, PR and issue are still open.
- **What confused me most this week?** `list(tasks)` — a copy whose dicts were still the caller's, so `target['done'] = True` changed a list I thought I had protected; and `argv` from the command line, where every word is a `str`, so `type("3") == int` is never true.
- **What is the #1 goal for Week 4?**keep motivation!

## Week 4 — 30 Nov–6 Dec 2026

### Day 1 — 2026-11-25 · linear scan, binary halving, the sorted precondition

**Shipped:** `week4/day01_drill01.py` prints `all drills pass`; reading lab 1 `week4/day01_readinglab1.py` **7/7**.

**Bug:** `binary_search([1, 3, 5, 7], 8)` raised `IndexError: list index out of range` at `week4/day01_drill01.py:47` — `high = len(items)` was one past the last index, so `mid` could equal `len(items)`, and the check block never asked for a target past the end. Earlier `area = list[items]` was a type alias, not a copy, so `len(area)` raised `TypeError: object of type 'types.GenericAlias' has no len()` at `:44`, and `low = middle` / `high = middle` kept the window the same size and looped forever on a miss.

**Learned:**
- Q: why `while lo < hi` and not `<=`? A: with `<=` on an absent target, `lo == hi` still enters, `mid == lo`, and `hi = mid` leaves the window unchanged — an infinite loop.
- Q: in `[1, 3, 3, 3, 7]`, why does `bisect_left` return `1` and not a later `3`? A: equality sets `hi = mid`, keeping the match inside the window and searching the left half again.
- A window is either half-open (`hi = len(items)`, `lo < hi`) or inclusive (`hi = len(items) - 1`, `lo <= hi`); mixing the two puts `mid` past the last index.

### Day 2 — 2026-11-26 · bubble sort, the comparison count, shrinking passes

**Shipped:** `week4/day02_drill02.py` prints `all drills pass`; reading lab 2 `week4/day02_readinglab2.py` **2/5**.

**Bug:** `old = result` copied the name, not the list, so `result != old` compared a list with itself and the pass loop never ran twice; `while result is not sorted` compared against the builtin function and was always true. `bubble_swaps(result[i], result[i+1])` asked the one-argument function to swap two ints → `TypeError: bubble_swaps() takes 1 positional argument but 2 were given`.

**Learned:**
- A bubble pass over `n` items costs `n-1` comparisons, not 1: on the sorted 4-item input every one of `(1,2)`, `(2,3)`, `(3,4)` is compared before `swapped` stays `False` and `break` fires — the miss in lab 2 line 1 (**1/5** on that line) and again in Q5, where sorted 8 items cost **7**, not the `28` of the worst case.
- Q: why is one pass shorter than the last? A: after pass `i` the largest `i+1` items are already at the end, so `range(len(values) - 1 - i)` skips a pair that cannot swap — and this is what turns the worst case into `n(n-1)/2`.
- The `break` is the O(n)-on-sorted saving and `- i` is not: the shrinking range alone still sweeps a second pass on sorted data, so Q4's "which line makes the difference" is `if not swapped: break`.
