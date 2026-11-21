"""Reading lab 2 - a stdlib module, a one-line function, and a hidden default.

READ FIRST, RUN LATER (20 minutes)
 1. Read the calls below and the quoted `capwords` body. No terminal yet.
 2. Write your five answers in the PREDICTION block at the bottom.
 3. Only then run:  python week3/day02_readinglab2.py
 4. Answer in journal.md: which character of the `capwords` body explains why
    "hello   world" comes out with ONE space? Nothing here is yours to write.

The stdlib version: string.py:37 `capwords`. Its whole body is one return:

    return (sep or ' ').join(map(str.capitalize, s.split(sep)))

Read it twice. `sep or ' '` is a default hidden inside an expression - sep is
None on a normal call, and `None or ' '` is `' '`. Then `s.split(sep)` with
sep=None does not split on a space character: it splits on ANY RUN of
whitespace and drops the empty strings. That second fact is prediction 1.
"""

import string


# --------------------------------------------------------------- the answers
if __name__ == "__main__":
    print('1) string.capwords("hello   world")      =', repr(string.capwords("hello   world")))
    print('2) string.capwords("they\'re ok")        =', repr(string.capwords("they're ok")))
    print('3) string.capwords("a-b c", sep="-")     =', repr(string.capwords("a-b c", sep="-")))
    print('4) string.capwords("  spam  ")           =', repr(string.capwords("  spam  ")))
    print('5) string.capwords("ABC def")            =', repr(string.capwords("ABC def")))


'''PREDICTION - write before running.

1) string.capwords("hello   world") =
2) string.capwords("they're ok") =
3) string.capwords("a-b c", sep="-") =
4) string.capwords("  spam  ") =
5) string.capwords("ABC def") =
   (which call surprised you, and which character of the body caused it?)


ACTUAL - paste after running.

1)
2)
3)
4)
5)

One sentence on the miss:
'''
