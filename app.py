#Importing the necessary libraries
import streamlit as st
import joblib
import numpy as np
import os



#Loading your saved model. Be sure to change the path if necessary
# Assuming the model trained on 'Phase' and 'Time Period' is saved as 'linear_regression_model.joblib'
# You might need to change the model file name if you saved it differently
model = joblib.load('telemed1.joblib') # Make sure this path is correct

st.title('Predicting patient adoption of telemedicine')
st.write("This app predicts patients adoption of telemedicine based on Phase, State, Group, and Time Period.")

# Input for Phase
phase = st.number_input('Phase', min_value=0.0, max_value=10.0, value=3.1)

# Input for State (Using a numeric representation since it was Label Encoded)
state = st.number_input('State (Numeric representation)', min_value=0, max_value=50, value=0)

# Input for Group (Using a numeric representation since it was Label Encoded)
group = st.number_input('Group (Numeric representation)', min_value=0, max_value=1, value=0)

# Input for Time Period
time_period = st.number_input('Time Period', min_value=0, max_value=100, value=29)


if st.button('Predict'):
    # Ensure input features match the training data's structure (Phase, State, Group, Time Period)
    input_features = np.array([[phase, state, group, time_period]])

    # Model prediction
    prediction = model.predict(input_features)
    st.write(f'Predicted Value (Telemedicine Usage): {prediction[0]:.2f}')