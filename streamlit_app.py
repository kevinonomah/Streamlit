import streamlit as st
from langchain_openai import ChatOpenAI

st.image("DSU_Logo.png", width=100)
st.title("🦜🔗 Quickstart App")

# The key is typed in by the user at runtime and never stored in the repo.
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
model = st.sidebar.text_input("Model", value="gpt-4o-mini")


def generate_response(input_text: str) -> None:
    llm = ChatOpenAI(model=model, temperature=0.7, api_key=openai_api_key)
    st.info(llm.invoke(input_text).content)


with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )
    submitted = st.form_submit_button("Submit")
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")
    if submitted and openai_api_key.startswith("sk-"):
        generate_response(text)
