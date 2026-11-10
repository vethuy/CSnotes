# Journal

Three lines a day, in the shape the plan asks for: **what happened, why, what fixed it.**
Daily entries first; the Week 1 review at the bottom gets filled on Day 7.

---

## Day 1 — 2026-11-07

**Shipped:** `week1/day01_fizzbuzz.py` and the reading lab (`week1/day01_reading1`, later to be renamed `reading01.py`).

- **Bug:** my trace of the reading snippet listed `n=6`. `range(1, 6)` stops at 5, so that iteration never happens.
  - **Why:** I read the second argument as inclusive.
  - **Fix:** `range` is half-open — 1,2,3,4,5. Named the parameter `end` in `oddsum` instead of `target` so the exclusivity is visible in the name.
- **Bug:** my odd-sum formula `(1+n)*n/4` gives 7.5 for n=5, but 1+3+5 = 9.
  - **Why:** sum of the first k odd numbers is k²; for odd n, k = (n+1)/2, so it's `(n+1)*(n+1)/4`.
  - **Fix:** the odd case is `(n+1)*(n+1)/4`; the even case `n*n/4` was already right. (Not yet edited in `day01_reading1` — it is still wrong in the file.)
- **Learned:** `continue` skips the rest of the body for that iteration but the loop keeps going — even numbers never reach `total += n`.
- **Learned:** a function should `return` its result and let the caller print it; `print` inside a computation function makes it untestable.
- **Confused about:** half-open ranges (the end value is excluded) — same rule as string slicing.
- **Notes:** `reading-notes.md` has this entry (prediction 9, actual 9).
- **Still open:** file has no `.py` extension and the folder is `week1`, while START_HERE says `week01/reading01.py`. Rename both before the Day 7 "definition of done" check. Also fix the odd-sum formula printed at the bottom of the file.

## Day 2 — 2026-11-08

**Shipped:** `week1/day02_grade_calculator.py` — score in, letter out, plus a "stronger version" with input handling.

- **Bug:** `elif score<90 and score>=80:` repeated a condition the chain had already ruled out.
  - **Why:** I didn't trust that `elif` only runs if every branch above it failed.
  - **Fix:** an `elif` chain carries the negation of everything above it, so it is just `elif score >= 80:` — dropped all the redundant `and` clauses.
- **Bug:** `grade()` returned the string `'reject'` for out-of-range scores, in the same channel as the letters (it now returns a whole sentence, `"-5 is not an acceptable score"` — still not a letter).
  - **Why:** I treated "error" and "result" as the same kind of value, so the caller can't tell them apart and `if result:` counts an error as success.
  - **Fix:** return `None` for "no grade"; the caller prints the message. (Not applied yet — the sentence is built in `stronggrade()` for now.)
- **Bug:** the `except` handler crashed with `UnboundLocalError: cannot access local variable 'score' where it is not associated with a value` on input `abc`.
  - **Why:** `score` is only created when `int(raw)` succeeds. When it raises, the handler prints a variable that was never assigned. A bare `except:` also hid which failure it was, and there was no `return`, so the line after the handler ran anyway.
  - **Fix:** keep the raw text, print that, and stop:
    ```python
    raw = input("Enter your score: ").strip()
    try:
        score = int(raw)
    except ValueError:
        print(f"{raw!r} is not an acceptable score")
        return
    print(stronggrade(score))
    ```
- **Fixed today:** the missing `f` in `"{score},is not an acceptable score"` — without the prefix the braces print literally. Now `-5` and `101` produce `-5 is not an acceptable score`.
- **Learned:** `except X` catches only `X` and its subclasses. `int('abc')` raises `ValueError` ("right type, impossible value"); `int(None)` raises `TypeError` ("wrong type entirely"). Catch the narrowest one you can name.
- **Learned:** wrap only the line that can raise. A `try` as wide as the function will report your own bugs as "bad user input".
- **Learned:** `try` + `except ValueError` = catch the raise, skip the wrong input, keep it from reaching the computation.
- **Learned:** return data, put the words at the edge — but a returned sentence is still a non-empty string, so it is truthy: sentinels must be `None`, not `'reject'`.
- **Still open:** apply the `raw` + `return` fix (input `abc` still crashes); rename `user()` → `main()`, add `if __name__ == "__main__":`, delete the dead code inside the `'''` block (git holds the old version); run the six test inputs.

## Day 3 — 2026-11-09

**Shipped:** `week1/day03_temperature.py` — C↔F converter with a mode menu. Every prompt now survives non-number text with a message and a clean exit instead of a traceback.

