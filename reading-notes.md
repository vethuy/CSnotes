# Reading notes

One entry per lab, newest at the bottom. Header = week, day, file, topic, score.
Then exactly three parts: **result / learned / still confusing**. Twenty lines
for the entry, no more — if it doesn't fit, the entry is copying the code back
out instead of writing down the lesson.

**Score so far:** Week 1 — 10/11 (Day 1 1/1 · Day 5 4/5 · Day 6 5/5) ·
Week 2 — 10/16 (Day 1 4/4 · Day 2 2/4 · Day 3 3/4 · Day 4 1/4)

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

## Week02 Day01 — day01_readinglab1.py: `statistics.mean` — result **4/4**

### 1. Result

Predicted `2.5` · `2` · `True` · `ZeroDivisionError`; actual `2.5` · `2.0` · `True` ·
`ZeroDivisionError`. Four values right, but call 2 printed **`2.0`**, not `2` — the
number was right and the type was not, and `repr()` is the only reason I saw it.

### 2. What I learned

`total / len(nums)` is true division, so `6 / 3` is `2.0` even though nothing is
fractional; `2.0 == 2` is still `True`, which is why prediction 3 was safe to make
on a wrong type. The accumulator runs `0→1→3→6` line by line, and on `[]` it simply
never runs — the crash is the division on the last line, so I was right to stop
suspecting the `for`.

### 3. Still confusing

The lab's docstring says the stdlib `mean` "hands back an int when it can", but this
file's `mean` never can: `/` always returns `float`. The real `statistics.mean([1, 2,
3])` is `2` because it computes exactly, with `Fraction`, and only converts at the
end. So prediction 2 was asking about the stdlib function while I was reading a
float-returning copy — the lesson is `2.0` vs `2`, not `2.5`.

---

## Week02 Day02 — drill02.py + readinglab2.py: `sorted`, keys, ties — result **2/4**

### 1. Result

Lab: predicted `[('a', 2), ('b', 2), ('c', 1)]` · `[('b', 2), ('a', 2)]` · `[]` ·
`None`; actual same · **`[('a', 2), ('b', 2)]`** · same · **`0`**. Two right, and
both misses were about behaviour, not arithmetic. Drill: `all drills pass`, but only
after `top_n` was rebuilt three times.

### 2. What I learned

A key is a *ruler*: `sorted` compares what the key returns but hands back the
original items. `key=lambda x: (-x[1], x[0])` reads "count descending, word
ascending" because the minus flips only the number and the tuple's second slot breaks
ties. `reverse=True` is not "reverse the list afterwards" — equal keys are never
compared, so stability keeps their arrival order: `other` inserts `c, a, b`, so its
two `2`s come out `a, b`. That is why `most_common` cannot alphabetise a tie and
`top_n` had to. `counts.items()` is the pairs my loop was rebuilding by hand, and
`dict.get(k, 0)` returns the default `0`, not `None`.

### 3. Still confusing

I reversed ties mentally, and read `get`'s missing key as `None` though I had passed
`0`. In the drill: `counts.items` without `()` sorts a method object
(`TypeError: 'builtin_function_or_method' object is not iterable`), `pair += (i,
counts[i],)` flattens the pairs, and a `sorted(...)` that is not assigned computes a
value nobody keeps — the function then fell through to its `raise`.

---

## Week02 Day03 — day03_readinglab3.py: set algebra, hash order — result **3/4**

### 1. Result

Predicted `{2, 3}` · `['a']` · `[3, 1, 2, 1]` · `2`; actual `{2, 3}` · `['a']` ·
`[1, 2, 3]` · `2`. Three right; call 3 missed on the dedupe and on the order.

### 2. What I learned

`set([3, 1, 2, 1])` removes the duplicate *at construction* — `list()` only wraps
what is already there, it never filters. The `[1, 2, 3]` order is hash-table order,
not sorting: small ints hash to themselves and only *look* ordered, so
`sorted(set(...))` is the one version that prints the same thing every run.

### 3. Still confusing

I read `set(x)` as "change the type of x" and expected the list to come through
unchanged. What call 4 proved is that `{'a', 'a', 'b'}` is already two elements
before `len` ever sees it — the literal is where the collapse happens.

---

## Week02 Day04 — day04_readinglab4.py: `csv.DictReader`, `restkey`/`restval` — result **1/4**

### 1. Result

Predicted `3` · `('ann', 30)` · `('cat', 25)` · `True`; actual `3` ·
`{'name': 'bob', 'age': None}` · `{'name': 'cat', 'age': '25', None: ['extra']}` ·
`False`. One right, and it was luck: I drew the row shape from `csv.reader`
while the lab calls `DictReader`, so I counted the header as a row and dropped
`bob` — wrong three rows, right count.

### 2. What I learned

`DictReader` gives a **dict per row keyed by the header**, not a tuple of cells;
the header becomes `fieldnames` (`csv.py:161-168`) and is never data, and
`dict(zip(fieldnames, row))` at `csv.py:186` pairs by *position* — swap the
header to `age,name` and the first cell becomes `age`. A short row keeps its key
and fills it with `restval` (`None`); a long row is not re-slotted, the surplus
becomes a list under `restkey` (also `None`). Cells are text, so `'25'` is a
`str` and `== 25` is `False`.

### 3. Still confusing

`list(...)` at `:28` made me read the result as a list of cell-pairs; `list()`
only wraps the outer container — the shelf is a list, the items are dicts — the
same trap as Day 3, where `list(set(...))` did not dedupe.

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
