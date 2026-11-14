# Python basics — reference

Lookup page, not a lesson. Find the section, read the line, close it, type.
Everything here is standard library — Python 3.13.

---

## 1. Syntax sheet

```python
x = 1                     # assignment
a, b = 1, 2               # unpacking
a, b = b, a               # swap
x += 1                    # augmented: += -= *= /= //= %= **=

if cond:                  # colon + indentation, 4 spaces
    ...
elif other:
    ...
else:
    ...

for i in range(3):        # iterate values
    ...
while cond:               # loop until false
    ...
break                     # leave the loop
continue                  # skip to the next iteration

def f(a, b=2):            # function, default argument
    """docstring: contract."""
    return a + b

try:
    ...
except ValueError as exc:
    ...
else:                     # no exception happened
    ...
finally:                  # always runs
    ...

with open("f.txt", encoding="utf-8") as fh:   # closes itself
    ...

import csv                 # module
from pathlib import Path   # one name
import numpy as np         # alias

# comment
"""block
docstring/comment"""
```

True / False / None (capitalised). `#` for comments, `"""` for docstrings.

---

## 2. Types and conversion

| Type | Literal | Convert | Check |
|---|---|---|---|
| `int` | `42`, `-7`, `0b1010` | `int(x)` | `isinstance(x, int)` |
| `float` | `3.5`, `1e3`, `.5` | `float(x)` | `isinstance(x, float)` |
| `complex` | `1+2j` | `complex(x)` | — |
| `str` | `"hi"`, `'hi'`, `"""…"""` | `str(x)` | `isinstance(x, str)` |
| `bool` | `True`, `False` | `bool(x)` | `isinstance(x, bool)` |
| `list` | `[1, 2]` | `list(x)` | `isinstance(x, list)` |
| `tuple` | `(1, 2)`, `1, 2` | `tuple(x)` | `isinstance(x, tuple)` |
| `dict` | `{"a": 1}` | `dict(x)` | `isinstance(x, dict)` |
| `set` | `{1, 2}`, `set()` | `set(x)` | `isinstance(x, set)` |
| `NoneType` | `None` | — | `x is None` |

Conversions that fail raise `ValueError`: `int("abc")`, `int("1.5")`,
`float("1,5")`. `int(" 12 ")` works; `int("12\n")` works.

**Falsy values:** `False`, `None`, `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `()`.
Everything else is truthy — including `"0"`, `[0]`, `"False"`.

`bool` is a subclass of `int`: `True + True == 2`, `True == 1`.

---

## 3. Operators

| Operator | Meaning | Note |
|---|---|---|
| `+ - * /` | arithmetic | `/` always returns a float |
| `//` | floor division | `7 // 2 == 3`, `-7 // 2 == -4` |
| `%` | remainder | wraps: `-1 % 26 == 25` |
| `**` | power | `2 ** 10 == 1024` |
| `== != < <= > >=` | comparison | chained: `0 <= x <= 10` |
| `and or not` | logic | returns an *operand*, not a bool |
| `in`, `not in` | membership | on str, list, dict (keys), set |
| `is`, `is not` | same object | use `is None` |
| `x if cond else y` | conditional value | not a statement |

Precedence: `**` → `* / // %` → `+ -` → comparisons → `not` → `and` → `or`.

Floats are approximations: `0.1 + 0.2 == 0.30000000000000004`. Compare with
`abs(a - b) < 1e-9` or `math.isclose`. Display with `f"{x:.2f}"`.

---

## 4. Built-in functions

