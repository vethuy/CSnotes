"""Week 2 . Days 1-5 - review practice, one function per day.

RUN THE CHECKS:   python week2/day05_practice.py

RULES
-----
1. Every function RETURNS its result. Nothing above the check block prints.
2. No input() in this file.
3. Do not modify the argument unless the contract says you may.
4. Look up syntax only when a name is missing; 5 minutes maximum, then ask.
5. The check block at the bottom is the acceptance test. Do not edit it.

THE POINT: five functions, five nights. Each one is a NEW shape of a skill you
already used - not a copy of the drill. If one of them feels familiar, that is
the spaced repetition working; if one feels impossible, that is this week
pointing at the night you should re-read.

    function 1  Day 1  lists, loops, tuples, edge cases
    function 2  Day 2  dicts, sorted(), the key as a ruler
    function 3  Day 3  sets for "in?", lists for order
    function 4  Day 4  files, strip/split/lower, counting
    function 5  Day 5  raising, line numbers, `from exc`

LOAD: 5 functions, about 40-50 minutes. Each function carries a CORE IDEA
line - read it before you type. Stuck 5 minutes after reading it? Ask.
"""


# CORE IDEA: one pass, one memory. Keep the run you are currently building and
# start a new one only when the item changes - that is why "a b a" is THREE
# runs of one, not one run of two. The item and its count travel together as a
# tuple, so the answer is a list of (item, count) pairs.
def compress_runs(items):
    if items==[]:
        return []
    else:
        result=[]
        cur=items[0]
        count=0
        for i in items:
            if cur==i:
                count+=1
            else:
                result.append((cur,count))
                cur=i
                count=1
            
    result.append((cur,count))           
    return result  

    """Return [(item, count), ...] collapsing runs of equal neighbours.

    Order is preserved and only NEIGHBOURS merge: "a a b a" has three runs.
    An empty list returns []. Do not change the input list.

    compress_runs([])                  -> []
    compress_runs(["a"])               -> [("a", 1)]
    compress_runs(["a", "a", "b"])     -> [("a", 2), ("b", 1)]
    compress_runs(["a", "b", "a"])     -> [("a", 1), ("b", 1), ("a", 1)]
    """
    raise NotImplementedError("compress_runs")


# CORE IDEA: a dict has no order to rely on, so the sorting has to happen
# INSIDE each value before you hand the dict back. `sorted` compares the
# strings themselves here - there is no key function to write - and Python
# compares them by character code, so "B" comes before "a".
def group_by_length(words):
    if words==[]:
        return {}
    else:
        result={}
        word=sorted(words)
        for i in word:
            if len(i) not in result:
                result[len(i)]=[]
            result[len(i)].append(i)
            
        return result

            
        
            

    """Return {length: [word, ...]} with every group sorted alphabetically.

    Case is kept as given. Duplicate words stay - each group is a list, not a
    set. An empty input returns {}. Do not change the input list.

    group_by_length([])                   -> {}
    group_by_length(["bb", "a", "cc"])    -> {2: ["bb", "cc"], 1: ["a"]}
    group_by_length(["b", "B"])           -> {1: ["B", "b"]}
    """
    raise NotImplementedError("group_by_length")


# CORE IDEA: a set answers "is it in there?" in one step but forgets order; a
# list remembers order but scans. Use both - a set for the membership test, a
# list for the answer - and the "seen" set is also what stops a duplicate
# appearing twice.
def missing_from(first, second):
    keep=set(first)
    throw=set(second)
    return sorted(keep - throw)
    """Return the items of first that are not in second, in first's order.

    Each item appears at most once, at the position of its FIRST occurrence in
    first. second may be any collection (list, set, tuple). Return a list.

    missing_from(["a", "b", "c"], ["b"])     -> ["a", "c"]
    missing_from(["a", "a", "b"], [])        -> ["a", "b"]
    missing_from([], ["a"])                  -> []
    missing_from(["a", "b"], ["a", "b", "c"]) -> []
    """
    raise NotImplementedError("missing_from")


# CORE IDEA: the file gives you LINES, not words. Strip the newline, split on
# whitespace, lower the case, then count - one canonical form, so "One" and
# "one" are the same word. And do not catch FileNotFoundError: you cannot fix
# a missing path in here, so let it crash.
def word_counts(path):
    with open(path,'r') as f:
        result={}
        for line in f:
            content=line.lower().split()
            for i in content:
                result[i]=result.get(i,0)+1
        return result


    
    """Return {word: count} for the words in a file, lowercased.

    Read the file line by line; split each line on whitespace; count every
    word after .lower(). Blank lines contribute nothing. A missing file is NOT
    handled - FileNotFoundError reaches the caller.

    file "One two\\n\\none\\n" -> {"one": 2, "two": 1}
    file ""                  -> {}
    """
    raise NotImplementedError("word_counts")


