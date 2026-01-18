import streamlit as st
from datetime import date
from api_client import post

st.header("Add Asset")

with st.form("add_asset_form"):
    asset_name = st.text_input("Asset Name")
    asset_type = st.text_input("Asset Type")
    serial_number = st.text_input("Serial Number")
    purchase_date = st.date_input("Purchase Date")
    expiry_date = st.date_input("Expiry Date")

    submitted = st.form_submit_button("Add Asset")

if submitted:
    data = {
        "asset_name": asset_name,
        "asset_type": asset_type,
        "serial_number": serial_number,
        "purchase_date": purchase_date.isoformat(),
        "expiry_date": expiry_date.isoformat()
    }

    try:
        post("/assets", data)
        st.success("Asset added successfully")
    except Exception as e:
        st.error(str(e))