| Function | Does |
|---|---|
| `print(*args, sep=" ", end="\n")` | write to stdout |
| `len(x)` | number of items / characters |
| `type(x)` | class of the object |
| `isinstance(x, T)` | isinstance check (accepts a tuple of types) |
| `int/float/str/bool/list/tuple/dict/set(x)` | convert |
| `range(start, stop, step)` | numbers, stop excluded |
| `enumerate(seq, start=0)` | `(index, value)` pairs |
| `zip(a, b, ...)` | tuples of parallel items, stops at the shortest |
| `sorted(seq, key=..., reverse=False)` | NEW sorted list, stable |
| `reversed(seq)` | iterator in reverse |
| `sum(seq)`, `min(seq)`, `max(seq)` | aggregates (`default=` on min/max) |
| `abs(x)`, `round(x, n)` | absolute value, rounding |
| `any(seq)`, `all(seq)` | truth tests |
| `map(f, seq)`, `filter(p, seq)` | lazy transforms / selections |
| `open(path, mode, encoding=...)` | file handle |
| `repr(x)`, `str(x)` | debugging view, display view |
| `help(x)`, `dir(x)` | docs, attribute list |
| `id(x)`, `hash(x)` | object identity, hash value |
| `chr(n)`, `ord(s)` | 97 ↔ `"a"` |
| `divmod(a, b)` | `(a // b, a % b)` |
| `pow(a, b, mod)` | power, optional modulus |
| `input(prompt)` | read a line, **always returns str** |
| `format(x, spec)` | same as the inside of an f-string |

---

## 5. Strings — immutable

```python
s = "Hello, World"
s[0]      # "H"        s[-1]     # "d"
s[0:5]    # "Hello"    s[:5]     # "Hello"     s[5:]  # ", World"
s[::-1]   # "dlroW ,olleH"                     s[::2] # every other char
len(s)    # 12         "World" in s  # True
```

| Method | Result |
|---|---|
| `s.upper()` / `s.lower()` | case copy |
| `s.strip()` / `lstrip` / `rstrip` | trim whitespace (or given chars) |
| `s.split(sep)` | list; `s.split()` on whitespace drops empties |
| `s.splitlines()` | no newlines kept |
| `sep.join(iterable)` | `"-".join(["a","b"]) → "a-b"` |
| `s.replace(old, new, count=-1)` | copy with replacements |
| `s.find(sub)` | index or `-1` |
| `s.index(sub)` | index or **`ValueError`** |
| `s.count(sub)` | occurrences |
| `s.startswith(p)` / `endswith(p)` | bool (accepts a tuple of prefixes) |
| `s.isdigit()` / `isalpha()` / `isspace()` | character-class tests |
| `s.zfill(n)` | `"7".zfill(3) → "007"` |
| `s.removeprefix(p)` / `removesuffix(p)` | 3.9+, no error if absent |
| `s.title()` / `capitalize()` | case helpers |

**Formatting (f-strings):**

```python
name, x = "ann", 3.14159
f"{name} is {x:.2f}"      # ann is 3.14
f"{x:8.3f}"               # right-aligned in 8 columns
f"{x:<8.3f}"  f"{x:^8.3f}"  # left, centred
f"{n:08.2f}"              # zero-padded
f"{1234567:,}"            # 1,234,567
f"{x!r}"                  # repr: quotes visible
f"{'yes' if ok else 'no'}"
f"{d['k']}"               # same quotes inside: f"{d["k"]}" is 3.12+
```

Old style also exists: `"%s = %.2f" % (name, x)`; prefer f-strings.

`str` is immutable: `s[0] = "h"` is a `TypeError`; build a new string instead.

---

## 6. Lists — ordered, mutable

```python
nums = [3, 1, 2]
nums.append(4)          # end
nums.extend([5, 6])     # several at once (or nums += [5, 6])
nums.insert(0, 9)       # at index
nums.remove(3)          # by VALUE, raises ValueError if absent
nums.pop()              # last, returns it; nums.pop(i) by index
nums.index(2)           # position, raises ValueError
nums.count(2)           # occurrences
nums.sort()             # in place, returns None
nums.sort(key=len, reverse=True)
nums.reverse()          # in place
nums.copy()             # shallow copy (same as nums[:] or list(nums))
len(nums)  sum(nums)  min(nums)  max(nums)  sorted(nums)
3 in nums               # O(n) scan
```

