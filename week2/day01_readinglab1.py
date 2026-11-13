"""Week 2 . Day 1 . reading lab 1 - statistics.mean  (Lib/statistics.py:472).

WHAT THIS LAB IS
----------------
You read one small function in the standard library, then close the file and
rebuild its shape from memory. Simplified is fine. Do not import the module you
are rewriting and do not paste from it.

LAST 3 MINUTES OF THE LAB: write the body below, from memory, then run the
check. If the check fails, do not reopen the source - read the error and think.

RUN THE CHECK:   python week2/day01_readinglab1.py
"""


def my_mean(data):
    """Return the arithmetic mean of data as a float.

    An empty sequence raises ValueError. data is not modified.
    my_mean([1, 2, 3]) -> 2.0
    """
    raise NotImplementedError("my_mean")


# --------------------------------------------------------------------------
# CHECK - do not edit below this line
# --------------------------------------------------------------------------
if __name__ == "__main__":
    assert my_mean([1, 2, 3]) == 2.0
    assert my_mean([2, 2]) == 2.0
    try:
        my_mean([])
    except ValueError:
        pass
    else:
        raise AssertionError("my_mean([]) must raise ValueError")

    print("rewrite 1 passes")
