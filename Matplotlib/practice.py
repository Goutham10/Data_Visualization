

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Arial'
labels = ["goutham", "ramya", "teja", "mohan", "krishna", "wasim", "pavan", "bobby", "dharma", "hairsh", "prakash"]
sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

fig, ax = plt.subplots(figsize=(3, 3), subplot_kw=dict(aspect="equal"))

wedges, texts = ax.pie(sizes, wedgeprops=dict(width=0.5), startangle=-40)

kw = dict(arrowprops=dict(arrowstyle="->"), va="center")
for p, label in zip(wedges, labels):
    ang = np.deg2rad((p.theta1 + p.theta2)/2)
    y = np.sin(ang)
    x = np.cos(ang)
    horizontalalignment = "center" if abs(x) < abs(y) else "right" if x < 0 else "left"
    ax.annotate(label, xy=(0.75*x, 0.75*y), xytext=(1.3*x, 1.3*y),
                horizontalalignment=horizontalalignment, **kw)
plt.tight_layout()
plt.show()
