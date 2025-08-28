#Importing the necessary libraries
import streamlit as st
import joblib
import numpy as np
import os

# Create the directory if it doesn't exist
#os.makedirs('/content/app', exist_ok=True)

#Loading your saved model. Be sure to change the path if necessary
# Assuming the model trained on 'Phase' and 'Time Period' is saved as 'linear_regression_model.joblib'
# You might need to change the model file name if you saved it differently
model = joblib.load('Dataset yyy.joblib') # Make sure this path is correct

st.title('Predicting patient adoption of telemedicine')
st.write("This app predicts patients adoption of telemedicine based on Phase and Time Period.")

# Input for Phase
phase = st.number_input('Phase', min_value=0, max_value=10, value=2)

# Input for Time Period
time_period = st.number_input('Time Period', min_value=0, max_value=100, value=29)

if st.button('Predict'):
    # Ensure input features match the training data's structure (Phase, Time Period)
    input_features = np.array([[phase, time_period]])

    # Model prediction
    prediction = model.predict(input_features)
    st.write(f'Predicted Value (Telemedicine Usage): {prediction[0]:.2f}')

