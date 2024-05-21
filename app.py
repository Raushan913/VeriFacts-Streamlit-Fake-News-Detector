'''
This is a Streamlit app that allows users to upload a machine learning model and CountVectorizer saved as pickle files. 
It then uses these files to predict whether a given news title is fake or real. Users can enter a news title in 
a text area, and upon clicking the "Predict" button, the app displays the prediction result. The app handles file 
uploads dynamically, ensuring the necessary files are loaded for making predictions.

'''



import streamlit as st
import pickle
import numpy as np
import os

# Define the file paths
model_path = '..\VeriFacts-Streamlit-Fake-News-Detector\model\multinomial_nb_model.pkl'
vectorizer_path = '..\VeriFacts-Streamlit-Fake-News-Detector\model\count_vectorizer.pkl'

# Check if files exist
if not os.path.exists(model_path) or not os.path.exists(vectorizer_path):
    st.error("Model or CountVectorizer file not found. Please check the file paths.")
else:
    # Load the saved model and CountVectorizer
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)

    with open(vectorizer_path, 'rb') as cv_file:
        cv = pickle.load(cv_file)

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

