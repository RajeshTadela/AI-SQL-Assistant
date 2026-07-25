import streamlit as st

from components.sidebar import render_sidebar
from components.upload_section import render_upload_section
from components.mysql_section import render_mysql_section
from components.chat import render_chat

st.set_page_config(
    page_title="AI SQL Assistant",
    page_icon="🤖",
    layout="wide"
)

render_sidebar()

st.title("🤖 AI SQL Assistant")

st.caption(
    "Ask questions about your database using natural language."
)

choice = st.radio(
    "Choose Data Source",
    [
        "Upload CSV Files",
        "Connect MySQL Database"
    ]
)

if choice == "Upload CSV Files":
    render_upload_section()

else:
    render_mysql_section()

st.divider()

render_chat()