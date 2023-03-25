import streamlit as st
import pickle 

# Finding the path of pkl file

from pathlib import Path

pkl_path = Path(__file__).parents[1]

#Loading pkl file

loan_model = pickle.load(open('loan_model.pkl', 'rb'))

st.header("Loan Approver Bot")

g = st.slider("Enter the gender (for male 1 and for female 0)",0,1)
m = st.slider("Enter marital status (for married 1 and for unmarried 0)",0,1)
d = st.number_input("Enter the number of dependents (for 3+ write 3 only)")
e = st.slider("Enter the educational qualification (for non-graduates press 1 and graduates 0)",0,1)
se = st.slider("Enter employment status (1 for employed 0 for un-employed)",0,1)
ai = st.number_input("Enter applicant's income in thousand rupees")
ci = st.number_input("Enter co-applicant's income in thousand rupees")
l = st.number_input("Enter loan amount (Total amount / 1000)")
t = st.number_input("Enter loan term in months")
h = st.slider("Enter credit history (1 for yes and 0 for no)",0,1)
a = st.slider("Enter property area (0 for rural, 1 for semi urban and 2 for urban)",0,1,2)

if st.button("Predict"):
    loan_status = loan_model.predict([[g,m,d,e,se,ai,ci,l,t,h,a]])
    if (loan_status[0] == 1):
        st.header("Congratulations applicant is eligible for loan")
    else:
        st.header("Sorry the applicant is not eligible for loan")