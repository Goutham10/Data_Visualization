from turtle import width
import matplotlib
from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(0, 2 * np.pi, 200)
# y = np.sin(x)

# fig, ax = plt.subplots()
# ax.plot(x, y)
# plt.show()

x_points = np.array([5, 2, 11, 7, 4, 6, 3, 8,1,9 , 10])
y_points = np.array(["goutham", "ramya", "teja", "mohan", "krishna", "wasim", "pavan", "bobby", "dharma", "hairsh", "prakash"])
plt.figure(figsize=(8,8))
plt.style.use('seaborn-whitegrid')
# plt.pie(x_points, labels=y_points)
# fig, ax = plt.subplots(figsize=(8,8), subplot_kw= dict(aspect="equal"))

# wedges, texts =  ax.pie(x_points, wedgeprops=dict(width=0.5),startangle=-10)


# kw = dict(arrowprops = dict(arrowstyle="->"), va = "center")
# for p, label in zip(wedges, y_points):
#     ang = np.deg2rad((p.theta1 + p.theta2) / 2 )
#     y = np.sin(ang)
#     x = np.cos(ang)
#     horizantalalignment = "center" if abs(x) < abs(y) else "right" if x < 0 else "left"
#     ax.annotate(label, xy=(0.75 * x, 0.75 * y), xytext = (1.3 * x, 1.3 * y),
#                 horizantalalignment = horizantalalignment, **kw)



# plt.hist(np.random.normal(170, 10, 250))
# plt.scatter()
# plt.grid()
# plt.xlabel("index")
# plt.ylabel("values")
# plt.legend(["x_points", "y_points"], loc = "lower right")
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x, y)

# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# plt.scatter(x, y)
# myexp = [0, 0, 0, 0,0,0,0,0,0,0,0.2]
# plt.pie(x_points, labels=y_points, startangle=90, explode= myexp, shadow= True)
# plt.xticks([i for i in range(len(x_points)+1)])
# plt.yticks([i for i in range(len(y_points)+1)])
# plt.legend()
plt.title("Plotting")
# plt.tight_layout()
plt.plot(y_points, x_points, 'o-g', linewidth=1)
plt.xlabel("person")
plt.ylabel("salary percentage")
plt.grid(True)

plt.tight_layout()
plt.show()
