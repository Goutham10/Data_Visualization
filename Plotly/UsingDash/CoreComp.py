from ssl import HAS_TLSv1_1
from dash import Dash, html, dcc

app = Dash(__name__)


app.layout = html.Div([
    html.Div(children=[
        html.Label("dropdown"),
        dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'], 'Montréal'),
        
        html.Br(),
        html.Label("Multi-select Dropdown"),
        dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'], ['Montréal','San Francisco'], multi=True),

        html.Br(),
        html.Label('Radio Items'),
        dcc.RadioItems(['New York City', 'Montréal', 'San Francisco'], 'Montréal'),

    ], style= {
        'padding' : 10, 'flex' :1
    }),

    html.Div(children=[
        html.Label("Checkboxes"),
        dcc.Checklist(['New York City', 'Montréal', 'San Francisco'],
                      ['Montréal', 'San Francisco']
        ),

        html.Br(),
        html.Label('Text Input'),
        dcc.Input(value='MTL', type='text'),

        html.Br(),
        html.Label('Slider'),
        dcc.Slider(
            min=0,
            max=9,
            marks={i: f'Label {i}' if i == 1 else str(i) for i in range(1, 6)},
            value=5,
        ),
    ],style={'padding': 10, 'flex': 2})    
],
style= {
    'display': 'flex', 
    'flex-direction': 'row'
}
)



if __name__ == "__main__":
    app.run_server(debug=True)