"""Week 2 . Day 4 . files.

RUN THE CHECKS:   python week2/day04_drill04.py

RULES
-----
1. Every function RETURNS its result. Nothing above the check block prints.
2. No input() in this file.
3. Do not modify the argument unless the contract says you may.
4. Look up syntax only when a name is missing; 5 minutes maximum, then ask.
5. The check block at the bottom is the acceptance test. Do not edit it.

THE POINT: a file is not a thing you read - it is a stream you walk one line
at a time. Every line still carries its "\\n" until you strip it.

LOAD: 1 drill, 3 functions, about 20-25 minutes. Each function carries a
CORE IDEA line - read it before you type. Stuck 5 minutes after reading it?
Ask. The check block writes its files into a temporary folder, so you never
need to clean anything up.
"""


# CORE IDEA: "how many lines" is not len(file) - it is a count of the lines
# that have something in them. Decide what an empty line means before you
# write the loop, and you will not need two passes over the file.
def count_lines(path):
    """Return how many lines in the file have visible text.

    A line that is empty or only whitespace does not count.
    path may be a str or a pathlib.Path.

    count_lines("one.txt") -> 3   # for a file with 5 lines, 2 of them blank
    """
    raise NotImplementedError("count_lines")


# CORE IDEA: "the longest" needs a memory, and the memory starts empty. Keep
# the best line you have seen so far and replace it only when the new line is
# strictly longer - "strictly" is what keeps the first one on a tie.
def longest_line(path):
    """Return the longest line with surrounding whitespace stripped.

    Return "" when the file has no non-blank line. On a tie return the line
    that appears first.

    longest_line("one.txt") -> "second line"
    """
    raise NotImplementedError("longest_line")


# CORE IDEA: a reader has two kinds of line: data and commentary. Skipping
# is a filter, and converting is a second step - keep them apart and the
# failure tells you which line was wrong.
def read_numbers(path):
    """Return a list of floats read from the file.

    Skip blank lines, and skip lines whose first non-space character is "#".
    A line that is not a number raises ValueError whose message contains the
    offending text.

    read_numbers("nums.txt") -> [1.5, 2.0, 3.25]
    """
    raise NotImplementedError("read_numbers")


# --------------------------------------------------------------------------
# CHECKS - do not edit below this line
# --------------------------------------------------------------------------
if __name__ == "__main__":
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as tmp:
        folder = Path(tmp)
        basic = folder / "basic.txt"
        basic.write_text("first\n\nsecond line\n   \nthird\n", encoding="utf-8")
        assert count_lines(basic) == 3
        assert longest_line(basic) == "second line"

        empty = folder / "empty.txt"
        empty.write_text("", encoding="utf-8")
        assert count_lines(empty) == 0
        assert longest_line(empty) == ""

        blanks = folder / "blanks.txt"
        blanks.write_text("\n   \n\t\n", encoding="utf-8")
        assert count_lines(blanks) == 0
        assert longest_line(blanks) == ""

        tie = folder / "tie.txt"
        tie.write_text("abcd\nwxyz\n", encoding="utf-8")
        assert longest_line(tie) == "abcd", "on a tie keep the first line"

        nums = folder / "nums.txt"
        nums.write_text("1.5\n\n# a note\n2\n  3.25  \n", encoding="utf-8")
        assert read_numbers(nums) == [1.5, 2.0, 3.25]
        assert read_numbers(empty) == []

        bad = folder / "bad.txt"
        bad.write_text("1.5\nnot-a-number\n", encoding="utf-8")
        try:
            read_numbers(bad)
            assert False, "a bad line must raise ValueError"
        except ValueError as exc:
            assert "not-a-number" in str(exc), "the message must name the bad line"

    print("all drills pass")
