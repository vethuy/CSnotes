# cs-notes

My notes and programming exercises for an 8-week CS study plan.(btw this is all ai planned.lets see my improvement 8 week later)

## Goal

- Write small programs from scratch.
- Read code I did not write.
- Publish a self-built algorithm project on GitHub.

## Week 1

| File | What it does |
|---|---|
| `week1/day01_fizzbuzz.py` | FizzBuzz using a function |
| `week1/day02_grade_calculator.py` | Converts a score to a grade |
| `week1/day03_temperature.py` | Celsius/Fahrenheit converter |
| `week1/day04_leap_year.py` | Leap-year checker |
| `week1/day05_days_between.py` | Days between two dates |

Reading labs — code I read and answered questions about, not code I wrote.

| File | Source | What it exercises |
|---|---|---|
| `week1/day01_reading1.py` | own snippet | `range` bounds, `continue`, accumulating a sum |
| `week1/day05_reading2.py` | CPython 3.13, `Lib/_pydatetime.py` | `_ymd2ord`, why leap days are added at lookup |
| `week1/day06_reading3.py` | own snippet | iterating a string, index + `% 26` to wrap |

## Week 2

| File | What it does |
|---|---|
| `week2/day01_drill01.py` | `second_largest`, `rotate_left`, `remove_duplicates` — lists, slicing, "fewer than two" edges |
| `week2/day02_drill02.py` | `char_count`, `group_by_first_letter`, `top_n` — dicts as counters, `sorted` with a key |
| `week2/day03_drill03.py` | `unique_words`, `common_words`, `dedupe_keep_order` — sets for "have I seen it", lists for order |
| `week2/day04_drill04.py` | `count_lines`, `longest_line`, `read_numbers` — reading a file, skipping blanks and `#`, converting with `try` |
| `week2/day05_drill05.py` | `safe_int`, `parse_amount`, `tally` — raising `ValueError` with the offending text, counting what fails |
| `week2/day06_todo.py` | JSON-backed to-do CLI — `load`/`save`/`add`/`complete`/`remove`/`render` plus `main(argv)` for `list`, `add`, `done`, `remove` |
| `week2/Week2_practice.py` | Five review functions, one per night's skill (days 1–5) |

Reading labs.

| File | Source | What it exercises |
|---|---|---|
| `week2/day01_readinglab1.py` | CPython 3.13, `Lib/statistics.py:472` | `total / len` returns a float even when exact; the empty list divides by zero |
| `week2/day02_readinglab2.py` | CPython 3.13, `Lib/collections/__init__.py` | `Counter.most_common` sorts on count alone and leans on a stable sort for ties |
| `week2/day03_readinglab3.py` | CPython 3.13, `Lib/graphlib.py:59` | sets for membership, an order you must not rely on, `sorted()` as the only predictable render |
| `week2/day04_readinglab4.py` | CPython 3.13, `Lib/csv.py:145` | `DictReader`: `restkey` collects leftovers, `restval` fills a short row |
| `week2/day05_readinglab5.py` | CPython 3.13, `Lib/json/decoder.py:353` | `JSONDecodeError` is a `ValueError`, and builds its own line/column message |

## Week 3

| File | What it does |
|---|---|
| `week3/day01_drill01.py` | `final_price`, `clamp_all`, `merge_prefs` — default and keyword arguments, returning a new value instead of changing the caller's |
| `week3/day02_drill02.py` | `simplify`, `strip_punctuation`, `is_palindrome` — `math.gcd`, `string.punctuation`, `str.casefold` instead of retyped loops |
| `week3/day03_drill03.py` | `append_all`, `with_tax`, `without_key` — pure functions: every check asserts the source is unchanged |
| `week3/day04_drill04.py` | `grade`, `parse_bool`, `format_duration` — boundary cases written as tests, `ValueError` for what is not a value |
| `week3/day05_drill05.py` | three programs that run and lie — find the mutation, the missing `nonlocal`, and the shared default; fix bodies only |
| `week3/day06_tools.py` | seven small pure functions for the Week-2 to-do data (`new_id` … `parse_command`), no file I/O and no `print` |
| `week3/day06_test_tools.py` | ten `pytest` tests, one edge case each; starts as 10 failed stubs, done at 10 passed |

Reading labs.

| File | Source | What it exercises |
|---|---|---|
| `week3/day01_readinglab1.py` | own snippet | a default argument is built once at `def`, so later calls share it; a local assignment never reaches the global |
| `week3/day02_readinglab2.py` | CPython 3.13, `Lib/string.py:37` | `capwords`: `sep or ' '` hides a default, `split(None)` collapses runs of whitespace |
| `week3/day03_readinglab3.py` | CPython 3.13, `Lib/statistics.py:621` | `median` sorts a copy (`sorted`, never `.sort()`), interpolates an even count, raises `StatisticsError` on empty |
| `week3/day04_readinglab4.py` | own snippet | a five-test file: one test passes on a type the docstring never promised, one call raises `ValueError` |
| `week3/day05_readinglab5.py` | own snippet | walking to the innermost traceback frame; exception type, message, and which function actually raised |
