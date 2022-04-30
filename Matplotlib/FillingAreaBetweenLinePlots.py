from random import randint
from statistics import mean
from turtle import clear
import pandas as pd
from matplotlib import pyplot as plt

# data  = pd.read_excel("/home/vy/sample.xls")

# first_name = data['First_Name']
# age = data['Age']
# country = data['Country']
# gender = data['Gender']

# plt.bar(first_name, age, width=0.5)
# plt.show()




# age_x = [i for i in range(25,36)]

# x_indexes = np.arange(len(age_x))
# width = 0.25


# dev_y = random.randint(35000, 99999, size=11)
# dev_y = [j for j in sorted(dev_y)[::-1]]

# lst = []
# for i in range(11):
#     lst.append(random.randint(30000, 90000))
# lst = (sorted(lst))
# print(lst)

# second_lst = []

# for i in lst:
#     second_lst.append(i + int(random.random() * 10000))
# print(second_lst)

# # py_dev_y = random.randint(35000, 99999, size=11)
# # py_dev_y = [j for j in sorted(py_dev_y)[::-1]]

# # js_dev_y = random.randint(35000, 99999, size=11)
# # js_dev_y = [j for j in sorted(js_dev_y)[::-1]]

# overall_median = int(mean(lst))

# plt.plot(age_x, lst, color = '#444444', label = "All Devs")
# plt.plot(age_x, second_lst, label = 'Python')
# plt.fill_between(age_x, 
#                 second_lst,
#                 overall_median,
#                 where=([overall_median <= i for i in second_lst]),  
#                 interpolate=True, 
#                 alpha = 0.25)
# plt.fill_between(age_x, 
#                 second_lst,
#                 overall_median,
#                 where=([overall_median >= i for i in second_lst]),  
#                 interpolate=True, 
#                 color ='red',
#                 alpha = 0.25)
# plt.legend()

# plt.title("plotting")
# plt.xlabel("Ages")
# plt.ylabel("median salary")
# plt.tight_layout()
# plt.show()




data = pd.read_csv('data.csv')


ages = data['Age']

dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

plt.plot(ages, py_salaries, label='Python')

# overall_median = 57287

plt.fill_between(ages, py_salaries, dev_salaries,
                 where=(py_salaries > dev_salaries),
                 interpolate=True, alpha=0.25, label='Above Avg')

plt.fill_between(ages, py_salaries, dev_salaries,
                 where=(py_salaries <= dev_salaries),
                 interpolate=True, color='red', alpha=0.25, label='Below Avg')

plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()

