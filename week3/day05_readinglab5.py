"""Reading lab 5 - the last line of a traceback is the frame that failed.

READ FIRST, RUN LATER (20 minutes)
 1. Read the two functions and the five calls. No terminal yet.
 2. Write your five answers in the PREDICTION block at the bottom.
 3. Only then run:  python week3/day05_readinglab5.py
 4. Answer in journal.md: `best` is the function you call, but which function
    does the traceback blame? Nothing here is yours to write.

The shape: `show` catches the exception and walks to the INNERMOST frame -
`while frame.tb_next is not None` - because that is where the bad value was
used. The outer frame only says who called it. That walk is exactly what the
debugger shows you as the highlighted line.
"""


def parse_line(line):
    """Split "name,score" into (name, int(score)). No error handling."""
    name, score = line.split(",")
    return name, int(score)


def best(lines):
    """Return (name, score) for the highest score, or None for no lines."""
    top = None
    for line in lines:
        name, score = parse_line(line)
        if top is None or score > top[1]:
            top = (name, score)
    return top


def show(label, lines):
    """Print best(lines), or the exception type, message and failing frame."""
    try:
        print(label, "->", repr(best(lines)))
    except Exception as exc:
        frame = exc.__traceback__
        while frame.tb_next is not None:
            frame = frame.tb_next
        print(label, "->", type(exc).__name__, "-", exc)
        name = frame.tb_frame.f_code.co_name
        print("     raised in", name, "at line", frame.tb_lineno)


# --------------------------------------------------------------- the answers
if __name__ == "__main__":
    show("1) best(['a,3', 'b,5']) ", ["a,3", "b,5"])
    show("2) best([])             ", [])
    show("3) best(['a,3', 'b'])   ", ["a,3", "b"])
    show("4) best(['a,3', 'b,x']) ", ["a,3", "b,x"])
    show("5) best(['a,3', ''])    ", ["a,3", ""])


'''PREDICTION - write before running.

1) best(["a,3", "b,5"]) =
2) best([]) =
3) best(["a,3", "b"])       raises: type / message / which function
4) best(["a,3", "b,x"])     raises: type / message / which function
5) best(["a,3", ""])        raises: type / message / which function


ACTUAL - paste after running.

1)
2)
3)
4)
5)

One sentence on the miss:
'''
