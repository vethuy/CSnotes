"""Reading lab 1 - pseudocode you can check, and the leftmost match.

READ FIRST, RUN LATER (20 minutes)
 1. Read the pseudocode block, then the Python under it. No terminal yet.
 2. Write your answers in the PREDICTION block at the bottom.
 3. Only then run:  python week4/day01_readinglab1.py
 4. Answer in journal.md: the loop says `while lo < hi`, not `<=`. What goes
    wrong with `<=` on a list where target is absent?  Nothing here is yours
    to write.

Pseudocode, the version from the book:

    lo = 0 ; hi = length
    while lo < hi:
        mid = (lo + hi) // 2
        if items[mid] < target:  lo = mid + 1
        else:                    hi = mid
    return lo

That is not "find the item". It is "find the place where the item belongs":
the returned index is the first item that is >= target, or len(items). The
Python below is the same loop, taken from CPython 3.13, Lib/bisect.py:74
(bisect_left, with the optional lo / hi / key parameters removed).

Source: CPython 3.13, Lib/bisect.py:74
"""


# FUNCTION INTRODUCTION: bisect_left(items, target) returns the first index i
# where items[i] >= target - the insertion point. It never raises on an empty
# list: lo and hi both start at 0, the loop body never runs, and 0 is returned.
def bisect_left(items, target):
    """Return the first index where target could be inserted, keeping order."""
    lo, hi = 0, len(items)
    while lo < hi:
        mid = (lo + hi) // 2
        if items[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


# --------------------------------------------------------------- the answers
if __name__ == "__main__":
    print("empty list     ", bisect_left([], 5))
    print("single hit     ", bisect_left([7], 7))
    print("single miss    ", bisect_left([7], 9))
    print("past the end   ", bisect_left([1, 3, 5], 9))
    print("duplicates     ", bisect_left([1, 3, 3, 3, 7], 3))
    print("between items  ", bisect_left([1, 3, 3, 5], 4))

    values = [1, 3, 5]
    values.insert(bisect_left(values, 4), 4)
    print("after insert   ", values)


'''PREDICTION - write before running.

1) empty list      -> ?
2) single hit      -> ?
3) single miss     -> ?
4) past the end    -> ?
5) duplicates      -> ?   (why is it not 2?)
6) between items   -> ?
7) after insert    -> ?
8) [1, 3, 5, 7, 9], target 9: how many times does the while loop run?

ACTUAL - paste after running.
'''
