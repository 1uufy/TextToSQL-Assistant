
import streamlit as st
import pandas as pd

from src.assistant import ask_database


st.set_page_config(
    page_title="Text-to-SQL Assistant",
    page_icon="🗄️",
    layout="wide"
)

st.title("🗄️ Intelligent Text-to-SQL Assistant")
st.write(
    "Ask questions about your employee database "
    "in plain English."
)

st.info(
    "Example: Show the five highest-paid employees."
)

# Keep conversation history during the session
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous questions and results
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message.get("sql"):
            st.code(message["sql"], language="sql")

        if message.get("rows") is not None:
            if message["rows"]:
                st.dataframe(
                    pd.DataFrame(message["rows"]),
                    use_container_width=True
                )
            else:
                st.write("The query returned no rows.")

        if message.get("error"):
            st.error(message["error"])

# Accept a new question
question = st.chat_input(
    "Ask a question about your employees..."
)

if question:
    # Display and save the user's question
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    # Generate SQL and retrieve database results
    with st.chat_message("assistant"):
        with st.spinner("Generating SQL and querying the database..."):
            try:
                result = ask_database(question)

                st.markdown("### Generated SQL")
                st.code(result["sql"], language="sql")

                if result["success"]:
                    st.markdown("### Query Results")

                    if result["rows"]:
                        df = pd.DataFrame(result["rows"])
                        st.dataframe(
                            df,
                            use_container_width=True
                        )
                    else:
                        st.info("No matching records found.")

                    st.caption(
                        f"Rows returned: {result['row_count']}"
                    )

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": "Here are your database results.",
                        "sql": result["sql"],
                        "rows": result["rows"]
                    })

                else:
                    st.error(result["error"])

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": "I couldn't complete that query.",
                        "sql": result["sql"],
                        "error": result["error"]
                    })

            except Exception as error:
                st.error(f"Something went wrong: {error}")

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": "The request failed.",
                    "error": str(error)
                })
