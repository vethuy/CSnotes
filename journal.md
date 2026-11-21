# Journal

One entry a night. Three parts, **two lines each**: **Shipped** (the files),
**Bug** (what broke and why), **Learned** (the rule you'd say out loud). No bug
that night? Part 2 becomes **Optimization:** the one change you would make next.
At the end of each week, three questions — name files, not feelings.

---

## Week 1 — 9–15 Nov 2026

### Day 1 — completed at 2026-11-07

**Shipped:** `week1/day01_fizzbuzz.py` + reading lab 1.
**Bug:** traced `range(1, 6)` as ending at 6 — it is half-open (1–5); odd-sum is `(n+1)**2/4`, not `(1+n)*n/4`.
**Learned:** `continue` skips the rest of one iteration, not the loop; a function should `return` and let the caller print.

### Day 2 — completed at 2026-11-08

**Shipped:** `week1/day02_grade_calculator.py`.
**Bug:** the `elif` chain repeated conditions already ruled out; the `except` printed `score` before it existed → `UnboundLocalError` on `abc`.
**Learned:** an `elif` already carries the negation of every branch above it; `except ValueError` catches only that class; return `None` for "no grade" — `'reject'` is a truthy string.

### Day 3 — completed at 2026-11-09

**Shipped:** `week1/day03_temperature.py`.
**Bug:** `mode(user)` got the string `"1"` instead of `1` (`"1" == 1` is False) and the program exited silently; `check_float(c)`'s result was thrown away; a `None` from the error branch reached the arithmetic.
**Learned:** `try` does not prevent the raise, it stops the raise ending the program — a failed `int()` aborts before assigning, so the name never exists.

### Day 4 — completed at 2026-11-10

**Shipped:** `week1/day04_leap_year.py`.
**Bug:** `is_leap` returned the strings `'True'`/`'False'`; output looked identical, but `bool('False')` is `True`, so `if is_leap(1900):` took the wrong branch.
**Learned:** a value's type is not its printout — check `type()`/`repr()`; `if X: return True / else: return False` is just `return X`; keep decide (`True`/`False`) separate from render (words).

### Day 5 — completed at 2026-11-11

**Shipped:** `week1/day05_days_between.py` + reading 2 (`_pydatetime.py`).
**Bug:** none found that night.
**Optimization:** drop `main(0)`'s counter for `while len(dates) < 2`, and make `parse_date` return a date instead of printing it.
**Learned:** a date is a number in a costume — `d2 - d1` → `timedelta`, `.days` → `int`; the leap day is added at lookup (`+ (month > 2 and _is_leap(year))`), not stored. `if __name__ == "__main__":` is a launch switch — `__name__` is `"__main__"` only when the file runs directly.

### Day 6 — completed at 2026-11-13

**Shipped:** polish on days 1–5 (typos, validation, re-ask on bad input) + reading 3 (Caesar cipher).
**Bug:** `day02` called `grade(a)` with the raw string instead of `grade(score)` → `TypeError` on valid input only; `day05` kept `from datetime import datetime` but used `date.fromisoformat` → `NameError` on every input, which `except ValueError` does not catch.
**Learned:** a validator is only as strict as the type it parses into — `datetime` accepts `2026-11-09 23:00`, `date` rejects it.

### Week 1 review   — completed at 2026-11-13

- **What shipped this week?** 5 programs — `day01_fizzbuzz.py`, `day02_grade_calculator.py`, `day03_temperature.py`, `day04_leap_year.py`, `day05_days_between.py` — plus 3 reading labs.
- **What confused me most this week?** Day 5: `_days_before_month(month, year)` and the `+ (month > 2 and _is_leap(year))` line — a lot of new material (the `datetime` module, the module-level loop), and I had to read outside sources to see how a module works.
- **What is the #1 goal for Week 2?** a small goal: finish the tasks on time.

---

## Week 2 — 16–22 Nov 2026

### Day 1 — completed at 2026-11-15

**Shipped:** `week2/day01_drill01.py` — `second_largest`, `rotate_left`, `remove_duplicates`, ends in `all drills pass` — plus `week2/day01_readinglab1.py` with `PREDICTION` and `ACTUAL` filled, 4/4.
**Bug:** `second_largest` guards on `len(nums) <= 2` when the contract is *fewer than two distinct values*, so `[1, 2]` returns `None` (should be `1`) and `[9, 9, 9]` returns `9` (should be `None`) — both outside the check block, which is why it still printed `all drills pass`.
**Learned:** the check block is a sample and the docstring is the spec — write the `[1, 2]` and `[9, 9, 9]` asserts yourself; a `raise NotImplementedError` left after a `return` can never run, so it is a comment pretending to be a guard.

### Day 2 — completed at 2026-11-16

**Shipped:** `week2/day02_drill02.py` — `char_count`, `group_by_first_letter`, `top_n`, ends in `all drills pass` — plus `week2/day02_readinglab2.py` against `collections.Counter.most_common`, 2/4.
**Bug:** three in `top_n`: `counts.items` without `()` sorted a method object (`TypeError: 'builtin_function_or_method' object is not iterable`); `pair += (i, counts[i],)` flattened the pairs into `('a', 3, 'b', 1)` instead of `(('a', 3), ('b', 1))`; and `sorted(...)` was never assigned, so the function fell through to `raise NotImplementedError` — a value computed and thrown away. Lab: predicted that `reverse=True` would reverse the ties and that `get('z', 0)` would answer `None`; both wrong.
**Learned:** a key function is a *ruler*, not the output — `sorted` compares the rulers but returns the original items; `key=lambda x: (-x[1], x[0])` reads "count descending, word ascending" because the minus flips only the number and the tuple's second slot breaks the tie. `reverse=True` flips the comparison, not the finished list: equal keys are never compared, so stability keeps their arrival order (`{"c": 1, "a": 2, "b": 2}` → `a, b`) — which is why `most_common` cannot alphabetise a tie and `top_n` had to. `get(k, default)` returns the default and never writes to the dict.

### Day 3 — completed at 2026-11-16

**Shipped:** `week2/day03_drill03.py` — `unique_words`, `common_words`, `dedupe_keep_order`, ends in `all drills pass` — plus `week2/day03_readinglab3.py`, 3/4.
**Bug:** `set={}` was an empty **dict**, so `.add` died with `AttributeError: 'dict' object has no attribute 'add'`; then `set.add('word')` called the method on the built-in type and passed the literal string, giving `TypeError: descriptor 'add' for 'set' objects doesn't apply to a 'str' object`.
**Learned:** `{}` is a dict and Python has no empty-set literal, so a set starts life as `set()`; a set operator hands back a set, and `sorted()` is the only step that turns it into the ordered list the contract asks for.

### Day 4 — completed at 2026-11-17

**Shipped:** `week2/day04_drill04.py` — `count_lines`, `longest_line`, `read_numbers`, ends in `all drills pass` — plus `week2/day04_readinglab4.py` with `PREDICTION` and `ACTUAL` filled, 1/4.
**Bug:** `float = []` shadowed the builtin, so `float(line)` died with `TypeError: 'list' object is not callable`; `if line != '' or line[0] != '#'` used `or` where `and` was meant and indexed `''` → `IndexError: string index out of range`; `longest_line` interleaved each word with its length, so `max(['second line', 11, …])` raised `TypeError: '>' not supported between instances of 'int' and 'str'`; and `raise NotImplementedError` had drifted to module level, killing the file with `NotImplementedError: read_numbers` on import.
**Learned:** never name a variable after a function you still have to call (`float`, `str`, `list`) — the local wins for the whole function, even on lines above the assignment. Filter before you convert: strip, test blank, test `#`, then `float(line)` inside a `try`, and raise `ValueError` naming the line. Keep one memory (`best`) instead of a parallel list of words and lengths. And a docstring written *after* its body is not a docstring — `__doc__` stays `None` and anything below the body can never run.

### Day 5 — completed at 2026-11-18

**Shipped:** `week2/day05_drill05.py` — `safe_int`, `parse_amount`, `tally`, ends in `all drills pass` — plus `week2/day05_readinglab5.py` with `PREDICTION` and `ACTUAL` filled, 3/5.
**Bug:** `raise a` tried to raise the float and died with `TypeError: exceptions must derive from BaseException`; the rewritten `except` then built its message out of `a`, which the failed `float(text)` never assigned → `UnboundLocalError: cannot access local variable 'a' where it is not associated with a value`; and `if i.strip == "":` compared the method object, so the skip never fired and `tally("")` returned `(0, [''])`.
**Learned:** `raise` wants an exception object built from names that exist on the failing path — `text`, not the result of the conversion that just failed; and `s.strip` is the method while `s.strip()` is its result, so a missing `()` is a comparison that is always false and never raises.

### Day 6 — completed at 2026-11-20

**Shipped:** `week2/day06_todo.py` — `load`, `save`, `add`, `complete`, `remove`, `render` and a `main(argv)` that answers `list`, `add`, `done`, `remove`, with `--path` for the checks; `python week2/day06_todo.py --check` ends in `all project checks pass`.
**Bug:** `main` first called `complete(argv)` with the whole argument list, not the id alone (`TypeError: complete() missing 1 required positional argument: 'n'`), then passed the id on as the string `"1"` while `complete` compares it to an `int` — `1 == "1"` is `False`, so a task that existed answered `No task with id 1`; the check never saw it because the only id it tries, `99`, does not exist either.
**Learned:** the check block is a sample and the docstring is the spec — the `try/except ValueError` wall is what turns a `raise` into `print(str(exc)); return 1` instead of a traceback, and an argument parsed twice is an argument parsed wrong once.

### Week 2 practice — completed at 2026-11-21

**Shipped:** `week2/Week2_practice.py` — `compress_runs`, `group_by_length`, `missing_from`, `word_counts`, `parse_config`; the 25 asserts in the check block were verified one at a time.
**Bug:** every docstring was written *under* its body, so all five `__doc__` were `None` and the five `raise NotImplementedError` lines after the body could never run; `missing_from` returned `sorted(...)`, so `(["c", "a"], [])` gave `['a', 'c']` where the contract asks for first's order — the check block only ever feeds it alphabetical input.
**Learned:** the docstring is the spec and the check block is a sample: the docstring goes directly under `def`, and a function whose answer is "in this order" must build that order, because `sorted` answers a different question — and no assertion in the sample caught it.

### Week 2 review —  22 Nov

- **What shipped this week?** Name the files, not the feelings.
- **What confused me most this week?** Name the line of code.
- **What is the #1 goal for Week 3?**

---

## Template — copy this for each new night

    ## Week 3 — 23–29 Nov 2026

    ### Day 1 — 23 Nov

    **Shipped:** the file(s) that now exist because of this night.
    **Bug:** what broke, and the one line that fixed it. No bug? **Optimization:** the one change you'd make next.
    **Learned:** the rule, in the words you'd use to explain it to someone else.
