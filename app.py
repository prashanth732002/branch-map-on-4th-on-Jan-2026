import streamlit as st
import pandas as pd
from io import BytesIO

st.title("Excel Role-wise Automation")

uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    required_cols = [
        "Branch", "Branch ID", "State",
        "AM", "AM Emp ID",
        "DM", "DM Emp ID",
        "RM", "RM Emp ID"
    ]

    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        st.error(f"Missing columns: {missing}")
    else:
        am_df = df[["Branch", "Branch ID", "State", "AM", "AM Emp ID"]].copy()
        am_df_
