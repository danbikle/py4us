"""
pdr1.py
This script should use pandas-datareader to get prices from google.com.
"""

# Line below depends on shell command:
# conda install pandas-datareader

import pandas_datareader as pdr
import datetime

start  = datetime.datetime(2016, 1, 1)
end    = datetime.datetime(2016, 12, 31)
prices = pdr.DataReader("IBM", 'google', start, end)
print(prices.head())
'bye'
