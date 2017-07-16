"""
sb14.py

Ref:
https://seaborn.pydata.org/tutorial/aesthetics.html#removing-spines-with-despine
"""

import seaborn as sns

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
np.random.seed(sum(map(ord, "aesthetics")))

def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
# style must be one of white, dark, whitegrid, darkgrid, ticks
sns.set_style("ticks")    
sinplot()
sns.despine()
plt.show()
'bye'
