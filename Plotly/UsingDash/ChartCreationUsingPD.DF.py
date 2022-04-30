import dash
from dash import Dash, html, dcc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

app = Dash(__name__)

df_tips = px.data.tips()

app.layout = html.Div([
    dcc.Graph(
        id = "Scatter_chart_from_DataFrame",
        figure = {
            'data' : [
                go.Scatter(
                    x = df_tips['day'],
                    y = df_tips['total_bill'],
                    mode = 'markers',
                )
            ],
            'layout' : go.Layout(
                title = 'Scatterplot for DF',
                xaxis = {
                    'title' : 'day',
                },
                yaxis = {
                    'title' : 'total_bill'
                }
            )
        }
    )
])


if __name__ == "__main__":
    app.run_server(debug=True)