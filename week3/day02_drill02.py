"""Week 3 . Day 2 . modules: borrow the function, keep the name.

RUN THE CHECKS:   python week3/day02_drill02.py

RULES
-----
1. Every function RETURNS its result. Nothing above the check block prints.
2. No input() in this file.
3. Do not modify the argument unless the contract says you may.
4. Look up syntax only when a name is missing; 5 minutes maximum, then ask.
5. The check block at the bottom is the acceptance test. Do not edit it.

THE POINT: a module is a shelf of functions somebody already tested. Importing
it and naming its function at the call site - math.gcd(...), string.punctuation -
is cheaper and safer than retyping the loop. Your job is to know which shelf,
and to keep your own function small around it.

LOAD: 1 drill, 3 functions, about 20-25 minutes. Read the FUNCTION
INTRODUCTION before you type. Each docstring is the spec; the check block only
samples it, so an edge case you can name is an assert worth adding.
"""


# FUNCTION INTRODUCTION: math.gcd(a, b) returns the greatest common divisor of
# two whole numbers and ignores their signs: math.gcd(-6, 8) is 2. It is not
# the fraction module - simplify still divides both parts yourself.
def simplify(num, den):
    """Return the fraction num/den as a reduced (numerator, denominator) tuple.

    The denominator is never 0 - the caller guarantees it. The returned
    denominator is always positive, so the sign moves to the numerator:
    simplify(6, -8) is (-3, 4). Zero is allowed on top: simplify(0, 7) is (0, 1).

    num and den are ints. Return ints, not floats.

    simplify(6, 8)     -> (3, 4)
    simplify(-6, 8)    -> (-3, 4)
    simplify(6, -8)    -> (-3, 4)
    simplify(0, 7)     -> (0, 1)
    simplify(10, 10)   -> (1, 1)
    """
    raise NotImplementedError("simplify")


# FUNCTION INTRODUCTION: string.punctuation is a str of the 32 ASCII
# punctuation characters, so "ch in string.punctuation" is a membership test -
# no list of characters to type, and no regex needed.
def strip_punctuation(text):
    """Return text with every ASCII punctuation character removed.

    Spaces and digits and letters stay. Punctuation is exactly the characters
    in string.punctuation; do not invent a wider set.

    text is a str. Return a new str; strings are immutable anyway.

    strip_punctuation("Hi, there!")        -> "Hi there"
    strip_punctuation("a-b")               -> "ab"
    strip_punctuation("wait... what?")     -> "wait what"
    strip_punctuation("")                  -> ""
    """
    raise NotImplementedError("strip_punctuation")


# FUNCTION INTRODUCTION: str.casefold() is the lower() you want for comparison:
# "Straße".casefold() is "strasse", while lower() leaves the sharp s alone.
def is_palindrome(text):
    """Return True when text reads the same forwards and backwards.

    Ignore case, spaces and punctuation before comparing - so
    "A man, a plan, a canal: Panama" is True and "12 21" is True. An empty
    string or a single character is a palindrome.

    text is a str. Build the cleaned string with strip_punctuation, then
    casefold it; do not mutate anything.

    is_palindrome("racecar")                          -> True
    is_palindrome("A man, a plan, a canal: Panama")    -> True
    is_palindrome("12 21")                            -> True
    is_palindrome("hello")                            -> False
    is_palindrome("")                                 -> True
    """
    raise NotImplementedError("is_palindrome")


if __name__ == "__main__":
    assert simplify(6, 8) == (3, 4)
    assert simplify(-6, 8) == (-3, 4)
    assert simplify(6, -8) == (-3, 4)
    assert simplify(-6, -8) == (3, 4)
    assert simplify(0, 7) == (0, 1)
    assert simplify(10, 10) == (1, 1)
    assert simplify(7, 1) == (7, 1)
    assert simplify(9, 6) == (3, 2)
    assert isinstance(simplify(6, 8), tuple)

    assert strip_punctuation("Hi, there!") == "Hi there"
    assert strip_punctuation("a-b") == "ab"
    assert strip_punctuation("wait... what?") == "wait what"
    assert strip_punctuation("") == ""
    assert strip_punctuation("abc 123") == "abc 123"
    assert strip_punctuation("!?.,;:'\"()[]{}") == ""

    assert is_palindrome("racecar") is True
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("12 21") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("") is True
    assert is_palindrome("a") is True
    assert is_palindrome("Abba") is True
    assert is_palindrome("ab") is False
    assert is_palindrome("No 'x' in Nixon") is True

    print("all drills pass")
