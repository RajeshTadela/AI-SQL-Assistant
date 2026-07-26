from pathlib import Path
import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


def get_csv_files(folder_path):
    folder = Path(folder_path)
    return list(folder.glob("*.csv"))


def read_csv(file_path):
    return pd.read_csv(file_path)


def infer_mysql_type(dtype):

    dtype = str(dtype)

    if "int" in dtype:
        return "INT"

    elif "float" in dtype:
        return "DOUBLE"

    elif "datetime" in dtype:
        return "DATETIME"

    elif "bool" in dtype:
        return "BOOLEAN"

    return "VARCHAR(255)"


def create_table(cursor, table_name, dataframe):
    """
    Create a MySQL table with an auto-generated primary key.
    """

    columns = [
        "`id` INT AUTO_INCREMENT PRIMARY KEY"
    ]

    for column_name, dtype in dataframe.dtypes.items():

        mysql_type = infer_mysql_type(dtype)

        columns.append(
            f"`{column_name}` {mysql_type}"
        )

    column_query = ",\n".join(columns)

    query = f"""
    CREATE TABLE IF NOT EXISTS `{table_name}` (
        {column_query}
    );
    """

    cursor.execute(query)


def insert_data(cursor, table_name, dataframe):

    dataframe = dataframe.where(pd.notnull(dataframe), None)

    columns = ", ".join(
        [f"`{c}`" for c in dataframe.columns]
    )

    placeholders = ", ".join(
        ["%s"] * len(dataframe.columns)
    )

    query = f"""
    INSERT INTO `{table_name}`
    ({columns})
    VALUES ({placeholders})
    """

    data = [
        tuple(row)
        for row in dataframe.itertuples(index=False)
    ]

    cursor.executemany(query, data)


def import_folder(folder, database_name):

    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    cursor = connection.cursor()

    cursor.execute(
        f"CREATE DATABASE IF NOT EXISTS `{database_name}`"
    )

    cursor.execute(
        f"USE `{database_name}`"
    )

    files = get_csv_files(folder)

    for file in files:

        dataframe = read_csv(file)

        table_name = (
            file.stem
            .replace("-", "_")
            .replace(" ", "_")
            .lower()
        )

        create_table(cursor, table_name, dataframe)

        insert_data(cursor, table_name, dataframe)

    connection.commit()

    cursor.close()
    connection.close()