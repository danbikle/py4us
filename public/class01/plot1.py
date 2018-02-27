"""
plot1.py

This script should Plot IBM Prices For 2016-11

Demo:
~/anaconda3/bin/python plot1.py
"""

import datetime
import pdb
import matplotlib.pyplot as plt
import pandas_datareader as pdr

# I should get the prices:
start_dt   = datetime.datetime(2016,  1,  1)
end_dt     = datetime.datetime(2026, 12, 31)
prices1_df = pdr.DataReader('IBM', 'google', start_dt, end_dt)
# I should get 2016-11 data:
pred_sr    = prices1_df.index > '2016-11'
prices2_df = prices1_df.copy()[['Close']][pred_sr]
# I should plot:
prices2_df.plot.line(title="My Plot")
plt.show()

'bye'
