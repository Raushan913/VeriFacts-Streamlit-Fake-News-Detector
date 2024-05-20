import streamlit as st
import joblib
import numpy as np

# Load the saved model and CountVectorizer
model = joblib.load('multinomial_nb_model.pkl')
cv = joblib.load('count_vectorizer.pkl')

# Define the prediction function
def predict(text):
    data = cv.transform([text]).toarray()
    prediction = model.predict(data)
    return prediction[0]

# Streamlit app
st.title("Fake News Detection")

# Text input
user_input = st.text_area("Enter the news title")

# Predict button
if st.button("Predict"):
    result = predict(user_input)
    st.write(f"The news is: {result}")

