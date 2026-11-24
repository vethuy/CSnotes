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
all labels in show()
1) best(["a,3", "b,5"]) = for line in  ["a,3", "b,5"]  (1)top = ('a',3)  (2)5>3 top=('b',5)
no Exception so print  best(["a,3", "b,5"])->('b',5)
2) best([]) =for line in [] no line ,so print best([]) -> None
3) best(["a,3", "b"]) for line in ['a,3', 'b'] (1)top=('a',3)then raise in here  name, score = line.split(",")(score missing)
so it raise ValueError/not enough values to unpack (expected 2, got 1) /line19:parse_line(line)    raises: type / message / which function
4) best(["a,3", "b,x"]) for line in ['a,3', 'b,x'] (1)top=('a',3)  then raise in int('x')
so it raise ValueError/invalid literal for int() with base 10: 'x' / line20:parse_line(line) raises: type / message / which function
5) best(["a,3", ""])   (1)top=('a',3)then raise in here  name, score = line.split(",")(score missing)
so it raise ValueError/not enough values to unpack (expected 2, got 1) /line19:parse_line(line)      raises: type / message / which function


ACTUAL - paste after running.

1) best(['a,3', 'b,5'])  -> ('b', 5)
2) best([])              -> None
3) best(['a,3', 'b'])    -> ValueError - not enough values to unpack (expected 2, got 1)
     raised in parse_line at line 19
4) best(['a,3', 'b,x'])  -> ValueError - invalid literal for int() with base 10: 'x'
     raised in parse_line at line 20
5) best(['a,3', ''])     -> ValueError - not enough values to unpack (expected 2, got 1)
     raised in parse_line at line 19
5/5
One sentence on the miss:
'''
