# Journal

One entry a day: **what happened, why, what fixed it.** The Week 1 review at the bottom gets filled on Day 7.

---

## Day 1 — 2026-11-07
**Shipped:** `week1/day01_fizzbuzz.py` + reading lab. **Bug:** traced `range(1, 6)` as ending at 6 — it is half-open (1–5); odd-sum is `(n+1)**2/4`, not `(1+n)*n/4`.
**Learned:** `continue` skips the rest of one iteration, not the loop; a function should `return` and let the caller print.

## Day 2 — 2026-11-08
**Shipped:** `week1/day02_grade_calculator.py`. **Bug:** the `elif` chain repeated conditions already ruled out, and the `except` printed `score` before it existed → `UnboundLocalError` on `abc`.
**Learned:** an `elif` already carries the negation of every branch above it; `except ValueError` catches only that class; return `None` for "no grade" — `'reject'` is a truthy string.

## Day 3 — 2026-11-09
**Shipped:** `week1/day03_temperature.py`. **Bug:** `mode(user)` got the string `"1"` instead of `1` (`"1" == 1` is False) and the program exited silently; `check_float(c)`'s result was thrown away; a `None` from the error branch reached the arithmetic.
**Learned:** `try` does not prevent the raise, it stops the raise ending the program — a failed `int()` aborts before assigning, so the name never exists.

## Day 4 — 2026-11-10
**Shipped:** `week1/day04_leap_year.py`. **Bug:** `is_leap` returned the strings `'True'`/`'False'`; output looked identical, but `bool('False')` is `True`, so `if is_leap(1900):` took the wrong branch.
**Learned:** a value's type is not its printout — check `type()`/`repr()`. `if X: return True / else: return False` is just `return X`; keep decide (`True`/`False`) separate from render (words).

## Day 5 — 2026-11-13
**Shipped:** `week1/day05_days_between.py` + reading2 (`_pydatetime.py`). **Learned:** a date is a number in a costume — `d2 - d1` → `timedelta`, `.days` → `int`; the leap day is added at lookup (`+ (month > 2 and _is_leap(year))`), not stored.
**Learned:** `if __name__ == "__main__":` is a launch switch — `__name__` is `"__main__"` only when the file is run directly.

## Day 6 — 2026-11-13
**Shipped:** polish on days 1–5 (typos, validation, re-ask on bad input) + reading3 (Caesar cipher). **Bug:** `day02` called `grade(a)` with the raw string instead of `grade(score)` → `TypeError` on valid input only; `day05` used `date.fromisoformat` but kept `from datetime import datetime` → `NameError` on every input, which `except ValueError` does not catch.
**Learned:** a validator is only as strict as the type it parses into — `datetime` accepts `2026-11-09 23:00`, `date` rejects it. **Still 

---

## Week 1 review — fill in on Day 7

- **What shipped this week?** 5 programs (fizzbuzz, grade calculator, temperature, leap year, days between) + 3 reading labs.
- **What confused me most?** _TODO — skim the entries above; the repeated one is the answer._
- **What is the #1 goal for Week 2?** _TODO_
