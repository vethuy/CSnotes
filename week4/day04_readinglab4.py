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

1) How many "call factorial(" lines?  ? 5 times 4,3,2,1,0
2) How many "return" lines?  ? 5
3) What is the LAST line printed by the factorial block? return 24
honestly. it is hard and boring to count every calls . so calls answer and numbers are provide by dsh
4) fib(5)  = ?   calls = ?     fib(5)  = 5  calls = 15
5) fib(8)  = ?   calls = ?     fib(8)  = 21   calls = 67
6) fib(10) = ?   calls = ?     fib(10) = 55   calls = 177
7) Each extra n multiplies the calls by roughly what number? 2

ACTUAL - paste after running.
--- factorial(4)
call factorial(4)
  call factorial(3)
    call factorial(2)
      call factorial(1)
        call factorial(0)
        return 1
      return 1
    return 2
  return 6
return 24
factorial(4) = 24
--- fib
fib(5) = 5  calls = 15
fib(8) = 21  calls = 67
fib(10) = 55  calls = 177
1)~3) correct 4)~6) doesnt count 7) need check by dsh
5/7
'''
