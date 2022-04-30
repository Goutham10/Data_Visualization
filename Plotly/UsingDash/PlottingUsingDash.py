import plotly.express as px
from dash import Dash, html, dcc
import pandas as pd
import numpy as np
# import chart_studio.plotly as py
import seaborn as sns
import cufflinks as cf
import plotly.graph_objects as go

# fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
# fig.write_html('first_figure.html', auto_open=True)

app = Dash(__name__)

#styling
colors = {
    'background' : '#11111',
    'text' : '#7FDBFF'
}

# random data 
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})


##plot by using bar plot
fig = px.bar(df, 
             x = 'Fruit',
             y = 'Amount',
             color = 'City',
             barmode= 'group'
            )

# fig = go.Figure()

# fig.add_trace(go.Scatter(data = df,
#                      x = ['Fruit'],
#                      y = ['Amount'],
#                      color = 'City',
#                      barmode = 'group', ))

# fig.update_layout(
#     plot_bgcolor = colors["background"],
#     paper_bgcolor = colors["background"],
#     font_color = colors["text"]
# )

#layout section using html components
app.layout = html.Div(style={'backgroundColor' : colors["background"]}, children=[
                html.H1(children='Hello Dash',
                        style={
                            'textAlign' : 'center',
                            'color' : colors["text"]
                        }
                        ),
                html.Div(children= '''
                    Dash : A web application framework for your data.
                ''', style= {
                    'textAlign' : 'center',
                    'color' : colors["text"]
                }),
                dcc.Graph(
                    id = 'example-graph',
                    figure= fig
                )
            ])
    
if __name__ == "__main__":
    app.run_server(debug=True)