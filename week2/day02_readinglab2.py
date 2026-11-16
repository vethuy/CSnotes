"""Reading lab 2 - sorting a dict by its values, and what happens to ties.

READ FIRST, RUN LATER (20 minutes)
 1. Read `most_common` and the four calls. No terminal yet.
 2. Write your four answers in the PREDICTION block at the bottom.
 3. Only then run:  python week2/day02_readinglab2.py
 4. Add one line to reading-notes.md: "when counts are equal, the order
    comes from ___". Nothing in this file is yours to write.

The stdlib version: collections/__init__.py `Counter.most_common`. It sorts
by count alone, exactly like this one, and leans on Python's sort being
STABLE. Read that method for the 12-minute part.
"""


def most_common(counts, n=None):
    """Return [(word, count), ...] with the biggest count first.

    Only the count is the sort key; ties keep the dict's own order.
    reverse=True means "biggest first". n=None means "all of them".
    """
    pairs = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
    return pairs if n is None else pairs[:n]


# --------------------------------------------------------------- the answers
if __name__ == "__main__":
    counts = {"a": 2, "b": 2, "c": 1}
    other = {"c": 1, "a": 2, "b": 2}
    print("1) most_common(counts) =", repr(most_common(counts)))
    print("2) most_common(other, 2) =", repr(most_common(other, 2)))
    print("3) most_common(counts, 0) =", repr(most_common(counts, 0)))
    print("4) counts.get('z', 0) =", repr(counts.get("z", 0)))


'''PREDICTION - write before running.
First analyse the code
pairs=sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
sorted counts all item  key is the dict value   then reverse
n=None return all .  else return pairs[:n]
1)most_common(counts) =
counts = {"a": 2, "b": 2, "c": 1} sort it by the value then reverse
n=None return all.so we get[("a": 2), ("b": 2), ("c": 1)] 

2)most_common(other, 2) =same step .so we can get sorted it{"c": 1, "a": 2, "b": 2}
then reverse {"b": 2, "a": 2, "c": 1}  n=2 mean return pairs[:2]
so return [("b": 2), ("a": 2)]

3)most_common(counts, 0) wait n=0? return pairs[:0]? so it return []

4)counts.get('z', 0) ='z'?  counts dict has no 'z' so there no value in it
so it return None

ACTUAL

1) most_common(counts) = [('a', 2), ('b', 2), ('c', 1)]
2) most_common(other, 2) = [('a', 2), ('b', 2)]
3) most_common(counts, 0) = []
4) counts.get('z', 0) = 0
2/4 diffcult one
One sentence on the miss (if any):
'''
