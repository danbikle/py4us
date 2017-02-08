# ch26.py

# ref:
# http://bokeh.pydata.org/en/latest/docs/user_guide/charts.html#histograms

# Or explicitly as the values keyword argument:

from bokeh.charts import Histogram, output_file, show
from bokeh.sampledata.autompg import autompg as df

p = Histogram(df, values='displ', title="DISPL Distribution")

output_file("histogram.html",)

show(p)

