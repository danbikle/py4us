"""
sb18.py

Ref:
https://seaborn.pydata.org/tutorial/aesthetics.html#scaling-plot-elements-with-plotting-context-and-set-context
"""

import seaborn as sns

import numpy as np
import matplotlib.pyplot as plt

def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)

sns.set()
sns.set_style("whitegrid")
sns.set_context("poster")
plt.figure(figsize=(16, 12))
sinplot()
plt.show()
