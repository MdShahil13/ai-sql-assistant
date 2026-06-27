try:
    from llm.lm import llm
except ModuleNotFoundError:
    from lm import llm

response = llm.invoke("Generate a SQL query to find the average salary of employees in the 'Engineering' department.")

print(response.content)