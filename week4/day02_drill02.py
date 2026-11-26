"""Week 4 . Day 2 . bubble sort: the first O(n^2), and how to count its work.

RUN THE CHECKS:   python week4/day02_drill02.py

RULES
-----
1. Every function RETURNS its result. Nothing above the check block prints.
2. No input() in this file.
3. The argument is the caller's data: every sort returns a NEW list.
4. Look up syntax only when a name is missing; 5 minutes maximum, then ask.
5. The check block at the bottom is the acceptance test. Do not edit it.

THE POINT: bubble sort compares neighbours and swaps them when they are out of
order, so the biggest remaining item drowns to the end of every pass. Big-O is
not a word you memorise, it is the count of those comparisons: a sorted list
costs one pass and n-1 comparisons, a reversed one costs n-1 passes. The two
counting functions below print nothing - they hand the number back, because
only the check block is allowed to print.

LOAD: 1 drill, 3 functions, about 20-25 minutes. Type `bubble_sort` first and
run it on [3, 2, 1] by hand, on paper, before you run the file.
"""


def bubble_sort(items):
    result=list(items)
    count=0
    old=[]
    while old!=result:
        old=result.copy()
        for i in range(len(items)-1-count):
            if result[i]>result[i+1]:
                result[i],result[i+1]=result[i+1],result[i]
        count+=1
    return result
    ''' 
    result=list(items)
    old=[]
    while result!=old :
        old=result.copy()
        for i in range(len(items)-1):
            if result[i]>result[i+1]:
                result[i],result[i+1]=result[i+1],result[i]
    return result
    '''
               


        


    """Return a NEW list with the same items sorted ascending.

    Compare neighbours and swap when the left one is bigger; after one pass the
    largest unsorted item is in place. Stop as soon as a whole pass makes no
    swap. The argument must not be modified.

    bubble_sort([3, 1, 2])   -> [1, 2, 3]
    bubble_sort([3, 2, 1])   -> [1, 2, 3]
    bubble_sort([2, 2, 1])   -> [1, 2, 2]
    bubble_sort([])          -> []
    bubble_sort([5])         -> [5]
    """
    raise NotImplementedError("bubble_sort")


def bubble_sort_counted(items):
    result=list(items)
    old=[]
    comparisons=0
    count=0
    while result!=old :
        old=result.copy()
        for i in range(len(items)-1-count):
            if result[i]>result[i+1]:
                comparisons+=1
                result[i],result[i+1]=result[i+1],result[i]
            else:
                comparisons+=1
        count+=1
    return (result,comparisons)
               
    """Return (sorted_list, comparisons) using the same algorithm as bubble_sort.

    One comparison is one `<` between two neighbouring items. The pass loop
    stops when a pass makes no swap. Count only comparisons that actually
    happen: on [1, 2, 3] the first pass compares twice, swaps nothing, ends.
    The argument must not be modified.

    bubble_sort_counted([3, 2, 1])   -> ([1, 2, 3], 3)
    bubble_sort_counted([1, 2, 3])   -> ([1, 2, 3], 2)
    bubble_sort_counted([2, 1])      -> ([1, 2], 1)
    bubble_sort_counted([5])         -> ([5], 0)
    bubble_sort_counted([])          -> ([], 0)
    """
    raise NotImplementedError("bubble_sort_counted")


def bubble_swaps(items):
    result=list(items)
    count=0
    old=[]
    swap=0
    while old!=result:
        old=result.copy()
        for i in range(len(items)-1-count):
            if result[i]>result[i+1]:
                result[i],result[i+1]=result[i+1],result[i]
                swap+=1
        count+=1
    return swap
    """Return how many swaps bubble_sort would make on items.

    A swap is the exchange of two neighbours. The count must agree with
    bubble_sort's result, so [3, 2, 1] needs three swaps and a sorted list
    needs none. The argument must not be modified.

    bubble_swaps([3, 2, 1])   -> 3
    bubble_swaps([1, 2, 3])   -> 0
    bubble_swaps([2, 1])      -> 1
    bubble_swaps([2, 1, 2])   -> 1
    bubble_swaps([])          -> 0
    """
    raise NotImplementedError("bubble_swaps")


# --------------------------------------------------------------------------
# CHECKS - do not edit below this line
# --------------------------------------------------------------------------
if __name__ == "__main__":
    # bubble_sort
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    assert bubble_sort([2, 2, 1]) == [1, 2, 2]
    assert bubble_sort([]) == []
    assert bubble_sort([5]) == [5]
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]
    source = [4, 2, 5, 1]
    result = bubble_sort(source)
    assert result == [1, 2, 4, 5]
    assert source == [4, 2, 5, 1], "bubble_sort must not modify its argument"
    assert result is not source, "bubble_sort must return a new list"

    # bubble_sort_counted
    assert bubble_sort_counted([3, 2, 1]) == ([1, 2, 3], 3)
    assert bubble_sort_counted([1, 2, 3]) == ([1, 2, 3], 2)
    assert bubble_sort_counted([2, 1]) == ([1, 2], 1)
    assert bubble_sort_counted([5]) == ([5], 0)
    assert bubble_sort_counted([]) == ([], 0)
    source = [2, 1, 3]
    sorted_list, comparisons = bubble_sort_counted(source)
    assert sorted_list == [1, 2, 3]
    assert comparisons == 3, "one swap, then a pass of two comparisons"
    assert source == [2, 1, 3], "bubble_sort_counted must not modify its argument"

    # bubble_swaps
    assert bubble_swaps([3, 2, 1]) == 3
    assert bubble_swaps([1, 2, 3]) == 0
    assert bubble_swaps([2, 1]) == 1
    assert bubble_swaps([2, 1, 2]) == 1
    assert bubble_swaps([]) == 0
    source = [3, 1, 2]
    assert bubble_swaps(source) == 2
    assert source == [3, 1, 2], "bubble_swaps must not modify its argument"

    print("all drills pass")
