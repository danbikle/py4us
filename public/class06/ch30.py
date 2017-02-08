# ch30.py

# ref:
# http://bokeh.pydata.org/en/latest/docs/user_guide/charts.html#scatter-plots

# The Scatter high-level chart can be used to generate 1D or (more
# commonly) 2D scatter plots. It is used by passing in DataFrame-like
# object as the first argument then specifying the columns to use for
# x and y coordinates:

from bokeh.charts import Scatter, output_file, show
from bokeh.sampledata.autompg import autompg as df

p = Scatter(df, x='mpg', y='hp', title="HP vs MPG",
            xlabel="Miles Per Gallon", ylabel="Horsepower")

output_file("scatter.html")

show(p)

