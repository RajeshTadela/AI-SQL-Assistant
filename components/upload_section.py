import streamlit as st
import os

from utils.file_manager import (
    save_uploaded_files,
    clear_uploads
)

from database.importer import import_folder


def render_upload_section():

    st.subheader("Upload CSV Files")

    database_name = st.text_input(
        "Database Name",
        placeholder="Example : sales_db"
    )

    uploaded_files = st.file_uploader(
        "Choose CSV Files",
        type=["csv"],
        accept_multiple_files=True
    )

    if st.button("📥 Import Files", use_container_width=True):

        if database_name.strip() == "":

            st.error("Please enter a database name.")

            return

        if not uploaded_files:

            st.error("Please upload at least one CSV file.")

            return

        folder = save_uploaded_files(uploaded_files)

        with st.spinner("Importing Database..."):

            import_folder(
                folder=folder,
                database_name=database_name
            )

        st.session_state.db_config = {
            "host": os.getenv("DB_HOST"),
            "port": int(os.getenv("DB_PORT")),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
            "database": database_name
        }

        clear_uploads()

        st.success("✅ Database Imported Successfully")