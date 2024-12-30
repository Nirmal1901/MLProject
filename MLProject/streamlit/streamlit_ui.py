import streamlit as st
import requests

# FastAPI base URL
API_URL = "http://127.0.0.1:8000/predict"

# Streamlit app setup
st.title("Sentiment Analysis App")
st.write("Enter a text below to analyze its sentiment using the trained model.")

# Input text box
user_input = st.text_area("Input Text:", placeholder="Type your text here...")

# Analyze button
if st.button("Analyze Sentiment"):
    if user_input.strip():
        try:
            # Send request to FastAPI
            response = requests.post(API_URL, json={"text": user_input})
            if response.status_code == 200:
                result = response.json()
                st.success(f"Sentiment: {result['sentiment'].capitalize()}")
                st.write(f"Original Text: {result['text']}")
            else:
                st.error("Error: Unable to process the request.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some text to analyze.")

# Footer
st.markdown("---")
st.write("Powered by FastAPI and Streamlit")
