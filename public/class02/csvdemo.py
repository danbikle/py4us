"""
csvdemo.py

This script should show-how-to use the CSV module to read a CSV file.

Ref:
https://docs.python.org/3/library/csv.html

Demo:
python csvdemo.py
"""

import csv
with open('some.csv') as f:
  csv_l = [row for row in csv.reader(f)]
print(csv_l)

