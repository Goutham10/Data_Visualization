import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# print(sns.get_dataset_names())


df = sns.load_dataset('car_crashes')
# print(df)

# sns.displot(df['speeding'], bins=20, color ='skyblue')

sns.jointplot(x='speeding',
              y='alcohol', 
              data=df,
              marker ="*",
              kind = 'reg',
              marginal_kws=dict(bins=25, fill=False),
              ratio = 2,
              marginal_ticks = True
              )
plt.show()