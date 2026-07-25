import pandas as pd
from database.connector import get_connection


def execute_query(query, config):

    connection = get_connection(config)

    cursor = connection.cursor()

    cursor.execute(query)

    rows = cursor.fetchall()

    columns = [column[0] for column in cursor.description]

    cursor.close()
    connection.close()

    return pd.DataFrame(rows, columns=columns)