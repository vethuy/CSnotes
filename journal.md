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

---

## Week 1 review — fill in on Day 7

- **What shipped this week?** 2 programs so far (fizzbuzz, grade calculator) + 1 reading lab.
- **What confused me most?** _TODO — skim the entries above; the repeated one is the answer._
- **What is the #1 goal for Week 2?** _TODO_
