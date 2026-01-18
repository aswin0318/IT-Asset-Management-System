import streamlit as st
from api_client import get, put

st.header("Return Asset")

assignments = get("/reports/active-assignments-detailed")

if not assignments:
    st.info("No active assignments.")
    st.stop()

# Build readable labels
assignment_map = {
    f'{a["asset_name"]} (SN: {a["serial_number"]}) → '
    f'{a["employee_name"]} [{a["department"]}] '
    f'| Assigned on {a["assigned_date"][:10]}'
    : a["assignment_id"]
    for a in assignments
}

selected_label = st.selectbox(
    "Select Assignment to Return",
    assignment_map.keys()
)

if st.button("Return Asset"):
    assignment_id = assignment_map[selected_label]
    try:
        put(f"/assignments/{assignment_id}/return")
        st.success("Asset returned successfully")
        st.rerun()
    except Exception as e:
        st.error(str(e))
