"""Week 4 . Day 5 . recursion over a list: the tail, and the stack limit.

RUN THE CHECKS:   python week4/day05_drill05.py

RULES
-----
1. Every function RETURNS its result. Nothing above the check block prints.
2. No input() in this file.
3. The argument is the caller's data: search and sort return new values.
4. Look up syntax only when a name is missing; 5 minutes maximum, then ask.
5. The check block at the bottom is the acceptance test. Do not edit it.

THE POINT: the usual recursive list function splits the list into "first item"
and "the rest of the list", then asks itself about the rest. That is the same
sentence as a for loop, with one difference: each call keeps its own frame, so
a 2000-item list needs 2000 frames and Python stops you at about 1000. Today
you write both - the recursive one, and a recursive binary search whose range
shrinks instead of the list - and tomorrow's lab shows the stack running out.

LOAD: 1 drill, 3 functions, about 20-25 minutes. For max_recursive, write the
sentence "the biggest of items is the first item, or the biggest of the rest"
on paper first, base case included.
"""


def sum_recursive(items):
    """Return the sum of the numbers in items, using recursion only.

    items may be empty. Do not use sum() or a loop: the base case is an empty
    list, the smaller call is items[1:]. Zero items add nothing.

    sum_recursive([])             -> 0
    sum_recursive([7])            -> 7
    sum_recursive([1, 2, 3, 4])   -> 10
    sum_recursive([-2, 5])        -> 3
    """
    raise NotImplementedError("sum_recursive")


def max_recursive(items):
    """Return the largest item in items, using recursion only.

    items must not be empty; raise ValueError("max_recursive: empty list")
    instead of returning None, so the caller can tell "no answer" from a
    real value. Duplicates are fine.

    max_recursive([3, 9, 2])   -> 9
    max_recursive([4])         -> 4
    max_recursive([5, 5])      -> 5
    """
    raise NotImplementedError("max_recursive")


def binary_search_recursive(items, target):
    """Return the index of ANY item equal to target, or -1 - with recursion.

    items is ALREADY sorted ascending. Keep the same contract as yesterday's
    loop: the returned index must hold target, and -1 means absent. Shrink the
    range (lo, hi) in each call, not the list - slicing would copy it.

    binary_search_recursive([1, 3, 5, 7], 7)   -> 3
    binary_search_recursive([1, 3, 5, 7], 4)   -> -1
    binary_search_recursive([2], 2)            -> 0
    binary_search_recursive([], 1)             -> -1
    """
    raise NotImplementedError("binary_search_recursive")


# --------------------------------------------------------------------------
# CHECKS - do not edit below this line
# --------------------------------------------------------------------------
if __name__ == "__main__":
    # sum_recursive
    assert sum_recursive([]) == 0
    assert sum_recursive([7]) == 7
    assert sum_recursive([1, 2, 3, 4]) == 10
    assert sum_recursive([-2, 5]) == 3
    source = [1, 2, 3]
    assert sum_recursive(source) == 6
    assert source == [1, 2, 3], "sum_recursive must not modify its argument"

    # max_recursive
    assert max_recursive([3, 9, 2]) == 9
    assert max_recursive([4]) == 4
    assert max_recursive([5, 5]) == 5
    assert max_recursive([1, 2, 3]) == 3
    try:
        max_recursive([])
    except ValueError as exc:
        assert "empty" in str(exc).lower()
    else:
        raise AssertionError("max_recursive must raise ValueError on an empty list")

    # binary_search_recursive
    assert binary_search_recursive([1, 3, 5, 7], 7) == 3
    assert binary_search_recursive([1, 3, 5, 7], 1) == 0
    assert binary_search_recursive([1, 3, 5, 7], 4) == -1
    assert binary_search_recursive([2], 2) == 0
    assert binary_search_recursive([2], 1) == -1
    assert binary_search_recursive([], 1) == -1
    ordered = [1, 2, 2, 3]
    found = binary_search_recursive(ordered, 2)
    assert found in (1, 2), "binary_search_recursive may return any index of 2"
    assert ordered[found] == 2

    print("all drills pass")
