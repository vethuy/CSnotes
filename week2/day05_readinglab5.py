"""Reading lab 5 - json.loads and the error it hands back.

READ FIRST, RUN LATER (20 minutes)
 1. Read `load` and the five calls. Keep the terminal closed.
 2. Write your five answers in the PREDICTION block at the bottom.
 3. Only then run:  python week2/day05_readinglab5.py
 4. Answer in reading-notes.md: JSONDecodeError inherits from which built-in
    class, and why does that make `except ValueError` enough?
    Nothing here is yours to write.

The stdlib version: json/decoder.py:353 `JSONDecodeError`, and
json/decoder.py:20 `JSONDecoder`. Read the exception class for 12 minutes -
its constructor builds the "line 1 column 8 (char 7)" part that prediction 4
turns on.
"""

import json


def load(text):
    """Parse JSON text; return the error message instead of raising."""
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        return f"bad at line {exc.lineno}, column {exc.colno}"


# --------------------------------------------------------------- the answers
if __name__ == "__main__":
    print("1) load('[1, 2]') =", repr(load("[1, 2]")))
    print("2) load('null') =", repr(load("null")))
    print("3) load('') =", repr(load("")))
    print("4) load('{\"a\": 1,}') =", repr(load('{"a": 1,}')))
    print(
        "5) issubclass(json.JSONDecodeError, ValueError) =",
        repr(issubclass(json.JSONDecodeError, ValueError)),
    )


'''PREDICTION - write before running.

1)
2)
3)
4)
5)

ACTUAL

1)
2)
3)
4)
5)

One sentence on the miss (if any):
'''
