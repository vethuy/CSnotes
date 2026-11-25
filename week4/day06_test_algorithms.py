"""Week 4 . Weekend project . twelve tests, twelve edge cases.

RUN THE TESTS:   python -m pytest week4/day06_test_algorithms.py -v

Run it from the CSnotes folder. Every test starts as `raise NotImplementedError`,
so the first run says 12 failed. Replace that one line with asserts until the
report says 12 passed. Do not rename a test, do not delete one, and do not
weaken `day06_algorithms.py` to make a test easier - the docstring is the
claim, and the code either keeps it or does not.

The tests are the four algorithms' contracts cut into pieces:

    empty list, one item, duplicates, target absent, caller's list unchanged

If a test fails, read the assert pytest points at, then the algorithm it calls.
`-x` stops at the first failure.
"""

from day06_algorithms import (
    binary_search,
    bubble_sort,
    insertion_sort,
    linear_search,
)


def test_linear_search_finds_first_match():
    raise NotImplementedError("test_linear_search_finds_first_match")
    """[2, 2, 3] searched for 2 -> 0, and [3, 1, 2] searched for 3 -> 0."""


def test_linear_search_missing_returns_minus_one():
    raise NotImplementedError("test_linear_search_missing_returns_minus_one")
    """[4, 1, 7] searched for 5 -> -1, and [] searched for 9 -> -1."""


def test_linear_search_leaves_the_list_alone():
    raise NotImplementedError("test_linear_search_leaves_the_list_alone")
    """Pass [3, 1, 2], search for 1, then the list still equals [3, 1, 2]."""


def test_binary_search_finds_a_match():
    raise NotImplementedError("test_binary_search_finds_a_match")
    """[1, 3, 5, 7] searched for 7 -> 3, and for 1 -> 0."""


def test_binary_search_missing_returns_minus_one():
    raise NotImplementedError("test_binary_search_missing_returns_minus_one")
    """[1, 3, 5, 7] searched for 4 -> -1, and [] searched for 1 -> -1."""


def test_binary_search_one_item():
    raise NotImplementedError("test_binary_search_one_item")
    """[2] searched for 2 -> 0, and [2] searched for 1 -> -1."""


def test_binary_search_duplicates_return_a_real_index():
    raise NotImplementedError("test_binary_search_duplicates_return_a_real_index")
    """On [1, 2, 2, 3] the answer must be 1 or 2, and items[answer] must be 2."""


def test_bubble_sort_sorts():
    raise NotImplementedError("test_bubble_sort_sorts")
    """[3, 1, 2] -> [1, 2, 3] and [3, 2, 1] -> [1, 2, 3]."""


def test_bubble_sort_empty_and_one_item():
    raise NotImplementedError("test_bubble_sort_empty_and_one_item")
    """[] -> [] and [5] -> [5]."""


def test_bubble_sort_returns_a_new_list():
    raise NotImplementedError("test_bubble_sort_returns_a_new_list")
    """Sort [2, 1, 2]; the result is [1, 2, 2], the argument is still [2, 1, 2]."""


def test_insertion_sort_sorts():
    raise NotImplementedError("test_insertion_sort_sorts")
    """[4, 2, 5, 1] -> [1, 2, 4, 5] and [2, 2, 1] -> [1, 2, 2]."""


def test_insertion_sort_returns_a_new_list():
    raise NotImplementedError("test_insertion_sort_returns_a_new_list")
    """Sort [3, 1, 2]; the result is [1, 2, 3], the argument is still [3, 1, 2]."""
