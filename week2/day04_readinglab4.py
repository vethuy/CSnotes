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
First analyse  rows = read_rows(DATA)
return list(csv.DictReader(text.splitlines())) First  text.splitlines()-->DATA.splitlines()
so now become ['name,age','ann,30','bob','cat,25,extra'] then csv.DictReader it
but a dict have bob only and extra? let guess  {'name':'age','ann':30,'cat':25} bob and extra got exclude?
after list it become [('name','age'),('ann',30),('cat',25)]
so answer the question now
1) len(rows) =3

2)rows[1] = ('ann',30)

3)rows[2] =('cat',25)

4) rows[2]['age'] == 25 =True

ACTUAL

1) len(rows) = 3
2) rows[1] = {'name': 'bob', 'age': None}
3) rows[2] = {'name': 'cat', 'age': '25', None: ['extra']}
4) rows[2]['age'] == 25 = False
1/4 the first analyse is wrong
One sentence on the miss (if any):I read the call as csv.reader and predicted cell-tuples of ints; it is DictReader, so the rows are dicts of strings.
'''
