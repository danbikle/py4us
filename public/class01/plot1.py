# plot1.py

# This script should Plot S&P 500 Prices For 2016-11

import pandas as pd
import pdb
import matplotlib.pyplot as plt

# I should get the data:
prices_df = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC')
# pdb.set_trace()
# I should get 2016-11 data:
pred_sr    = prices_df.Date > '2016-11'
prices0_df = prices_df.copy()[['Date','Close']][pred_sr]

# I should sort by Date ascending:
prices1_df = prices0_df.sort_values('Date')

# I should set index to Date column:
prices2_df = prices1_df.set_index('Date')

# I should plot:
prices2_df.plot.line(title="My Plot")
plt.show()

'bye'
