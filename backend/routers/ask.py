from fastapi import APIRouter
from pydantic import BaseModel

from services.query_service import ask_database

router = APIRouter()


class Question(BaseModel):
    question: str


@router.post("/ask")
def ask(question: Question):

    return ask_database(question.question)