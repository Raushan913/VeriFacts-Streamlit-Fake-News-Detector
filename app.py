'''

The file provides an interactive web interface built with Streamlit,
allowing users to input news headlines and instantly receive predictions 
on their authenticity.

'''

import streamlit as st
import pickle
import numpy as np

# Load the saved model and CountVectorizer
with open('multinomial_nb_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('count_vectorizer.pkl', 'rb') as cv_file:
    cv = pickle.load(cv_file)

# Define the prediction function
def predict(text):
    data = cv.transform([text]).toarray()
    prediction = model.predict(data)
    return prediction[0]

st.title("Fake News Detection")

user_input = st.text_area("Enter the news title")

if st.button("Predict"):
    result = predict(user_input)
    st.write(f"The news is: {result}")