- Indexing `nums[0]`, `nums[-1]`; slicing `nums[a:b]` (stop excluded), `nums[::2]`.
- Out of range → `IndexError`.
- `b = a` aliases; `b = a[:]` copies.
- Deleting while looping skips items — loop over a copy (`for x in nums[:]:`)
  or build a new list.

---

## 7. Tuples — ordered, immutable

```python
point = (3, 4)
x, y = point              # unpacking
a, b = b, a               # swap
single = (5,)             # the comma makes the tuple
t[0], t[-1], len(t), t + (6,)   # no append / no item assignment
```

Returned by `enumerate`, `zip`, `dict.items()`, `divmod`, `str.partition`.
Hashable if its contents are — so a tuple can be a dict key or a set member,
a list cannot. Named tuples: `from collections import namedtuple`.

---

## 8. Dicts — key → value, insertion ordered

```python
d = {"a": 1, "b": 2}
d["c"] = 3                # add / overwrite
d["a"]                    # KeyError if missing
d.get("z")                # None if missing
d.get("z", 0)             # default if missing
d["a"] = d.get("a", 0) + 1     # counting idiom
"a" in d                  # tests KEYS
del d["a"]                # raises KeyError if absent
```

| Method | Result |
|---|---|
| `d.keys()` / `.values()` / `.items()` | live **views**, not lists |
| `d.pop(k[, default])` | remove and return |
| `d.popitem()` | last inserted pair, LIFO |
| `d.update(other)` | merge, right side wins |
| `d.setdefault(k, v)` | value for `k`, inserting `v` if absent |
| `d.copy()` | shallow copy |
| `d.clear()` | empty it |
| `dict.fromkeys(seq, v)` | keys from a sequence |

```python
for k, v in d.items(): ...
sorted(d)                              # sorted KEYS
sorted(d.items(), key=lambda kv: kv[1], reverse=True)   # by value
{k: v for k, v in d.items() if v > 1}  # filtered copy
```

Dicts keep insertion order (3.7+). You cannot sort a dict — you sort its items.
Keys must be hashable (str, int, tuple ok; list not).

---

## 9. Sets — unordered, unique, hashable members

```python
s = set()                 # {} is an EMPTY DICT
s = {1, 2, 3}
s.add(4)                  # not append
s.remove(2)               # KeyError if absent
s.discard(2)              # no error if absent
s.pop()                   # arbitrary element
1 in s                    # O(1)
```

| Expression | Meaning |
|---|---|
| `a & b` / `a.intersection(b)` | in both |
| `a \| b` / `a.union(b)` | in either |
| `a - b` / `a.difference(b)` | in `a`, not `b` |
| `a ^ b` / `symmetric_difference` | in exactly one |
| `a <= b` / `a.issubset(b)` | every element of `a` is in `b` |
| `a >= b` / `a.issuperset(b)` | contains all of `b` |
| `a.isdisjoint(b)` | no common elements |

No order, no indexing (`s[0]` fails). Printing order is not something to rely
on — `sorted(s)` when the order must be stable. `frozenset` is the immutable
version, and the only one that can be a dict key.

**Choosing:** order matters → `list`; fixed record → `tuple`; "which different
ones"/fast `in` → `set`; "how many"/lookup by name → `dict`.

---

## 10. Control flow

```python
if 0 <= score <= 100:     # chained comparison
    ...
elif score > 100:         # elif already means "and not the above"
    ...
else:
    ...
```

- Order branches most-specific first, or an earlier branch makes a later one
  unreachable (`i % 3 == 0` before `i % 15 == 0` kills the FizzBuzz case).
- `and` / `or` short-circuit and return an operand: `x and y` is `y` if `x` is
  truthy, else `x`.
- `range(a, b)` excludes `b`; `range(1, 6)` is 1–5. `range(5, 0, -1)` counts down.
- `for` when the count is known, `while` when it is not.
- `break` exits the loop, `continue` skips the rest of the current iteration.
- Loop `else:` runs only if the loop was not broken — rarely used, easy to misread.

