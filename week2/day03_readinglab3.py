"""Reading lab 3 - set algebra, and an order you must not rely on.

READ FIRST, RUN LATER (20 minutes)
 1. Read the two functions and the four calls. No terminal yet.
 2. Write your four answers in the PREDICTION block at the bottom.
 3. Only then run:  python week2/day03_readinglab3.py
 4. Answer in reading-notes.md: why is `sorted(...)` the only way to write a
    set to the screen in a predictable order? Nothing here is yours to write.

The stdlib version: graphlib.py:59 `TopologicalSorter` keeps `_predecessors`
as a dict of SETS, because "who must come before me" is a membership
question, not a list of history. Read `add` and `prepare` for 12 minutes.

Note: the predictions ask about INT sets only. A set of strings prints in an
order that changes between runs - never predict that.
"""


def overlap(a, b):
    """Return the items that are in both sets."""
    return a & b


def only_in(a, b):
    """Return the items of a that are not in b."""
    return a - b


# --------------------------------------------------------------- the answers
if __name__ == "__main__":
    print("1) overlap({1, 2, 3}, {2, 3, 4}) =", repr(overlap({1, 2, 3}, {2, 3, 4})))
    print("2) sorted(only_in({'a', 'b'}, {'b'})) =", repr(sorted(only_in({"a", "b"}, {"b"}))))
    print("3) list(set([3, 1, 2, 1])) =", repr(list(set([3, 1, 2, 1]))))
    print("4) len({'a', 'a', 'b'}) =", repr(len({"a", "a", "b"})))


'''PREDICTION - write before running.

1)
2)
3)
4)

ACTUAL

1)
2)
3)
4)

One sentence on the miss (if any):
'''
