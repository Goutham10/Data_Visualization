import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = html.Div([
        dbc.Alert(
        "Hello, Bootstrap!", className="m-5"
    ),

    html.Div([
        dbc.Button("Success", color="success", className="mr-1")
    ])
])

if __name__ == "__main__":
    app.run_server()