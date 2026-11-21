"""Reading lab 3 - a stdlib function that sorts a copy, and one that raises.

READ FIRST, RUN LATER (20 minutes)
 1. Read `median` below and the five calls. No terminal yet.
 2. Write your five answers in the PREDICTION block at the bottom.
 3. Only then run:  python week3/day03_readinglab3.py
 4. Answer in journal.md: what would break if line 634 were `data.sort()`
    instead of `data = sorted(data)`? Nothing here is yours to write.

The stdlib version: statistics.py:621 `median`, read lines 621-642. Line 634 is
the one to notice:

    data = sorted(data)

`sorted` returns a NEW list; `data.sort()` would return None and reorder the
caller's list. That one choice is what makes `median` pure. Line 636-637 is the
other one: an empty input raises `StatisticsError`, a ValueError subclass the
module defines for itself.
"""

import statistics


# --------------------------------------------------------------- the answers
if __name__ == "__main__":
    print("1) statistics.median([3, 1, 2])       =", repr(statistics.median([3, 1, 2])))
    print("2) statistics.median([1, 2, 3, 4])    =", repr(statistics.median([1, 2, 3, 4])))
    print("3) statistics.median([3, 1, 2, 1])    =", repr(statistics.median([3, 1, 2, 1])))

    source = [3, 1, 2]
    statistics.median(source)
    print("4) the list [3, 1, 2] after the call  =", repr(source))

    try:
        statistics.median([])
    except Exception as exc:
        print("5) statistics.median([]) raises     =", type(exc).__name__, "-", exc)


'''PREDICTION - write before running.

1) statistics.median([3, 1, 2]) =
2) statistics.median([1, 2, 3, 4]) =
3) statistics.median([3, 1, 2, 1]) =
4) the list [3, 1, 2] after the call =
5) statistics.median([]) raises  (type and message) =


ACTUAL - paste after running.

1)
2)
3)
4)
5)

One sentence on the miss:
'''
