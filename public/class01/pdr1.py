"""
pdr1.py
This script should use pandas-datareader to get prices from google.com.

Demo:
conda install pandas-datareader
~/anaconda3/bin/python pdr1.py
"""

# pandas_datareader depends on shell command:
# conda install pandas-datareader

import pandas_datareader as pdr
import datetime
import pdb

# I should stop the script here and start the debugger:
pdb.set_trace()

start_dt  = datetime.datetime(2016,  1,  1)
end_dt    = datetime.datetime(2026, 12, 31)
prices_df = pdr.DataReader('IBM', 'google', start_dt, end_dt)
print(prices_df.head())

# I should write the prices to a CSV file in /tmp:
prices_df.to_csv('/tmp/prices_ibm.csv', float_format='%4.3f')

# I should end the script with a simple string which might be a
# convenient breakpoint for the debugger:

'bye'
