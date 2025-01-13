# Runway API interaction logic

# Runway API interaction logic

import requests
import json
import streamlit as st

def call_runway_model(prompt, model_endpoint):
    """Generic function to call Runway API models."""
    api_key = st.secrets["RUNWAY_API_KEY"]
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        # Add Accept header if required for the API version
        "Accept": "application/vnd.runwayml.v2+json"
    }
    data = {"prompt": prompt}
    
    response = requests.post(model_endpoint, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 400:
        st.error(f"Invalid Request: {response.json().get('error')}")
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
    return None

def generate_image(prompt):
    """Call the Stable Diffusion model."""
    endpoint = "https://api.runwayml.com/v1/models/stable-diffusion"
    result = call_runway_model(prompt, endpoint)
    if result:
        return result.get("image")
    return None

def inpaint_image(prompt, image_path):
    """Call an inpainting model for image reconstruction."""
    endpoint = "https://api.runwayml.com/v1/models/inpainting"
    headers = {
        "Authorization": f"Bearer {st.secrets['RUNWAY_API_KEY']}",
        "Accept": "application/vnd.runwayml.v2+json"
    }
    files = {"image": open(image_path, "rb")}
    data = {"prompt": prompt}
    response = requests.post(endpoint, headers=headers, data=data, files=files)
    if response.status_code == 200:
        return response.json().get("image")
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
    return None

def text_to_speech(text, language):
    """Call a TTS model."""
    endpoint = "https://api.runwayml.com/v1/models/text-to-speech"
    result = call_runway_model(text, endpoint)
    if result:
        return result.get("audio")
    return None
