import dash
from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = html.Div([
    html.Label('choose a city'),
    
    dcc.Dropdown(
        id = 'first_dropdown',
        options = [
            {
                'label' : 'San Francisco',
                'value' : 'SF'
            },
            {
                'label' : 'New York City', 
                'value' : 'NY'
            },
            {
                'label' : 'Raleigh Durham', 
                'value' : 'RDU',
                'disabled' : True  # this is used to disable the option
            },
        ],
        # value = "NY", # auto selected value 
        # multi = True # multi is used to select multiple options
        placeholder = "Select a city" # placeholder
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)