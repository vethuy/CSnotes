"""Week 2 . Day 2 . dict.

RUN THE CHECKS:   python week2/day02_drill02.py

RULES
-----
1. Every function RETURNS its result. Nothing above the check block prints.
2. No input() in this file.
3. Do not modify the argument unless the contract says you may.
4. Look up syntax only when a name is missing; 5 minutes maximum, then ask.
5. The check block at the bottom is the acceptance test. Do not edit it.

THE POINT: a list makes you search for what you saw before. A dict makes
that search a single lookup, so counting stops being a loop over the past.

LOAD: 1 drill, 3 functions, about 20-25 minutes. Each function carries a
CORE IDEA line - read it before you type. Stuck 5 minutes after reading it?
Ask.
"""


# CORE IDEA: counts[ch] += 1 fails because the key is not there yet. The
# question is not "how do I add one?" but "what is the count of a key I have
# never seen?" - and the answer to that is 0.
def char_count(text):
    """Return {character: how many times it appears}, ignoring spaces.

    text is a str. Case is NOT folded ("A" and "a" are different keys).
    Return {} for "".

    char_count("aab")  -> {"a": 2, "b": 1}
    char_count("a a")  -> {"a": 2}
    char_count("")     -> {}
    """
    raise NotImplementedError("char_count")


# CORE IDEA: a dict of lists is built in two steps - get the bucket, then
# append. First time the key appears the bucket does not exist, so create it
# on demand instead of testing `if key in d` first.
def group_by_first_letter(words):
    """Return {first_letter: [words starting with it]} keeping input order.

    words is a list of non-empty strings. The dict keeps the order in which
    each first letter was seen. Return {} for [].

    group_by_first_letter(["apple", "ant", "bee"])
        -> {"a": ["apple", "ant"], "b": ["bee"]}
    group_by_first_letter(["bee", "ant", "apple"])
        -> {"b": ["bee"], "a": ["ant", "apple"]}
    """
    raise NotImplementedError("group_by_first_letter")


# CORE IDEA: two rules (count high first, then alphabetical) look like two
# sorts. They are one sort if you sort on a tuple: (-count, word) puts the
# big counts first and breaks ties by name.
def top_n(counts, n):
    """Return the n most common pairs of counts as [(word, count), ...].

    Order: count descending, then word ascending for equal counts.
    Return [] when n <= 0 or counts is empty. Never modify counts.

    top_n({"a": 3, "b": 1, "c": 2}, 2) -> [("a", 3), ("c", 2)]
    top_n({"a": 1, "b": 1}, 2)         -> [("a", 1), ("b", 1)]
    top_n({"a": 1}, 0)                 -> []
    """
    raise NotImplementedError("top_n")


# --------------------------------------------------------------------------
# CHECKS - do not edit below this line
# --------------------------------------------------------------------------
if __name__ == "__main__":
    # char_count
    assert char_count("aab") == {"a": 2, "b": 1}
    assert char_count("") == {}
    assert char_count("a a") == {"a": 2}
    assert " " not in char_count("a b")
    assert char_count("Aa") == {"A": 1, "a": 1}

    # group_by_first_letter
    assert group_by_first_letter(["apple", "ant", "bee"]) == {
        "a": ["apple", "ant"],
        "b": ["bee"],
    }
    assert group_by_first_letter([]) == {}
    assert group_by_first_letter(["bee", "ant", "apple"])["a"] == ["ant", "apple"]
    assert list(group_by_first_letter(["b", "a"])) == ["b", "a"], "keep first-seen order"

    # top_n
    assert top_n({"a": 3, "b": 1, "c": 2}, 2) == [("a", 3), ("c", 2)]
    assert top_n({"a": 1, "b": 1}, 2) == [("a", 1), ("b", 1)]
    assert top_n({"b": 1, "a": 1}, 2) == [("a", 1), ("b", 1)]
    assert top_n({"a": 1}, 5) == [("a", 1)]
    assert top_n({"a": 1}, 0) == []
    assert top_n({}, 3) == []
    original = {"a": 3, "b": 1}
    top_n(original, 2)
    assert original == {"a": 3, "b": 1}, "top_n must not modify its argument"

    print("all drills pass")
