import streamlit as st
from api_client import get

st.header("All Assets")

assets = get("/assets")
st.dataframe(assets, use_container_width=True)
