"""Week 2 . Day 2-3 . day02_word_count.py

RUN THE PROGRAM:   python week2/day02_word_count.py
                   python week2/day02_word_count.py week2/data/day02_sample.txt
RUN THE CHECKS:    python week2/day02_word_count.py --check v0     (Tuesday)
                   python week2/day02_word_count.py --check v1     (Wednesday, default)

REQUIREMENTS - v0 (Tuesday)
---------------------------
* read_words(path) -> list[str]: read the UTF-8 file, skip blank lines and
  lines whose stripped form starts with "#", return the normalised words of
  the remaining lines.
* normalize(text) -> list[str]: lowercase every token, strip the characters
  in string.punctuation from both ends, drop tokens that become empty.
* count_words(words) -> dict word -> count.
* top_n(counts, n) -> list of (word, count), highest count first, ties
  alphabetical, n entries (same contract as Day 2).
* main() -> None: read the path from sys.argv[1] (default data/day02_sample.txt),
  print the report, print nothing else.

REQUIREMENTS - v1 (Wednesday, on top of v0)
-------------------------------------------
* unique_count(words) -> int: how many distinct words.
* The report's first line becomes "<N> words, <U> unique" and main() shows
  the top 10 instead of the top 5.

REPORT FORMAT (judged by eye, not asserted)
-------------------------------------------
    21 words, 11 unique

    the        4
    dog        3
    fox        3

One word per line, count in a second column, blank line after the summary.

CHECKS
------
python week2/day02_word_count.py --check       prints "v1 checks pass"
python week2/day02_word_count.py --check v0    prints "v0 checks pass"
"""

import sys
from pathlib import Path

DATA = Path(__file__).resolve().parent / "data"
SAMPLE = DATA / "day02_sample.txt"


def read_words(path):
    """Return the words of the UTF-8 text file at path, comments and blanks out."""
    raise NotImplementedError("read_words")


def normalize(text):
    """Return the lowercased, punctuation-stripped tokens of text, empties dropped."""
    raise NotImplementedError("normalize")


def count_words(words):
    """Return a dict word -> how many times it occurs."""
    raise NotImplementedError("count_words")


def top_n(counts, n):
    """Return the n highest (word, count) pairs: count desc, then word asc."""
    raise NotImplementedError("top_n")


def unique_count(words):
    """Return how many distinct words are in words.  (v1, Wednesday)"""
    raise NotImplementedError("unique_count")


def main():
    """Print the report: summary line, blank line, then the top words."""
    raise NotImplementedError("main")


# --------------------------------------------------------------------------
# CHECKS - do not edit below this line
# --------------------------------------------------------------------------
def check_v0():
    words = read_words(SAMPLE)
    assert len(words) == 21, f"expected 21 words, got {len(words)}"
    assert words[0] == "the", f"first word should be 'the', got {words[0]!r}"
    assert "comment" not in words, "lines starting with # must be skipped"
    assert "" not in words, "empty tokens must be dropped"

    assert normalize("Hi, THERE!") == ["hi", "there"]
    assert normalize("   ") == []

    counts = count_words(words)
    assert counts["the"] == 4
    assert counts["dog"] == 3
    assert counts["fox"] == 3
    assert len(counts) == 11
    assert sum(counts.values()) == 21

    assert top_n(counts, 3) == [("the", 4), ("dog", 3), ("fox", 3)]
    assert top_n(counts, 0) == []
    print("v0 checks pass")


def check_v1():
    words = read_words(SAMPLE)
    assert unique_count(words) == 11
    counts = count_words(words)
    assert top_n(counts, 10)[0] == ("the", 4)
    assert len(top_n(counts, 10)) == 10
    assert len(top_n(counts, 99)) == 11
    print("v1 checks pass")


if __name__ == "__main__":
    argv = sys.argv[1:]
    if "--check" in argv:
        rest = argv[argv.index("--check") + 1:]
        mode = rest[0] if rest else "v1"
        check_v0()
        if mode == "v1":
            check_v1()
    else:
        main()
