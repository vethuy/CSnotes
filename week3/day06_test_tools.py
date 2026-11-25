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
    assert new_id([{'id':1},{'id':3}])==4
    """Ids 3 and 1 -> next is 4. Gaps are not filled."""
 


def test_add_task_does_not_modify_the_original():
    tasks=[{'id': 1,'text': 'read','done': False}]
    assert add_task(tasks,'write') == [{'id': 1,'text': 'read','done': False},{'id': 2,'text': 'write','done': False}]
    assert tasks==[{'id': 1,'text': 'read','done': False}]
    """add_task returns a NEW list; the caller's list is the same length afterwards."""
    


def test_add_task_uses_the_next_id():
    tasks=[{'id': 1,'text': 'read','done': False},{'id': 3,'text': 'write','done': False}]
    assert add_task(tasks,'speak')==[{'id': 1,'text': 'read','done': False},{'id': 3,'text': 'write','done': False},{'id': 4,'text': 'speak','done': False}]
    """The appended task gets the id new_id(tasks) would return, and starts open."""
    


def test_find_task_finds_or_returns_none():
    tasks=[{'id': 1,'text': 'read','done': False},{'id': 3,'text': 'write','done': False}]
    assert find_task(tasks,3)=={'id': 3,'text': 'write','done': False}
    assert find_task([],1)==None
    assert find_task(tasks,7)==None
    """find_task returns the task dict for a known id and None for an unknown one."""


def test_complete_task_marks_done():
    tasks=[{'id': 1,'text': 'read','done': False},{'id': 3,'text': 'write','done': False}]
    assert complete_task(tasks,1)==[{'id': 1,'text': 'read','done': True},{'id': 3,'text': 'write','done': False}]
    assert tasks==[{'id': 1,'text': 'read','done': False},{'id': 3,'text': 'write','done': False}]
    """The returned list has that task's done True - and the original still has False."""
    


def test_complete_task_unknown_id_raises():
    tasks=[{'id': 1,'text': 'read','done': False},{'id': 3,'text': 'write','done': False}]
    try:
        complete_task(tasks,7)
    except ValueError:
        pass
    """Completing an id that does not exist raises ValueError."""
    


def test_remove_task_removes_or_raises():
    tasks=[{'id': 1,'text': 'read','done': False},{'id': 3,'text': 'write','done': False}]
    assert remove_task(tasks,1)==[{'id': 3,'text': 'write','done': False}]
    assert tasks==[{'id': 1,'text': 'read','done': False},{'id': 3,'text': 'write','done': False}]
    try:
        remove_task(tasks,99)
    except ValueError:
        pass
    """Removing id 1 drops exactly that task; removing id 99 raises ValueError."""
    

def test_render_task_open_and_done():
    tasks=[{'id': 1,'text': 'read','done': False},{'id': 3,'text': 'write','done': False}]
    assert render_task(tasks)=='1. [ ] read\n3. [ ] write'
    finish=complete_task(tasks,1)
    assert render_task(finish)=='1. [x] read\n3. [ ] write'
    """An open task renders "1. [ ] read"; a done one renders "1. [x] read"."""
    


def test_parse_command():
    assert parse_command(["list"])  == ("list",)
    assert parse_command(["add", "read"]) == ("add", "read")
    assert parse_command(["add", "read","book"]) == ("add", "read book")
    assert parse_command(["done", "3"])   == ("done", 3)
    assert parse_command(["remove", "3"]) == ("remove", 3)
    try:
        parse_command([])   
    except ValueError:
        pass      
    try:
        parse_command(["nope"])   
    except ValueError:
        pass             
    try:
        parse_command(["remove", "x"])   
    except ValueError:
        pass    
    try:
            parse_command(["add", "/","8"])   
    except ValueError:
            pass 
    """list/add/done/remove parse to tuples; empty, unknown and a bad id raise ValueError."""
   
