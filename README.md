# patch-compliance-reporter

Check which hosts are overdue for patching from a CSV of last-patch dates, against a maximum patch age in days.

## How to run

```sh
python3 main.py hosts.csv --max-age-days 30
```

## Example output

```
web01: COMPLIANT (9 days since patch)
db01: OVERDUE (89 days since patch)
1/2 host(s) overdue.
```

Standard library only. Run the tests with `python3 -m unittest discover`.
