"""Week 3 . Day 4 . tests as specs: name the edge before you write the body.

RUN THE CHECKS:   python week3/day04_drill04.py

RULES
-----
1. Every function RETURNS its result. Nothing above the check block prints.
2. No input() in this file.
3. Do not modify the argument unless the contract says you may.
4. Look up syntax only when a name is missing; 5 minutes maximum, then ask.
5. The check block at the bottom is the acceptance test. Do not edit it.

THE POINT: a test is a sentence about behaviour, written so a machine can say
"false". The boundary is where the sentence gets interesting: 90 is an A and
89.9 is not, 59 is "0:59" and 60 is "1:00", "yes" is True and "maybe" raises.
Before each body, write the one input a careless version would get wrong.

LOAD: 1 drill, 3 functions, about 25-30 minutes. Read the FUNCTION
INTRODUCTION before you type. Each docstring is the spec; the check block only
samples it.
"""


# FUNCTION INTRODUCTION: chains of `if ... elif ... else` checked top-down are
# the natural shape here - the first true branch wins, so the order high-to-low
# is the whole algorithm.
def grade(score):
    if 0<=score<=100:
        if score>=90:
            return 'A'
        elif score>=80:
            return 'B'
        elif score>=70:
            return 'C'
        elif score>=60:
            return 'D'
        else:
            return 'F'
    else:
        raise ValueError(f"{score} is not an acceptable score")
    """Return the letter grade for a numeric score.

    A is 90 and above, B is 80 and above, C is 70 and above, D is 60 and above,
    F is anything lower. A score below 0 or above 100 is not a grade: raise
    ValueError with a message that names the score.

    score is a number (int or float). Boundaries are inclusive on the high end.

    grade(90)     -> "A"
    grade(89.9)   -> "B"
    grade(100)    -> "A"
    grade(0)      -> "F"
    grade(59.9)   -> "F"
    """
    raise NotImplementedError("grade")


# FUNCTION INTRODUCTION: text.strip().lower() normalises before a membership
# test, so "  YES " and "yes" take the same branch.
def parse_bool(text):
    word=text.lower().strip()
    if word=='true' or word=='yes' or word=='1':
        return True
    elif word=='false' or word=='no' or word=='0':
        return False
    else:
        raise ValueError(f"{text} is not a boolean express")
    
    """
    Return True or False for a yes/no string.

    Case and surrounding spaces are ignored. "true", "yes" and "1" are True;
    "false", "no" and "0" are False. Anything else is not a boolean: raise
    ValueError whose message contains the original text.

    text is a str, never a bool. Return a real bool, not a string.

    parse_bool("true")    -> True
    parse_bool(" YES ")   -> True
    parse_bool("0")       -> False
    parse_bool("no")      -> False
    """
    raise NotImplementedError("parse_bool")


# FUNCTION INTRODUCTION: divmod(total, 60) returns (minutes, seconds) in one
# step - and `:02d` pads a number to two digits inside an f-string.
def format_duration(seconds):
    if seconds<0:
        raise ValueError(seconds,'is not a time')
    elif seconds<3600:
        min,sec=divmod(seconds,60)
        return f"{min}:{sec:02d}"
    else:
        min,sec=divmod(seconds,60)
        hour,minute=divmod(min,60)
        return f"{hour}:{minute:02d}:{sec:02d}"
    

    """Return a clock-style string for a whole number of seconds.

    Under an hour the shape is "M:SS" (minutes unpadded, seconds always two
    digits). An hour or more the shape is "H:MM:SS". A negative number of
    seconds is not a duration: raise ValueError.

    seconds is an int. Do not use datetime; this is divmod and an f-string.

    format_duration(59)      -> "0:59"
    format_duration(60)      -> "1:00"
    format_duration(3599)    -> "59:59"
    format_duration(3600)    -> "1:00:00"
    format_duration(3661)    -> "1:01:01"
    """
    raise NotImplementedError("format_duration")


if __name__ == "__main__":
    assert grade(90) == "A"
    assert grade(100) == "A"
    assert grade(89.9) == "B"
    assert grade(80) == "B"
    assert grade(70) == "C"
    assert grade(69.9) == "D"
    assert grade(60) == "D"
    assert grade(59.9) == "F"
    assert grade(0) == "F"

    for bad in (-1, 101, -0.1):
        try:
            grade(bad)
        except ValueError:
            pass
        else:
            raise AssertionError(f"grade({bad}) should raise ValueError")

    assert parse_bool("true") is True
    assert parse_bool("YES") is True
    assert parse_bool("  Yes  ") is True
    assert parse_bool("1") is True
    assert parse_bool("false") is False
    assert parse_bool("No") is False
    assert parse_bool("0") is False

    try:
        parse_bool("maybe")
    except ValueError as exc:
        assert "maybe" in str(exc)
    else:
        raise AssertionError("parse_bool('maybe') should raise ValueError")
    
    assert format_duration(0) == "0:00"
    assert format_duration(59) == "0:59"
    assert format_duration(60) == "1:00"
    assert format_duration(3599) == "59:59"
    assert format_duration(3600) == "1:00:00"
    assert format_duration(3661) == "1:01:01"
    assert format_duration(86399) == "23:59:59"
    assert format_duration(86400) == "24:00:00"

    try:
        format_duration(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("format_duration(-1) should raise ValueError")

    print("all drills pass")
