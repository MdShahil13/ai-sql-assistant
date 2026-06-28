from sqlalchemy import create_engine, inspect

engine = create_engine(
    "postgresql://postgres:Shahil%4013@localhost:5432/ai_sql_assistant"
)

def get_database_schema():

    inspector = inspect(engine)

    schema = ""

    tables = inspector.get_table_names()

    for table in tables:

        schema += f"\nTable: {table}\n"

        columns = inspector.get_columns(table)

        for column in columns:
            schema += f"- {column['name']} ({column['type']})\n"

    return schema