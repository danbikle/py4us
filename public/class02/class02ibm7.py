# class02ibm7.py

# This script should Create a list of 2016-11 IBM prices.
# I should Copy the prices.
# I should Delete the last price

# Ref:
# https://finance.yahoo.com/quote/IBM/history?p=IBM

# Demo:
# python class02ibm7.py

import pdb

prices_l = [
  162.220001
  ,163.529999
  ,164.520004
  ,163.139999
  ,161.979996
  ,162.669998
  ,162.770004
  ,160.389999
  ,159.800003
  ,159.289993
  ,158.669998
  ,158.210007
  ,161.270004
  ,160.220001
  ,154.809998
  ,155.169998
  ,155.720001
  ,152.429993
  ,152.369995
  ,151.949997
  ,152.789993
]

# I should Copy the prices
copy1_l = prices_l

# I should Copy the prices
copy2_l = list(prices_l)

pdb.set_trace()

# I should Delete the last price in prices_l
del(prices_l[-1])

# I should list the prices
print(len(prices_l))
print(len(copy1_l))
print(len(copy2_l))
print(prices_l[-4:])
print(copy1_l[ -4:])
print(copy2_l[ -4:])

'bye'

