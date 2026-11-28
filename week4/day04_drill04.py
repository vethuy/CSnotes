"""Week 4 . Day 4 . recursion: a base case, a smaller call, and a stack.

RUN THE CHECKS:   python week4/day04_drill04.py

RULES
-----
1. Every function RETURNS its result. Nothing above the check block prints.
2. No input() in this file.
3. The argument is the caller's data: search and sort return new values.
4. Look up syntax only when a name is missing; 5 minutes maximum, then ask.
5. The check block at the bottom is the acceptance test. Do not edit it.

THE POINT: a recursive function answers the smallest question directly (the
base case) and answers every other question by asking itself a slightly
smaller one. Every call gets its own frame on the call stack, with its own
copy of the argument, so the "answer coming back" is a value, not a print.
Write these functions with recursion only - no for, no while - because the
loop version is tomorrow's, and the point today is the shape.

LOAD: 1 drill, 3 functions, about 20-25 minutes. Trace factorial(4) on paper,
writing each call and each return, before you type anything.
"""


def factorial(n):
    if n<0:
        raise ValueError('n must <=0')
    if n==0:
        return 1
    value=n*factorial(n-1)
    return value
    
    """Return n! for a whole number n >= 0; raise ValueError otherwise.

    factorial(0) is 1 by definition, so the base case is n == 0 and every
    other call is n * factorial(n - 1).

    factorial(0)   -> 1
    factorial(1)   -> 1
    factorial(5)   -> 120
    factorial(6)   -> 720
    """
    raise NotImplementedError("factorial")


def fib(n):
    if n<0:
        raise ValueError('n must >=0')
    if n==0:
        return 0
    if n==1:
        return 1
    value=fib(n-1)+fib(n-2)
    return value
    """Return the nth Fibonacci number, with fib(0) == 0 and fib(1) == 1.

    Write the slow, obvious recursion: two calls per step, no loop and no
    cache. It is correct and it is exponential - Week 6 makes it fast, and
    today you only need to feel why fib(30) takes a while.

    fib(0)    -> 0
    fib(1)    -> 1
    fib(2)    -> 1
    fib(10)   -> 55
    fib(15)   -> 610
    """
    raise NotImplementedError("fib")


def sum_to(n):
    if n<0:
        raise ValueError('n must >=0')
    if n==0:
        return 0
    value=n+sum_to(n-1)
    return value
    """Return 1 + 2 + ... + n for n >= 0; raise ValueError otherwise.

    The base case is n == 0, which adds nothing, so sum_to(0) -> 0 and
    sum_to(4) -> 4 + 3 + 2 + 1.

    sum_to(0)   -> 0
    sum_to(1)   -> 1
    sum_to(4)   -> 10
    sum_to(10)  -> 55
    """
    raise NotImplementedError("sum_to")


# --------------------------------------------------------------------------
# CHECKS - do not edit below this line
# --------------------------------------------------------------------------
if __name__ == "__main__":
    # factorial
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(6) == 720
    try:
        factorial(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("factorial must raise ValueError for a negative n")

    # fib
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(10) == 55
    assert fib(15) == 610
    try:
        fib(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("fib must raise ValueError for a negative n")

    # sum_to
    assert sum_to(0) == 0
    assert sum_to(1) == 1
    assert sum_to(4) == 10
    assert sum_to(10) == 55
    try:
        sum_to(-2)
    except ValueError:
        pass
    else:
        raise AssertionError("sum_to must raise ValueError for a negative n")

    print("all drills pass")
