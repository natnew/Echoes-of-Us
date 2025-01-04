# Historical artifact reconstruction

import streamlit as st
from utils.runway_api import inpaint_image

# Historical Reconstruction Page Title
st.title("Historical Reconstruction")

# Description
st.markdown("""
Restore damaged or missing cultural artifacts using AI-powered image inpainting.
Upload an image and provide a description of what’s missing or damaged, and let the AI restore it for you.
""")

# File Uploader
uploaded_file = st.file_uploader("Upload an image of the artifact:", type=["jpg", "jpeg", "png"])
prompt = st.text_input("Describe the missing or damaged parts:")

# Reconstruction Button
if st.button("Reconstruct Artifact"):
    if uploaded_file and prompt:
        reconstructed_image = inpaint_image(uploaded_file, prompt)
        if reconstructed_image:
            st.image(reconstructed_image, caption="Reconstructed Artifact")
        else:
            st.error("Error reconstructing the artifact. Please try again.")
    elif not uploaded_file:
        st.warning("Please upload an image.")
    elif not prompt:
        st.warning("Please provide a description of the missing parts.")

