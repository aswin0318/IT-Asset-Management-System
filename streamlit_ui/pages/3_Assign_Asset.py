import streamlit as st
from api_client import get, post

st.header("Assign Asset")

assets = get("/assets")
employees = get("/employees")

available_assets = [a for a in assets if a["status"] == "Available"]

asset_map = {f'{a["asset_name"]} ({a["id"]})': a["id"] for a in available_assets}
employee_map = {f'{e["name"]} ({e["id"]})': e["id"] for e in employees}

asset_choice = st.selectbox("Select Asset", asset_map.keys())
employee_choice = st.selectbox("Select Employee", employee_map.keys())

if st.button("Assign"):
    try:
        post("/assignments", {
            "asset_id": asset_map[asset_choice],
            "employee_id": employee_map[employee_choice]
        })
        st.success("Asset assigned successfully")
    except Exception as e:
        st.error(str(e))
