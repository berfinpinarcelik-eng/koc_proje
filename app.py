import streamlit as st
import os
from groq import Groq
import json
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="LearnerAI Coach", page_icon=":grad:", layout="wide", initial_sidebar_state="collapsed")

# --- PREMIUM CSS ENTEGRASYONU ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap');
        :root {
                --primary: #6366f1;
                        --secondary: #a855f7;
                                --bg: #0f172a;
                                    }
                                    
