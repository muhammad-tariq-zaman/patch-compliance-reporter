"""Report patch compliance from a CSV (host,last_patch_date) against a max age.

Usage: python3 main.py hosts.csv --max-age-days 30 --today 2026-10-29
Dates must be ISO format, e.g. 2026-09-15.
"""
import argparse
import csv
import sys
from datetime import date


def status(last_patch, today, max_age):
    age = (today - last_patch).days
    return age, ("COMPLIANT" if age <= max_age else "OVERDUE")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="CSV with host,last_patch_date columns")
    parser.add_argument("--max-age-days", type=int, default=30)
    parser.add_argument("--today", default=None, help="Reference date YYYY-MM-DD (default: today)")
    args = parser.parse_args(argv)
    today = date.fromisoformat(args.today) if args.today else date.today()
    overdue = 0
    with open(args.path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        age, state = status(date.fromisoformat(row["last_patch_date"]), today, args.max_age_days)
        overdue += state == "OVERDUE"
        print(f"{row['host']}: {state} ({age} days since patch)")
    print(f"{overdue}/{len(rows)} host(s) overdue.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
