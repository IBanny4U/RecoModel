import streamlit as st
import pandas as pd
import requests
from io import StringIO
import pickle

# ✅ Correct Google Drive direct link format
url = "https://drive.google.com/uc?id=1VODI54uN5BGNE1W2oQcHcS-Zncss4jhg"

# Download file content
response = requests.get(url)
data = StringIO(response.text)

# Dataset ဖတ် (comma-separated CSV)
df = pd.read_csv(data, sep=",", encoding="utf-8", on_bad_lines="skip")

# Load recommender function from pkl file
with open("recommender.pkl", "rb") as f:
    loaded_model = pickle.load(f)

# Streamlit UI
st.title("📚 Question Recommender")

subject_input = st.text_input("Enter subject:")

if st.button("Submit"):
    # Use recommender function from pkl
    question = loaded_model(subject_input)
    st.write("Recommended Question:", question)
