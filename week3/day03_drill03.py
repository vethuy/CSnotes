"""Week 3 . Day 3 . pure functions: the caller's data cannot change.

RUN THE CHECKS:   python week3/day03_drill03.py

RULES
-----
1. Every function RETURNS its result. Nothing above the check block prints.
2. No input() in this file.
3. Do not modify the argument unless the contract says you may - and in this
   file no contract does.
4. Look up syntax only when a name is missing; 5 minutes maximum, then ask.
5. The check block at the bottom is the acceptance test. Do not edit it.

THE POINT: a pure function depends only on its arguments and changes nothing
the caller can see. list(x), dict(x) and sorted(x) all build a NEW object, so
the caller keeps their list, their dict and their order. Every check below
tests the result and then tests that the source is unchanged - the second
assert is the one that fails when "new list" was only a comment.

LOAD: 1 drill, 3 functions, about 20-25 minutes. Read the FUNCTION
INTRODUCTION before you type. Each docstring is the spec; the check block only
samples it.
"""


# FUNCTION INTRODUCTION: items + extra already returns a NEW list, so
# append_all is one expression - the bug to avoid is out = items followed by
# out.append(...), which edits the caller's list in place.
def append_all(items, extra):
    result=[]
    for i in items:
        result.append(i)
    for j in extra:
        result.append(j)
    return result
    """Return a new list: everything in items, then everything in extra.

    Neither items nor extra may be modified. The result is always a new list,
    even when extra is empty.

    items and extra are lists (extra may be any sequence).

    append_all([1, 2], [3])      -> [1, 2, 3]
    append_all([], [1])          -> [1]
    append_all([1], [])          -> [1]
    append_all(["a"], ["b", "c"]) -> ["a", "b", "c"]
    """
    raise NotImplementedError("append_all")


# FUNCTION INTRODUCTION: a list comprehension over a list builds a new list;
# there is no copy step to forget. with_tax(amounts, 0.1) returns new prices.
def with_tax(amounts, rate):
    result=[]
    for i in amounts:
        result.append(round(i*(1+rate),2))
    return result

    """Return a NEW list: each amount multiplied by (1 + rate), rounded to 2.

    rate is a fraction: 0.1 is 10% tax, 0.0 leaves every amount as it is.
    amounts must not be modified. Round each result once.

    amounts is a list of numbers; rate is a number.

    with_tax([100, 50], 0.1)        -> [110.0, 55.0]
    with_tax([100], 0.0)            -> [100.0]
    with_tax([], 0.1)               -> []
    with_tax([19.99], 0.1)          -> [21.99]
    """
    raise NotImplementedError("with_tax")


# FUNCTION INTRODUCTION: dict(mapping) makes a shallow copy, so removing a key
# from the copy cannot remove it from the caller's dict.
def without_key(mapping, key):
    new=dict(mapping)
    try:
        new.pop(key)
    except KeyError:
        pass
    return new
    """Return a NEW dict: a copy of mapping with key removed.

    mapping must not be modified. A key that is not in mapping is not an
    error - the copy is simply returned whole.

    mapping is a dict; key may be any hashable value.

    without_key({"a": 1, "b": 2}, "a")   -> {"b": 2}
    without_key({"a": 1}, "z")           -> {"a": 1}
    without_key({}, "a")                 -> {}
    without_key({"a": 1, "b": 2}, "b")   -> {"a": 1}
    """
    raise NotImplementedError("without_key")


if __name__ == "__main__":
    source = [1, 2]
    extra = [3, 4]
    result = append_all(source, extra)
    assert result == [1, 2, 3, 4]
    assert result is not source
    assert source == [1, 2]
    assert extra == [3, 4]

    assert append_all([], [1]) == [1]
    assert append_all([1], []) == [1]
    assert append_all(["a"], ["b", "c"]) == ["a", "b", "c"]

    amounts = [100, 50]
    taxed = with_tax(amounts, 0.1)
    assert taxed == [110.0, 55.0]
    assert taxed is not amounts
    assert amounts == [100, 50]
    assert with_tax([100], 0.0) == [100.0]
    assert with_tax([], 0.1) == []
    assert with_tax([19.99], 0.1) == [21.99]

    prefs = {"a": 1, "b": 2}
    smaller = without_key(prefs, "a")
    assert smaller == {"b": 2}
    assert smaller is not prefs
    assert prefs == {"a": 1, "b": 2}
    assert without_key({"a": 1}, "z") == {"a": 1}
    assert without_key({}, "a") == {}

    print("all drills pass")
