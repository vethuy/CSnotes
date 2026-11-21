"""Week 3 . Day 1 . functions: defaults, keywords, a clean return.

RUN THE CHECKS:   python week3/day01_drill01.py

RULES
-----
1. Every function RETURNS its result. Nothing above the check block prints.
2. No input() in this file.
3. Do not modify the argument unless the contract says you may.
4. Look up syntax only when a name is missing; 5 minutes maximum, then ask.
5. The check block at the bottom is the acceptance test. Do not edit it.

THE POINT: a function is an interface - its argument list says what the caller
may vary, its return value says what the caller gets. A default keeps the
common call short, a keyword makes the rare call readable, and a new return
value means the caller's data cannot change behind their back.

LOAD: 1 drill, 3 functions, about 20-25 minutes. Read the FUNCTION
INTRODUCTION before you type. Each docstring is the spec; the check block only
samples it, so an edge case you can name is an assert worth adding.
"""


# FUNCTION INTRODUCTION: a default argument, final_price(price, discount=0.0,
# tax=0.0), may be omitted; a keyword call names it: final_price(100, tax=0.1).
def final_price(price, discount=0.0, tax=0.0):
    """Return price after discount, then tax, rounded to 2 decimals.

    discount and tax are fractions of price: 0.25 is 25% off, 0.1 is 10% tax.
    Both are optional and are meant to be passed by keyword - a bare second
    positional argument silently means discount.

    price is a number; round only once, at the end.

    final_price(100)                       -> 100.0
    final_price(100, tax=0.1)              -> 110.0
    final_price(100, discount=0.25)        -> 75.0
    final_price(19.99, discount=0.1)       -> 17.99
    final_price(100, discount=1.0)         -> 0.0
    """
    raise NotImplementedError("final_price")


def clamp_all(values, low=0, high=100):
    """Return a NEW list: every value clamped into [low, high], inclusive.

    A value below low becomes low; a value above high becomes high.
    values must not be modified; low and high are numbers, not lists.

    clamp_all([-5, 50, 150])    -> [0, 50, 100]
    clamp_all([1, 2], low=2)    -> [2, 2]
    clamp_all([], low=3)        -> []
    clamp_all([150], high=10)   -> [10]
    """
    raise NotImplementedError("clamp_all")


# FUNCTION INTRODUCTION: dict.update(other) copies other's key/value pairs into
# a dict in place and returns None; merge_prefs builds the new dict first.
def merge_prefs(user, base=None):
    """Return a NEW dict: base's pairs with user's pairs laid on top.

    user wins when both dicts hold the same key. base is optional; base=None
    means "start from an empty dict". Neither argument may be modified, and the
    returned dict must be a new object, not either argument.

    merge_prefs({"theme": "dark"})
        -> {"theme": "dark"}
    merge_prefs({"theme": "dark"}, {"theme": "light", "wrap": True})
        -> {"theme": "dark", "wrap": True}
    merge_prefs({}, {"font": "mono"})
        -> {"font": "mono"}
    """
    raise NotImplementedError("merge_prefs")


# --------------------------------------------------------------------------
# CHECKS - do not edit below this line
# --------------------------------------------------------------------------
if __name__ == "__main__":
    # final_price
    assert final_price(100) == 100.0
    assert final_price(100, discount=0.25) == 75.0
    assert final_price(100, tax=0.1) == 110.0
    assert final_price(19.99, discount=0.1) == 17.99
    assert final_price(100, discount=1.0) == 0.0
    assert final_price(100, discount=0.25, tax=0.1) == 82.5
    assert final_price(100, tax=0.1, discount=0.25) == 82.5
    assert final_price(100, 0.25) == 75.0

    # clamp_all
    assert clamp_all([-5, 50, 150]) == [0, 50, 100]
    assert clamp_all([1, 2], low=2) == [2, 2]
    assert clamp_all([], low=3) == []
    assert clamp_all([150], high=10) == [10]
    source = [3, -1, 120]
    clamped = clamp_all(source)
    assert clamped == [3, 0, 100]
    assert source == [3, -1, 120], "clamp_all must not modify its argument"
    assert clamped is not source, "clamp_all must return a new list"

    # merge_prefs
    assert merge_prefs({"theme": "dark"}) == {"theme": "dark"}
    assert merge_prefs(
        {"theme": "dark"}, {"theme": "light", "wrap": True}
    ) == {"theme": "dark", "wrap": True}
    assert merge_prefs({}, {"font": "mono"}) == {"font": "mono"}
    assert merge_prefs({"x": 1}) == {"x": 1}
    assert merge_prefs({"y": 2}) == {"y": 2}
    base = {"a": 1}
    merged = merge_prefs({"b": 2}, base)
    assert merged == {"a": 1, "b": 2}
    assert base == {"a": 1}, "merge_prefs must not modify base"
    assert merged is not base, "merge_prefs must return a new dict"

    print("all drills pass")
