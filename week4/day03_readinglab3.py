"""Reading lab 3 - one list, two sorts, and what the list looks like halfway.

READ FIRST, RUN LATER (20 minutes)
 1. Read both functions and trace [4, 2, 5, 1] on paper. No terminal yet.
 2. Write your answers in the PREDICTION block at the bottom.
 3. Only then run:  python week4/day03_readinglab3.py
 4. Answer in journal.md: selection sort prints the same list twice in a row
    at the start. Which pass did no work, and why is that not a bug?
    Nothing here is yours to write.

`selection_steps` prints after every swap position, even when the smallest item
was already there (then `smallest == i` and no swap happens). `insertion_steps`
prints after every new item is dropped into the sorted prefix, and counts the
number of items it had to slide right to make room.
"""


def selection_steps(items):
    """Selection sort, printing the list after each position; returns (list, swaps)."""
    values = list(items)
    swaps = 0
    for i in range(len(values)):
        smallest = i
        for j in range(i + 1, len(values)):
            if values[j] < values[smallest]:
                smallest = j
        if smallest != i:
            values[i], values[smallest] = values[smallest], values[i]
            swaps += 1
        print("selection after", i + 1, values)
    return values, swaps


def insertion_steps(items):
    """Insertion sort, printing after each item; returns (list, shifts)."""
    values = list(items)
    shifts = 0
    for i in range(1, len(values)):
        value = values[i]
        pos = i
        while pos > 0 and values[pos - 1] > value:
            values[pos] = values[pos - 1]
            pos -= 1
            shifts += 1
        values[pos] = value
        print("insertion after", i, values)
    return values, shifts


# --------------------------------------------------------------- the answers
if __name__ == "__main__":
    data = [4, 2, 5, 1]
    selected, swaps = selection_steps(data)
    inserted, shifts = insertion_steps(data)
    print("selection result", selected, "swaps", swaps)
    print("insertion result", inserted, "shifts", shifts)
    print("original untouched", data)


'''PREDICTION - write before running.

1) selection after 1 -> ?
2) selection after 2 -> ?
3) selection after 3 -> ?
4) selection after 4 -> ?
5) insertion after 1 -> ?
6) insertion after 2 -> ?
7) insertion after 3 -> ?
8) swaps = ?   shifts = ?
9) Which sort moved the fewest items for this input?

ACTUAL - paste after running.
'''
