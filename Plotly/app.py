# import pandas as pd
# import numpy as np
# import chart_studio.plotly as py
# import seaborn as sns
# import plotly.express as py
# import cufflinks as cf

# # from plotly.offline import download_plotlyjs, init_notbook_mode, plot, iplot, init_notebook_mode(connected=True)
# # cf.go_offline()   these two lines are for jupyter notebook

# arr = np.random.randn(50,4)
# df = pd.DataFrame(arr, columns=['A', 'B', 'C', 'D'])
# df.plot()


# import plotly.express as px

# df = px.data.gapminder().query("country=='Canada'")
# fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
# fig.show()


from fileinput import filename
import plotly.express as px
import chart_studio
chart_studio.tools.set_credentials_file(username = 'boine_goutham10', api_key = 'mGAPpdFEAffBYMdfLqW5')
import plotly.graph_objs as go
import numpy as np
import matplotlib.pyplot as plt
import math #needed for definition of pi
import pandas as pd

df_stocks = px.data.stocks()
# print(df_stocks.head())

fig = px.line(df_stocks, x = 'date', y = 'GOOG', labels={'x': 'Date', 'y' : 'Price'})
fig.show()


from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv',dtype = {'fips' : str})

fig = px.choropleth(df,
                    geojson = counties,
                    locations = 'fips',
                    color = 'unemp',
                    color_continuos_scale = 'Viridis',
                    range_color = (0, 12),
                    scope = 'usa',
                    labels = {'unemp' : 'unemployment rate'}
                   )
fig
