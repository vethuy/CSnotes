"""Week 2 . Day 5 . exceptions.

RUN THE CHECKS:   python week2/day05_drill05.py

RULES
-----
1. Every function RETURNS its result. Nothing above the check block prints.
2. No input() in this file.
3. Do not modify the argument unless the contract says you may.
4. Look up syntax only when a name is missing; 5 minutes maximum, then ask.
5. The check block at the bottom is the acceptance test. Do not edit it.

THE POINT: a function that cannot do its job must SAY so - by raising, or by
returning a value that means "nothing". Printing is the caller's decision.
Returning None means "not found". Raising means "this input is broken".

LOAD: 1 drill, 3 functions, about 20-25 minutes. Each function carries a
CORE IDEA line - read it before you type. Stuck 5 minutes after reading it?
Ask.
"""


# CORE IDEA: a bare `except:` also catches Ctrl-C, SystemExit and the typo
# in your own next line. Catch what you can name - ValueError is "the text
# is not a number" - and let everything else be a real crash.
def safe_int(text, default=None):
    """Return text as an int, or default when that is impossible.

    Never raises. A non-string (None, a list) is also "impossible".
    " 42 " -> 42 because int() ignores surrounding spaces.

    safe_int("42")      -> 42
    safe_int("4.2")     -> None
    safe_int("x", 0)    -> 0
    safe_int(None)      -> None
    """
    raise NotImplementedError("safe_int")


# CORE IDEA: the message is the API. "could not convert string to float:
# '12,50'" is what a stranger needs to fix the file, and it is why you raise
# instead of returning 0.0 - 0.0 is a wrong answer, an exception is a signal.
def parse_amount(text):
    """Return text as a float. Raise ValueError for anything unparseable.

    The ValueError message must contain repr(text), so the caller knows
    which value broke.
    "12,50" must raise - a comma is not a decimal point in Python.

    parse_amount("12.50") -> 12.5
    parse_amount(" 3 ")   -> 3.0
    """
    raise NotImplementedError("parse_amount")


# CORE IDEA: one bad token should not destroy the other nine. Collect the
# failures in a list, keep the sum of what worked, and let main() decide
# whether to warn, stop, or ignore - the function only reports.
def tally(text):
    """Return (total, bad_tokens) for a comma-separated string of amounts.

    Split on ",", strip each token, skip empty tokens. Good tokens are added
    to total; bad ones go into the list as the stripped text, in order.

    tally("1.25, 2.5")     -> (3.75, [])
    tally("1.25, x, 2.5")  -> (3.75, ["x"])
    tally("")              -> (0.0, [])
    tally(" , ")           -> (0.0, [])
    """
    raise NotImplementedError("tally")


# --------------------------------------------------------------------------
# CHECKS - do not edit below this line
# --------------------------------------------------------------------------
if __name__ == "__main__":
    # safe_int
    assert safe_int("42") == 42
    assert safe_int(" 42 ") == 42
    assert safe_int("-7") == -7
    assert safe_int("4.2") is None
    assert safe_int("x", 0) == 0
    assert safe_int("") is None
    assert safe_int(None) is None
    assert safe_int(None, 0) == 0
    assert safe_int(["1"]) is None

    # parse_amount
    assert parse_amount("12.50") == 12.5
    assert parse_amount(" 3 ") == 3.0
    assert parse_amount("-1.5") == -1.5
    for bad in ("12,50", "", "abc", "1.2.3"):
        try:
            parse_amount(bad)
            assert False, f"parse_amount({bad!r}) must raise"
        except ValueError as exc:
            assert repr(bad) in str(exc), "the message must contain repr(text)"

    # tally
    assert tally("1.25, 2.5") == (3.75, [])
    assert tally("1.25, x, 2.5") == (3.75, ["x"])
    assert tally("") == (0.0, [])
    assert tally(" , ") == (0.0, [])
    assert tally("a, b") == (0.0, ["a", "b"])
    assert tally("0.5") == (0.5, [])

    print("all drills pass")
