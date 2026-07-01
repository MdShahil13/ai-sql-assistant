from fastapi import FastAPI, UploadFile, File
import pandas as pd
from sqlalchemy import create_engine
from routers.query import router as query_router
from routers.ask import router as ask_router
import os
from fastapi.middleware.cors import CORSMiddleware
from services.table_state import set_current_table

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

    set_current_table(table_name)

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

app.include_router(query_router)
app.include_router(ask_router)