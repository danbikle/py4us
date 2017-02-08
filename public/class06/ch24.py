# ch24.py

# ref:
# http://bokeh.pydata.org/en/latest/docs/user_guide/charts.html#histograms

# The Histogram high-level chart can be used to quickly display the
# distribution of values in a set of data. It can be used by simply
# passing it a literal sequence of values (e.g a python list, NumPy or
# Pandas DataFrame column):

from bokeh.charts import Histogram, output_file, show
from bokeh.sampledata.autompg import autompg as df

p = Histogram(df['mpg'], title="MPG Distribution")

output_file("histogram.html",)

show(p)
