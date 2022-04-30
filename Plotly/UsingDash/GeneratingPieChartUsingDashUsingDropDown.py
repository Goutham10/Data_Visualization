import pandas as pd 
from dash import Dash, html, dcc, Input, Output
import plotly.express as px 


df = pd.read_csv('/home/vy/Downloads/Urban_Park_Ranger_Animal_Condition.csv')

app = Dash(__name__)

app.layout = html.Div([
    
    html.Div([
        dcc.Graph(id = "our_graph")
    ], className = "nine columns"),

    html.Div([
        html.Br(),
        html.Div(id = 'output_data'),
        html.Br(),

        html.Label(['Choose column : '], style = {'font-weight' : 'bold', 'text-align' : 'center'}),

        dcc.Dropdown(id = 'my_dropdown',
            options = [
                {'label': 'Species', 'value': 'Animal Class'},
                {'label': 'Final Ranger Action', 'value': 'Final Ranger Action'},
                {'label': 'Age', 'value': 'Age', 'disabled':True},
                {'label': 'Animal Condition', 'value': 'Animal Condition'},
                {'label': 'Borough', 'value': 'Borough'},
                {'label': 'Species Status', 'value': 'Species Status'}
            ],
            optionHeight = 35,
            value = 'Borough',
            disabled = False,
            multi = False,
            searchable = True,
            search_value= '',
            placeholder='please select...',
            clearable= True, 
            style={'width' : '90%'},
            className = 'select_box',
            persistence=True,
            persistence_type='session'
        )
    ], className = 'three columns')

])


@app.callback(
    Output(component_id = 'our_graph', component_property = 'figure'),
    [Input(component_id='my_dropdown', component_property="value")]
)

def build_graph(column_chosen):
    dff=df
    fig = px.pie(dff,names=column_chosen)
    fig.update_traces(textinfo='percent+label')
    fig.update_layout(title={'text':'NYC Calls for Animal Rescue',
                      'font':{'size':28},'x':0.5,'xanchor':'center'})
    return fig


@app.callback(
    Output(component_id='output_data', component_property='children'),
    [Input(component_id='my_dropdown', component_property='search_value')]
)

def build_graph(data_chosen):
    return ('Search value was: " {} "'.format(data_chosen))


# def update_graph(my_dropdown):
#     dff = df

#     pie_chart = px.pie(
#         data_frame = dff,
#         names = my_dropdown,
#         hole = 0.3
#     )

#     return pie_chart


if __name__ =="__main__":
    app.run_server(debug = True)