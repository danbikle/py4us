"""
sb12.py

Ref:
https://seaborn.pydata.org/tutorial/aesthetics.html#styling-figures-with-axes-style-and-set-style
"""

import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

sns.set_style("whitegrid")
data = np.random.normal(size=(20, 6)) + np.arange(6) / 2
sns.boxplot(data=data)
plt.show()
'bye'
