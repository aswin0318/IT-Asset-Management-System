import streamlit as st
from api_client import post

st.header("Add Employee")

with st.form("add_employee_form"):
    name = st.text_input("Name")
    department = st.text_input("Department")
    email = st.text_input("Email")

    submitted = st.form_submit_button("Add Employee")

if submitted:
    data = {
        "name": name,
        "department": department,
        "email": email
    }

    try:
        post("/employees", data)
        st.success("Employee added successfully")
    except Exception as e:
        st.error(str(e))
