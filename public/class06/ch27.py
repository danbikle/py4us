# ch27.py

# ref:
# http://bokeh.pydata.org/en/latest/docs/user_guide/charts.html#number-of-bins

# The bins argument can be used to specify the number of bins to use when computing the histogram:

from bokeh.charts import Histogram, output_file, show
from bokeh.sampledata.autompg import autompg as df

p = Histogram(df, values='mpg', bins=50,
              title="MPG Distribution (50 bins)")

output_file("histogram_bins.html")

show(p)



