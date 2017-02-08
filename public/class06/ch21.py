# ch21.py

# ref:
# http://bokeh.pydata.org/en/latest/docs/user_guide/charts.html#whisker-color

# whiskers shaded by CYL grouping automatically:

from bokeh.charts import BoxPlot, output_file, show
from bokeh.sampledata.autompg import autompg as df

p = BoxPlot(df, values='mpg', label='cyl', whisker_color='cyl',
            title="MPG Summary (grouped and whiskers shaded by CYL)")

output_file("boxplot.html")

show(p)

