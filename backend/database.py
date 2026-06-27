import psycopg2

try:
  connection = psycopg2.connect(
    host="localhost",
    database="ai_sql_assistant",
    user="postgres",
    password="Shahil@13" 
    )
  print("Database connection successful!")
except Exception as e:
  print("Error connecting to the database:", e)
