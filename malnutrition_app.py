import streamlit as st
import pandas as pd
import joblib

# Load the trained model (version 1)
model = joblib.load('malnutrition_model_v1.pkl')

# App title
st.title("Child Malnutrition Risk Predictor")

st.write("Enter child nutrition indicators to predict malnutrition risk:")

# Input fields for features
severe_wasting = st.number_input("Severe Wasting (%)", min_value=0.0, max_value=50.0, value=0.0)
wasting = st.number_input("Wasting (%)", min_value=0.0, max_value=50.0, value=0.0)
overweight = st.number_input("Overweight (%)", min_value=0.0, max_value=50.0, value=0.0)
stunting = st.number_input("Stunting (%)", min_value=0.0, max_value=50.0, value=0.0)
underweight = st.number_input("Underweight (%)", min_value=0.0, max_value=50.0, value=0.0)

# Predict button
if st.button("Predict Risk"):
    # Prepare input data for model
    input_data = pd.DataFrame([[severe_wasting, wasting, overweight, stunting, underweight]],
                              columns=['severe_wasting','wasting','overweight','stunting','underweight'])
    
    # Predict
    prediction = model.predict(input_data)[0]
    
    # Display result
    if prediction == 1:
        st.error("⚠️ Malnutrition Risk: HIGH")
    else:
        st.success("✅ Malnutrition Risk: LOW")