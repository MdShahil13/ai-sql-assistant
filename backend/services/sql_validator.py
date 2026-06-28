def validate_sql(sql: str):
    """
    Allow only SELECT queries.
    Raise an exception for anything else.
    """

    sql = sql.strip().lower()

    if not sql.startswith("select"):
        raise Exception("Only SELECT queries are allowed.")

    return True
