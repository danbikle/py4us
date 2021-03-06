"""
class02fb14.py

This script should Plot FB prices vs dates

Ref:
https://finance.yahoo.com/quote/FB/history?p=FB

Demo:
python class02fb14.py
"""

import pdb

prices_l = [
    118.419998
    ,120.870003
    ,120.410004
    ,120.379997
    ,120.839996
    ,121.470001
    ,121.769997
    ,117.019997
    ,117.790001
    ,116.339996
    ,117.199997
    ,115.080002
    ,119.019997
    ,120.800003
    ,123.18
    ,124.220001
    ,122.150002
    ,120.75
    ,120
    ,127.169998
    ,129.5
]

dates_s_l = [
    '2016-11-30'
    ,'2016-11-29'
    ,'2016-11-28'
    ,'2016-11-25'
    ,'2016-11-23'
    ,'2016-11-22'
    ,'2016-11-21'
    ,'2016-11-18'
    ,'2016-11-17'
    ,'2016-11-16'
    ,'2016-11-15'
    ,'2016-11-14'
    ,'2016-11-11'
    ,'2016-11-10'
    ,'2016-11-09'
    ,'2016-11-08'
    ,'2016-11-07'
    ,'2016-11-04'
    ,'2016-11-03'
    ,'2016-11-02'
    ,'2016-11-01'
]

len_i = len(prices_l)

prices4plot_l = []
for p_i in range(len_i-1,-1,-1):
    prices4plot_l.append(prices_l[p_i])

dates_s4plot_l = []
for p_i in range(len_i-1,-1,-1):
    dates_s4plot_l.append(dates_s_l[p_i])

# I should convert each date-string into a date-time
from datetime import datetime

dates_dt4plot_l = []
for d_s in dates_s4plot_l:
    d_dt = datetime.strptime(d_s, '%Y-%m-%d')
    dates_dt4plot_l.append(d_dt)
    
import matplotlib.pyplot as plt
plt.plot(dates_dt4plot_l, prices4plot_l)
plt.show()

'bye'
