import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="AI Learning Coach", layout="wide")

f = open("index.html", "r", encoding="utf-8")
html_code = f.read()
f.close()

components.html(html_code, height=1000, scrolling=True)
