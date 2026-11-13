"""Week 2 . Day 4 . files.

RUN THE CHECKS:   python week2/day04_drill04.py

RULES
-----
1. Every function RETURNS its result (or None when it only writes).
2. Always pass encoding="utf-8" to open().
3. A path that does not exist must raise FileNotFoundError - do not catch it
   here; Friday's job is to decide what main() says about it.
4. The check block is the acceptance test. Do not edit it.

MANUAL CHECKS (they create files, so they are not in the check block).
Run these from the CSnotes folder, then look at the result:

    python -c "from week2 import day04_drill04 as d; d.write_numbered('week2/data/out.txt', ['first', 'second'])"
    type week2\\data\\out.txt

Expected content of week2\\data\\out.txt:

    1. first
    2. second

    python -c "from week2 import day04_drill04 as d; d.append_log('week2/data/out.txt', 'hello')"
    type week2\\data\\out.txt

The second command adds a line shaped like  2026-11-19 20:31 | hello
(run it twice: the line is appended, nothing is overwritten).
Delete week2\\data\\out.txt when you are done.
"""

from pathlib import Path

DATA = Path(__file__).resolve().parent / "data"
SAMPLE = DATA / "day02_sample.txt"
NUMBERS = DATA / "day04_numbers.txt"


def count_lines(path):
    """Return how many lines of the file are not blank.

    A line holding only whitespace counts as blank. The "\\n" is not content.

    count_lines(week2/data/day02_sample.txt) -> 3
    """
    raise NotImplementedError("count_lines")


def longest_line(path):
    """Return the stripped text of the longest line that carries content.

    Blank lines and lines whose stripped form starts with "#" are skipped.
    Ties: the first one wins.
    The returned string has no trailing "\\n".

    longest_line(week2/data/day02_sample.txt).startswith("The dog barks") -> True
    longest_line(week2/data/day04_numbers.txt)                           -> "-3.25"
    """
    raise NotImplementedError("longest_line")


def read_numbers(path):
    """Return the file's numbers as a list of float.

    Blank lines and lines whose stripped form starts with "#" are skipped.
    Anything else must convert with float(); a bad line raises ValueError
    and is not skipped silently.

    read_numbers(week2/data/day04_numbers.txt) -> [12.5, 7.0, -3.25, 42.0]
    """
    raise NotImplementedError("read_numbers")


def write_numbered(path, lines):
    """Write lines to path as "1. <line>" numbered from 1, one per row.

    The file is overwritten. The last row ends with a newline.
    Returns None.
    """
    raise NotImplementedError("write_numbered")


def append_log(path, message):
    """Append one line to path: "<YYYY-MM-DD HH:MM> | <message>".

    The timestamp comes from datetime.now().strftime("%Y-%m-%d %H:%M").
    The file is created when it does not exist. Earlier content is kept.
    Returns None.
    """
    raise NotImplementedError("append_log")


# --------------------------------------------------------------------------
# CHECKS - do not edit below this line
# --------------------------------------------------------------------------
if __name__ == "__main__":
    # count_lines
    assert count_lines(SAMPLE) == 3
    assert count_lines(NUMBERS) == 5

    # longest_line
    longest = longest_line(SAMPLE)
    assert longest.startswith("The dog barks"), f"got {longest!r}"
    assert not longest.endswith("\n")
    assert longest_line(NUMBERS) == "-3.25"

    # read_numbers
    assert read_numbers(NUMBERS) == [12.5, 7.0, -3.25, 42.0]
    assert all(isinstance(value, float) for value in read_numbers(NUMBERS))

    # a path that does not exist must not be swallowed here
    for func in (count_lines, longest_line, read_numbers):
        try:
            func(DATA / "no_such_file.txt")
        except FileNotFoundError:
            pass
        else:
            raise AssertionError(f"{func.__name__} must let FileNotFoundError escape")

    print("all checks pass")
