from cProfile import label
from turtle import color
import matplotlib.pyplot as plt
import numpy as np
from numpy import random
    

age_x = [i for i in range(25,36)]

x_indexes = np.arange(len(age_x))
width = 0.25

dev_y = random.randint(35000, 99999, size=11)
dev_y = [j for j in sorted(dev_y)[::-1]]

py_dev_y = random.randint(35000, 99999, size=11)
py_dev_y = [j for j in sorted(py_dev_y)[::-1]]

js_dev_y = random.randint(35000, 99999, size=11)
js_dev_y = [j for j in sorted(js_dev_y)[::-1]]

plt.bar(x_indexes - width, dev_y, color='#444444', width= width, label='All Devs')

plt.bar(x_indexes, py_dev_y, color="lightblue", width= width, label="Python Devs")

plt.bar(x_indexes + width, js_dev_y, color="lightskyblue", width= width,  label="JS Devs")

plt.xticks(ticks= x_indexes, labels= age_x)

plt.show()