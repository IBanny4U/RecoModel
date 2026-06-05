import streamlit as st
import pandas as pd
import requests
from io import StringIO

# ✅ Google Drive direct link (uc?id format)
url = "https://drive.google.com/uc?id=1VODI54uN5BGNE1W2oQcHcS-Zncss4jhg"

# Download file content
response = requests.get(url)
data = StringIO(response.text)

# Dataset ဖတ် (comma-separated CSV)
df = pd.read_csv(data, sep=",", encoding="utf-8", on_bad_lines="skip")

# Streamlit UI
st.title("📚 Question Recommender")

subject_input = st.text_input("Enter subject:")

if st.button("Submit"):
    # Subject အလိုက် filter
    filtered = df[df["Subject"].str.lower() == subject_input.lower()]
    if not filtered.empty:
        
        # Random question တစ်ခုရွေး
        
        question = filtered.sample(1)["Question"].values[0]
        st.write("Recommended Question:", question)
        st.write(question)
    else:
        st.write("No question found for that subject.")
