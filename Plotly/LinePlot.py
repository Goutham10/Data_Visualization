import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
# import chart_studio.plotly as py
import seaborn as sns
import plotly.express as py
import cufflinks as cf


df_stocks = px.data.stocks()
px.line(df_stocks, x ='date', y = 'GOOG', labels={'x' : 'Date', 'y': 'price'})
df_stocks.plot()