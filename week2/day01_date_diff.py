"""Week 2 . Day 1 . day01_date_diff.py (week1/day05_days_between.py, refactored).

RUN THE PROGRAM:   python week2/day01_date_diff.py
RUN THE CHECKS:    python week2/day01_date_diff.py --check

REQUIREMENTS
------------
Behaviour is week-1 day05 with the main(0) counter removed.

* Read two dates from the user, in any order; print the gap in days.
* A date the program cannot parse prints a message and asks again.
  The program never exits because of bad input.
* parse_date, days_between and describe RETURN values and print nothing.
  main() owns every print() and every input().
* --check runs the checks and exits without asking for input.

CHECKS
------
python week2/day01_date_diff.py --check   prints "all checks pass"
"""

import sys
from datetime import date

DATE_FORMAT_HINT = "YYYY-MM-DD"


def parse_date(text):
    """Return a datetime.date for text in YYYY-MM-DD form, else None.

    Surrounding whitespace is ignored. Nothing is printed here and no
    exception escapes: an unparsable text simply returns None.

    parse_date("2026-11-09")   -> date(2026, 11, 9)
    parse_date(" 2026-11-09 ") -> date(2026, 11, 9)
    parse_date("2026-13-01")   -> None
    parse_date("9 Nov 2026")   -> None
    """
    raise NotImplementedError("parse_date")


def days_between(first, second):
    """Return the gap in days between two dates as a non-negative int.

    days_between(date(2026, 11, 9), date(2027, 1, 3)) -> 55
    days_between(date(2027, 1, 3), date(2026, 11, 9)) -> 55
    days_between(a, a)                                -> 0
    """
    raise NotImplementedError("days_between")


def describe(first, second):
    """Return a one-line description of the two dates.

    Equal dates -> "same date"
    Otherwise   -> "<earlier date in ISO form> is earlier"

    describe(date(2026, 11, 9), date(2027, 1, 3)) -> "2026-11-09 is earlier"
    describe(date(2027, 1, 3), date(2026, 11, 9)) -> "2026-11-09 is earlier"
    describe(date(2026, 11, 9), date(2026, 11, 9))-> "same date"
    """
    raise NotImplementedError("describe")


def main():
    """Ask for two dates, then print the gap and the description.

    Loop until both parse. For a bad date print one line naming the text and
    the expected form, then ask again. Print the two dates, the gap in days
    and describe(first, second).

    Example session:
        First date (YYYY-MM-DD): 2026-11-09
        Second date (YYYY-MM-DD): 2027-01-03
        2026-11-09 -> 2027-01-03
        55 days
        2026-11-09 is earlier
    """
    raise NotImplementedError("main")


# --------------------------------------------------------------------------
# CHECKS - do not edit below this line
# --------------------------------------------------------------------------
def run_checks():
    assert parse_date("2026-11-09") == date(2026, 11, 9)
    assert parse_date(" 2026-11-09 ") == date(2026, 11, 9)
    assert parse_date("2026-13-01") is None
    assert parse_date("2026-02-30") is None
    assert parse_date("9 Nov 2026") is None
    assert parse_date("") is None

    assert days_between(date(2026, 11, 9), date(2027, 1, 3)) == 55
    assert days_between(date(2027, 1, 3), date(2026, 11, 9)) == 55
    assert days_between(date(2026, 11, 9), date(2026, 11, 9)) == 0
    assert days_between(date(2024, 2, 28), date(2024, 3, 1)) == 2

    assert describe(date(2026, 11, 9), date(2027, 1, 3)) == "2026-11-09 is earlier"
    assert describe(date(2027, 1, 3), date(2026, 11, 9)) == "2026-11-09 is earlier"
    assert describe(date(2026, 11, 9), date(2026, 11, 9)) == "same date"

    print("all checks pass")


if __name__ == "__main__":
    if "--check" in sys.argv[1:]:
        run_checks()
    else:
        main()
