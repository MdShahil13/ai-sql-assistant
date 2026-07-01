from services.schema_service import get_database_schema
from services.sql_generator import generate_sql
from services.sql_executor import execute_sql


def ask_database(question: str):

    schema = get_database_schema()

    sql = generate_sql(
        schema=schema,
        question=question
    )

    results = execute_sql(sql)

    return {
        "generated_sql": sql,
        "results": results
    }