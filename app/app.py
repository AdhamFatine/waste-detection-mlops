import streamlit as st
import requests

st.title("Waste Detection")

user_input = st.text_input("Enter data")

API_URL = "https://waste-detection-api-2csu.onrender.com/predict"

if st.button("Predict"):

    response = requests.post(
        API_URL,
        json={"data": user_input}
    )

    result = response.json()

    st.success(result["prediction"])


if response.status_code == 200:
    result = response.json()
    st.success(result["prediction"])
else:
    st.error("API error")