"""Reading lab 1 - defaults are built once, at def time.

READ FIRST, RUN LATER (20 minutes)
 1. Read the four functions and the calls. No terminal yet.
 2. Write your five answers in the PREDICTION block at the bottom.
 3. Only then run:  python week3/day01_readinglab1.py
 4. Answer in journal.md -> Learned: why does the second add_tag call see the
    first call's item?
    Nothing in this file is yours to write except the prediction block.

This file has the shape of a test: one function, then the calls that pin down
its behaviour. Predictions 1 and 2 are the two asserts a test writer would
write first - and the second one is the one that fails. That is the point of
reading tests before writing them.
"""

label = "global"


def add_tag(tag, tags=[]):
    tags.append(tag)
    return tags


def read_label():
    return label


def write_label():
    label = "local"
    return label


count = 0


def bump():
    count = count + 1
    return count


# --------------------------------------------------------------- the answers
# Predict these five, IN THE BLOCK AT THE BOTTOM, before running.
if __name__ == "__main__":
    print("1) add_tag('a') =", repr(add_tag("a")))
    print("2) add_tag('b') =", repr(add_tag("b")))
    print("3) read_label() =", repr(read_label()))
    print("4) write_label() then label =", repr(write_label()), repr(label))
    try:
        bump()
    except Exception as exc:
        # type(exc).__name__ is the class name of what went wrong, as a string.
        print("5) bump() ->", type(exc).__name__)


'''PREDICTION - write before running.

1)add_tag('a') = add_tag('a',[])  then tags.append('a')
so tags=['a']  return ['a'] 

2)add_tag('b') = add_tag('b',[]) then tags.append('b')
so tags=['b']  return ['b']

3)read_label() = return label--> return "global"

4)write_label() then label = write label label = "local"
    return "local"  but label is gobal value so label= "global"

5)bump() ->", type(exc).__name__
well it seem no problem ? count=0+1 then return 1 isnt it? 
or it just keep running count+=1?  well i have to take a guess
if real action is keep looping. it will cause runtime error.
ACTUAL

1) add_tag('a') = ['a']
2) add_tag('b') = ['a', 'b']
3) read_label() = 'global'
4) write_label() then label = 'local' 'global'
5) bump() -> UnboundLocalError
3/5 not bad 

One sentence on the miss (if any):
'''
