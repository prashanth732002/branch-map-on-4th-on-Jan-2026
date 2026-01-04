import streamlit as st
import pandas as pd

st.set_page_config(page_title="Excel Column Automation", layout="centered")

st.title("📊 Excel Column Filter")
st.write("Upload an Excel file. Only required columns will be kept automatically.")

REQUIRED_COLUMNS = [
    "Branch",
    "Branch ID",
    "State",
    "AM",
    "AM Emp ID",
    "DM",
    "DM Emp ID",
    "RM",
    "RM Emp ID"
]

uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)

        missing_cols = [c for c in REQUIRED_COLUMNS if c not in df.columns]

        if missing_cols:
            st.error(f"Missing columns: {missing_cols}")
        else:
            filtered_df = df[REQUIRED_COLUMNS]

            st.success("✅ File processed successfully")
            st.dataframe(filtered_df)

            st.download_button(
                label="⬇️ Download Filtered Excel",
                data=filtered_df.to_excel(index=False),
                file_name="filtered_output.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    except Exception as e:
        st.error(f"Error: {e}")
