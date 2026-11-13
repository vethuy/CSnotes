"""Week 2 . Day 3 . set, and choosing the right container.

RUN THE CHECKS:   python week2/day03_drill03.py

RULES
-----
1. Every function RETURNS its result. Nothing above the check block prints.
2. No input() in this file.
3. Set order is never guaranteed: where the contract asks for a list,
   the list has to be sorted or built by you.
4. The check block is the acceptance test. Do not edit it.

The __main__ block also runs a timing experiment. Its two numbers go into
journal.md with one line: which container, and why.
"""

import string
import time


def unique_words(text):
    """Return the set of distinct words in text.

    Same normalisation as Day 2: lowercase, strip string.punctuation at both
    ends, drop empties.

    unique_words("Red red BLUE") -> {"red", "blue"}
    unique_words("")             -> set()
    """
    raise NotImplementedError("unique_words")


def common_words(first, second):
    """Return the words present in BOTH sets, as a sorted list.

    common_words({"red", "blue"}, {"blue", "green"}) -> ["blue"]
    common_words(set(), {"a"})                       -> []
    """
    raise NotImplementedError("common_words")


def missing_letters(text):
    """Return the set of lowercase letters a-z that do not occur in text.

    Case is ignored; characters that are not letters are ignored.

    missing_letters("The quick brown fox jumps over the lazy dog") -> set()
    len(missing_letters("abc"))                                    -> 23
    """
    raise NotImplementedError("missing_letters")


def dedupe_fast(nums):
    """Return the distinct items of nums as a list, in ANY order.

    The body is one line and uses a set.
    """
    raise NotImplementedError("dedupe_fast")


def dedupe_keep_order(nums):
    """Return the distinct items of nums, first-seen order kept.

    One pass: a set that remembers what you have seen plus a list you append to.

    dedupe_keep_order([3, 1, 3, 2]) -> [3, 1, 2]
    """
    raise NotImplementedError("dedupe_keep_order")


# --------------------------------------------------------------------------
# CHECKS - do not edit below this line
# --------------------------------------------------------------------------
if __name__ == "__main__":
    # unique_words
    assert unique_words("Red red BLUE") == {"red", "blue"}
    assert unique_words("") == set()
    assert unique_words("dog, dog.") == {"dog"}

    # common_words
    assert common_words({"red", "blue"}, {"blue", "green"}) == ["blue"]
    assert common_words(set(), {"a"}) == []
    assert common_words({"b", "a"}, {"a", "b"}) == ["a", "b"]

    # missing_letters
    assert len(missing_letters("abc")) == 23
    assert missing_letters("abc") == set(string.ascii_lowercase) - set("abc")
    assert missing_letters("The quick brown fox jumps over the lazy dog") == set()
    assert missing_letters("") == set(string.ascii_lowercase)

    # dedupe
    assert sorted(dedupe_fast([3, 1, 3, 2])) == [1, 2, 3]
    assert dedupe_fast([]) == []
    assert dedupe_keep_order([3, 1, 3, 2]) == [3, 1, 2]
    assert dedupe_keep_order([]) == []
    assert dedupe_keep_order(["a", "a"]) == ["a"]

    # timing experiment (prints, does not assert) - copy both numbers to journal.md
    big_list = list(range(200_000))
    big_set = set(big_list)
    for name, container in (("list", big_list), ("set", big_set)):
        start = time.perf_counter()
        for _ in range(1000):
            199_999 in container
        elapsed_ms = round((time.perf_counter() - start) * 1000, 1)
        print(f"{name:5} {elapsed_ms:>8} ms")

    print("all drills pass")
