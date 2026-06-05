import streamlit as st
import pandas as pd
import random
import pickle

# Dataset ဖတ်
df = pd.read_csv("questions.csv")

# Load recommender function
with open("recommender.pkl", "rb") as f:
    loaded_model = pickle.load(f)

# Streamlit UI
st.title("📚 Question Recommender")

subject_input = st.text_input("Enter subject:")

if st.button("Submit"):
    question = loaded_model(subject_input)
    st.write("Recommended Question:", question)
