import streamlit as st
import pickle
import numpy as np

# Load Model
with open("loan.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="Loan Approval Prediction", page_icon="🏦")

st.title("🏦 Loan Approval Prediction")
st.write("Fill the details below")

# Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])

income = st.number_input(
    "Applicant Income",
    min_value=0,
    step=1000
)

loan_amount = st.number_input(
    "Loan Amount",
    min_value=0,
    step=1000
)

credit = st.selectbox(
    "Credit History",
    ["Good (1)", "Bad (0)"]
)

# Encoding
gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0
credit = 1 if credit == "Good (1)" else 0

# Prediction
if st.button("Predict Loan Status"):

    data = np.array([[gender,
                      married,
                      income,
                      loan_amount,
                      credit]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
        st.balloons()
    else:
        st.error("❌ Loan Rejected")