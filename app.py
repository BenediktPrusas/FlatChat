import streamlit as st
from scraper import get_wg_gesucht_flat_description
from text_generation import generate_intro, generate_intro_self_improvement
from utils import init_session

init_session()

st.title("FlatChats :house:")
st.markdown("""
Willkommen bei FlatChat, Ihrem automatisierten Assistenten zur Generierung von Anschreiben für Wohngemeinschaften.
Geben Sie einfach den Link zur Anzeige auf WG-Gesucht unten ein.
FlatChat personalisiert Ihre Nachricht basierend auf den Informationen, die auf der Seite 'Persönliche Informationen' hinterlegt sind.
Der Grundtext kann ebenfalls auf einer separaten Seite eingesehen und angepasst werden.
""")

url = st.text_input("Enter WG-Gesucht URL:")
self_improvement = st.checkbox("Self-Improvement Mode")
st.divider()

if st.button("Generate Intro"):
    flat_description = get_wg_gesucht_flat_description(url)

    if not self_improvement:
        flat_intro = generate_intro(flat_description, st.session_state["personal_info"], st.session_state["base_prompt"])
        st.markdown(flat_intro)
    else:
        flat_intro_2, flat_intro_1, critiqe = generate_intro_self_improvement(flat_description, st.session_state["personal_info"], st.session_state["base_prompt"])
        st.markdown(flat_intro_2)
        with st.expander("Kritik"):
            st.markdown("Erster Vorschlag:")
            st.markdown(flat_intro_1)
            st.markdown("Hier ist die Kritik von GPT:")
            st.markdown(critiqe)