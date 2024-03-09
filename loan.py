import streamlit as st
import pandas as pd
import joblib


st.set_page_config(
    page_title='Loan Prediction',
    page_icon='newspaper.png',
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None
)

model = joblib.load('loan_prediction_model.pkl')

gender_mapping = {'Male': 1, 'Female': 0}
married_mapping = {'Yes': 1, 'No': 0}
education_mapping = {'Graduate': 0, 'Not Graduate': 1}
self_employed_mapping = {'Yes': 1, 'No': 0}
property_area_mapping = {'Urban': 2, 'Semiurban': 1, 'Rural': 0}
dependents_mapping = {'0': 0, '1': 1, '2': 2, '3+': 3}

def predict_loan_status(input_data):
    input_data['Gender'] = gender_mapping[input_data['Gender']]
    input_data['Married'] = married_mapping[input_data['Married']]
    input_data['Education'] = education_mapping[input_data['Education']]
    input_data['Self_Employed'] = self_employed_mapping[input_data['Self_Employed']]
    input_data['Property_Area'] = property_area_mapping[input_data['Property_Area']]
    input_data['Dependents'] = dependents_mapping[input_data['Dependents']]
    
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)
    return prediction[0]

st.markdown(
        "<center><h1 style='font-family: Comic Sans MS; font-weight: 600; font-size: 36px;'>Loan Prediction</h1></center>",
        unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    gender = st.selectbox('Gender', ('Male', 'Female'))

with col2:
    married = st.selectbox('Married', ('Yes', 'No'))

col3, col4 = st.columns(2)
with col3:
    dependents = st.selectbox('Dependents', ('0', '1', '2', '3+'))
with col4:
    self_employed = st.selectbox('Self Employed', ('Yes', 'No'))

education = st.selectbox('Education', ('Graduate', 'Not Graduate'))

col5, col6 = st.columns(2)
with col5:
    applicant_income = st.number_input('Applicant Income', min_value=0)
with col6:
    coapplicant_income = st.number_input('Coapplicant Income', min_value=0)

col7, col8 = st.columns(2)
with col7:
    loan_amount = st.number_input('Loan Amount', min_value=0)
with col8:
    loan_amount_term = st.number_input('Loan Amount Term', min_value=0)


col9, col10 = st.columns(2)
with col9:
    credit_history = st.selectbox('Credit History', ('1', '0'))
with col10:
    property_area = st.selectbox('Property Area', ('Urban', 'Semiurban', 'Rural'))


if st.button('Predict Loan Status'):
    input_data = {
        'Gender': gender,
        'Married': married,
        'Dependents': dependents,
        'Education': education,
        'Self_Employed': self_employed,
        'ApplicantIncome': applicant_income,
        'CoapplicantIncome': coapplicant_income,
        'LoanAmount': loan_amount,
        'Loan_Amount_Term': loan_amount_term,
        'Credit_History': credit_history,
        'Property_Area': property_area
    }
    
    status = predict_loan_status(input_data)
    if status == 1:
        st.success('Loan can be **APPROVED**.')
    else:
        st.error('Loan Approval is **Unlikely**.')