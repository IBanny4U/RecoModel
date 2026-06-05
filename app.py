import streamlit as st
import pandas as pd
import requests
from io import StringIO
import pickle

# Google Drive direct link
url = "https://drive.google.com/file/d/1VODI54uN5BGNE1W2oQcHcS-Zncss4jhg/view?usp=sharing"

# Download file content
response = requests.get(url)
data = StringIO(response.text)

# Dataset ဖတ် (comma-separated CSV)
df = pd.read_csv(data, sep=",", encoding="utf-8", on_bad_lines="skip")

# Load recommender function
with open("recommender.pkl", "rb") as f:
    loaded_model = pickle.load(f)

# Streamlit UI
st.title("📚 Question Recommender")

subject_input = st.text_input("Enter subject:")

if st.button("Submit"):
    # Filter by subject
    filtered = df[df["Subject"].str.lower() == subject_input.lower()]
    if not filtered.empty:
        question = filtered.sample(1)["Question"].values[0]
        st.write("Recommended Question:", question)
    else:
        st.write("No question found for that subject.")
