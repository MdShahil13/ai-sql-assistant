import psycopg2

try:
  connection = psycopg2.connect(
    host="localhost",
    database="ai_sql_assistant",
    user="postgres",
    password="Shahil@13" 
    )
  print("Database connection successful!")
  cursor = connection.cursor()
  cursor.execute(""" 
               CREATE TABLE IF NOT EXISTS Employess (
               id SERIAL PRIMARY KEY,
               name VARCHAR(100) NOT NULL,  
               salary INT)
               """)

  connection.commit()
  print("Table created successfully!")
  cursor.close()
  connection.close()
except Exception as e:
  print("Error connecting to the database:", e)
