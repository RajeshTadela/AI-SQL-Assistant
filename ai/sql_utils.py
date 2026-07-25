import re


def clean_sql(sql: str) -> str:
    """
    Remove markdown formatting and extra whitespace.
    """

    sql = re.sub(r"```sql", "", sql, flags=re.IGNORECASE)
    sql = re.sub(r"```", "", sql)

    return sql.strip()


def validate_sql(sql: str):
    """
    Basic SQL validation.
    """

    if not sql:
        return False, "Empty SQL generated."

    if sql.upper() == "CANNOT_GENERATE_SQL":
        return False, "Cannot generate SQL for this question."

    return True, ""