# class02fb13.py

# This script should Use a For-Loop to sort the prices for plotting

# Ref:
# https://finance.yahoo.com/quote/FB/history?p=FB

# Demo:
# python class02fb13.py

import pdb

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

len_i = len(dates_s_l)

dates_s4plot_l = []
for p_i in range(len_i-1,-1,-1):
    dates_s4plot_l.append(dates_s_l[p_i])

print(dates_s4plot_l)

'bye'
