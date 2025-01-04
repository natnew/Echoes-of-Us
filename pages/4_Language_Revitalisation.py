# Language preservation tools

import streamlit as st
from utils.runway_api import text_to_speech

# Language Revitalisation Page Title
st.title("Language Revitalisation")

# Description
st.markdown("""
Preserve endangered languages by generating text or audio resources using AI.
- Convert text into audio in endangered languages.
- Create teaching materials for language preservation.
""")

# Input Fields
language = st.selectbox("Choose a language:", ["Swahili", "Mandarin", "Hausa", "Others"])
text = st.text_area("Enter text to convert to speech:", placeholder="Type your text here...")

# Generate Audio
if st.button("Generate Audio"):
    if text:
        audio = text_to_speech(text, language)
        if audio:
            st.audio(audio, format="audio/mp3", start_time=0)
        else:
            st.error("Error generating audio. Please try again.")
    else:
        st.warning("Please enter text to convert.")
