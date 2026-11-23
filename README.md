# LangChain Quickstart (Streamlit)

A small Streamlit app that sends a prompt to an OpenAI chat model through
[LangChain](https://python.langchain.com/) and shows the answer. Built as an
introduction to LLM apps at Dakota State University.

## Run it

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Enter your OpenAI API key in the sidebar (it's a password field and is only
held for the session), type a prompt, and press **Submit**. The model name
can be changed in the sidebar; it defaults to `gpt-4o-mini`.

Never commit an API key to this repo. The app asks for it at runtime so it
doesn't need one in the code.
