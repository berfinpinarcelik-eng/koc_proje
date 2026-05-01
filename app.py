import streamlit as st
import os
from groq import Groq
import json
from dotenv import load_dotenv

load_dotenv()

# Sayfa Konfigurasyonu
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

                                            .main {
                                                    background-color: var(--bg);
                                                            font-family: 'Plus Jakarta Sans', sans-serif;
                                                                }

                                                                    /* Arka Plan Efektleri */
                                                                        .stApp {
                                                                                background: radial-gradient(circle at 0% 0%, rgba(99, 102, 241, 0.15) 0%, transparent 50%),
                                                                                                    radial-gradient(circle at 100% 100%, rgba(168, 85, 247, 0.15) 0%, transparent 50%);
                                                                                                        }
                                                                                                        
                                                                                                            /* Kart Tasarimi */
                                                                                                                .st-emotion-cache-1r6slb0, .st-emotion-cache-12w0qpk {
                                                                                                                        background: rgba(30, 41, 59, 0.7) !important;
                                                                                                                                backdrop-filter:
