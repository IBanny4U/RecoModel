import streamlit as st
import pandas as pd
import random
import pickle
import requests
from io import StringIO

# Google Drive direct link (replace with your FILE_ID)
url = "https://drive.google.com/file/d/1VODI54uN5BGNE1W2oQcHcS-Zncss4jhg/view?usp=sharing"

# Download file content
response = requests.get(url)
data = StringIO(response.text)

# Dataset ဖတ်
df = pd.read_csv(data)

# Load recommender function
with open("recommender.pkl", "rb") as f:
    loaded_model = pickle.load(f)

# Streamlit UI
st.title("📚 Question Recommender")

subject_input = st.text_input("Enter subject:")

if st.button("Submit"):
    question = loaded_model(subject_input)
    st.write("Recommended Question:", question)
