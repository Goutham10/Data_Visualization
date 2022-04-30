from cProfile import label
import pandas as pd 
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('/home/vy/Data_Visualization/Matplotlib/data.csv')

ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']


############# one way of doing ##############
# fig, (ax1,ax2) = plt.subplots(nrows=2, ncols=1, sharex= True)
#                 #sharex is used to share the xticks commonly
# ax1.plot(ages, dev_salaries, '--', label="All Devs")

# ax2.plot(ages, py_salaries, label='Python')
# ax2.plot(ages, js_salaries, label='JavaScript')


# ax1.legend()

# ax1.set_title("Median Salary by Age")
# # ax1.set_xlabel("Ages")
# ax1.set_ylabel("Salaries")

# ax2.legend()

# # ax2.set_title("Median Salary by Age")
# ax2.set_xlabel("Ages")
# ax2.set_ylabel("Salaries")
# plt.tight_layout()
# plt.show()


########## another way of doing #########

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

ax1.plot(ages, dev_salaries, '--', label="All Devs")

ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')


ax1.legend() 
ax1.set_title("Median Salary by Age")
ax1.set_xlabel("Ages")
ax1.set_ylabel("Salaries")

ax2.legend()

ax2.set_title("Median Salary by Age")
ax2.set_xlabel("Ages")
ax2.set_ylabel("Salaries")
plt.tight_layout()
plt.show()
