# ch39.py

# ref
# http://bokeh.pydata.org/en/latest/docs/user_guide/charts.html#chart-defaults

# The bokeh.charts modules contains a defaults attribute. Setting
# attributes on this object is an easy way to control default
# properties on all charts created, in one place. For instance:

from bokeh.charts import defaults

defaults.width = 800
defaults.height = 800

from bokeh.charts import Scatter, output_file, show
from bokeh.sampledata.autompg import autompg as df

tooltips=[
    ('Cylinders', '@cyl'),
    ('Displacement', '@displ'),
    ('Weight', '@weight'),
    ('Acceleration', '@accel')
]

p = Scatter(df, x='mpg', y='hp', title="HP vs MPG",
            xlabel="Miles Per Gallon", ylabel="Horsepower",
            tooltips=tooltips)

output_file("scatter.html")

show(p)