- **Bug:** `abc` at the mode prompt crashed with `NameError` — the handler printed `user`, but `user` is only created when `int()` succeeds.
  - **Why:** `try` does not check anything; `int()`/`float()` are the parsers, and they raise `ValueError`. A failed conversion aborts the line *before* the assignment, so the name never exists — same trap as Day 2's `score`. There was also a bare `except:`.
  - **Fix:** read the text first, convert inside `try`, report the raw text:
    ```python
    raw = input("what mode? 1.C->F  2.F->C:")
    try:
        user = int(raw)
    except ValueError:
        print(raw, "is not an available mode")
    else:
        mode(user)
    ```
    `else:` only runs when the conversion succeeded, so `mode()` can never receive unvalidated text.
- **Bug:** after that fix, `mode(user)` was called with the string `"1"`, and `if u == 1` was False — the program exited with no output and no error at all.
  - **Why:** I computed `check = int(user)` and then passed `user`; the converted value was dropped. `"1" == 1` is False — a string never equals an int.
  - **Fix:** pass `check`, or reassign in place with `user = int(user)` — on failure `int()` raises before assigning, so `user` still holds the text for the message.
- **Bug:** `if user is not 1:` was always true for typed input.
  - **Why:** `is` compares identity (same object), not value, and I was comparing a string to an int. Small ints are cached so `is` can *look* right and then fail unpredictably later.
  - **Fix:** convert first, then `if user not in (1, 2):` — listing what is allowed excludes 3, 4, 5 and everything else, and adding a mode later means editing one tuple.
- **Bug:** `check_float(c)` on its own line threw the result away, so `c` stayed a string and the conversion did `"35" * 9` (string repetition!) then failed on `/ 5` with `TypeError`.
  - **Why:** Python passes values, not names — assigning a local inside the helper cannot change the caller's variable. The call site must be `c = check_float(c)`.
  - **Fix:** assign every checked value back.
- **Bug:** `abc` — or just pressing Enter — at the temperature prompt crashed with `TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'`.
  - **Why:** `check_float` prints and then falls off the end of the error branch, so it returns `None`; the caller passed that `None` straight into the arithmetic. A message on screen is not the same as a handled error.
  - **Fix:** guard the caller: `if c is None: return`, before computing anything.
