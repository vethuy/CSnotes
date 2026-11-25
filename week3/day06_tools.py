"""Week 3 . Weekend project . the to-do data, refactored into small functions.

RUN THE TESTS:   python -m pytest week3/day06_test_tools.py -v

This module is the data half of Week 2's `day06_todo.py` with the file I/O,
the printing and `sys.argv` removed. Nothing here reads a file, writes a file
or prints; every function takes a list of task dicts and returns a value.

A task is one dict with three keys:

    {"id": 1, "text": "read chapter 3", "done": False}

THE POINT of the refactor: each function is small enough to describe in one
line and call in a test. `add_task` does not save; `complete_task` does not
print; `parse_command` does not know a keyboard exists. The CLI shell that
does those three things stays in `week2/day06_todo.py` - do not move it here.

Read every docstring before you type. The ten tests in
`day06_test_tools.py` fail on purpose: each one names an edge case, and the
body is yours to write. Done when the report says 10 passed.
"""

# FUNCTION INTRODUCTION: max(...) with a generator is the "highest so far"
# idiom - max(t["id"] for t in tasks) - and the empty case needs its own answer
# because max() of nothing raises ValueError.
def new_id(tasks):
    if tasks==[]:
        return 1
    else:
        result=max(i['id'] for i in tasks)
        return result+1

    """Return the id the next task should get: highest existing id + 1.

    An empty list gets 1. Gaps are not filled: if the ids are 3 and 1, the next
    id is 4, not 2. Ids are ints.

    tasks is a list of task dicts; it must not be modified.

    new_id([])                                        -> 1
    new_id([{"id": 1}])                               -> 2
    new_id([{"id": 3}, {"id": 1}])                    -> 4
    new_id([{"id": 2}, {"id": 2}])                    -> 3
    """
    raise NotImplementedError("new_id")


def add_task(tasks, text):
    result=list(tasks)
    add={'id': new_id(tasks),'text': text,'done': False}
    result.append(add)
    return result
    """Return a NEW list: the old tasks, then a new open task with the next id.

    tasks must not be modified. text is a str and is stored unchanged; the new
    task starts with "done": False.

    add_task([], "read")                     -> [{"id": 1, "text": "read", "done": False}]
    add_task([{"id": 1, "text": "a", "done": True}], "b")
                                             -> [{"id": 1, "text": "a", "done": True},
                                                 {"id": 2, "text": "b", "done": False}]
    """
    raise NotImplementedError("add_task")


def find_task(tasks, task_id):
    for i in tasks:
        if i['id'] == task_id:
            return i
    return None
    """Return the task dict with this id, or None when there is no such task.

    Do not raise for a missing id; the caller decides what a missing task
    means. tasks must not be modified.

    find_task([{"id": 1, "text": "a", "done": False}], 1)
        -> {"id": 1, "text": "a", "done": False}
    find_task([], 1)                         -> None
    """
    raise NotImplementedError("find_task")


def complete_task(tasks, task_id):
    if find_task(tasks,task_id)==None:
        raise ValueError(f"no task with id: {task_id}")
    result=[]
    for i in tasks:
        if i['id']==task_id:
            result.append({**i,'done': True})
        else:
            result.append(i)
    return result

        
    """Return a NEW list with that task marked done.

    tasks must not be modified - the old list still has the task open. If no
    task has this id, raise ValueError naming the id.

    complete_task([{"id": 1, "text": "a", "done": False}], 1)
        -> [{"id": 1, "text": "a", "done": True}]
    """
    raise NotImplementedError("complete_task")


def remove_task(tasks, task_id):
    if find_task(tasks,task_id)==None:
        raise ValueError(f"no task with id: {task_id}")
    result=[]
    for i in tasks:
        if i['id']==task_id:
            continue
        else:
            result.append(i)
    return result
    """Return a NEW list without that task.

    tasks must not be modified. If no task has this id, raise ValueError
    naming the id.

    remove_task([{"id": 1}, {"id": 2}], 1)     -> [{"id": 2}]
    """
    raise NotImplementedError("remove_task")


def render_task(task):
    lines=[]
    for i in task:
        id,text,done=i['id'],i['text'],i['done']
        if done==True:
            lines.append(f"{id}. [x] {text}")
        else:
            lines.append(f"{id}. [ ] {text}")
    return '\n'.join(lines)

    """Return full text of task: the id, a done box, and the text.

    The box is "[x]" when done is True and "[ ]" when it is False. The id is
    followed by a dot and a space.

    render_task({"id": 1, "text": "read", "done": False})   -> "1. [ ] read"
    render_task({"id": 2, "text": "rest", "done": True})    -> "2. [x] rest"
    """
    raise NotImplementedError("render_task")


def parse_command(argv):
    if argv==[]:
        raise ValueError(f"this is not a command")
    command=['list','add','done','remove']
    if argv[0] not in command :
        raise ValueError(f"this is not a command")
    if argv[0]=='list':
        return (argv[0],)
    elif argv[0]=='add':
        try:
            str(argv[1:])
        except ValueError:
            raise ValueError(f"{argv[1:]} is not a vaild")
        else:
            return (argv[0],' '.join(argv[1:]))
    elif argv[0]=='done':
        try:
            int(argv[1])
        except ValueError:
            raise ValueError(f"{argv[1]} is not a vaild")
        else:
            return (argv[0],int(argv[1]))
    elif argv[0]=='remove':
        try:
             int(argv[1])
        except ValueError:
            raise ValueError(f"{argv[1]} is not a vaild")
        else:
            return (argv[0],int(argv[1]))
    else:
        raise ValueError(f"{argv[1]} is not a vaild")
    """Return a command tuple from the words after the program name.

    ("list",) for no extra words · ("add", text) for add · ("done", id) and
    ("remove", id) for the other two. Ids are ints, and `add` keeps the rest of
    the words as one text with single spaces.

    A missing command, an unknown command, a missing id, or an id that is not
    a whole number all raise ValueError.

    parse_command([])                    -> ValueError
    parse_command(["list"])              -> ("list",)
    parse_command(["add", "read"])       -> ("add", "read")
    parse_command(["done", "3"])         -> ("done", 3)
    parse_command(["remove", "3"])       -> ("remove", 3)
    parse_command(["nope"])              -> ValueError
    """
    raise NotImplementedError("parse_command")
