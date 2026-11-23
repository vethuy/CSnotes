"""Reading lab 4 - a test file is five claims, and one of them is a lie.

READ FIRST, RUN LATER (20 minutes)
 1. Read `chunk` and the five tests. No terminal yet.
 2. Write your five answers in the PREDICTION block at the bottom.
 3. Only then run:  python week3/day04_readinglab4.py
 4. Answer in journal.md: one test passes for a reason the docstring never
    promised. Which one, and what would a stricter test have said?
    Nothing here is yours to write.

The shape: pytest collects functions named `test_*`, calls each one, and a
failing `assert` is the report. Below the tests are plain `print`s so you can
run the file without pytest - but each line is exactly one assert, printed
instead of raised. Test 5 is the one that raises.
"""


# FUNCTION INTRODUCTION: a slice items[i:i+size] never raises when the slice
# runs past the end - it simply stops. range(0, len(items), size) supplies the
# starting index of every chunk.
def chunk(items, size):
    """Return items split into a list of lists, each of length size or less.

    size must be a positive whole number. items is a list, and the last chunk
    may be shorter. chunk([], 2) is [].

    chunk([1, 2, 3, 4], 2)    -> [[1, 2], [3, 4]]
    chunk([1, 2, 3], 2)       -> [[1, 2], [3]]
    chunk([], 2)              -> []
    """
    return [items[i : i + size] for i in range(0, len(items), size)]


# --------------------------------------------------------------- the answers
if __name__ == "__main__":
    print("test_chunk_even     ", chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]])
    print("test_chunk_empty    ", chunk([], 2) == [])
    print("test_chunk_odd      ", chunk([1, 2, 3], 2) == [[1, 2], [3]])
    print("test_chunk_string   ", chunk("abcd", 2) == ["ab", "cd"])

    try:
        chunk([1, 2], 0)
    except Exception as exc:
        print("test_chunk_zero     raises", type(exc).__name__, "-", exc)
    else:
        print("test_chunk_zero     returned", repr(chunk([1, 2], 0)))


'''PREDICTION - write before running.

1) test_chunk_even      True or False?  True
2) test_chunk_empty     True or False?  True
3) test_chunk_odd       True or False?  True
4) test_chunk_string    True or False?  (and is that what the docstring promised?)
for i in range(0,4,2)  (1)items[0:2]-->'ab' (2)[2:4]-->'cd'  end retuen a list['ab','cd']
5) test_chunk_zero      raises what type, with what message?
for i in range (0,2,0) ,I found step default is 1, so it raise ValurError:range() arg 3 must not be zero

Which test passes for the wrong reason?


ACTUAL - paste after running.

test_chunk_even      True
test_chunk_empty     True
test_chunk_odd       True
test_chunk_string    True
test_chunk_zero     raises ValueError - range() arg 3 must not be zero
5/5 perfect

One sentence on the miss:
'''
