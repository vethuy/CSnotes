# Journal

One entry a night. Three parts, **two lines each**: **Shipped** (the files),
**Bug** (what broke and why), **Learned** (the rule you'd say out loud). No bug
that night? Part 2 becomes **Optimization:** the one change you would make next.
At the end of each week, three questions — name files, not feelings.

---

## Week 1 — 7–13 Nov 2026

### Day 1 — 2026-11-07

**Shipped:** `week1/day01_fizzbuzz.py` + reading lab 1.
**Bug:** traced `range(1, 6)` as ending at 6 — it is half-open (1–5); odd-sum is `(n+1)**2/4`, not `(1+n)*n/4`.
**Learned:** `continue` skips the rest of one iteration, not the loop; a function should `return` and let the caller print.

### Day 2 — 2026-11-08

**Shipped:** `week1/day02_grade_calculator.py`.
**Bug:** the `elif` chain repeated conditions already ruled out; the `except` printed `score` before it existed → `UnboundLocalError` on `abc`.
**Learned:** an `elif` already carries the negation of every branch above it; `except ValueError` catches only that class; return `None` for "no grade" — `'reject'` is a truthy string.

### Day 3 — 2026-11-09

**Shipped:** `week1/day03_temperature.py`.
**Bug:** `mode(user)` got the string `"1"` instead of `1` (`"1" == 1` is False) and the program exited silently; `check_float(c)`'s result was thrown away; a `None` from the error branch reached the arithmetic.
**Learned:** `try` does not prevent the raise, it stops the raise ending the program — a failed `int()` aborts before assigning, so the name never exists.

### Day 4 — 2026-11-10

**Shipped:** `week1/day04_leap_year.py`.
**Bug:** `is_leap` returned the strings `'True'`/`'False'`; output looked identical, but `bool('False')` is `True`, so `if is_leap(1900):` took the wrong branch.
**Learned:** a value's type is not its printout — check `type()`/`repr()`; `if X: return True / else: return False` is just `return X`; keep decide (`True`/`False`) separate from render (words).

### Day 5 — 2026-11-11

**Shipped:** `week1/day05_days_between.py` + reading 2 (`_pydatetime.py`).
**Bug:** none found that night.
**Optimization:** drop `main(0)`'s counter for `while len(dates) < 2`, and make `parse_date` return a date instead of printing it.
**Learned:** a date is a number in a costume — `d2 - d1` → `timedelta`, `.days` → `int`; the leap day is added at lookup (`+ (month > 2 and _is_leap(year))`), not stored. `if __name__ == "__main__":` is a launch switch — `__name__` is `"__main__"` only when the file runs directly.

### Day 6 and Day 7 — 2026-11-12

**Shipped:** polish on days 1–5 (typos, validation, re-ask on bad input) + reading 3 (Caesar cipher).
**Bug:** `day02` called `grade(a)` with the raw string instead of `grade(score)` → `TypeError` on valid input only; `day05` kept `from datetime import datetime` but used `date.fromisoformat` → `NameError` on every input, which `except ValueError` does not catch.
**Learned:** a validator is only as strict as the type it parses into — `datetime` accepts `2026-11-09 23:00`, `date` rejects it.

### Week 1 review

- **What shipped this week?** 5 programs — `day01_fizzbuzz.py`, `day02_grade_calculator.py`, `day03_temperature.py`, `day04_leap_year.py`, `day05_days_between.py` — plus 3 reading labs.
- **What confused me most this week?** Day 5: `_days_before_month(month, year)` and the `+ (month > 2 and _is_leap(year))` line — a lot of new material (the `datetime` module, the module-level loop), and I had to read outside sources to see how a module works.
- **What is the #1 goal for Week 2?** a small goal: finish the tasks on time.

---

## Week 2 — 16–22 Nov 2026

### Day 1 — 16 Nov

**Shipped:**
**Bug:**
**Learned:**

### Day 2 — 17 Nov

**Shipped:**
**Bug:**
**Learned:**

### Day 3 — 18 Nov

**Shipped:**
**Bug:**
**Learned:**

### Day 4 — 19 Nov

**Shipped:**
**Bug:**
**Learned:**

### Day 5 — 20 Nov

**Shipped:**
**Bug:**
**Learned:**

### Day 6 — 21 Nov (project)

**Shipped:**
**Bug:**
**Learned:**

### Week 2 review — Sunday 22 Nov

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
