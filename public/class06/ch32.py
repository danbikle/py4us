# ch32.py

# ref:
# http://bokeh.pydata.org/en/latest/docs/user_guide/charts.html#userguide-charts-scatter-color-groups

# if color is supplied with the name of a data column then the data is
# first grouped by the values of that column, and then a different
# color is used for every group:

from bokeh.charts import Scatter, output_file, show
from bokeh.sampledata.autompg import autompg as df

p = Scatter(df, x='mpg', y='hp', color='cyl', title="HP vs MPG (shaded by CYL)",
            xlabel="Miles Per Gallon", ylabel="Horsepower")

output_file("/tmp/ch32.html")

show(p)


