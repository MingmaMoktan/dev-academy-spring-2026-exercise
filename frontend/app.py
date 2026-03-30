import streamlit as st

# Set page title
st.set_page_config(page_title="Solita Electricity Data")

st.title("Solita Electricity Dashboard")
st.write("Frontend is running! Now we just need to fetch some data from the backend.")

# Simple test button
if st.button('Check Backend Connection'):
    st.write("Checking...")
    # Later we will add: requests.get("http://backend:8000/")