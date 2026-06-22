import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:Shahil%4013@localhost:5432/ai_sql_assistant')

df = pd.read_csv('sample.csv')

df.to_sql(
    "sample_data",
    engine,
    if_exists="replace",
    index=False
)

print("CSV uploaded successfully!")