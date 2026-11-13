"""Week 2 . Day 3 . reading lab 3 - graphlib, dict of sets  (Lib/graphlib.py:59).

WHAT THIS LAB IS
----------------
You read one small part of the standard library, then close the file and
rebuild its shape from memory. Simplified is fine. Do not import the module you
are rewriting and do not paste from it.

LAST 3 MINUTES OF THE LAB: write the body below, from memory, then run the
check. If the check fails, do not reopen the source - read the error and think.

RUN THE CHECK:   python week2/day03_readinglab3.py
"""


def predecessor_counts(node_to_predecessors):
    """Return dict node -> how many predecessors it has.

    The argument has the shape graphlib keeps internally: node -> set of nodes.

    predecessor_counts({"a": set(), "b": {"a"}}) -> {"a": 0, "b": 1}
    """
    raise NotImplementedError("predecessor_counts")


# --------------------------------------------------------------------------
# CHECK - do not edit below this line
# --------------------------------------------------------------------------
if __name__ == "__main__":
    assert predecessor_counts({"a": set(), "b": {"a"}, "c": {"a", "b"}}) == {
        "a": 0,
        "b": 1,
        "c": 2,
    }

    print("rewrite 3 passes")
