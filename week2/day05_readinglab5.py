"""Week 2 . Day 5 . reading lab 5 - json.decoder, an error with a position
(Lib/json/decoder.py:20).

WHAT THIS LAB IS
----------------
You read how the json module reports WHERE parsing failed, then close the file
and rebuild the shape from memory. Simplified is fine. Do not import the module
you are rewriting and do not paste from it.

LAST 3 MINUTES OF THE LAB: write the body below, from memory, then run the
check. If the check fails, do not reopen the source - read the error and think.

RUN THE CHECK:   python week2/day05_readinglab5.py
"""


def my_parse_ints(text):
    """Parse "1,2,3" into [1, 2, 3].

    A token that is not an int raises ValueError whose message contains the
    offending token and its 0-based position, the way JSONDecodeError names
    the spot:  "bad token 'x' at position 1".
    """
    raise NotImplementedError("my_parse_ints")


# --------------------------------------------------------------------------
# CHECK - do not edit below this line
# --------------------------------------------------------------------------
if __name__ == "__main__":
    assert my_parse_ints("1,2,3") == [1, 2, 3]
    try:
        my_parse_ints("1,x,3")
    except ValueError as exc:
        assert "x" in str(exc), f"message should name the token, got {exc}"
        assert "1" in str(exc), f"message should name the position, got {exc}"
    else:
        raise AssertionError("my_parse_ints('1,x,3') must raise ValueError")

    print("rewrite 5 passes")
