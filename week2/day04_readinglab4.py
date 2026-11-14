"""Reading lab 4 - what csv.DictReader does to a broken row.

READ FIRST, RUN LATER (20 minutes)
 1. Read DATA and read_rows(), then the four calls. No terminal yet.
 2. Write your four answers in the PREDICTION block at the bottom.
 3. Only then run:  python week2/day04_readinglab4.py
 4. Answer in reading-notes.md: where does a leftover field go, and what
    fills a missing one? Nothing here is yours to write.

The stdlib version: csv.py:145 `DictReader`. Read `fieldnames` and
`__next__` for the 12-minute part - they are short, and they explain both
surprises below.

The plan opens a real CSV file here. This lab keeps the same bytes in a
string and hands DictReader one line at a time, so there is no fixture file
to lose and nothing new to learn about `open` before Friday. Everything
else is identical. `text.splitlines()` is the one new name in this file: it
is `.split("\n")` without a trailing empty string.
"""

import csv

DATA = "name,age\nann,30\nbob\ncat,25,extra\n"


def read_rows(text):
    """Parse CSV text into a list of dicts, using the stdlib reader."""
    return list(csv.DictReader(text.splitlines()))


# --------------------------------------------------------------- the answers
if __name__ == "__main__":
    rows = read_rows(DATA)
    print("1) len(rows) =", repr(len(rows)))
    print("2) rows[1] =", repr(rows[1]))
    print("3) rows[2] =", repr(rows[2]))
    print("4) rows[2]['age'] == 25 =", repr(rows[2]["age"] == 25))


'''PREDICTION - write before running.

1)
2)
3)
4)

ACTUAL

1)
2)
3)
4)

One sentence on the miss (if any):
'''
