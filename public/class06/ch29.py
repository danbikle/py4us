# ch29.py

# ref:
# http://bokeh.pydata.org/en/latest/docs/user_guide/charts.html#color-groups

# However, the color parameter can also be used to group the data. If
# the value of the color parameter is one of the DataFrame column
# names, the data is first grouped by this column, and a histogram is
# generated for each group. Each histogram is automatically colored
# differently, and a legend displayed:

from bokeh.charts import Histogram, output_file, show
from bokeh.sampledata.autompg import autompg as df

p = Histogram(df, values='hp', color='cyl',
              title="HP Distribution (color grouped by CYL)",
              legend='top_right')

output_file("histogram_color.html")

show(p)


