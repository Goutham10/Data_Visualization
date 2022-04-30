from dash import Dash, html, dcc, Input, Output, dash_table
import pandas as pd
from collections import OrderedDict

from sqlalchemy import column

app = Dash(__name__)

# df = pd.DataFrame(OrderedDict([
#     ('climate', ['Sunny', 'Snowy', 'Sunny', 'Rainy']),
#     ('temperature', [13, 43, 50, 30]),
#     ('city', ['NYC', 'Montreal', 'Miami', 'NYC'])
# ]))


# app.layout = html.Div([
#     dash_table.DataTable(
#         id='table-dropdown',
#         data=df.to_dict('records'),     #the contents of the table
#         columns=[
#             {'id': 'climate', 'name': 'climate', 'presentation': 'dropdown'},
#             {'id': 'temperature', 'name': 'temperature'},
#             {'id': 'city', 'name': 'city', 'presentation': 'dropdown'},
#         ],
#         editable=True,

#         dropdown={                      #dictionary of keys that represent column IDs,
#             'climate': {                #its values are 'options' and 'clearable'
#                 'options': [            #'options' represents all rows' data under that column
#                     {'label': i, 'value': i}
#                     for i in df['climate'].unique()
#                 ],

#                 'clearable':True
#             },
#             'city': {
#                 'options':[
#                     {'label': 'NYC', 'value': 'NYC'},
#                     {'label': 'Miami', 'value': 'Miami'},
#                     {'label': 'Montreal', 'value': 'Montreal'}
#                 ],

#                 'clearable':False
#             }
#         }
#     ),
# ])


#-------------------------------------------------------------------
# 2. DataTable with Per-Row Dropdowns (row-by-row: from first row to as many as you want)

df = pd.DataFrame(OrderedDict([
    ('climate', ['Sunny', 'Snowy', 'Sunny', 'Rainy']),
    ('temperature', [13, 43, 50, 30]),
    ('city', ['NYC', 'Montreal', 'Miami', 'NYC'])
]))


app.layout = html.Div([
    dash_table.DataTable(
        id='table-dropdown',
        data=df.to_dict('records'),
        columns=[
            {'id': 'climate', 'name': 'climate', 'presentation': 'dropdown'},
            {'id': 'temperature', 'name': 'temperature'},
            {'id': 'city', 'name': 'city', 'presentation': 'dropdown'},
        ],
        editable=True,
                                        #list of dictionaries. One dict per row
        dropdown_data=[{                #their keys represent column IDs
            'climate': {                #their values are 'options' and 'clearable'
                'options': [            #'options' represent cell data
                    {'label': i, 'value': i}
                    for i in df['climate'].unique()
                ],

                'clearable':True
            },

            'city': {
                'options': [
                    {'label': i, 'value': i}
                    for i in df['city'].unique()
                ],

                'clearable':True
            },
        } for x in range(4)
        ],

    ),
])


#-------------------------------------------------------------------
# 3. DataTable with Per-Row-Col Dropdowns (conditional, you choose which row/column)

# df = pd.DataFrame(OrderedDict([
#     ('City', ['NYC', 'Montreal', 'Los Angeles']),
#     ('Neighborhood', ['Brooklyn', 'Mile End', 'Venice']),
#     ('Temperature (F)', [70, 60, 90]),
# ]))
#
#
# app.layout = html.Div([
#     dash_table.DataTable(
#         id='dropdown_per_row',
#         data=df.to_dict('records'),
#         columns=[
#             {'id': 'City', 'name': 'City'},
#             {'id': 'Neighborhood', 'name': 'Neighborhood', 'presentation': 'dropdown'},
#             {'id': 'Temperature (F)', 'name': 'Temperature (F)'}
#         ],
#         editable=True,
#                                         #list of dictionaries. One dict per per condition/if
#         dropdown_conditional=[{         #its keys are 'clearable', 'if', 'options'
#             'if': {
#                 'column_id': 'Neighborhood',       # if under city column, a row == NYC, then the data
#                 'filter_query': '{City} eq "NYC"'  # under same row under Neighborhood column will be...
#             },
#             'options': [
#                             {'label': i, 'value': i}
#                             for i in [
#                                 'Brooklyn',
#                                 'Queens',
#                                 'Staten Island'
#                             ]
#                         ],
#             'clearable':True
#         },
#
#         {
#             'if': {
#                 'column_id': 'Neighborhood',
#                 'filter_query': '{City} eq "Los Angeles"'
#             },
#             'options': [
#                             {'label': i, 'value': i}
#                             for i in [
#                                 'Venice',
#                                 'Hollywood',
#                                 'Los Feliz'
#                             ]
#                         ],
#             'clearable':True
#         }]
#     ),
#
# ])

if __name__ == "__main__":
    app.run_server(debug=True)