"""Reading lab 2 - a real snippet from CPython's standard library.

Source: CPython 3.13, Lib/_pydatetime.py, lines 39-73
        (the pure-Python version of datetime.date).
I did not write this code. I am reading it, not copying it.

How to use (30 minutes, ladder steps 1 + 2):
  1. Read everything below the header WITHOUT running it.
  2. Write your predictions for the 5 questions at the bottom of this file
     into reading-notes.md.
  3. Only then run:  python day05_reading2.py
  4. Make the trace table for the module-level for loop (dbm, dim).

Question I should be able to answer afterwards:
   why does _days_before_month return a number when the last part is a
   True/False test?
"""

# -1 is a placeholder for indexing purposes.
_DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

_DAYS_BEFORE_MONTH = [-1]  # -1 is a placeholder for indexing purposes.
dbm = 0
for dim in _DAYS_IN_MONTH[1:]:
    _DAYS_BEFORE_MONTH.append(dbm)
    dbm += dim
del dbm, dim


def _is_leap(year):
    "year -> 1 if leap year, else 0."
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def _days_before_year(year):
    "year -> number of days before January 1st of year."
    y = year - 1
    return y*365 + y//4 - y//100 + y//400


def _days_in_month(year, month):
    "year, month -> number of days in that month in that year."
    assert 1 <= month <= 12, month
    if month == 2 and _is_leap(year):
        return 29
    return _DAYS_IN_MONTH[month]


def _days_before_month(year, month):
    "year, month -> number of days in year preceding first day of month."
    assert 1 <= month <= 12, 'month must be in 1..12'
    return _DAYS_BEFORE_MONTH[month] + (month > 2 and _is_leap(year))


def _ymd2ord(year, month, day):
    "year, month, day -> ordinal, considering 01-Jan-0001 as day 1."
    assert 1 <= month <= 12, 'month must be in 1..12'
    dim = _days_in_month(year, month)
    assert 1 <= day <= dim, ('day must be in 1..%d' % dim)
    return (_days_before_year(year) +
            _days_before_month(year, month) +
            day)


# ---------------------------------------------------------------- predict 5
# Write these in reading-notes.md BEFORE running the file.

# __name__ is "__main__" only when Python runs THIS file; on import it is
# "day05_reading2", so the guard below is a launch-mode switch, not a self-test.
if __name__ == "__main__":
    print("1) whole list _DAYS_BEFORE_MONTH =",
          _DAYS_BEFORE_MONTH)
    print("2) _days_before_year(2024) =", _days_before_year(2024))
    print("3) _days_before_month(2024, 3) =", _days_before_month(2024, 3),
          "   _days_before_month(2023, 3) =", _days_before_month(2023, 3))
    print("4) _ymd2ord(2024,11,11) - _ymd2ord(2024,11,1) =",
          _ymd2ord(2024, 11, 11) - _ymd2ord(2024, 11, 1))
    print("5) _days_in_month(1900, 2) =", _days_in_month(1900, 2),
          "   _days_in_month(2024, 2) =", _days_in_month(2024, 2))