---

## 11. Functions

```python
def area(width, height=1):
    """Return width * height.

    area(3)    -> 3
    area(3, 2) -> 6
    """
    return width * height

area(3, 2)          # positional
area(width=3, height=2)   # keyword
```

- No `return` → returns `None`.
- Defaults are evaluated **once** at definition; never use a mutable default
  (`def f(items=[])`) — use `None` and build inside.
- Names assigned inside a function are local; reading a global works, writing
  needs `global` (avoid it — pass and return instead).
- `def f(*args, **kwargs)` collects extras; `f(*[1,2])` unpacks into a call.
- `lambda x: x * 2` is a one-expression anonymous function — mostly for `key=`.
- A docstring is the contract: inputs, output, whether arguments change.

---

## 12. Comprehensions

```python
[f(x) for x in xs]                  # list
[f(x) for x in xs if p(x)]          # with filter
[f(x) if p(x) else g(x) for x in xs]   # conditional VALUE, before the for
{x: v for k, v in pairs}            # dict
{x for x in xs}                     # set
sum(x for x in xs)                  # generator, no list built
```

Read them inside-out: the `for` is the loop, everything before it is the body.
Nested: `[x for row in grid for x in row]` flattens. If the body needs two
statements, write a normal loop.

---

## 13. Iteration and sorting

```python
for i, x in enumerate(xs, start=1): ...
for a, b in zip(xs, ys): ...
for k, v in d.items(): ...
for line in open(path, encoding="utf-8"): ...   # prefer `with`

sorted(xs)                                  # new sorted list
sorted(xs, reverse=True)
sorted(words, key=len)
sorted(words, key=str.lower)
sorted(d.items(), key=lambda kv: (-kv[1], kv[0]))   # count desc, then name
xs.sort(key=...)                            # in place, returns None
```

`sorted` is **stable**: equal keys keep their original order. `min`/`max` also
take `key=`.

---

## 14. Files and paths

```python
from pathlib import Path

p = Path("data") / "sessions.json"          # join with /
p.parent.mkdir(parents=True, exist_ok=True) # create missing folders
p.exists()   p.is_file()   p.name   p.stem   p.suffix

text = p.read_text(encoding="utf-8")
p.write_text("hi\n", encoding="utf-8")

with open(p, encoding="utf-8") as fh:       # read line by line
    for line in fh:
        row = line.strip()                  # "\n" is still attached
```

- `open(p, "w")` truncates; `open(p, "a")` appends; default is `"r"`.
- `with` closes the handle even if the body raises.
- Relative paths resolve against the **current working directory**, not the
  script: `Path(__file__).resolve().parent` is the script's own folder.
- Writing into a missing folder raises `FileNotFoundError` — `mkdir` first.

---

## 15. CSV and JSON

```python
import csv

with open(p, newline="", encoding="utf-8") as fh:
    for row in csv.reader(fh):            # list of strings
        ...
    for row in csv.DictReader(fh):        # dict per row, keys = header
        ...

with open(p, "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=["name", "age"])
    w.writeheader(); w.writerow({"name": "ann", "age": 30})
```

`DictReader`: a short row gives `None` for the missing field; a long row puts
extras under the key `None`. Neither raises.

```python
import json

obj = json.loads(text)          # str  -> object
text = json.dumps(obj, indent=2)
with open(p, encoding="utf-8") as fh:
    obj = json.load(fh)
json.dump(obj, fh, indent=2)
```

JSON types map to `dict / list / str / int / float / bool / None`. Trailing
commas and single quotes are errors — always write with `json.dump`.

---

## 16. Errors

```python
try:
    n = int(text)
except ValueError as exc:
    print("bad number:", exc)
else:
    print("ok", n)
finally:
    print("done")
```

