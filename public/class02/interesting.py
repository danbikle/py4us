"""
interesting.py

This script shows some syntax-answers for the Class02 'Interesting' Lab.

Ref:
http://py4.us/cclasses/class02#other

Demo:
git clone https://github.com/danbikle/py4us
cd py4us/public/class02/
~/anaconda3/bin/python interesting.py
"""

import pdb
import pandas as pd
import numpy as np
import io

list0 = [0,1,2,3]
# Create a Tuple from a List
tuple0 = tuple(list0)

# Create a Set from a List
set0 = set(list0)

# Use a Set to get unique items from a List
list1     = [0,1,2,3,3,4,4,5,5]
list_uniq = list(set(list1))

# Create a Pandas Series from a List
series0 = pd.Series(list1)

# Create a Pandas DataFrame, then add a List to it
df0 = pd.DataFrame()
df0['col0'] = list1
df0['col1'] = list1

# Create a NumPy Array from a List
a0 = np.array(list0)

# Write a simple example of the zip() function
list_zip = list(zip(list1,list1))

# Create a dictionary, then create a List from its keys
d0 = {'k1':1, 'k2':'v2', 'k3': [3]}
list_keys = list(d0.keys())

# Create a dictionary, then create a List from its values
list_values = list(d0.values())

# Find all values in list1 which are in list2
list1   = [0,1,2,3,3,4,4,5,5]
list2   = [4,5,5,6,7,7]
set1    = set(list1)
set2    = set(list2)
list_in = list(set1 & set2) # intersection of two sets
# Find all values in list1 which are not in list2
list_notin = list(set1 - set2) # difference of two sets

# Reverse the order of a List
list_rev = list(reversed(list1))

# Sort the items in a List
list_sorted = sorted([9,3,7,4,8,1,6])

# Loop through lines in a text file to create List of strings
with open('/etc/group', 'r') as fh:
    list_str = [line_s for line_s in fh]

# Write a simple example of using loc[] with a Pandas Series
sr0 = pd.Series([10,11,12,13,14,15,16,17,18,19])
sr_booleans = sr0 > 15
sr1 = sr0.loc[sr_booleans]
# Write a simple example of using iloc[] with a Pandas Series
list_ints = [0,3,1,6]
sr2 = sr0.iloc[list_ints]
sr3 = sr0.iloc[5]

# Implicit loc[]:
sr4 = sr0[sr_booleans]
# Implicit iloc[]:
sr5 = sr0[list_ints]

# Describe how loc is different than iloc
print('loc takes booleans, iloc takes integers')

# Write an example of the filter() function
list1         = [0,1,2,3,3,4,4,5,5]
list_filtered = list(filter(lambda x_i: x_i > 2, list1))
# Write an example of the map() function
list_mapped = list(map(lambda x_i: x_i ** 2, list1))

# Write an example of the reduce() function
from functools import reduce
int_reduced = reduce(lambda a_i, b_i: a_i+b_i, list1)

# Write an example of the Pandas apply() function
sr0 = pd.Series([10,11,12,13,14,15,16,17,18,19])
sr6 = sr0.apply(np.sqrt)

# With one line of syntax, square all numbers in a List
list2 = np.square(list1).tolist()

# With one line of syntax, read py4.us/gspc.csv into a DataFrame
gspc_df = pd.read_csv('http://py4.us/gspc.csv')
# Use the CSV module to read a CSV file into a list of lists
import csv
with open('some.csv') as f:
  csv_l = [row for row in csv.reader(f)]
print(csv_l)

# Use modules: CSV, io, and Requests to read py4.us/gspc.csv into a List of Lists
import io
import requests
csv_req = requests.get('http://py4.us/some.csv')
s_io    = io.StringIO(csv_req.text)
csv_l   = [row for row in csv.reader(s_io)]

# Read all filenames from /etc-folder into a list
import glob
list_fn = glob.glob('/etc/*')

'bye'

  

