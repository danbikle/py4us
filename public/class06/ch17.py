# ch17.py

# ref:
# http://bokeh.pydata.org/en/latest/docs/user_guide/charts.html#box-plots

# The label can also accept a list of column names, in which case the
# data is grouped by all the groups in the list:

from bokeh.charts import BoxPlot, output_file, show
from bokeh.sampledata.autompg import autompg as df

p = BoxPlot(df, values='mpg', label=['cyl', 'origin'],
            title="MPG Summary (grouped by CYL, ORIGIN)")

output_file("boxplot.html")

show(p)


