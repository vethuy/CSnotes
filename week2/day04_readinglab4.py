"""Week 2 . Day 4 . reading lab 4 - csv.DictReader  (Lib/csv.py:145).

WHAT THIS LAB IS
----------------
You read one small class in the standard library, then close the file and
rebuild its shape from memory. Simplified is fine. Do not import the module you
are rewriting and do not paste from it.

LAST 3 MINUTES OF THE LAB: write the body below, from memory, then run the
check. If the check fails, do not reopen the source - read the error and think.

RUN THE CHECK:   python week2/day04_readinglab4.py
"""


def my_dict_reader(lines):
    """Turn CSV lines into a list of dicts: first line = header.

    No quoting support. Rows must have as many fields as the header.
    my_dict_reader(["a,b", "1,2", "3,4"]) -> [{"a": "1", "b": "2"}, {"a": "3", "b": "4"}]
    """
    raise NotImplementedError("my_dict_reader")


# --------------------------------------------------------------------------
# CHECK - do not edit below this line
# --------------------------------------------------------------------------
if __name__ == "__main__":
    assert my_dict_reader(["a,b", "1,2", "3,4"]) == [
        {"a": "1", "b": "2"},
        {"a": "3", "b": "4"},
    ]
    assert my_dict_reader([]) == []

    print("rewrite 4 passes")
