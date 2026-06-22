import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:Shahil%4013@localhost:5432/ai_sql_assistant')
df = pd.read_sql("SELECT * FROM sample_data WHERE department = 'IT'", engine)

print(df)