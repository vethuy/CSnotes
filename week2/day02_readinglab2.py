"""Week 2 . Day 2 . reading lab 2 - Counter.most_common  (Lib/collections/__init__.py:622).

WHAT THIS LAB IS
----------------
You read one small function in the standard library, then close the file and
rebuild its shape from memory. Simplified is fine. Do not import the module you
are rewriting and do not paste from it.

LAST 3 MINUTES OF THE LAB: write the body below, from memory, then run the
check. If the check fails, do not reopen the source - read the error and think.

RUN THE CHECK:   python week2/day02_readinglab2.py
"""


def my_most_common(counts, n):
    """Return the n highest (key, count) pairs, highest first.

    Ties keep the order the keys already have in counts (that is how Counter
    behaves). n larger than len(counts) returns every pair.

    my_most_common({"a": 3, "b": 1, "c": 2}, 2) -> [("a", 3), ("c", 2)]
    """
    raise NotImplementedError("my_most_common")


# --------------------------------------------------------------------------
# CHECK - do not edit below this line
# --------------------------------------------------------------------------
if __name__ == "__main__":
    assert my_most_common({"a": 3, "b": 1, "c": 2}, 2) == [("a", 3), ("c", 2)]
    assert my_most_common({"b": 1, "a": 1}, 2) == [("b", 1), ("a", 1)]
    assert my_most_common({"a": 1}, 5) == [("a", 1)]

    print("rewrite 2 passes")
