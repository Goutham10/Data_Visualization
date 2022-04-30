import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import HoverTool
from collections import OrderedDict


x = np.sort(np.random.rand(15))
y = np.sort(np.random.rand(15))
names = np.array(list("ABCDEFGHIJKLMNO"))

p = figure(plot_width=1000, plot_height=600,
           tools="pan,hover", 
           title="Changes",
           x_axis_label='Year', 
           y_axis_label='Weight',
           toolbar_location="left"
          )

hover = p.select(dict(type=HoverTool))
hover.tooltips = OrderedDict([('Year', '@x'), ('Weight', '$y')])

output_notebook()

p.line(x, y, legend="Weight")
p.line(x, y, legend="Height", line_color="red")

show(p)  