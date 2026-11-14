"""Reading lab 1 - what a returned number really is.

READ FIRST, RUN LATER (20 minutes)
 1. Read mean() and the four calls below. Leave the terminal closed.
 2. Write your four answers in the PREDICTION block at the bottom.
 3. Only then run:  python week2/day01_readinglab1.py
 4. Copy the printed lines into ACTUAL and mark each one right or wrong.
    Nothing in this file is yours to write.

The stdlib version: statistics.py:472 `mean`. Read it for the 12-minute part;
it guards the empty list and hands back an int when it can. That int is the
surprise prediction 2 is about.

The try/except around call 4 is only there so the file can finish and show
you the answer. Friday is when you learn it properly - read it as "catch the
error, print its name".
"""


def mean(nums):
    """Return the arithmetic mean of nums. nums must be non-empty."""
    total = 0
    for n in nums:
        total = total + n
    return total / len(nums)


# --------------------------------------------------------------- the answers
# Predict these four, IN THE BLOCK AT THE BOTTOM, before running.
if __name__ == "__main__":
    print("1) mean([1, 2, 3, 4]) =", repr(mean([1, 2, 3, 4])))
    print("2) mean([1, 2, 3]) =", repr(mean([1, 2, 3])))
    print("3) mean([1, 2, 3]) == 2 =", repr(mean([1, 2, 3]) == 2))
    try:
        mean([])
    except Exception as exc:
        # type(exc).__name__ is the class name of what went wrong, as a string.
        print("4) mean([]) ->", type(exc).__name__)


'''PREDICTION - write these four lines BEFORE running the file.

1)
2)
3)
4)

ACTUAL - paste the four printed lines here, then compare.

1)
2)
3)
4)

One sentence on the miss (if any):
'''
