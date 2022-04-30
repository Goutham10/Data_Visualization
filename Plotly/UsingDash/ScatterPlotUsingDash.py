import dash
from dash import html, dcc
from matplotlib.pyplot import title
import numpy as np
import plotly.graph_objects as go

app = dash.Dash(__name__)

x_rand = np.random.randint(1, 61, 60)
y_rand = np.random.randint(1, 61, 60)



app.layout = html.Div([
    
    dcc.Graph(
        id = "scatter chart",
        figure = {
            'data' : [
                go.Scatter(
                    x = x_rand,
                    y = y_rand,
                    mode = 'markers'
                )
            ],
            'layout' : 
                go.Layout(
                    title = 'Scatter points of random 60 points',
                    xaxis = {
                        'title' : 'Random x values',
                    },
                    yaxis = {
                        'title' : 'Random y values',
                    },
                    plot_bgcolor = '#D3D3D3',
                    paper_bgcolor = "#D3D3D3"
                )
            
        }
        
    )
])



if __name__ == "__main__":
    app.run_server(debug=True)


# print(help(html.Div))   # use this help() to know about anything in dash

