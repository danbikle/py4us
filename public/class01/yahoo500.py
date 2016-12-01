# yahoo500.py

# This script should Download S&P 500 Prices from Yahoo

import pandas as pd
import pdb

# I should stop the script here and start the debugger:
pdb.set_trace()

# I should get the prices and use pandas to read them into a DataFrame:
prices_df = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC')

# I should use the head() method to display some of the prices:
prices_df.head()

# I should write the prices to a CSV file in /tmp:
prices_df.to_csv('/tmp/prices_gspc.csv', float_format='%4.2f', index=False)

# I should end the script with a simple string which might be a
# convenient breakpoint for the debugger:

'bye'

