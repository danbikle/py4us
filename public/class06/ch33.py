# ch33.py

# ref:
# http://bokeh.pydata.org/en/latest/docs/user_guide/charts.html#legends

# When grouping, a legend is usually useful, and it’s location can be
# specified by the legend parameter:

from bokeh.charts import Scatter, output_file, show
from bokeh.sampledata.autompg import autompg as df

p = Scatter(df, x='displ', y='hp', color='cyl',
            title="HP vs DISPL (shaded by CYL)", legend="top_left",
            xlabel="Displacement", ylabel="Horsepower")

output_file("scatter.html")

show(p)


