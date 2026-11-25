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

1) empty list      -> 0 while 0<0 False return 0
2) single hit      -> 0 while 0<1 True mid=0  items[0]=7<7 False hi=0 while 0<0 False return 0
3) single miss     -> 1 while 0<1 True mid=0 item[0]=7<9 True lo=1 while 1<1 False return 1
4) past the end    -> 3 while 0<3 True mid=1 item[1]=3<9 True lo=2 while 2<3 True mid=2 item[2]=5<9 True lo=3 while 3<3 False return 3
5) duplicates      -> 1 while 0<5 mid=2 item[2]=3<3 False hi=2 while 0<2 mid=1 item[1]=3<3 False hi=1 while 0<1 mid=0 item[0]=1<3 True lo=1
                        while 1<1 False return 1  (why is it not 2?)
6) between items   -> 3 while 0<4 mid=2 item[2]=3<4 True lo=3 while3<4 mid=3 item[3]=5<4 False hi=3 while 3<3 False return 3
7) after insert    -> after insert  [1,3,4,5] while 0<3 mid=1 items[1]=3<4 True lo=2 while 2<3 mid=2 item[2]=5<4 False hi=2 while 2<2 False return 2
                       it become values.insert(2, 4)  so print after insert  [1,3,4,5]
8) [1, 3, 5, 7, 9], target 9: how many times does the while loop run? 0<5(1) mid=2 5<9 lo=3 3<5(2) mid=4 9<9 False hi=4 3<4(3) mid=3 7<9 lo=4 while4<4 end
                            actual run 3 times  return 4

ACTUAL - paste after running.
empty list      0
single hit      0
single miss     1
past the end    3
duplicates      1
between items   3
after insert    [1, 3, 4, 5]
7/7
8) check by dsh.No actual output
checked 8/8
'''
