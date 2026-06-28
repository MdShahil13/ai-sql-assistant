from fastapi import APIRouter
from pydantic import BaseModel

from services.schema_service import get_database_schema
from services.sql_generator import generate_sql

router = APIRouter()


class Question(BaseModel):
    question: str


@router.post("/generate-sql")
def generate(question: Question):

    schema = get_database_schema()

    sql = generate_sql(
        schema=schema,
        question=question.question
    )

    return {
        "generated_sql": sql
    }