import streamlit as st
import requests

API_URL = "http://fastapi-backend:8000"

# Set page title
st.set_page_config(page_title="Solita Electricity Data")

st.title("Solita Electricity Dashboard")
st.write("Frontend is running! Now we just need to fetch some data from the backend.")

# Simple test button
def get_data():
    response = requests.get(f"{API_URL}/")
    return response.json()