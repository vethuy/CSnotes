"""Week 2 . Day 5 . exceptions.

RUN THE CHECKS:   python week2/day05_drill05.py

RULES
-----
1. Every function RETURNS its result; nothing above the check block prints.
2. The rule of the day: a worker either returns a value or raises. It never
   both computes and prints, and it never hides an error the caller must see.
3. Do not widen an except clause to make a check pass.
4. The check block is the acceptance test. Do not edit it.

fix1, fix2 and fix3 are shipped broken on purpose. Their docstrings state the
contract; the bodies do not meet it. Fix the bodies, keep the signatures.
"""

import json
from pathlib import Path

DATA = Path(__file__).resolve().parent / "data"
CONFIG = DATA / "day05_config.json"


def safe_int(text, default=None):
    """Return int(text) when text converts, otherwise return default.

    Never raises for bad input, including None or a non-string.

    safe_int("42")           -> 42
    safe_int("x")            -> None
    safe_int("x", 0)         -> 0
    safe_int(None)           -> None
    """
    raise NotImplementedError("safe_int")


def parse_amount(text):
    """Return text as a float, or raise ValueError naming the bad text.

    The message must contain the original text, so "12,50" fails with a
    message the user can act on. Whitespace around the number is allowed.

    parse_amount("12.50") -> 12.5
    parse_amount("12,50") -> ValueError containing "12,50"
    """
    raise NotImplementedError("parse_amount")


def load_config(path):
    """Return the JSON object stored at path as a dict.

    A missing file must raise FileNotFoundError and a broken file must raise
    json.JSONDecodeError. Neither is caught here: main() decides the message.

    load_config(week2/data/day05_config.json)["font_size"] -> 13
    """
    raise NotImplementedError("load_config")


def divide(top, bottom):
    """Return top / bottom as a float.

    bottom == 0 raises ValueError("cannot divide by zero").

    divide(10, 2) -> 5.0
    divide(1, 0)  -> ValueError("cannot divide by zero")
    """
    raise NotImplementedError("divide")


def fix1(text):
    """Required behaviour: return int(text); return None when text cannot be
    converted; never suppress KeyboardInterrupt or SystemExit.

    This implementation does not meet the contract. Fix the body.
    """
    try:
        return int(text)
    except:
        return None


def fix2(data, key):
    """Required behaviour: return data[key] when the key is there; return None
    when it is missing; every other error (a list given as data, an unhashable
    key) must propagate to the caller.

    This implementation does not meet the contract. Fix the body.
    """
    try:
        return data[key]
    except ValueError:
        return None


def fix3(n):
    """Required behaviour: return 10 // n; return None when n is 0; nothing
    else may change the returned value.

    This implementation does not meet the contract. Fix the body.
    """
    try:
        return 10 // n
    except ZeroDivisionError:
        return None
    finally:
        return -1


# --------------------------------------------------------------------------
# CHECKS - do not edit below this line
# --------------------------------------------------------------------------
if __name__ == "__main__":
    # safe_int
    assert safe_int("42") == 42
    assert safe_int("x") is None
    assert safe_int("x", 0) == 0
    assert safe_int(None) is None
    assert safe_int("x", "fallback") == "fallback"

    # parse_amount
    assert parse_amount("12.50") == 12.5
    assert parse_amount(" 7 ") == 7.0
    for bad in ("12,50", "abc"):
        try:
            parse_amount(bad)
        except ValueError as exc:
            assert bad in str(exc), f"message should name {bad!r}, got {exc}"
        else:
            raise AssertionError(f"parse_amount({bad!r}) must raise ValueError")

    # load_config
    assert load_config(CONFIG)["font_size"] == 13
    try:
        load_config(DATA / "no_such_config.json")
    except FileNotFoundError:
        pass
    else:
        raise AssertionError("load_config must let FileNotFoundError escape")

    # divide
    assert divide(10, 2) == 5.0
    try:
        divide(1, 0)
    except ValueError as exc:
        assert "cannot divide by zero" in str(exc).lower()
    else:
        raise AssertionError("divide(1, 0) must raise ValueError")

    # fix1: the wide except still returns the right answer, so only the
    # contract is checked here; proving KeyboardInterrupt escapes is a
    # manual test you run once.
    assert fix1("42") == 42
    assert fix1("x") is None

    # fix2
    assert fix2({"a": 1}, "a") == 1
    assert fix2({}, "a") is None
    try:
        fix2([1, 2], "a")
    except TypeError:
        pass
    else:
        raise AssertionError("fix2 must not swallow TypeError")

    # fix3
    assert fix3(2) == 5
    assert fix3(0) is None
    assert fix3(3) == 3

    print("all drills pass")
