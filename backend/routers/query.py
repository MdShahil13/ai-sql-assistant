from fastapi import APIRouter
from pydantic import BaseModel

from services.schema_service import get_database_schema
from services.sql_generator import generate_sql
from services.sql_validator import validate_sql
from services.sql_executor import execute_sql

router = APIRouter()


class Question(BaseModel):
    question: str


@router.post("/generate-sql")
def generate(question: Question):

    # Step 1: Read database schema
    schema = get_database_schema()

    # Step 2: Generate SQL using LLM
    sql = generate_sql(
        schema=schema,
        question=question.question
    )

    # Step 3: Validate SQL
    validate_sql(sql)

    # Step 4: Execute SQL
    result = execute_sql(sql)

    # Step 5: Return response
    return {
        "generated_sql": sql,
        "result": result
    }