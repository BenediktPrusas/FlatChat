import streamlit as st

def init_session():

    if "base_prompt" not in st.session_state:
        with open('base_prompt.txt') as f:
            st.session_state["base_prompt"] = f.read()

    if "personal_info" not in st.session_state:
        with open('personal_information.txt') as f:
            st.session_state["personal_info"] = f.read()