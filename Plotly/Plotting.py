import plotly.express as px
import numpy as np
import pandas as pd 
import plotly.graph_objects as go


df = px.data.tips()
# print(df.head())

fig = go.Figure(
    data = go.Scatter(
        x = df['day'],
        y = df['tip'],
        mode = 'markers',
    )
)


fig.update_layout(
    updatemenus = [
        dict(
            # type="buttons",
            # direction = 'left',  uncomment these two lines to place the buttons side by side 
            buttons = list([
            dict(
                args = ['type', 'scatter'],
                label = 'Scatter plot',
                method = 'restyle'
            ),
            dict(
                args = ['type', 'bar'],
                label = 'Bar plot',
                method = 'restyle'
            )
        ]),
            direction = 'up' # this is used as drop down selection 
        ),
        
    ]
)

fig.show()