| Exception | Cause |
|---|---|
| `SyntaxError` | the file does not parse (often a missing `:` or bracket) |
| `NameError` | name used before assignment, or missing import |
| `TypeError` | wrong type (`"1" + 1`, calling a non-function) |
| `ValueError` | right type, bad value (`int("abc")`) |
| `IndexError` | list/string index out of range |
| `KeyError` | missing dict key |
| `AttributeError` | the object has no such attribute (`str.appnd`) |
| `ZeroDivisionError` | division by zero |
| `FileNotFoundError` | path does not exist (wrong folder is the usual cause) |
| `UnboundLocalError` | local name used before assignment (often after a failed `try`) |
| `RecursionError` | function calls itself forever |
| `json.JSONDecodeError` | malformed JSON (subclass of `ValueError`) |

Rules: catch the **narrowest** type; a bare `except:` swallows typos and
Ctrl-C. `raise ValueError(f"bad: {text!r}")` names the offending value.
Functions **raise**, the caller decides what to print. `assert cond, "msg"` is
for internal assumptions only (`python -O` removes it).

Read a traceback bottom-up: last line = type + message, the line above = where,
and each `File "…", line N` is one step in the call path.

---

## 17. Modules worth knowing

```python
import math                     # sqrt, floor, ceil, pi, isclose
import random                   # randint(a,b), choice(seq), shuffle(lst), seed(n)
import sys                      # argv, exit(code), path
import os                       # getcwd(), listdir(), makedirs()
from datetime import date, datetime, timedelta
from collections import Counter, defaultdict
```

```python
date.today()                    # 2026-11-14
date.fromisoformat("2026-11-14")   # ValueError on bad text
d2 - d1                         # timedelta
(td).days                       # int
d.strftime("%Y-%m-%d")          # format
datetime.now()

Counter("aab")                  # Counter({'a': 2, 'b': 1})
c.most_common(2)                # [('a', 2), ('b', 1)]
c["a"] += 1                     # counts missing keys as 0

defaultdict(list)               # d[key].append(x) without KeyError
```

`__name__` is `"__main__"` only when the file is run directly; `if __name__ ==
"__main__":` keeps import side effects out. `sys.argv` is the command line
(`sys.argv[0]` is the script); `sys.exit(1)` ends with a failure code.

---

## 18. Recipes

```python
# count characters
counts = {}
for ch in text:
    counts[ch] = counts.get(ch, 0) + 1

# dedupe, keep first-seen order
seen, out = set(), []
for x in nums:
    if x not in seen:
        seen.add(x); out.append(x)

# group by a key
groups = {}
for item in items:
    groups.setdefault(item["topic"], []).append(item)

# sum by category
totals = {}
for row in rows:
    totals[row["cat"]] = totals.get(row["cat"], 0) + row["amount"]

# top n of a dict
sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:n]

# rank with alphabetical ties
sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))

# read a file into stripped, non-empty lines
lines = [ln.strip() for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip()]

# flatten one level
flat = [x for row in grid for x in row]

# safe int
def safe_int(text, default=None):
    try:
        return int(text)
    except (TypeError, ValueError):
        return default
```

---

## 19. Fast lookups

```powershell
python -c "help(str.split)"      # signature + one example
python -c "import csv, inspect; print(inspect.getsource(csv.DictReader))"
python -c "import sys; print(sys.version)"
python -m json.tool file.json     # pretty-print / validate JSON
python -m pydoc csv               # module docs in a pager
```

```python
help(x)        # docs for a function/class/module
dir(x)         # every attribute name
```

Stop rule: 5 minutes. One question, one answer, close the page.

---

## 20. Git, in five commands

```powershell
git status                     # what changed
git add .                      # stage everything
git commit -m "feat: thing"    # one logical change
git push                       # upload
git log --oneline --graph -10  # history
```

Prefixes: `feat:` new behaviour · `fix:` repairs a wrong answer · `docs:` prose
only. `fetch first` → `git pull --rebase`, then push. Never force-push.
