"""
sb15.py

Ref:
https://seaborn.pydata.org/tutorial/aesthetics.html#removing-spines-with-despine
"""

import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

data = np.random.normal(size=(20, 6)) + np.arange(6) / 2
sns.set_style("whitegrid")
sns.boxplot(data=data, palette="deep")
sns.despine(left=True)
plt.show()
'bye'
