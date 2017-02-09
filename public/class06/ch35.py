# ch35.py

# ref:
# http://bokeh.pydata.org/en/latest/docs/user_guide/charts.html#userguide-charts-scatter-marker

# The marker parameter can be used to control the shape of the scatter marker:

from bokeh.charts import Scatter, output_file, show
from bokeh.sampledata.autompg import autompg as df

p = Scatter(df, x='displ', y='hp', marker='square',
            title="HP vs DISPL", legend="top_left",
            xlabel="Displacement", ylabel="Horsepower")

output_file("scatter.html")

show(p)


