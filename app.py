import streamlit as st 
import numpy as np
import joblib

# Load trained model
model = joblib.load("salary_prediction_model.pkl")

st.set_page_config(page_title="Salary Predictor", layout="centered")
st.title("💼 Salary Prediction using Ensemble Model")

st.markdown("### Fill the fields below to predict the salary:")

# Input form
age = st.number_input("Age", min_value=18, max_value=100, value=25)
experience = st.number_input("Years of Experience", min_value=0.0, value=1.0, step=0.5)
gender = st.selectbox("Gender", ["Male", "Female"])
education = st.selectbox("Education Level", ["Bachelor's", "Master's", "PhD"])

# Extended job titles across fields
job_titles = [
    # CSE/AI/DS
    "Software Engineer", "Data Scientist", "AI Engineer", "Machine Learning Engineer",
    "Deep Learning Engineer", "Data Analyst", "DevOps Engineer", "Cybersecurity Analyst",

    # Electrical / EEE
    "Electrical Engineer", "Power System Engineer", "Embedded Systems Engineer", "Control Systems Engineer",
    "Electronics Design Engineer",

    # Mechanical
    "Mechanical Engineer", "Automotive Engineer", "Production Engineer", "Maintenance Engineer",

    # Civil
    "Civil Engineer", "Site Engineer", "Structural Engineer", "Construction Manager",

    # Biotech
    "Biotech Researcher", "Genetic Engineer", "Biomedical Engineer", "Pharmaceutical Analyst",

    # Generic Roles
    "Manager", "HR", "Technical Writer", "Project Coordinator", "Others"
]

job_title = st.selectbox("Job Title", job_titles)

# Encoding inputs
gender_encoded = 1 if gender == "Male" else 0
education_map = {"Bachelor's": 0, "Master's": 1, "PhD": 2}
education_encoded = education_map[education]

# Encode job titles dynamically
job_encoded = job_titles.index(job_title)  # index will act as unique label encoding

# Predict
if st.button("Predict Salary"):
    input_data = np.array([[age, experience, gender_encoded, education_encoded, job_encoded]])
    prediction = model.predict(input_data)
    st.success(f"💰 Estimated Salary: ₹{prediction[0]:,.2f}")
