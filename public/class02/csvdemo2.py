"""
csvdemo2.py

This script should show-how-to use the CSV module to read a CSV file.
And with requests.

Ref:
http://docs.python-requests.org/en/master/user/quickstart/#make-a-request
https://docs.python.org/3/library/csv.html

Demo:
python csvdemo2.py
"""

import csv
import io
import requests

csv_req = requests.get('http://py4.us/some.csv')
s_io    = io.StringIO(csv_req.text)
csv_l   = [row for row in csv.reader(s_io)]
print(csv_l)