# CORE IDEA: the message is the API. The line number says WHERE, repr(value)
# says WHAT, and `raise ValueError(...) from exc` keeps the original cause in
# the traceback instead of hiding it behind your own exception.
def parse_config(text):
    if text=='':
        return {}
    else:
        result={}
        lines=text.split('\n')
        for lineno,line in enumerate(lines,1):
            line=line.strip()
            if line == '' or line.startswith('#'):
                continue
            if '=' not in line:
                raise ValueError(f"line {lineno} doesnt have '='")
            else:
                key,value=line.split('=',1)
                try:
                    result[key.strip()]=int(value.strip())
                except ValueError as exc:
                    raise ValueError(f'naming{value!r}is not a available value') from exc
    return result

    """Return a dict of int settings parsed from "key=value" lines.

    Skip blank lines and lines starting with "#". Split each line on the FIRST
    "=" only, and strip both halves. A line with no "=" raises ValueError
    naming the line number (1-based, blank lines counted). A value that is not
    an int raises ValueError naming repr(value), with the original exception
    attached using `from exc`.

    parse_config("a=1\\n\\n# note\\nb = 2\\n") -> {"a": 1, "b": 2}
    parse_config("")                       -> {}
    parse_config("a=1\\nnoequal\\n")         -> ValueError naming "line 2"
    parse_config("a=x\\n")                  -> ValueError naming 'x'
    """
    raise NotImplementedError("parse_config")


# --------------------------------------------------------------------------
# CHECKS - do not edit below this line
# --------------------------------------------------------------------------
if __name__ == "__main__":
    import pathlib
    import tempfile

    # 1. compress_runs - Day 1
    assert compress_runs([]) == []
    assert compress_runs(["a"]) == [("a", 1)]
    assert compress_runs(["a", "a", "b"]) == [("a", 2), ("b", 1)]
    assert compress_runs(["a", "b", "a"]) == [("a", 1), ("b", 1), ("a", 1)]
    assert compress_runs(["x", "x", "x", "x"]) == [("x", 4)]
    assert isinstance(compress_runs(["a", "a"])[0], tuple), "a run is a tuple"

    # 2. group_by_length - Day 2
    assert group_by_length([]) == {}
    assert group_by_length(["bb", "a", "cc"]) == {2: ["bb", "cc"], 1: ["a"]}
    assert group_by_length(["b", "B"]) == {1: ["B", "b"]}, "sorted is ASCII order"
    assert group_by_length(["aaa", "b"]) == {3: ["aaa"], 1: ["b"]}
    assert group_by_length(["dd", "cc", "bb"]) == {2: ["bb", "cc", "dd"]}, "each group is sorted"

    # 3. missing_from - Day 3
    assert missing_from(["a", "b", "c"], ["b"]) == ["a", "c"]
    assert missing_from(["a", "a", "b"], []) == ["a", "b"]
    assert missing_from([], ["a"]) == []
    assert missing_from(["a", "b"], ["a", "b", "c"]) == []
    assert missing_from(["b", "a", "b"], {"a"}) == ["b"], "order of first, no duplicates"

    # 4. word_counts - Day 4
    with tempfile.TemporaryDirectory() as tmp:
        mixed = pathlib.Path(tmp) / "mixed.txt"
        mixed.write_text("One two\n\none\n", encoding="utf-8")
        assert word_counts(mixed) == {"one": 2, "two": 1}

        empty = pathlib.Path(tmp) / "empty.txt"
        empty.write_text("", encoding="utf-8")
        assert word_counts(empty) == {}

        spaced = pathlib.Path(tmp) / "spaced.txt"
        spaced.write_text("  a\tb  \n\nb\n", encoding="utf-8")
        assert word_counts(spaced) == {"a": 1, "b": 2}

        try:
            word_counts(pathlib.Path(tmp) / "missing.txt")
            assert False, "a missing file must raise FileNotFoundError"
        except FileNotFoundError:
            pass

    # 5. parse_config - Day 5
    assert parse_config("a=1\n\n# note\nb = 2\n") == {"a": 1, "b": 2}
    assert parse_config("") == {}

    try:
        parse_config("a=1\nnoequal\n")
        assert False, "a line without '=' must raise"
    except ValueError as exc:
        assert "line 2" in str(exc), "the message must name the line number"

    try:
        parse_config("a=x\n")
        assert False, "a value that is not an int must raise"
    except ValueError as exc:
        assert "'x'" in str(exc), "the message must name repr(value)"
        assert exc.__cause__ is not None, "attach the original with `from exc`"

    try:
        parse_config("k=v=w\n")
        assert False, "only the first '=' splits"
    except ValueError as exc:
        assert "'v=w'" in str(exc), "the whole value is 'v=w'"

    print("all drills pass")
