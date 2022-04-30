import matplotlib.pyplot as plt
import numpy as np

plt.style.use("fivethirtyeight")
# slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
# labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']
slices = [60, 40, 20, 90,50]
labels = ["sxity", "forty", "twenty", "onetwenty", "fifty"]
# colors = ["lightskyblue", "red", "lightgreen", "lightblue"]
explode = [0, 0, 0, 0.08, 0]

plt.pie(slices, 
        labels= labels, 
        # colors=colors, 
        wedgeprops={'edgecolor': 'black'},
        explode=explode,
        shadow=True,
        startangle= 90,
        autopct= "%1.1f%%"  #to get the percentage of each part of the pie
        )

plt.title("pie- plotting")
plt.tight_layout()
plt.show()