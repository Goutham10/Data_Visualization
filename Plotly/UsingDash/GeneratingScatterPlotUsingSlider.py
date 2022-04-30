import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc
from dash.dependencies import Input, Output


df = px.data.gapminder()

# print(min(df['year']), max(df['year']))

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(
        id= 'graph_with_slider'
    ),

    dcc.Slider(
        min = min(df['year']),
        max = max(df['year']),
        step = None,
        value = min(df['year']),
        marks = {str(year): str(year) for year in df['year'].unique()},
        id = 'year_slider' 
    )
],
style= {
    'margin-top' : '7%',
    'margin-left' : '10%',
    'margin-right' : '30%'
}
)


@app.callback(
    Output(component_id='graph_with_slider', component_property='figure'),
    Input(component_id='year_slider', component_property='value')
)

def update_graph(year_slider):
    filtered_df = df[df['year']  == year_slider]

    fig = px.scatter(
        filtered_df,
        x = 'gdpPercap',
        y = 'lifeExp',
        size = 'pop',
        color = 'continent',
        hover_name= 'country',
        log_x= True,
        size_max= 55
    )

    fig.update_layout(transition_duration = 500)

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)