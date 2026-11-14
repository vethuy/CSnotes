# Reading notes

One entry per lab, newest at the bottom. Header = week, day, file, topic, score.
Then exactly three parts: **result / learned / still confusing**. Twenty lines
for the entry, no more — if it doesn't fit, the entry is copying the code back
out instead of writing down the lesson.

**Score so far:** Week 1 — 10/11 (Day 1 1/1 · Day 5 4/5 · Day 6 5/5)

---

## Week01 Day01 — reading01.py: `for`, `range`, `continue` — result **1/1**

### 1. Result

Predicted `9`, actual `9`. `range(1, 7)` walks 1 to 6, and `continue` throws
away 2, 4 and 6 before they reach `total += n`, so the total is `1 + 3 + 5`.

### 2. What I learned

`continue` skips the rest of the *body* for that iteration only — the loop
itself carries on to the next value. Even numbers never touch `total += n`.

### 3. Still confusing

I thought the loop reached `n = 6`. It stops at `5`: `range` excludes its stop
value, and 6 was the one even number I never had to explain.

---

## Week01 Day05 — reading2.py: `datetime` internals, month offsets — result **4/5**

### 1. Result

| # | What I predicted | Actual | |
|---|---|---|---|
| 1 | `_DAYS_BEFORE_MONTH` ends `…, 334, 365]` (14 items) | `…, 334]` (13 items, no `365`) | ✗ |
| 2 | `_days_before_year(2024)` = `738885` | `738885` | ✓ |
| 3 | `_days_before_month(2024, 3)` / `(2023, 3)` = `60` / `59` | `60` / `59` | ✓ |
| 4 | the ordinal difference = `10` | `10` | ✓ |
| 5 | `_days_in_month(1900, 2)` / `(2024, 2)` = `28` / `29` | `28` / `29` | ✓ |

Four right, and the miss was one element at the very end of a list.

### 2. What I learned

`_DAYS_BEFORE_MONTH[m]` is "days in the year before month `m` starts", so the
index *is* the month and the `-1` at index 0 is a dummy that lines month 1 up
with index 1. The table is a **non-leap** table — the Feb 29 day is added at
lookup time and only when `month > 2`, which is why March 2024 is `60` and
March 2023 is `59`. `_ymd2ord` then just adds three offsets, with 1 Jan 0001 as
day 1. And `and` does not return a bool, it returns an operand, so
`59 + True == 60` because `bool` subclasses `int`.

### 3. Still confusing

I predicted `365` would be appended. The loop runs **12** times — once per
month in `_DAYS_IN_MONTH[1:]` — so it appends 12 values on top of the `-1`
placeholder (13 entries) and the final `dbm = 365` is never appended at all;
`del dbm, dim` throws it away. I mentally added a 13th iteration.

---

## Week01 Day06 — reading3.py: Caesar cipher, `% 26`, `repr` — result **5/5**

### 1. Result

All five matched: `bcd` · `abc` · `Ifmmp, Xpsme!` · `Week 1` · `z`, `z`.

### 2. What I learned

`encode` builds a new string — `result = ""` then `result += …` — because
strings are immutable; the input is never changed. `LOWER.index(ch)` turns a
letter into 0–25 and `% 26` turns any number back into a valid position, which
is the whole wraparound (`x` = 23, +3 = 26, `26 % 26` = 0 = `a`). `decode` is
one line because `-shift` travels through the *same* `% 26`: Python's modulo is
never negative (`-1 % 26 == 25`), where C or Java would give `-1`. Uppercase
must use `UPPER.index`, and anything else falls through `return ch`.

### 3. Still confusing

I thought my answers were wrong because they printed with quotes — that is
`repr()`, the debugging view, which makes leading and trailing spaces visible.
Also, in question 5 I wrote `LOWER[-1 % 26]`; the real expression is
`LOWER[(LOWER.index('a') + -1) % 26]`, and the `index('a')` term only vanished
because `'a'` happens to be 0 — with `'b'` my version gives the wrong letter.

---

## Template — copy this for each new lab

    ## Week02 Day01 — day01_readinglab1.py: `statistics.mean` — result **?/4**

    ### 1. Result
    Predicted … — Actual … — the one that missed, and why it missed.

    ### 2. What I learned
    The one line of code that made it work, in one sentence.

    ### 3. Still confusing
    The one thing I could not explain without running it.

Week 2 question counts, so the score is honest: lab1 **4** · lab2 **4** ·
lab3 **4** · lab4 **4** · lab5 **5**.
