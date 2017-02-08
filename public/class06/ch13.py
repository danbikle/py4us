# ch13.py

# ref:
# http://bokeh.pydata.org/en/latest/docs/user_guide/charts.html#bar-color

from bokeh.charts import Bar, output_file, show
from bokeh.sampledata.autompg import autompg as df

p = Bar(df, 'yr', values='displ',
        title="Total DISPL by YR", color="wheat")

output_file("bar.html")

show(p)