- **Learned:** `try:` does not prevent the raise — it stops the raise from ending the program. The flow is: run the block → `int`/`float` raises `ValueError` → jump to `except`, and the rest of the `try` is skipped (that's why the variable is missing) → `else` runs only if nothing raised. The `except` block decides what happens next; it does not stop anything by itself. `raise SystemExit`, `return`, or `continue` are what stop / retry, and an empty `except` just swallows the error and carries on.
- **Learned:** `x is None` (singleton identity) vs `x == None` (`__eq__`, overridable — a numpy array comparison returns an array and blows up in `if`). `if not x:` is also wrong for numbers: `0` is a valid temperature but `not 0` is True.
- **Learned:** a helper that prints *and* returns `None` splits the contract — the caller must both watch for `None` and avoid printing again, which is exactly how I got two messages per bad input. Better: the helper loops until the input is valid, so it can never return `None` and no call site needs a guard.
- **Still open:** `check_int` now returns silently while `check_float` still prints (asymmetric); the invalid-mode message prints `None` instead of the typed text (keep `raw`); `round` lives inside the conversion functions instead of `:.1f` at print time; redundant `return int(a)` / `float(a)`; `[1, 2]` → `(1, 2)`; typos "convent" → "convert", "a available" → "an available".
- **Notes:** verified by piping input — `1/100` → 212.0 F, `1/37` → 98.6 F, `2/212` → 100.0 C, `1/-40` → -40.0 F; `1/abc`, `2/<Enter>`, `abc`, `1.5`, `5` all print one message and exit without a traceback. Idea for next time: one `ask_number(prompt, cast, choices)` helper that loops, with `ask_int` / `ask_float` as one-line wrappers.

## Day 4 — 2026-11-10

**Shipped:** `week1/day04_leap_year.py` — leap-year checker with input validation. All four test years come out right (`2024`/`2000` → leap, `1900`/`2023` → not leap), and `abc` or an empty line prints a message instead of a traceback.

- **Bug (the big one):** `is_leap` returned the strings `'True'` / `'False'`, not the booleans `True` / `False`.
  - **Why:** I read "returns `True` or `False`" as "prints the word True / False", so I put quotes around them. Quotes make a `str`; the requirement was a `bool`. And `print()` calls `str()` on its arguments, while `str(True) == str('True') == "True"` — so the console output was **identical** either way and the bug was invisible from outside.
  - **How I caught it:** stop looking at the output, look at the value. `type(is_leap(2024))` → `str`, not `bool`. `is_leap(2024) == True` → `False`. And the dangerous one: `bool(is_leap(1900))` → `True`, because a non-empty string is always truthy — so `if is_leap(1900):` takes the **true** branch, and every caller that trusts the return value reports a non-leap year as leap. My four "correct" outputs were hiding a wrong function.
  - **Fix:** return the values, not their names — `return True` / `return False`, no quotes. Better still, the rule is *already* a boolean expression, so the nested `if` collapses to one line:
    ```python
    def is_leap(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    ```
  - **Same family of traps:** `true` / `false` lowercase are `NameError` (Python is case-sensitive, unlike Java/C#); `bool("")` is `False` but `bool("False")` is `True`; `not year % 100 == 0` parses as `not (year % 100 == 0)` — correct, but a double negative, so write `year % 100 != 0`.

- **The view that unlocked it — two layers, not one.** I was asking `is_leap` to do two jobs at once: *decide the fact* and *tell the human*. They are different layers:

  ```
  raw text ──check_int──▶ int or None
                            │
                        is_leap(year) ──▶ True / False      DECIDE   (pure: no input(), no print())
                            │
                        main(): words + print              RENDER   (the only layer that talks to a human)
  ```

  - `is_leap` answers *"is this year leap?"* as data. `main()` turns that data into the sentence *"2024 is a leap year"*.
  - The sentence is a **rendering** of `True`, not the thing itself. Rendering can change — a sentence, a table cell, `✓`, Chinese — without touching the rule.
  - So the requirement was never in conflict: *"print whether it is a leap year"* and *"`is_leap` returns `True`/`False`"* are both satisfied — by two different functions. The printing moves **out of** `is_leap`, not away.
  - **Proof the layers are real:** with a bool-returning `is_leap` I can ask questions no `input()` prompt can ask — `[y for y in range(1990, 2011) if is_leap(y)]` → `[1992, 1996, 2000, 2004, 2008]`; `sum(1 for y in range(1900, 2101) if is_leap(y))` → `49`. Against a printing version, that list comprehension would be swallowing 21 lines of `yes`/`no`. And `assert is_leap(2024) is True` needs a *value* to compare — that's the seed of Week 3's pytest.
  - **Rule I'm keeping:** compute → decide → render, and only the outermost layer may `print`. Same shape as Day 2's `grade()` returning `'A'` and Day 3's `check_float` printing *and* returning `None` — there I already wrote the cost down ("the caller must both watch for `None` and avoid printing again, which is exactly how I got two messages"); I just hadn't seen it as a layer rule yet.

- **Bug:** the `input()` sat at module level, so the file ran on *import*.
  - **Why:** `from day04_leap_year import is_leap` executes the file top to bottom, reaches the prompt, and dies with `EOFError: EOF when reading a line`. The function was unreachable from any other file — so "it returns a value" had no one to return it to yet.
  - **Fix:** wrap the driver in `main()` and guard it:
    ```python
    if __name__ == "__main__":
        main()
    ```
    Then importing the file gives me `is_leap` silently, and running it still asks the question.

- **Bug (waste, not breakage):** `if year%4==0: … return True else: return False` — a condition compared only to hand back the condition.
  - **Why:** I thought the `if` had to "produce" the boolean. It doesn't: `if` is a **statement** — it chooses a path, it never returns a value. The comparison `year % 4 == 0` is *already* `True`/`False`.
  - **Fix:** every `if X: return True / else: return False` is just `return X`.

- **Fixed today:** `return int(a)` → `return a` in `check_int` (`a` is already an `int`); typo "avaliable" → "available" (third time this week — start `Ctrl+F`-ing before commit).
- **Learned:** a value's *type* is not its *printout*. `print` is lossy: it can't tell `True` from `'True'`, `1` from `'1'`, `None` from `'None'`. When something looks right, check `type()` and `repr()` before believing it.
- **Learned:** "returns `True` or `False`" in a spec is a statement about the **type**, not the wording. Specs describe interfaces; the user-facing sentence is mine to write at the edge.
- **Still open:** the quotes are still in the file (`return 'True'` ×2, `return 'False'` ×2) and there's no `main()` yet; the error message still doesn't echo what was typed (`raw`); the module docstring is still the assignment text instead of "what this file does"; 
---

## Week 1 review — fill in on Day 7

- **What shipped this week?** 3 programs so far (fizzbuzz, grade calculator, temperature converter) + 1 reading lab.
- **What confused me most?** _TODO — skim the entries above; the repeated one is the answer._
- **What is the #1 goal for Week 2?** _TODO_
