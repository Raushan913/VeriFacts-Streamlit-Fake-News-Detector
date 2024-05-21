'''

The file provides an interactive web interface built with Streamlit,
allowing users to input news headlines and instantly receive predictions 
on their authenticity.

'''

import streamlit as st
import joblib

# Load the saved model and CountVectorizer
model = joblib.load('model/multinomial_nb_model.pkl')
cv = joblib.load('model/count_vectorizer.pkl')

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

