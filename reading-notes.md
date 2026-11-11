# Reading notes

## Day 1 — reading01.py

**Prediction:** 9

**Actual:** 9

**What I learned:** `continue` skips the rest of the loop body for that
iteration, but the loop keeps going. Even numbers never reach `total += n`.

**One thing that confused me:** I thought the loop reached n = 6 actually it only reach n=5

## Day 5 — reading2.py

**Prediction:**

1. `_DAYS_BEFORE_MONTH = [-1, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]`
2. `_days_before_year(2024) = 738885`
3. `_days_before_month(2024, 3) = 60`, `_days_before_month(2023, 3) = 59`
4. `10`
5. `_days_in_month(1900, 2) = 28`, `_days_in_month(2024, 2) = 29`

**Actual:**

1. `[-1, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]` — one element short, no `365`
2. `738885`
3. `60`, `59`
4. `10`
5. `28`, `29`

**Trace table — the module-level loop**

| # | `dim` | append `dbm` | `dbm` after `dbm += dim` |
|---|---|---|---|
| 1 | 31 | 0 | 31 |
| 2 | 28 | 31 | 59 |
| 3 | 31 | 59 | 90 |
| 4 | 30 | 90 | 120 |
| 5 | 31 | 120 | 151 |
| 6 | 30 | 151 | 181 |
| 7 | 31 | 181 | 212 |
| 8 | 31 | 212 | 243 |
| 9 | 30 | 243 | 273 |
| 10 | 31 | 273 | 304 |
| 11 | 30 | 304 | 334 |
| 12 | 31 | 334 | 365 |

The loop runs 12 times — once per month in `_DAYS_IN_MONTH[1:]` — so it appends 12 values on top of the `-1` placeholder, giving 13 entries. `dbm` ends at 365, but that total is never appended; `del dbm, dim` then removes the two module globals.

**What I learned:** `_DAYS_BEFORE_MONTH[m]` means "days in the year before month `m` starts", so the index *is* the month number, and the `-1` at index 0 is a dummy so that month 1 lines up with index 1. The table is built for a **non-leap year**; the extra day from Feb 29 is added later, at lookup time, and only when `month > 2`. That is why March 2024 gives 60 while March 2023 gives 59. `_ymd2ord` then just adds the three offsets together to get an ordinal, with 1 Jan 0001 as day 1 — which is why subtracting two ordinals in the same month cancels out and leaves the difference in days.

**Why does `_days_before_month` return a number when the last part is a True/False test?** Because `and` does not turn its operands into a bool — it returns one of them. In `(month > 2 and _is_leap(year))`, if `month > 2` is `False` the expression is `False`; otherwise it is whatever `_is_leap(year)` returned, which is `True` or `False`. Then `59 + True` is `60` and `59 + False` is `59`, because `bool` is a subclass of `int`: `True == 1` and `False == 0`. (The docstring on `_is_leap` says "1 if leap year, else 0", but it actually returns `True`/`False` — it behaves the same way for this reason.)

**One thing that confused me:** I predicted the list would end with 365. My step-by-step trace was right — append first, then add, so `dbm` is always the days *before* the current month — but I mentally added a 13th iteration and appended the final total. There are only 12 iterations, so 365 stays in `dbm` and gets thrown away by `del`.