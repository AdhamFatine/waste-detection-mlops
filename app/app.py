import streamlit as st
import requests

st.title("Waste Detection")

user_input = st.text_input("Enter data")

if st.button("Predict"):

    response = requests.post(
        "http://api:8000/predict",
        json={"data": user_input}
    )

    result = response.json()

    st.success(result["prediction"])