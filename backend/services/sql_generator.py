from llm.lm import llm

def generate_sql(schema: str, question: str):

    prompt = f"""
You are an expert PostgreSQL SQL generator.

Database Schema:

{schema}

Rules:
1. Return ONLY SQL.
2. Do not explain anything.
3. Do not use markdown.
4. Use only tables and columns from the schema.

User Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content.strip()