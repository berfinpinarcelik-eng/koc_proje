import streamlit as st
import streamlit.components.v1 as components
import os
from groq import Groq

st.set_page_config(page_title="AI Learning Coach", layout="wide")

GROQ_API_KEY = st.secrets.get("GROQ_API_KEY")

if GROQ_API_KEY:
      st.sidebar.success("API Key is active")
else:
      st.sidebar.error("Please add GROQ_API_KEY to Secrets")

try:
      with open("index.html", "r", encoding="utf-8") as f:
                html_code = f.read()
            components.html(html_code, height=1000, scrolling=True)
except Exception as e:
    st.error(f"Error loading HTML: {e}")
