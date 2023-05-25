import streamlit as st
import pickle 

# Finding the path of pkl file

from pathlib import Path

pkl_path = Path(__file__).parents[1]

#Loading pkl file

loan_model = pickle.load(open('loan_model.pkl', 'rb'))

st.sidebar.image('https://www.klaggarwal.com/wp-content/uploads/2022/12/loan-wood-block-arrange-business-man-model-scaled-e1669889850576-768x340.jpg')
st.sidebar.title('Loan Approver Bot')
st.sidebar.text('Select the right customer for\nThe right amount')

st.header('Please fille the below details:')

col1, col2, col3 = st.columns([7,7,7])

with col1:
    g = st.selectbox('Enter the gender', ('Male','Female'))
with col2:
    m = st.selectbox("Enter marital status",('Married','Unmarried'))
with col3:
    d = st.selectbox("Enter the number of dependents",(0,1,2,3,'3+'))

col4, col5, col6 = st.columns([7,7,7])

with col4:
    e = st.selectbox("Enter the educational qualification",('Graduate','Non-Graduate'))
with col5:
    se = st.selectbox("Enter employment status",('Employed','Un-Employed'))
with col6:
    a = st.selectbox("Enter property area",('Rural','Urban','Semi-Urban'))

col7, col8 = st.columns([12,12])
with col7:
    ai = st.number_input("Enter applicant's income in rupees")
with col8:
    ci = st.number_input("Enter co-applicant's income in rupees")

col9, col10 = st.columns([12,12])
with col9:
    l = st.number_input("Enter the loan amount in rupees")
with col10:
    t = st.selectbox("Enter loan term in months",(6,12,18,24,36,48,60))

if g == 'Male':
    g = 1
else:
    g = 0

if m == 'Married':
    m = 1
else:
    m = 0

if d == '3+':
    d = 3

if e == 'Graduate':
    e = 0
else:
    e = 1

if se == 'Employed':
    se = 1
else:
    se = 0

if a == 'Rural':
    a = 0
elif a == 'Semi-Urban':
    a = 1
else:
    a = 2

if st.button("Predict"):
    loan_status = loan_model.predict([[g,m,d,e,se,ai,ci,l,t,a]])
    if (loan_status[0] == 1):
        st.sidebar.write("Congratulations applicant is eligible for loan")
    else:
        st.sidebar.write("Sorry the applicant is not eligible for loan")
