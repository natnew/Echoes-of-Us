# Entry point for the app

import streamlit as st

# Set the page title and layout
st.set_page_config(
    page_title="Echoes of Us",  # This sets the browser tab name
    layout="wide"
)

st.sidebar.title("Echoes of Us")
st.sidebar.write("Preserving diverse cultural heritage with AI.")
st.sidebar.markdown("""
- **[Home](1_Home.py)**  
- **[Virtual Museum](2_Virtual_Museum.py)**  
- **[Historical Reconstruction](3_Historical_Reconstruction.py)**  
- **[Language Revitalisation](4_Language_Revitalisation.py)**  
- **[About](5_About.py)**  
""")

st.write("Welcome to *Echoes of Us*! Use the menu on the left to navigate.")

