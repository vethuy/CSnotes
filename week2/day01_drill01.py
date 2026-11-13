"""Week 2 . Day 1 . list, slicing, tuple.

RUN THE CHECKS:   python week2/day01_drill01.py

RULES
-----
1. Every function RETURNS its result. Nothing above the check block prints.
2. No input() in this file.
3. Do not modify the argument unless the contract says you may.
4. Look up syntax only when a name is missing; 5 minutes maximum, then ask.
5. The check block at the bottom is the acceptance test. Do not edit it.

THE POINT: week 1 printed from inside the worker. From today the worker hands
a value back and lets the caller decide what to do with it.
"""


def second_largest(nums):
    """Return the largest value in nums strictly smaller than max(nums).

    Return None when nums has fewer than two distinct values.
    nums must not be modified.

    second_largest([3, 1, 3, 2]) -> 2
    second_largest([5, 5])       -> None
    second_largest([])           -> None
    """
    raise NotImplementedError("second_largest")


def rotate_left(nums, k):
    """Return a NEW list: the items of nums rotated left by k positions.

    k is a non-negative int and may be larger than len(nums).
    rotate_left([], 3) returns [].
    nums must not be modified.

    rotate_left([1, 2, 3, 4, 5], 2) -> [3, 4, 5, 1, 2]
    rotate_left([1, 2, 3, 4, 5], 7) -> [3, 4, 5, 1, 2]
    """
    raise NotImplementedError("rotate_left")


def remove_duplicates(nums):
    """Return a new list with duplicates removed, first-seen order kept.

    remove_duplicates([3, 1, 3, 2, 1]) -> [3, 1, 2]
    remove_duplicates([])              -> []
    """
    raise NotImplementedError("remove_duplicates")


def chunk(nums, size):
    """Split nums into a list of lists, each of length size except the last.

    size is a positive int. chunk([], size) returns [].

    chunk([1, 2, 3, 4, 5], 2) -> [[1, 2], [3, 4], [5]]
    chunk([1, 2, 3], 5)       -> [[1, 2, 3]]
    """
    raise NotImplementedError("chunk")


def middle(nums):
    """Return the middle item of an odd-length list, a TUPLE of the two
    middle items of an even-length list, and None for an empty list.

    middle([1, 2, 3])    -> 2
    middle([1, 2, 3, 4]) -> (2, 3)
    middle([])           -> None
    """
    raise NotImplementedError("middle")


def is_palindrome(text):
    """Return True when text reads the same backwards, ignoring case,
    spaces and punctuation. Return False otherwise. "" is True.

    Only letters and digits are compared.

    is_palindrome("Level")                          -> True
    is_palindrome("A man, a plan, a canal: Panama") -> True
    is_palindrome("abc")                            -> False
    """
    raise NotImplementedError("is_palindrome")


# --------------------------------------------------------------------------
# CHECKS - do not edit below this line
# --------------------------------------------------------------------------
if __name__ == "__main__":
    # second_largest
    assert second_largest([3, 1, 3, 2]) == 2
    assert second_largest([5, 5]) is None
    assert second_largest([]) is None
    assert second_largest([7]) is None
    assert second_largest([-4, -9, -1]) == -4

    # rotate_left
    assert rotate_left([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]
    assert rotate_left([1, 2, 3, 4, 5], 7) == [3, 4, 5, 1, 2]
    assert rotate_left([1, 2], 0) == [1, 2]
    assert rotate_left([], 3) == []
    source = [1, 2, 3]
    rotate_left(source, 1)
    assert source == [1, 2, 3], "rotate_left must not modify its argument"

    # remove_duplicates
    assert remove_duplicates([3, 1, 3, 2, 1]) == [3, 1, 2]
    assert remove_duplicates([]) == []
    assert remove_duplicates([1, 1, 1]) == [1]

    # chunk
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert chunk([], 2) == []
    assert chunk([1, 2, 3], 5) == [[1, 2, 3]]

    # middle
    assert middle([1, 2, 3]) == 2
    assert middle([1, 2, 3, 4]) == (2, 3)
    assert middle([]) is None

    # is_palindrome
    assert is_palindrome("level") is True
    assert is_palindrome("Level") is True
    assert is_palindrome("") is True
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("abc") is False

    print("all drills pass")
