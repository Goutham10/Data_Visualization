import pandas as pd 
import plotly.express as px
import plotly.io as pio


df = pd.read_csv('/home/vy/Downloads/covid-19-states-daily.csv')

df['dateChecked'] = pd.to_datetime(df['dateChecked'])

df = df[df['dateChecked'].dt.date.astype(str) == "2020-03-17"]

pie_chart = px.pie(
    data_frame = df,
    values = 'death',
    names = 'state',
    color = 'state',
    # color_discrete_sequence= ['red', 'yellow', 'green','blue']
    # color_discrete_map= {'WA' : 'yellow', 'Ak' : 'red', 'AZ' : 'cyan', 'KS' : 'orange'}
    # hover_name = 'negative'
    # hover_data = ['positive', 'negative']
    # custom_data=['total']
    # labels = {"state" : "The State"}
    title="Coronavirus in USA",
    # template='presentation',
    # width=3000,
    # height=800,
    # hole= 0.5


)

pie_chart.update_traces(
    textposition = 'outside',
    textinfo = 'percent + label',
    # marker = 'line',
    pull = [0,0,0.2,0],
    opacity = 0.7,
    rotation = 180)


pio.show(pie_chart)