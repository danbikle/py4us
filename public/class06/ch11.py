# ch11.py

# ref:
# http://bokeh.pydata.org/en/latest/docs/user_guide/charts.html#aggregations

# The agg parameter may be used to specify how each group should be aggregated:

from bokeh.charts import Bar, output_file, show
from bokeh.sampledata.autompg import autompg as df

p = Bar(df, label='yr', values='mpg', agg='mean', title="Average MPG by YR")

output_file("bar.html")

show(p)
