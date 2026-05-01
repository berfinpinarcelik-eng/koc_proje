import streamlit as st
import os
from groq import Groq
import json
from dotenv import load_dotenv
load_dotenv()
st.set_page_config(page_title="Coach")
client = Groq()
st.title("Coach")
if "messages" not in st.session_state:
        st.session_state.messages = []
    for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])
        if prompt := st.chat_input("Sor?"):
                st.session_state.messages.append({"role": "user", "content": prompt})
                st.chat_message("user").write(prompt)
                resp = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=[{"role": "user", "content": prompt}])
                st.session_state.messages.append({"role": "assistant", "content": resp.choices[0].message.content})
                st.chat_message("assistant").write(resp.choices[0].message.content)
            
