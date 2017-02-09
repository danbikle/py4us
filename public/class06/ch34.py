# ch34.py

# ref:
# http://bokeh.pydata.org/en/latest/docs/user_guide/charts.html#legends

# Legends are not sorted by default but this behavior can be changed
# by using the legend_sort_field attribute to specify the attribute to
# sort by and legend_sort_direction to set the order (ascending or
# descending).

from bokeh.charts import Scatter, output_file, show
from bokeh.sampledata.autompg import autompg as df

p = Scatter(df, x='displ', y='hp', color='cyl',
            title="HP vs DISPL (shaded by CYL)", legend="top_left",
            legend_sort_field = 'color',
            legend_sort_direction = 'ascending',
            xlabel="Displacement",
            ylabel="Horsepower")

output_file("scatter.html")

show(p)


