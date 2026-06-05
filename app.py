import streamlit as st
import pickle

# Load ML model + vectorizer
with open("recommender.pkl", "rb") as f:
    model, vectorizer = pickle.load(f)

st.title("📚 Question Recommender")

question_input = st.text_input("Enter a question:")

if st.button("Predict Subject"):
    if question_input.strip():
        # Transform input question into vector
        question_vec = vectorizer.transform([question_input])
        prediction = model.predict(question_vec)[0]
        st.write("Predicted Subject:", prediction)
    else:
        st.write("Please enter a question.")
