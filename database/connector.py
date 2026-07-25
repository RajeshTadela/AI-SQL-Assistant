import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


def get_connection(config):
    """
    Returns a MySQL connection.

    Priority:
    1. Use provided config
    2. Otherwise use .env values
    """

    if config:

        host = config["host"]
        port = config["port"]
        user = config["user"]
        password = config["password"]
        database = config["database"]

    else:

        host = os.getenv("DB_HOST")
        port = os.getenv("DB_PORT")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        database = os.getenv("DB_NAME")

    connection = mysql.connector.connect(

        host=host,
        port=port,
        user=user,
        password=password,
        database=database

    )

    return connection

def test_connection():

    try:

        connection = get_connection(None)

        if connection.is_connected():

            print("✅ Successfully connected to MySQL!")

            connection.close()

            print("Connection closed")

    except Exception as e:

        print("❌ Connection Failed")

        print(e)


if __name__ == "__main__":

    test_connection()