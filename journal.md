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

---

## Week 1 review — fill in on Day 7

- **What shipped this week?** 3 programs so far (fizzbuzz, grade calculator, temperature converter) + 1 reading lab.
- **What confused me most?** _TODO — skim the entries above; the repeated one is the answer._
- **What is the #1 goal for Week 2?** _TODO_
