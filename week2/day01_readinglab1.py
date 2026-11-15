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
def mean(nums):
    """Return the arithmetic mean of nums. nums must be non-empty."""
    total = 0
    for n in nums:
        total = total + n
    return total / len(nums)
1)mean([1, 2, 3, 4])=
total=0  n=1   total = 0+1=1
total=1  n=2   total = 1+2=3
total=3  n=3   total = 3+3=6
total=6  n=4   total = 6+4=10
return total / len(nums)=10/4=2.5
      
2) mean([1, 2, 3])=
total=0  n=1   total = 0+1=1
total=1  n=2   total = 1+2=3
total=3  n=3   total = 3+3=6
return total / len(nums)=6/3=2

3) mean([1, 2, 3]) == 2 =
we know that 2)=2
so it return True(boolean)

4) try:mean([])
nums is empty. so the error occur at for loop?
no it may skip it.so the actual error is return
return total / len(nums)=0/0 this is not acceptable
so it raise ZeroDivisionError Exception

ACTUAL - paste the four printed lines here, then compare.

1) mean([1, 2, 3, 4]) = 2.5
2) mean([1, 2, 3]) = 2.0
3) mean([1, 2, 3]) == 2 = True
4) mean([]) -> ZeroDivisionError
all correct
One sentence on the miss (if any):
'''
