# About the project and contributors

import streamlit as st

# About Page Title
st.title("About Echoes of Us")
st.markdown("### Celebrating Cultural Diversity with Cutting-Edge AI")

# Section: Overview
st.markdown("""
At **Echoes of Us**, we blend creativity and technology to preserve, restore, and celebrate cultural heritage.  
Our tools empower individuals and communities to use AI for cultural preservation and exploration.  
""")

# Section: Features Overview (Similar to "Generate Anything")
st.markdown("---")
st.header("Explore Our Features")

# Feature 1: Virtual Museum
col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://via.placeholder.com/200", caption="Virtual Museum")
with col2:
    st.markdown("""
    **Virtual Museum**  
    Create AI-powered cultural artifacts and visuals.  
    Describe a scene or object, and let the AI bring it to life!
    """)

# Feature 2: Historical Reconstruction
col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://via.placeholder.com/200", caption="Historical Reconstruction")
with col2:
    st.markdown("""
    **Historical Reconstruction**  
    Restore damaged or incomplete cultural artifacts using advanced models.
    Upload an image, and the AI will help reconstruct its missing parts.
    """)

# Feature 3: Language Revitalisation
col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://via.placeholder.com/200", caption="Language Revitalisation")
with col2:
    st.markdown("""
    **Language Revitalisation**  
    Preserve endangered languages with AI-generated text and audio tools.  
    Perfect for creating teaching materials or preserving oral traditions.
    """)

# Section: Acknowledgements
st.markdown("---")
st.header("Acknowledgements")
st.markdown("""
We are deeply grateful to our partners and supporters for their contributions:
- **OpenAI**: Foundational AI research and technology.
- **RunwayML**: Tools for creative AI workflows.
- **Cultural Heritage Preservation Society**: Expertise and guidance.

Together, we aim to ensure that the echoes of our shared history resonate for generations to come.
""")

# Section: Call to Action
st.markdown("---")
st.header("Join Us")
st.markdown("""
Want to contribute to the mission?  
Reach out to us at [support@echoesofus.com](mailto:support@echoesofus.com).  
Let's preserve the world's cultural heritage together.
""")
