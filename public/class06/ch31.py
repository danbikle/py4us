# ch31.py

# ref:
# http://bokeh.pydata.org/en/latest/docs/user_guide/charts.html#color

# The color parameter can be used to control the color of the scatter markers:

from bokeh.charts import Scatter, output_file, show
from bokeh.sampledata.autompg import autompg as df

p = Scatter(df, x='mpg', y='hp', title="HP vs MPG", color="navy",
            xlabel="Miles Per Gallon", ylabel="Horsepower")

output_file("scatter.html")

show(p)


