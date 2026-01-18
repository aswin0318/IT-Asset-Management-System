import streamlit as st
from api_client import get, download_file

st.header("Reports")

st.subheader("Assignment Audit")
st.dataframe(get("/reports/assignment-audit"), use_container_width=True)

if st.button("Download Assignment Audit PDF"):
    pdf = download_file("/reports/assignment-audit/pdf")
    st.download_button(
        "Download PDF",
        data=pdf,
        file_name="assignment_audit_report.pdf",
        mime="application/pdf"
    )

st.subheader("Currently Assigned Assets")
st.dataframe(get("/reports/currently-assigned"), use_container_width=True)

if st.button("Download Currently Assigned PDF"):
    pdf = download_file("/reports/currently-assigned/pdf")
    st.download_button(
        "Download PDF",
        data=pdf,
        file_name="currently_assigned_assets.pdf",
        mime="application/pdf"
    )

st.subheader("Expired Assets")
st.dataframe(get("/reports/expired-assets"), use_container_width=True)

if st.button("Download Expired Assets PDF"):
    pdf = download_file("/reports/expired-assets/pdf")
    st.download_button(
        "Download PDF",
        data=pdf,
        file_name="expired_assets_report.pdf",
        mime="application/pdf"
    )
