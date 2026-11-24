"""Week 3 . Weekend project . ten tests, ten edge cases.

RUN THE TESTS:   python -m pytest week3/day06_test_tools.py -v

Every test below starts as `raise NotImplementedError`, so the first run says
10 failed. Replace that one line with asserts until the report says 10 passed.
Do not rename a test, do not delete one, and do not change `day06_tools.py` to
make a test easier - the docstring is the claim, and the code either keeps it
or does not.

A task is one dict:  {"id": 1, "text": "read", "done": False}

pytest reports the FIRST failing assert in a test, so when a test fails, read
the line pytest points at, then read the function it calls. `-x` stops at the
first failure:  python -m pytest week3/day06_test_tools.py -x -v
"""

from day06_tools import (
    add_task,
    complete_task,
    find_task,
    new_id,
    parse_command,
    remove_task,
    render_task,
)


def test_new_id_on_empty_list():
    assert new_id([])==1
    """The first task in an empty list gets id 1."""


def test_new_id_is_highest_plus_one():
    """Ids 3 and 1 -> next is 4. Gaps are not filled."""
    raise NotImplementedError("test_new_id_is_highest_plus_one")


def test_add_task_does_not_modify_the_original():
    """add_task returns a NEW list; the caller's list is the same length afterwards."""
    raise NotImplementedError("test_add_task_does_not_modify_the_original")


def test_add_task_uses_the_next_id():
    """The appended task gets the id new_id(tasks) would return, and starts open."""
    raise NotImplementedError("test_add_task_uses_the_next_id")


def test_find_task_finds_or_returns_none():
    """find_task returns the task dict for a known id and None for an unknown one."""
    raise NotImplementedError("test_find_task_finds_or_returns_none")


def test_complete_task_marks_done():
    """The returned list has that task's done True - and the original still has False."""
    raise NotImplementedError("test_complete_task_marks_done")


def test_complete_task_unknown_id_raises():
    """Completing an id that does not exist raises ValueError."""
    raise NotImplementedError("test_complete_task_unknown_id_raises")


def test_remove_task_removes_or_raises():
    """Removing id 1 drops exactly that task; removing id 99 raises ValueError."""
    raise NotImplementedError("test_remove_task_removes_or_raises")


def test_render_task_open_and_done():
    """An open task renders "1. [ ] read"; a done one renders "1. [x] read"."""
    raise NotImplementedError("test_render_task_open_and_done")


def test_parse_command():
    """list/add/done/remove parse to tuples; empty, unknown and a bad id raise ValueError."""
    raise NotImplementedError("test_parse_command")
