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

1) selection after 1 -> ? i=0 1 is the smallest in range(1,4) swap to [1,2,5,4]
2) selection after 2 -> ? i=1 nothing smaller then 2 no swap
3) selection after 3 -> ? i=2 4 is the smallest in range(3,4) swap to [1,2,4,5]
4) selection after 4 -> ? i=3 5 itself so no swap
5) insertion after 1 -> ? i=1 4>2 shift to [2,4,5,1]
6) insertion after 2 -> ? i=2 2,4<5 no shift
7) insertion after 3 -> ? i=3 2,4,5>1 shift to [1,2,4,5]
8) swaps = ?   shifts = ? swaps = 2   shifts = 4
9) Which sort moved the fewest items for this input? moved the fewest items:selection sort
(extra:add by roy insertion use 3 moves and selection use 4 move.)

ACTUAL - paste after running.
selection after 1 [1, 2, 5, 4]
selection after 2 [1, 2, 5, 4]
selection after 3 [1, 2, 4, 5]
selection after 4 [1, 2, 4, 5]
insertion after 1 [2, 4, 5, 1]
insertion after 2 [2, 4, 5, 1]
insertion after 3 [1, 2, 4, 5]
selection result [1, 2, 4, 5] swaps 2
insertion result [1, 2, 4, 5] shifts 4
original untouched [4, 2, 5, 1]
1)~8) correct 9) need to check by dsh

'''
