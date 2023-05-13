import streamlit as st
from utils import init_session

init_session()

st.session_state["personal_info"]= st.text_area("Persönliche Informationen über dich:",
                                                value=st.session_state["personal_info"],
                                                height=600)