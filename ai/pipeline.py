from ai.sql_generator import generate_sql
from database.sql_executor import execute_query
from prompts.sql_prompt import build_sql_prompt
from ai.sql_corrector import correct_sql


def ask_database(question: str, config: dict):

    response = {
        "question": question,
        "sql": "",
        "data": None,
        "error": None
    }

    try:

        # -------------------------
        # Generate SQL
        # -------------------------

        sql = generate_sql(
            question,
            config
        )

        response["sql"] = sql

        print("\nGenerated SQL:\n")
        print(sql)

        # -------------------------
        # Execute SQL
        # -------------------------

        data = execute_query(
            sql,
            config
        )

        response["data"] = data

    except Exception as sql_error:

        print("\nSQL Execution Failed")
        print(sql_error)

        try:

            print("\nTrying to correct SQL...\n")

            prompt = build_sql_prompt(
                question,
                config
            )

            fixed_sql = correct_sql(
                sql,
                str(sql_error),
                prompt
            )

            response["sql"] = fixed_sql

            print("\nCorrected SQL:\n")
            print(fixed_sql)

            data = execute_query(
                fixed_sql,
                config
            )

            response["data"] = data

        except Exception as final_error:

            error_message = str(final_error)

            if (
                "429" in error_message
                or "RESOURCE_EXHAUSTED" in error_message
            ):

                error_message = (
                    "⚠️ Gemini API quota exceeded. Please wait a minute and try again."
                )

            response["error"] = error_message

    return response


if __name__ == "__main__":

    question = input("Ask: ")

    config = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "YOUR_PASSWORD",
        "database": "YOUR_DATABASE"
    }

    result = ask_database(
        question,
        config
    )

    print("\nGenerated SQL:\n")
    print(result["sql"])

    print("\nResult:\n")
    print(result["data"])

    if result["error"]:

        print("\nError:")
        print(result["error"])