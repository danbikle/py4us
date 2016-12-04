# class02fb12.py

# This script should Use a For-Loop to sort the prices for plotting

# Ref:
# https://finance.yahoo.com/quote/FB/history?p=FB

# Demo:
# python class02fb12.py

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

len_i = len(prices_l)

prices4plot_l = []
for p_i in range(len_i-1,-1,-1):
    print(p_i)
    prices4plot_l.append(prices_l[p_i])

print(prices4plot_l)

'bye'
