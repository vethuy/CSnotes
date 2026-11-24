"""Week 3 . Day 5 . debugging: three programs that run and lie.

RUN THE CHECKS:   python week3/day05_drill05.py

RULES
-----
1. Every function RETURNS its result. Nothing above the check block prints.
2. No input() in this file.
3. Do not modify the argument unless the contract says you may.
4. Look up syntax only when a name is missing; 5 minutes maximum, then ask.
5. The check block at the bottom is the acceptance test. Do not edit it.

THE POINT: this drill is different. The three functions below are ALREADY
WRITTEN, and every one of them is wrong in a way that still runs. The check
block is the spec; your job is to read each failure, find the one line that
causes it, and change the BODY only. Run the file after each fix: the first
assert that fails is the next bug.

Use `breakpoint()` on at least one of them: stop inside the function, step
over one line, and watch the argument before and after the call. Delete the
breakpoint before you commit.

LOAD: 1 drill, 3 bugs, about 25-30 minutes. The docstrings are correct; the
bodies are not.
"""


# THE BUG: the first assert passes. The second one says the caller's list is
# not what it was - read where `out` comes from.
def running_total(nums):

    """Return a NEW list of running totals: each entry is the sum so far.

    nums must not be modified. running_total([]) is [].

    running_total([1, 2, 3])    -> [1, 3, 6]
    running_total([5])          -> [5]
    running_total([])           -> []
    """
    out = list(nums)
    for i in range(1, len(out)):
        out[i] = out[i - 1] + out[i]
    return out


# THE BUG: the traceback ends in bump, at the line that adds 1. The name on the
# left of the = is not the name the function is reading.
def make_counter(start=0):

    """Return a function that returns start+1, then start+2, then start+3...

    Each call to make_counter gets its OWN count; counters do not share it.

    c = make_counter(); c() -> 1; c() -> 2
    d = make_counter(10); d() -> 11; c() -> 3
    """
    
    count = start

    def bump():
        nonlocal count
        count = count + 1
        return count

    return bump


# THE BUG: the first two asserts pass. The third call returns a list that
# remembers the earlier calls - look at when the default was built.
def add_label(text, labels=None):
    """Return a NEW list: labels plus text at the end.

    labels must not be modified. A missing labels means an empty new list, and
    two calls with no labels argument must not share a list.

    add_label("a")                    -> ["a"]
    add_label("b")                    -> ["b"]
    add_label("b", ["a"])             -> ["a", "b"]
    """
    if labels is None:
        labels=[]
    a=list(labels)
    a.append(text)
    return a


if __name__ == "__main__":
    source = [1, 2, 3]
    assert running_total(source) == [1, 3, 6]
    assert source == [1, 2, 3]
    assert running_total([]) == []

    first = make_counter()
    assert first() == 1
    assert first() == 2
    second = make_counter(10)
    assert second() == 11
    assert first() == 3
    
    assert add_label("a") == ["a"]
    assert add_label("b") == ["b"]
    assert add_label("b", ["a"]) == ["a", "b"]
    labels_source = ["keep"]
    result = add_label("new", labels_source)
    assert result == ["keep", "new"]
    assert labels_source == ["keep"]

    print("all drills pass")
