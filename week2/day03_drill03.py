"""Week 2 . Day 3 . set, and choosing the container.

RUN THE CHECKS:   python week2/day03_drill03.py

RULES
-----
1. Every function RETURNS its result. Nothing above the check block prints.
2. No input() in this file.
3. Do not modify the argument unless the contract says you may.
4. Look up syntax only when a name is missing; 5 minutes maximum, then ask.
5. The check block at the bottom is the acceptance test. Do not edit it.

THE POINT: "have I seen this before?" is a set question. Once you answer it
with a set, half your loops disappear - and so does the duplicate bug.

LOAD: 1 drill, 3 functions, about 20-25 minutes. Each function carries a
CORE IDEA line - read it before you type. Stuck 5 minutes after reading it?
Ask.
"""

PUNCTUATION = ".,!?;:\"'"


# CORE IDEA: a set is not "a list with no duplicates" - it is the answer to
# "which different things are in here?". Build it with a comprehension and
# let the set do the de-duplicating you were writing by hand in week 1.
def unique_words(text):
    """Return the set of distinct words in text.

    Lowercase the text, strip PUNCTUATION from both ends of each word, and
    drop words that are empty after stripping. Return set() for "".

    unique_words("The cat, the dog!") -> {"the", "cat", "dog"}
    unique_words("a a A")             -> {"a"}
    unique_words("")                  -> set()
    """
    raise NotImplementedError("unique_words")


# CORE IDEA: & is intersection, | is union, - is difference. The operator
# already means "both", so there is no loop left to write - only the sort,
# because a set's order is not yours to choose.
def common_words(a, b):
    """Return a sorted list of the words that are in both a and b.

    a and b are sets of words. Return [] when either is empty.

    common_words({"red", "blue"}, {"blue", "green"}) -> ["blue"]
    common_words({"b", "a"}, {"a", "b"})             -> ["a", "b"]
    common_words(set(), {"a"})                       -> []
    """
    raise NotImplementedError("common_words")


# CORE IDEA: keep order and remove duplicates at the same time: one list for
# the answer, one set for "already answered". The set is a notebook, not the
# output - so the output keeps its order.
def dedupe_keep_order(nums):
    """Return a new list, duplicates removed, first-seen order kept.

    nums must not be modified.

    dedupe_keep_order([3, 1, 3, 2, 1]) -> [3, 1, 2]
    dedupe_keep_order([])              -> []
    """
    raise NotImplementedError("dedupe_keep_order")


# --------------------------------------------------------------------------
# CHECKS - do not edit below this line
# --------------------------------------------------------------------------
if __name__ == "__main__":
    # unique_words
    assert unique_words("The cat, the dog!") == {"the", "cat", "dog"}
    assert isinstance(unique_words("x"), set), "must return a set, not a list"
    assert unique_words("a a A") == {"a"}
    assert unique_words("") == set()
    assert unique_words("word") == {"word"}

    # common_words
    assert common_words({"red", "blue"}, {"blue", "green"}) == ["blue"]
    assert common_words({"b", "a"}, {"a", "b"}) == ["a", "b"]
    assert common_words(set(), {"a"}) == []
    assert common_words({"a"}, set()) == []
    assert common_words({"a", "b"}, {"a", "b"}) == ["a", "b"]

    # dedupe_keep_order
    assert dedupe_keep_order([3, 1, 3, 2, 1]) == [3, 1, 2]
    assert dedupe_keep_order([]) == []
    assert dedupe_keep_order([1, 1, 1]) == [1]
    source = [4, 4, 5]
    dedupe_keep_order(source)
    assert source == [4, 4, 5], "dedupe_keep_order must not modify its argument"

    print("all drills pass")
