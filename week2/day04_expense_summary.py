"""Week 2 . Day 4-5 . day04_expense_summary.py

RUN THE PROGRAM:   python week2/day04_expense_summary.py
                   python week2/day04_expense_summary.py week2/data/day04_expenses.csv
RUN THE CHECKS:    python week2/day04_expense_summary.py --check

REQUIREMENTS (Thursday - the build)
-----------------------------------
* load_expenses(path) -> list[dict]: one dict per CSV row with the keys
  date, item, category, amount. amount becomes a float, the rest stay str.
  A missing file raises FileNotFoundError; an amount that is not a number
  raises ValueError whose message contains the offending text. Neither is
  caught here.
* summarize(rows) -> dict category -> total (float). rows is not modified.
* grand_total(totals) -> float: the sum of the totals.
* main() -> None: read the path from sys.argv[1] (default data/day04_expenses.csv),
  print the report, print nothing else.

REPORT FORMAT (judged by eye, not asserted)
-------------------------------------------
    food           32.20
    school         17.24
    transport       9.20
    fun             9.00

    total          67.64
    12 rows

Category lines sorted by total, highest first, ties by name. Name column 12
wide, amounts with two decimals. One blank line before "total".

ADDED FRIDAY (the hardening) - main() only, the functions keep raising
----------------------------------------------------------------------
* FileNotFoundError -> print "Cannot read <path>" to sys.stderr, exit code 1.
* A row with a bad amount -> print one warning naming the file and the text
  to sys.stderr, keep the good rows, exit code 0.
* Do not wrap the helpers in try/except: parse raises, main decides.

CHECKS
------
python week2/day04_expense_summary.py --check   prints "all checks pass"
"""

import csv
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parent / "data"
EXPENSES = DATA / "day04_expenses.csv"
EXPENSES_BAD = DATA / "day05_expenses_bad.csv"


def load_expenses(path):
    """Return the CSV rows as dicts, amount as float, other fields as str."""
    raise NotImplementedError("load_expenses")


def summarize(rows):
    """Return dict category -> total amount."""
    raise NotImplementedError("summarize")


def grand_total(totals):
    """Return the sum of the totals as a float."""
    raise NotImplementedError("grand_total")


def main():
    """Print the per-category report and the grand total."""
    raise NotImplementedError("main")


# --------------------------------------------------------------------------
# CHECKS - do not edit below this line
# --------------------------------------------------------------------------
def run_checks():
    rows = load_expenses(EXPENSES)
    assert len(rows) == 12, f"expected 12 rows, got {len(rows)}"
    assert rows[0]["category"] == "food"
    assert rows[0]["amount"] == 3.5
    assert isinstance(rows[0]["amount"], float)
    assert rows[0]["date"] == "2026-11-16"

    before = [dict(row) for row in rows]
    totals = summarize(rows)
    assert set(totals) == {"food", "transport", "school", "fun"}
    assert round(totals["food"], 2) == 32.20
    assert round(totals["transport"], 2) == 9.20
    assert round(totals["school"], 2) == 17.24
    assert round(totals["fun"], 2) == 9.00
    assert rows[:] == before, "summarize must not modify rows"
    assert len(rows[0]) == 4, "each row keeps exactly 4 fields"

    assert round(grand_total(totals), 2) == 67.64

    try:
        load_expenses(DATA / "no_such_file.csv")
    except FileNotFoundError:
        pass
    else:
        raise AssertionError("load_expenses must let FileNotFoundError escape")

    try:
        load_expenses(EXPENSES_BAD)
    except ValueError as exc:
        assert "3,50" in str(exc), f"message should name the bad text, got {exc}"
    else:
        raise AssertionError("load_expenses must raise ValueError for '3,50'")

    print("all checks pass")


if __name__ == "__main__":
    argv = sys.argv[1:]
    if "--check" in argv:
        run_checks()
    else:
        main()
