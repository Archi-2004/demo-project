import streamlit as st
import joblib
import numpy as np

import streamlit as st
import numpy as np
import joblib

# Sidebar navigation
st.sidebar.title("Navigation")
option = st.sidebar.radio("Go to", ["Home", "Predict Credit Risk", "About Project"])

# Home Page
if option == "Home":
    st.title("Credit Risk Prediction App")

    st.markdown("""
    Welcome to the App!  
    This app uses **Machine Learning** to help predict whether a person is likely to default on a loan (Credit Risk).

    It considers financial features such as:
    - Credit Amount
    - Duration of loan (months)
    - Income
    - Other relevant features

    """)


    st.markdown("""
    ---
    ### How It Works:
    1. Navigate to "Predict Credit Risk" using the sidebar.
    2. Enter the loan details like amount, duration, etc.
    3. The app will predict whether the loan is **risky** or **not risky**.

    > ⚠️ **Disclaimer**: This is a demo tool and should not be used for real financial decisions.
    """)

# Prediction Page
elif option == "Predict Credit Risk":
    st.title("Credit Risk Prediction using Machine Learning")

    # Load trained model
    model = joblib.load("./savedModels/gradient_boosting_model.joblib")

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

    
# About Page
elif option == "About Project":
    st.title("About the Credit Risk Prediction Project")
    st.markdown("""
    This project demonstrates a basic credit risk classification using financial inputs.
    
    It uses:
    - Streamlit for UI
    - A simple rule-based model or machine learning
    - Python, NumPy, and joblib for backend

    Built with ❤️ for educational purposes.
    """)
st.markdown("Submitted by Archi"
            

"Btech Electronics and computer engineering"


"Guru Nanak Dev University Amritsar")
