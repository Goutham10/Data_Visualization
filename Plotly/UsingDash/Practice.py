import dash
from dash import html, dcc

app = dash.Dash(__name__)


colors = {
    'text' : '#ff0000',
    'plot_color' : '#D3D3D3',
    'paper_color' : '00FFFF'
}

app.layout = html.Div([
    html.H1(
            children = 'Hello Dash!!!',
            style = {
                'textAlign' : 'center',
                'color' : colors['text'],
            }
        ),
    html.Div(
            children = 'Dash - A data product development framework from plotly',
            style = {
                'textAlign' : 'center',
                'color' : colors['text'],
            }
        ),
    dcc.Graph(
        id = 'sample_graph',
        figure = {
            'data' : [
                {
                    'x' : [5,6,7],
                    'y' : [12,15,18],
                     'type' : 'bar',
                    'name' : 'first_chart'
                },
                {
                    'x' : [5,6,7],
                    'y' : [20,24,26],
                    'type' : 'bar',
                    'name' : 'Second_chart'
                }
            ],
            'layout' : {
                'plot_bgcolor' : colors['plot_color'],
                'paper_bgcolor' : colors['plot_color'],
                'font' : {
                    'color' : colors['text']
                },
                'title' : 'Data using Bar chart'
            }
        }
    )
])



if __name__ == "__main__":
    app.run_server(debug=True)


# print(help(html.Div))   # use this help() to know about anything in dash

