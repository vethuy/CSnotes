"""Reading lab 5 - the stack has a ceiling, and 2000 items are enough to hit it.

READ FIRST, RUN LATER (20 minutes)
 1. Read `sum_recursive` and `depth`. How many frames does each item add?
    No terminal yet.
 2. Write your answers in the PREDICTION block at the bottom.
 3. Only then run:  python week4/day05_readinglab5.py
 4. Answer in journal.md: the loop and the recursion compute the same number.
    Which one would you put in a library, and why is the other still worth
    knowing?  Nothing here is yours to write.

`depth` has no base case on purpose: it is a controlled crash, caught by the
`except`, to show that Python refuses to grow the stack forever. The default
limit is 1000 frames on CPython (sys.getrecursionlimit()), and every call in
`sum_recursive` - including the slices - adds at least one.
"""

import sys


def sum_loop(items):
    """Return the sum with a for loop."""
    total = 0
    for item in items:
        total += item
    return total


def sum_recursive(items):
    """Return the sum with recursion: first item plus the sum of the rest."""
    if not items:
        return 0
    return items[0] + sum_recursive(items[1:])


def depth(n):
    """Recurse forever; the interpreter stops us, not this line."""
    return 1 + depth(n + 1)


# --------------------------------------------------------------- the answers
if __name__ == "__main__":
    print("recursion limit   ", sys.getrecursionlimit())
    print("loop 2000 items   ", sum_loop(list(range(2000))))
    print("recursion 100     ", sum_recursive(list(range(100))))
    try:
        print("recursion 2000    ", sum_recursive(list(range(2000))))
    except RecursionError as exc:
        print("recursion 2000    raises", type(exc).__name__, "-", exc)
    try:
        depth(0)
    except RecursionError as exc:
        print("depth(0)          raises", type(exc).__name__, "-", exc)


'''PREDICTION - write before running.

1) recursion limit = ?
2) loop 2000 items = ?
3) recursion 100   = ?
4) recursion 2000  -> a number, or an exception?  Which type, which message?
5) depth(0)        -> which type, which message?
6) Are the two exception messages the same?  Why?

ACTUAL - paste after running.
'''
