"""
sb10.py

Ref:
https://seaborn.pydata.org/tutorial/aesthetics.html

This demo does not use seaborn.
"""

import numpy as np
import matplotlib.pyplot as plt

def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
sinplot()
plt.show()
'bye'
