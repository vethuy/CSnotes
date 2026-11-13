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

## Day 6 — reading3.py (Caesar cipher)

**Prediction:**

1. `bcd`
2. `abc`
3. `Ifmmp, Xpsme!`
4. `Week 1`
5. `z`, `z`

**Actual:** all five identical — 5/5 correct.

**What I learned:**

- `encode` builds a new string one character at a time: `result = ""` before the loop, then `result += shift_char(ch, shift)` inside it. The input string is never modified — strings are immutable, so every step produces a new one.
- `LOWER.index(ch)` turns a character into a number (its position 0–25), and `% 26` turns any number back into a valid position. That is the whole wraparound: `x` at 23, plus shift 3 gives 26, and `26 % 26` is 0, so it becomes `a`.
- `decode` is a single line because `-shift` travels through the *same* `% 26`. This only works because Python's modulo returns a non-negative answer for a negative operand: `-1 % 26 == 25` and `-27 % 26 == 25`. In C or Java the same expression would give `-1` (they truncate toward zero), so the code would need an extra `(x + 26) % 26` fix-up before it could index anything.
- The three branches in `shift_char` are ordered so each character takes exactly one path: lowercase → `LOWER`, uppercase → `UPPER`, anything else (comma, space, digit) falls through to `return ch`. Uppercase must use `UPPER.index` and `UPPER[...]`; `LOWER.index('H')` would raise `ValueError`.
- The quotes around each printed answer come from `repr()`, not from the string: `print('bcd')` shows `bcd`, `print(repr('bcd'))` shows `'bcd'`. `repr` is the debugging view, where the quotes make leading and trailing spaces visible.

**One thing that confused me:** I thought my answers were wrong because the program printed them with `''` around them. The answers themselves were right — `repr()` adds the quotes to show exactly what the string contains. Also, in question 5 I first wrote the index as `LOWER[-1 % 26]`, but the real expression is `LOWER[(LOWER.index('a') + -1) % 26]`; the `index(ch)` term only disappeared because `'a'` happens to be 0. With `'b'` the omitted term would give the wrong letter.