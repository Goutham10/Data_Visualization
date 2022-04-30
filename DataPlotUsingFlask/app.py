from flask import Flask
import dash
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px
from dash import Dash, html, dcc, Input, Output, dash_table


app = Flask(__name__)
dash_app = Dash(server=app, 
                # name="File_Based_Dashboard", 
                # external_stylesheets=[dbc.themes.BOOTSTRAP], 
                url_base_pathname="/dash/"
                )
df = pd.read_excel('/home/vy/Downloads/COVID-19-geographic-disbtribution-worldwide-2020-03-29.xlsx')

dff = df.groupby('countriesAndTerritories', as_index= False)[['deaths', 'cases']].sum()

# print(dff)

dash_app.layout = html.Div([
    html.Div([
        dash_table.DataTable(
            id='datatable_id',
            data=dff.to_dict('records'),
            columns=[
                {"name": i, "id": i, "deletable": False, "selectable": False} for i in dff.columns
            ],
            editable=False,
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            row_selectable="multi",
            row_deletable=False,
            selected_rows=[],
            page_action="native",
            page_current= 0,
            page_size= 6,
            # page_action='none',
            # style_cell={
            # 'whiteSpace': 'normal'
            # },
            # fixed_rows={ 'headers': True, 'data': 0 },
            # virtualization=False,
            style_cell_conditional=[
                {'if': {'column_id': 'countriesAndTerritories'},
                'width': '40%', 'textAlign': 'left'},
                {'if': {'column_id': 'deaths'},
                'width': '30%', 'textAlign': 'left'},
                {'if': {'column_id': 'cases'},
                'width': '30%', 'textAlign': 'left'},
            ],
        ),
    ],className=''),

    html.Div([
        html.Div([
            dcc.Dropdown(id='linedropdown',
                options=[
                        {'label': 'Deaths', 'value': 'deaths'},
                        {'label': 'Cases', 'value': 'cases'}
                ],
                value='deaths',
                multi=False,
                clearable=False
            ),
        ],style={'width' : '35%'}),

        html.Div([
        dcc.Dropdown(id='piedropdown',
            options=[
                    {'label': 'Deaths', 'value': 'deaths'},
                    {'label': 'Cases', 'value': 'cases'}
            ],
            value='cases',
            multi=False,
            clearable=False
        ),
        ],style={'width' : '35%'}),

    ],style={'display': 'flex',
            'flex-direction': 'row',
            'justify-content': 'space-around',
            'padding': '40px'}),

    html.Div([
        html.Div([
            dcc.Graph(id='linechart'),
        ],className='six columns'),

        html.Div([
            dcc.Graph(id='piechart'),
        ],className='six columns'),

    ],style={'display': 'flex',
            'flex-direction': 'row',
            'justify-content': 'space-around',
            'padding': '40px'}),


], style={
    'margin' : '50px',
    'min-height' : '100vh'
})

@dash_app.callback(
    [Output('piechart', 'figure'),
    Output('linechart', 'figure')],
    [Input('datatable_id', 'selected_rows'),
    Input('piedropdown', 'value'),
    Input('linedropdown', 'value')]
)
def update_data(chosen_rows,piedropval,linedropval):
    if len(chosen_rows)==0:
        df_filterd = dff[dff['countriesAndTerritories'].isin(['China','Iran','Spain','Italy'])]
    else:
        print(chosen_rows)
        df_filterd = dff[dff.index.isin(chosen_rows)]

    pie_chart=px.pie(
            data_frame=df_filterd,
            names='countriesAndTerritories',
            values=piedropval,
            hole=.3,
            labels={'countriesAndTerritories':'Countries'}
            )


    #extract list of chosen countries
    list_chosen_countries=df_filterd['countriesAndTerritories'].tolist()
    #filter original df according to chosen countries
    #because original df has all the complete dates
    df_line = df[df['countriesAndTerritories'].isin(list_chosen_countries)]

    line_chart = px.line(
            data_frame=df_line,
            x='dateRep',
            y=linedropval,
            color='countriesAndTerritories',
            labels={'countriesAndTerritories':'Countries', 'dateRep':'date'},
            )
    line_chart.update_layout(uirevision='foo')

    return (pie_chart,line_chart)

@app.route('/dash')
def home():
  return "" 
    



if __name__ == "__main__":
    app.run(debug=True)