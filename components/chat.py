import streamlit as st

from ai.pipeline import ask_database


def render_chat():

    if "messages" not in st.session_state:

        st.session_state.messages = []

    # ---------------- Chat History ---------------- #

    for i, message in enumerate(st.session_state.messages):

        with st.chat_message(message["role"]):

            if message["role"] == "user":

                st.write(message["content"])

            else:

                st.subheader("Generated SQL")

                st.code(
                    message["sql"],
                    language="sql"
                )

                if message["data"] is not None:

                    st.subheader("Result")

                    st.dataframe(
                        message["data"],
                        use_container_width=True
                    )

                    csv = message["data"].to_csv(
                        index=False
                    ).encode("utf-8")

                    st.download_button(

                        "📥 Download CSV",

                        csv,

                        file_name=f"query_{i}.csv",

                        mime="text/csv",

                        key=f"download_{i}"

                    )

    # ---------------- Chat Input ---------------- #

    question = st.chat_input(
        "Ask anything about your database..."
    )

    if question:

        if "db_config" not in st.session_state:

            st.error(
                "Please upload a database or connect MySQL first."
            )

            return

        st.session_state.messages.append(

            {

                "role": "user",

                "content": question

            }

        )

        with st.spinner("Generating SQL..."):

            result = ask_database(

                question,

                st.session_state.db_config

            )

        if result["error"]:

            st.error(result["error"])

            return

        st.session_state.messages.append(

            {

                "role": "assistant",

                "sql": result["sql"],

                "data": result["data"]

            }

        )

        st.rerun()