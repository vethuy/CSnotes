# Week 2 - recall (day00: used before every day)

Ten minutes at the start of every session, before any code, every tab closed.

How to use it:

1. Read the three questions for the day.
2. Answer out loud or on paper - not in your head.
3. Mark the answer: wrote it correctly, or did not.
4. Anything you got wrong goes into `journal.md` as one line.
5. Delete this file on Sunday after the weekly review.

A wrong answer here is worth more than a right one: it tells you what Tuesday
needs to start with.

---

## Day 1 - Monday

1. In `day05_days_between.py`, what did `time_check` do that made it hard to
   reuse, and what should it return instead?
2. `range(1, 6)` produces how many values, and what was your original mistake
   in week 1?
3. What type does `date - date` return, and which attribute turns it into an
   `int`?

## Day 2 - Tuesday

1. `a[:]` versus `a` - which one do you need before sorting a copy?
2. What does `rotate_left([1, 2], 5)` return, and why does `k` need
   `len(nums)`?
3. Which line of `statistics.mean` proves it does not modify its argument?

## Day 3 - Wednesday

1. Why does `invert({"a": 1, "b": 1})` lose an entry?
2. Write the counting idiom from memory: how do you add one to a dict entry
   that may not exist yet?
3. In `day02_word_count.py`, which function knows about printing?

## Day 4 - Thursday

1. List versus set membership: which is O(1), and what did you measure?
2. What does `list(set(x))` cost besides speed?
3. Write `dedupe_keep_order` from memory, in words.

## Day 5 - Friday

1. Why do you `.strip()` almost every line you read from a file?
2. What does `csv.DictReader` do with a row that has too few fields?
3. Which function in `day04_expense_summary.py` turns strings into numbers, and
   what does it raise on `"3,50"`?

## Day 6 - Saturday

1. Why does `day06_todo.load()` return `[]` for a missing file but let
   `JSONDecodeError` escape for a broken one?
2. Which value decides the process exit code, and which function produces it?
3. After `remove 2`, why must a new task not take id 2?

## Day 7 - Sunday (weekly review)

1. What shipped? Name the files, not the feelings.
2. What confused you most this week? Name the line of code.
3. What is Week 3's number one goal?
