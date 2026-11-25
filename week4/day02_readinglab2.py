"""Reading lab 2 - the same sort twice: one stops early, one never does.

READ FIRST, RUN LATER (20 minutes)
 1. Read both functions and count comparisons by hand for [4, 2, 3, 1].
 2. Write your answers in the PREDICTION block at the bottom.
 3. Only then run:  python week4/day02_readinglab2.py
 4. Answer in journal.md: one of these is O(n) on sorted input and the other
    is O(n^2). Which, and which line makes the difference?
    Nothing here is yours to write.

Two bubble sorts. `bubble_shrinking` is the one you wrote tonight: each pass
looks only at the unsorted prefix, and the pass loop stops when nothing was
swapped. `bubble_plain` has neither idea - it runs n-1 passes of n-1
comparisons no matter what the data looks like.
"""


def bubble_shrinking(items):
    """Bubble sort with a shrinking pass and an early exit; counts comparisons."""
    values = list(items)
    comparisons = 0
    for i in range(len(values) - 1):
        swapped = False
        for j in range(len(values) - 1 - i):
            comparisons += 1
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True
        if not swapped:
            break
    return values, comparisons


def bubble_plain(items):
    """Bubble sort with no flag and no shrinking; counts comparisons."""
    values = list(items)
    comparisons = 0
    for _ in range(len(values) - 1):
        for j in range(len(values) - 1):
            comparisons += 1
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
    return values, comparisons


# --------------------------------------------------------------- the answers
if __name__ == "__main__":
    for name, items in [
        ("sorted", [1, 2, 3, 4]),
        ("reversed", [4, 3, 2, 1]),
        ("mixed", [4, 2, 3, 1]),
    ]:
        early_list, early = bubble_shrinking(items)
        plain_list, plain = bubble_plain(items)
        print(name.ljust(9), "early:", early, " plain:", plain, " result:", early_list)
        assert early_list == plain_list == sorted(items)


'''PREDICTION - write before running.

1) sorted    [1, 2, 3, 4] : early comparisons = ?   plain = ?
2) reversed  [4, 3, 2, 1] : early comparisons = ?   plain = ?
3) mixed     [4, 2, 3, 1] : early comparisons = ?   plain = ?
4) Which function does the same work on sorted and reversed data, and why?
5) How many comparisons does bubble_shrinking need for 8 sorted items?

ACTUAL - paste after running.
'''
