import pandas as pd
import numpy as np
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px


df  = pd.read_csv('/home/vy/Downloads/Urban_Park_Ranger_Animal_Condition_Response.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.Label('NYC calls for Animal Rescue'),
        dcc.Dropdown(
            id = 'my_dropdown',
            options=[
                {'label': 'Action Taken by Ranger', 'value': 'Final Ranger Action'},
                {'label': 'Age', 'value': 'Age'},
                {'label': 'Animal Health', 'value': 'Animal Condition'},
                {'label': 'Borough', 'value': 'Borough'},
                {'label': 'Species', 'value': 'Animal Class'},
                {'label': 'Species Status', 'value': 'Species Status'}
            ],
            value= 'Animal Class',
            multi=False,
            clearable=False,
            style={
                'width' : '50%'
            }
        ),
    ]),
    html.Div([
        dcc.Graph(id = 'the_graph')
    ])   
])



@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)

def update_graph(my_dropdown):
    dff = df

    piechart = px.pie(
        data_frame= dff,
        names=my_dropdown,
        hole= 0.3,
    )

    return piechart


if __name__ == "__main__":
    app.run_server(debug=True)