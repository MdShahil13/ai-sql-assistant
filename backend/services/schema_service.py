from sqlalchemy import create_engine, inspect

engine = create_engine(
    "postgresql://postgres:Shahil%4013@localhost:5432/ai_sql_assistant"
)


def get_database_schema(table_name):

    inspector = inspect(engine)

    schema = f"Table: {table_name}\n"

    columns = inspector.get_columns(table_name)

    for column in columns:
        schema += f"- {column['name']} ({column['type']})\n"

    return schema