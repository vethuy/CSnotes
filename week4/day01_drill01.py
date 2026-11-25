"""Week 4 . Day 1 . searching: a scan, a halving, and one precondition.

RUN THE CHECKS:   python week4/day01_drill01.py

RULES
-----
1. Every function RETURNS its result. Nothing above the check block prints.
2. No input() in this file.
3. The argument is the caller's data: search and sort return new values.
4. Look up syntax only when a name is missing; 5 minutes maximum, then ask.
5. The check block at the bottom is the acceptance test. Do not edit it.

THE POINT: linear search touches items until it finds one - O(n). Binary search
throws away half of what is left on every comparison - O(log n) - but only
because the list is already sorted. That "must" is a precondition, and
`is_sorted` is how a caller checks it. A fast function with an unstated
precondition is a bug waiting for Tuesday's data.

LOAD: 1 drill, 3 functions, about 20-25 minutes. Before you type the second
function, draw lo / mid / hi on paper for [1, 3, 5, 7, 9] looking for 7.
"""


def linear_search(items, target):
    for i in items:
        if i == target:
            return items.index(i)
    return -1
    """Return the index of the FIRST item equal to target, or -1.

    items may be empty and in any order. Must not be modified. -1 means
    "not there", which is safe because no list index is negative.

    linear_search([4, 1, 7], 7)   -> 2
    linear_search([4, 1, 7], 5)   -> -1
    linear_search([2, 2, 3], 2)   -> 0
    linear_search([], 9)          -> -1
    """
    raise NotImplementedError("linear_search")


def binary_search(items, target):
    low=0
    high=len(items)-1
    while low<=high:
        middle=(low+high)//2
        if items[middle]==target:
            return middle
            break
        elif items[middle]<target:
            low=middle+1
        elif items[middle]>target:
            high=middle-1
    return -1
    """Return the index of ANY item equal to target, or -1.

    items is ALREADY sorted ascending - that is the price of the speed, and
    this function does not check it. Duplicates may exist, so more than one
    index is correct: the docstring promises an index, not the first one.
    Must not be modified.

    binary_search([1, 3, 5, 7], 7)   -> 3
    binary_search([1, 3, 5, 7], 4)   -> -1
    binary_search([2], 2)            -> 0
    binary_search([], 1)             -> -1
    """
    raise NotImplementedError("binary_search")


def is_sorted(items):
    return items==sorted(items)
    """Return True when items is in non-decreasing order, else False.

    Empty and one-item lists count as sorted. Equal neighbours are allowed.
    Must not be modified.

    is_sorted([])              -> True
    is_sorted([1])             -> True
    is_sorted([1, 2, 2, 3])    -> True
    is_sorted([3, 1])          -> False
    is_sorted([1, 3, 2])       -> False
    """
    raise NotImplementedError("is_sorted")


# --------------------------------------------------------------------------
# CHECKS - do not edit below this line
# --------------------------------------------------------------------------
if __name__ == "__main__":
    # linear_search
    assert linear_search([4, 1, 7], 7) == 2
    assert linear_search([4, 1, 7], 5) == -1
    assert linear_search([2, 2, 3], 2) == 0
    assert linear_search([3, 1, 2], 3) == 0
    assert linear_search([], 9) == -1
    source = [3, 3, 1]
    assert linear_search(source, 3) == 0
    assert source == [3, 3, 1], "linear_search must not modify its argument"

    # binary_search
    assert binary_search([1, 3, 5, 7], 7) == 3
    assert binary_search([1, 3, 5, 7], 1) == 0
    assert binary_search([1, 3, 5, 7], 4) == -1
    assert binary_search([2], 2) == 0
    assert binary_search([2], 1) == -1
    assert binary_search([], 1) == -1
    ordered = [1, 2, 2, 3]
    found = binary_search(ordered, 2)
    assert found in (1, 2), "binary_search may return any index of 2"
    assert ordered[found] == 2
    assert ordered == [1, 2, 2, 3], "binary_search must not modify its argument"

    # is_sorted
    assert is_sorted([]) is True
    assert is_sorted([1]) is True
    assert is_sorted([1, 2, 2, 3]) is True
    assert is_sorted([3, 1]) is False
    assert is_sorted([1, 3, 2]) is False
    source = [1, 2, 3]
    assert is_sorted(source) is True
    assert source == [1, 2, 3], "is_sorted must not modify its argument"

    print("all drills pass")
