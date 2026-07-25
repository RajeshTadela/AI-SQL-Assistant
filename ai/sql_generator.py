from ai.llm import ask_gemini
from prompts.sql_prompt import build_sql_prompt
from ai.sql_utils import clean_sql, validate_sql


def generate_sql(question: str, config: dict) -> str:
    """
    Generate SQL from a natural language question.
    """

    # Build prompt using current database schema
    prompt = build_sql_prompt(
        question,
        config
    )

    # Ask Gemini
    sql = ask_gemini(prompt)

    # Clean generated SQL
    sql = clean_sql(sql)

    # Validate SQL
    valid, message = validate_sql(sql)

    if not valid:
        raise ValueError(message)

    return sql


if __name__ == "__main__":

    question = input("Ask a question: ")

    # Example configuration
    config = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "YOUR_PASSWORD",
        "database": "YOUR_DATABASE"
    }

    sql = generate_sql(
        question,
        config
    )

    print("\nGenerated SQL:\n")
    print(sql)