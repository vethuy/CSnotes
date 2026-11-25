"""Reading lab 4 - trace the calls: a stack of frames, and fib's fan-out.

READ FIRST, RUN LATER (20 minutes)
 1. Read the three functions. For factorial(4), write the order of the lines
    you expect to see. No terminal yet.
 2. Count fib's calls for n = 5 on paper, using a tally on a corner of the page.
 3. Write your answers in the PREDICTION block, then run:
       python week4/day04_readinglab4.py
 4. Answer in journal.md: factorial prints its returns in the opposite order
    to its calls. Which data structure in the interpreter makes that happen?
    Nothing here is yours to write.

`factorial` prints on the way in and on the way out; the indentation is the
depth, so it is a picture of the call stack. `fib` has no prints - only a
counter in a one-item list, which is the smallest way to keep a total across
calls without a global statement.
"""


def factorial(n, depth=0):
    """Return n!, printing the call and the return with depth spaces."""
    pad = "  " * depth
    print(pad + "call factorial(" + str(n) + ")")
    if n == 0:
        print(pad + "return 1")
        return 1
    result = n * factorial(n - 1, depth + 1)
    print(pad + "return " + str(result))
    return result


calls = [0]


def fib(n):
    """Return the nth Fibonacci number, counting every call in calls[0]."""
    calls[0] += 1
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# --------------------------------------------------------------- the answers
if __name__ == "__main__":
    print("--- factorial(4)")
    print("factorial(4) =", factorial(4))

    print("--- fib")
    for n in (5, 8, 10):
        calls[0] = 0
        value = fib(n)
        print("fib(" + str(n) + ")", "=", value, " calls =", calls[0])


'''PREDICTION - write before running.

1) How many "call factorial(" lines?  ?
2) How many "return" lines?  ?
3) What is the LAST line printed by the factorial block?
4) fib(5)  = ?   calls = ?
5) fib(8)  = ?   calls = ?
6) fib(10) = ?   calls = ?
7) Each extra n multiplies the calls by roughly what number?

ACTUAL - paste after running.
'''
