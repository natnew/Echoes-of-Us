# Virtual museum: artifact and scene generation

import streamlit as st
from utils.runway_api import generate_image

st.title("Virtual Museum")
st.write("Describe an artifact or scene to generate a visual representation.")

prompt = st.text_input("Enter your description:")
if st.button("Generate Artifact"):
    if prompt:
        result = generate_image(prompt)
        if result:
            st.image(result, caption="Generated Artifact")
        else:
            st.error("Unable to generate the artifact. Please try again.")
    else:
        st.warning("Please enter a description.")
