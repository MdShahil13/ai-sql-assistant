from fastapi import FastAPI, UploadFile, File
import pandas as pd
from sqlalchemy import create_engine
import os

app = FastAPI()

engine = create_engine(
    "postgresql://postgres:Shahil%4013@localhost:5432/ai_sql_assistant"
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "AI SQL ASSISTANT Backend is running!"}

@app.post("/upload")
async def upload_csv(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    df = pd.read_csv(file_path)

    table_name = file.filename.split(".")[0]

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    return {
        "message": "File uploaded successfully",
        "table_name": table_name,
        "rows": len(df)
    }