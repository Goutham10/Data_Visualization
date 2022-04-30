import dash
from dash import Dash, html, dcc
from datetime import datetime as dt

app = Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id = "sample_dropdown",
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
    ),
    html.Br(),
    html.Br(),

    html.Label("Slider adjustment"),
    dcc.Slider(
        min = 1, 
        max = 10,
        value = 5,
        step = .5,
        marks = {i: f"{i}" for i in range(10)}
    ),
    html.Br(),
    html.Br(),
    html.Label("This is range slider"),
    dcc.RangeSlider(
        min = 1,
        max = 10,
        step = .5,
        value = [3,7],
        marks = {i: f"{i}" for i in range(10)}
    ),
    html.Br(),
    html.Div([
        html.Label("this is input field"),
        html.Br(),
        html.Br(),
        dcc.Input(
            placeholder = "enter any input",
            type = "text",
            
        )
    ]),

    html.Br(),
    html.Br(),

    html.Label("Feedback : "),
    html.Br(),html.Br(),
    html.Textarea(
        placeholder = "enter feedback",
        style = {
            'width' : '75%'
        }
    ),

    html.Br(),
    html.Br(),

    html.Label("choose your options"),
    html.Br(),
    html.Br(),
    dcc.Checklist(
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
        value = ['SF']
    ),
    html.Br(),
    html.Br(),
    html.Label("choose your options"),
    html.Br(),
    html.Br(),
    dcc.RadioItems(
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
        value = 'SF'
    ),
    
    html.Br(),
    html.Br(),
    html.Label("select date : "),
    html.Br(),
    dcc.DatePickerSingle(
        id = "dt-pick-single",
        date = dt(2022, 1, 10)
    ),

    html.Br(),
    html.Br(),
    html.Label("select end date : "),
    html.Br(),
    dcc.DatePickerRange(
        id = "dt-pick-range",
        start_date = dt.now(),
        end_date_placeholder_text = "select the end date" 
    ),


    html.Br(),
    html.Button('Submit', id = 'Submit-form'),
])


if __name__ == "__main__":
    app.run_server(debug=True)