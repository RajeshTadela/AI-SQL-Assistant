import streamlit as st

from database.connector import get_connection


def render_mysql_section():

    st.subheader("Connect MySQL Database")

    host = st.text_input(
        "Host",
        value="localhost"
    )

    port = st.text_input(
        "Port",
        value="3306"
    )

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    database = st.text_input("Database")

    if st.button("🔗 Connect", use_container_width=True):

        config = {

            "host": host,

            "port": port,

            "user": username,

            "password": password,

            "database": database

        }

        try:

            connection = get_connection(config)

            connection.close()

            st.session_state.db_config = config

            st.success("✅ Connected Successfully")

        except Exception as e:

            st.error(str(e))