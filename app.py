import streamlit as st
import pandas as pd
import random
import pickle

url = "https://drive.google.com/file/d/1VODI54uN5BGNE1W2oQcHcS-Zncss4jhg/view?usp=sharing"

# Dataset ဖတ်
df = pd.read_csv(url)

# Load recommender function
with open("recommender.pkl", "rb") as f:
    loaded_model = pickle.load(f)

# Streamlit UI
st.title("📚 Question Recommender")

subject_input = st.text_input("Enter subject:")

if st.button("Submit"):
    question = loaded_model(subject_input)
    st.write("Recommended Question:", question)
