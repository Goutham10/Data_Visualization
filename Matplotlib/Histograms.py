import statistics
import pandas as pd 
from matplotlib import pyplot as plt


plt.style.use('fivethirtyeight')

# ages = [18, 19, 21, 25, 26, 30, 32, 38, 45, 55]

# plt.hist(ages, bins=5, edgecolor = 'black')


data = pd.read_csv('/home/vy/Data_Visualization/Matplotlib/data_for_hist.csv')
# print(data)
ids = data['Responder_id']
ages = data['Age']


bins = [i*10 for i in range(1,11)]
# plt.hist(ages, bins=bins, edgecolor = 'black')

plt.hist(ages, bins=bins, edgecolor = 'black', log=True)
plt.axvline(statistics.mean(ages), color="orange", linewidth=2)

plt.title("Ages of respondents")
plt.xlabel("ages")
plt.ylabel("total  respondents")
plt.tight_layout()

plt.show()
