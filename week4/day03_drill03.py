"""Week 4 . Day 3 . selection and insertion: two ways to be O(n^2), one helper.

RUN THE CHECKS:   python week4/day03_drill03.py

RULES
-----
1. Every function RETURNS its result. Nothing above the check block prints.
2. No input() in this file.
3. The argument is the caller's data: every sort returns a NEW list.
4. Look up syntax only when a name is missing; 5 minutes maximum, then ask.
5. The check block at the bottom is the acceptance test. Do not edit it.

THE POINT: bubble sort repeatedly moves the biggest item to the end. Selection
sort walks the unsorted part once, finds the smallest, and swaps it into place.
Insertion sort grows a sorted prefix and slides each new item left until it is
home. Same O(n^2) worst case, different amount of copying - and `min_index` is
the one piece of selection sort worth writing on its own, because a helper you
can test alone is a bug you can find alone.

LOAD: 1 drill, 3 functions, about 20-25 minutes. Do selection sort on paper
for [4, 2, 5, 1] and write down the list after each swap; you will check it in
tonight's reading lab.
"""


def min_index(items, start):
    if items[start:]==[]:
        raise ValueError('min_index: empty range')
    min=max(items)
    for i in items[start:]:
        if i < min:
            min=i
    return items.index(min)

    
    """Return the index of the smallest item in items[start:], first one on a tie.

    `start` is a valid index into a non-empty slice. If items[start:] is empty,
    raise ValueError("min_index: empty range"). Must not be modified.

    min_index([3, 1, 2], 0)   -> 1
    min_index([3, 1, 2], 1)   -> 1
    min_index([3, 1, 2], 2)   -> 2
    min_index([2, 2], 0)      -> 0
    min_index([5], 0)         -> 0
    """
    raise NotImplementedError("min_index")


def selection_sort(items):
    result=list(items)
    for i in range(len(items)):
        small_index=(min_index(result,i))
        if i==small_index:
            continue
        else:
            result[i],result[small_index]=result[small_index],result[i]
    return result
            
    """Return a NEW list, sorted ascending, using selection sort.

    For each position i, find the smallest item in items[i:] and swap it into
    place. Selection sort is not a stable sort in general - a swap can jump an
    equal item over its twin - so the check block asserts values, not order.
    The argument must not be modified.

    selection_sort([4, 2, 5, 1])   -> [1, 2, 4, 5]
    selection_sort([2, 1, 2])      -> [1, 2, 2]
    selection_sort([])             -> []
    selection_sort([5])            -> [5]
    """
    raise NotImplementedError("selection_sort")


# FUNCTION INTRODUCTION: result.insert(pos, value) shifts everything from pos
# right and puts value there - see week1/day05_days_between.py:26.
def insertion_sort(items):
    result=list(items)
    for i in range(1,len(items)):
        value=result[i]
        for j in result[0:i]:
            if value<j:
                ind=result.index(j)
                result[ind],result[i]=result[i],result[ind]           
    return result

    """Return a NEW list, sorted ascending, using insertion sort.

    Grow a sorted prefix: take the next item, slide the bigger items in the
    prefix one place right, and drop it into the gap with `insert` (or by
    shifting). The argument must not be modified.

    insertion_sort([4, 2, 5, 1])   -> [1, 2, 4, 5]
    insertion_sort([2, 1, 2])      -> [1, 2, 2]
    insertion_sort([])             -> []
    insertion_sort([5])            -> [5]
    """
    raise NotImplementedError("insertion_sort")


# --------------------------------------------------------------------------
# CHECKS - do not edit below this line
# --------------------------------------------------------------------------
if __name__ == "__main__":
    # min_index
    assert min_index([3, 1, 2], 0) == 1
    assert min_index([3, 1, 2], 1) == 1
    assert min_index([3, 1, 2], 2) == 2
    assert min_index([2, 2], 0) == 0
    assert min_index([5], 0) == 0
    assert min_index([4, 4, 1], 0) == 2
    source = [3, 1, 2]
    assert min_index(source, 0) == 1
    assert source == [3, 1, 2], "min_index must not modify its argument"
    try:
        min_index([], 0)
    except ValueError as exc:
        assert "empty" in str(exc).lower()
    else:
        raise AssertionError("min_index must raise ValueError on an empty range")

    # selection_sort
    assert selection_sort([4, 2, 5, 1]) == [1, 2, 4, 5]
    assert selection_sort([2, 1, 2]) == [1, 2, 2]
    assert selection_sort([]) == []
    assert selection_sort([5]) == [5]
    assert selection_sort([1, 2, 3]) == [1, 2, 3]
    source = [3, 1, 2]
    result = selection_sort(source)
    assert result == [1, 2, 3]
    assert source == [3, 1, 2], "selection_sort must not modify its argument"
    assert result is not source, "selection_sort must return a new list"

    # insertion_sort
    assert insertion_sort([4, 2, 5, 1]) == [1, 2, 4, 5]
    assert insertion_sort([2, 1, 2]) == [1, 2, 2]
    assert insertion_sort([]) == []
    assert insertion_sort([5]) == [5]
    assert insertion_sort([1, 2, 3]) == [1, 2, 3]
    source = [3, 1, 2]
    result = insertion_sort(source)
    assert result == [1, 2, 3]
    assert source == [3, 1, 2], "insertion_sort must not modify its argument"
    assert result is not source, "insertion_sort must return a new list"

    print("all drills pass")
