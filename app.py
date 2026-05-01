import streamlit as st
import os
from groq import Groq
import json
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="LearnerAI Coach", page_icon="grad_cap", layout="wide")

st.markdown("""
<style>
    :root { --primary: #6366f1; --secondary: #a855f7; --bg: #0f172a; }
        .stApp { background: radial-gradient(circle at 0% 0%, rgba(99, 102, 241, 0.15) 0%, transparent 50%); }
            .grad-text { background: linear-gradient(135deg, #6366f1, #a855f7); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 900; }
            </style>
            """, unsafe_allow_html=True)

st.markdown('<h1 class="grad-text">LearnerAI Coach</h1>', unsafe_allow_html=True)
st.write("Premium UI is loading...")
