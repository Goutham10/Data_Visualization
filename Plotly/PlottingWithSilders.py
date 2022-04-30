import plotly.express as px
import numpy as np
import pandas as pd
import plotly.graph_objects as go

df = px.data.tips()

fig  = go.Figure(
    data = [
        go.Scatter(
            # x = df['total_bill'],
            y = df['tip'],
            mode = 'lines', # type of plot like lines, markers, etc 
        )
    ]
)

fig.update_layout(
    xaxis = dict(
                rangeselector = dict(
                    buttons = list([
                        dict(count = 1,
                            step = 'day',
                            stepmode = 'backward'
                        ),
                    ])
                ),
                rangeslider = dict(
                    visible = True
                ),
            )
    )

fig.show()