"""Week 4 . Weekend project . four algorithms from pseudocode, no tutorial.

RUN THE TESTS:   python -m pytest week4/day06_test_algorithms.py -v

This file is the first four entries of the capstone (`algo-lab`): two searches
and two sorts. Every function is a stub - the docstring is the contract, the
complexity line is the claim about its cost, and the test file is how the claim
gets checked. Do not copy an implementation from a tutorial: write it from the
docstring, then let the failing tests tell you what you got wrong.

The four functions, with their worst-case costs:

    linear_search         O(n)        scan until found, or -1
    binary_search         O(log n)    sorted input only, halve the range
    bubble_sort           O(n^2)      swap neighbours, early exit when clean
    insertion_sort        O(n^2)      grow a sorted prefix, slide items right

Nothing here prints. Results are returned; the check block is the test file,
not a `print("all drills pass")` line.
"""


def linear_search(items, target):
    """Return the index of the first item equal to target, or -1.

    Complexity: O(n) time, O(1) space - the list may be unsorted, and in the
    worst case every item is compared once. Must not modify items.

    linear_search([4, 1, 7], 7)   -> 2
    linear_search([4, 1, 7], 5)   -> -1
    """
    raise NotImplementedError("linear_search")


def binary_search(items, target):
    """Return the index of any item equal to target, or -1.

    Complexity: O(log n) time, O(1) space. Precondition: items is sorted
    ascending. Duplicates are allowed, so the first or any matching index is a
    correct answer. Must not modify items.

    binary_search([1, 3, 5, 7], 5)   -> 2
    binary_search([1, 3, 5, 7], 4)   -> -1
    """
    raise NotImplementedError("binary_search")


def bubble_sort(items):
    """Return a new list with the same items sorted ascending.

    Complexity: O(n^2) time, O(n) space for the copy. Worst and average are
    n-1 passes; best case is one pass when the list is already sorted, because
    the pass loop stops as soon as no swap happened. Must not modify items.

    bubble_sort([3, 1, 2])   -> [1, 2, 3]
    bubble_sort([])          -> []
    """
    raise NotImplementedError("bubble_sort")


def insertion_sort(items):
    """Return a new list with the same items sorted ascending.

    Complexity: O(n^2) time, O(n) space. Each new item slides left over the
    bigger items already in the prefix; a sorted input needs no slide at all,
    so the best case is O(n). Must not modify items.

    insertion_sort([4, 2, 5, 1])   -> [1, 2, 4, 5]
    insertion_sort([2, 2, 1])      -> [1, 2, 2]
    """
    raise NotImplementedError("insertion_sort")
