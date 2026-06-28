from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql://postgres:Shahil%4013@localhost:5432/ai_sql_assistant"
)

def execute_sql(sql: str):
    """
    Executes a SELECT query and returns the result as a list of dictionaries.
    """

    with engine.connect() as connection:

        result = connection.execute(text(sql))

        rows = result.fetchall()

        columns = result.keys()

        data = []

        for row in rows:
            data.append(dict(zip(columns, row)))

        return data