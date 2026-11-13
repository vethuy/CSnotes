"""Week 2 . Day 2 . dict.

RUN THE CHECKS:   python week2/day02_drill02.py

RULES
-----
1. Every function RETURNS its result. Nothing above the check block prints.
2. No input() in this file.
3. Do not modify the argument unless the contract says you may.
4. Where a contract says "keys in first-appearance order", that order matters.
5. The check block is the acceptance test. Do not edit it.
"""


def char_count(text):
    """Return a dict of character -> how many times it occurs in text.

    Whitespace is ignored. Case is kept as written (so "aA" is not "aa").
    Keys appear in first-appearance order.

    char_count("aab")   -> {"a": 2, "b": 1}
    char_count("a b")   -> {"a": 1, "b": 1}
    char_count("")      -> {}
    """
    raise NotImplementedError("char_count")


def invert(mapping):
    """Return a new dict with keys and values swapped.

    When two keys share a value, the LAST one wins.
    invert({"a": 1, "b": 1}) -> {1: "b"}
    """
    raise NotImplementedError("invert")


def group_by_first_letter(words):
    """Group words by their first character.

    Return a dict char -> list of words, both in the order the words appear.
    group_by_first_letter([]) returns {}.
    The input list must not be modified.

    group_by_first_letter(["apple", "ant", "bee"])
        -> {"a": ["apple", "ant"], "b": ["bee"]}
    """
    raise NotImplementedError("group_by_first_letter")


def word_lengths(sentence):
    """Return a dict word -> len(word) for sentence.split().

    Implement the body as a single dict comprehension (one line).
    Duplicated words keep their first position, last value is the same anyway.

    word_lengths("hi there") -> {"hi": 2, "there": 5}
    word_lengths("")         -> {}
    """
    raise NotImplementedError("word_lengths")


def top_n(counts, n):
    """Return the n highest entries of counts as a list of (key, count) tuples.

    Highest count first; equal counts in alphabetical order of the key.
    n may be 0 (-> []) or larger than len(counts) (-> every entry).
    counts must not be modified.

    top_n({"a": 3, "b": 1, "c": 2}, 2) -> [("a", 3), ("c", 2)]
    top_n({"b": 1, "a": 1}, 2)         -> [("a", 1), ("b", 1)]
    """
    raise NotImplementedError("top_n")


def merge_counts(first, second):
    """Return a new dict: counts added together for shared keys, keys kept
    from both dicts, first's keys before second's new keys.

    Neither argument is modified.

    merge_counts({"a": 2, "b": 1}, {"b": 3, "c": 4}) -> {"a": 2, "b": 4, "c": 4}
    """
    raise NotImplementedError("merge_counts")


# --------------------------------------------------------------------------
# CHECKS - do not edit below this line
# --------------------------------------------------------------------------
if __name__ == "__main__":
    # char_count
    assert char_count("aab") == {"a": 2, "b": 1}
    assert char_count("a b") == {"a": 1, "b": 1}
    assert char_count("") == {}
    assert list(char_count("aab")) == ["a", "b"]
    assert char_count("aA") == {"a": 1, "A": 1}

    # invert
    assert invert({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    assert invert({"a": 1, "b": 1}) == {1: "b"}
    assert invert({}) == {}

    # group_by_first_letter
    assert group_by_first_letter(["apple", "ant", "bee"]) == {
        "a": ["apple", "ant"],
        "b": ["bee"],
    }
    assert group_by_first_letter([]) == {}
    assert list(group_by_first_letter(["bee", "ant"])) == ["b", "a"]
    words = ["apple", "ant"]
    group_by_first_letter(words)
    assert words == ["apple", "ant"], "group_by_first_letter must not modify its input"

    # word_lengths
    assert word_lengths("hi there") == {"hi": 2, "there": 5}
    assert word_lengths("") == {}

    # top_n
    assert top_n({"a": 3, "b": 1, "c": 2}, 2) == [("a", 3), ("c", 2)]
    assert top_n({"b": 1, "a": 1}, 2) == [("a", 1), ("b", 1)]
    assert top_n({"a": 1}, 0) == []
    assert top_n({"a": 1}, 5) == [("a", 1)]
    counts = {"a": 1}
    top_n(counts, 1)
    assert counts == {"a": 1}, "top_n must not modify counts"

    # merge_counts
    assert merge_counts({"a": 2, "b": 1}, {"b": 3, "c": 4}) == {"a": 2, "b": 4, "c": 4}
    assert list(merge_counts({"a": 1}, {"b": 2})) == ["a", "b"]
    assert merge_counts({}, {}) == {}

    print("all drills pass")
