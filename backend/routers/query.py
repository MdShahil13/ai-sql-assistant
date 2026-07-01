from fastapi import APIRouter
from pydantic import BaseModel

from services.schema_service import get_database_schema
from services.sql_generator import generate_sql
from services.sql_executor import execute_sql
from services.table_state import get_current_table

router = APIRouter()


class Question(BaseModel):
    question: str


@router.post("/ask")
def ask(question: Question):

    table_name = get_current_table()

    if table_name is None:
        return {
            "error": "No CSV uploaded."
        }

    schema = get_database_schema(table_name)

    sql = generate_sql(
        schema=schema,
        question=question.question
    )

    print("Generated SQL:")
    print(sql)

    results = execute_sql(sql)

    return {
        "table": table_name,
        "generated_sql": sql,
        "results": results
    }