import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

df = px.data.tips()

connection_string = "postgresql://postgres:sunny123@localhost:5432/postgre_flask"
df.to_sql("tip_table", connection_string)

print("completes")