import streamlit as st
import joblib
import numpy as np

MODEL_PATH = "./savedModels/gradient_boosting_model.joblib"
model = joblib.load(MODEL_PATH)

st.title("Credit Risk Prediction")

st.header("Enter the details to predict credit risk")


Age = st.number_input("Age", min_value=0.0, step=0.1)
Job = st.number_input("Job", min_value=0.0, step=0.1)
CreditAmount = st.number_input("Credit Amount", min_value=0.0, step=0.1)
Duration = st.number_input("Duration", min_value=0.0, step=0.1)
if Duration > 0:
    InstallmentRate = CreditAmount / Duration
    st.write(f"Installment Rate (calculated): {InstallmentRate:.2f}")
else:
    InstallmentRate = 0.0
    st.write("Installment Rate: Duration must be greater than 0 to calculate.")

if st.button("Predict"):
    input_data = np.array([[Age, Job, CreditAmount, Duration, InstallmentRate]])
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.success("Good Credit Risk")
    else:
        st.success("Bad Credit Risk")