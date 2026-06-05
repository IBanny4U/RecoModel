import streamlit as st
import pickle

# Load ML model + vectorizer
with open("recommender.pkl", "rb") as f:
    model, vectorizer = pickle.load(f)

st.title("📚 Question Recommender")

subject_input = st.text_input("Enter subject:")

if st.button("Submit"):
    # Transform input subject into vector
    subject_vec = vectorizer.transform([subject_input])
    prediction = model.predict(subject_vec)[0]

    st.write("Predicted Subject:", prediction)
