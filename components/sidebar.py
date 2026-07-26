import streamlit as st


def render_sidebar():
    with st.sidebar:

        st.title("🤖 AI SQL Assistant")

        st.markdown("---")

        if "db_config" in st.session_state:

            database = st.session_state.db_config.get("database", "")

            st.success(f"🟢 Connected\n\n{database}")

        else:

            st.warning("🔴 No Database Connected")

        st.markdown("---")

        if st.button("🗑 Clear Chat", use_container_width=True):

            st.session_state.messages = []

            st.rerun()