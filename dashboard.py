import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Logistics Data Quality Dashboard",
    page_icon="🚚",
    layout="wide"
)

st.title("🚚 Logistics Data Quality & Preprocessing Dashboard")
st.write("Dashboard for monitoring logistics data quality and preprocessing results.")

# Load cleaned data
file_path = "data/logistics_cleaned.csv"

if os.path.exists(file_path):
    df = pd.read_csv(file_path)

    # KPI calculations
    total_records = len(df)
    total_columns = len(df.columns)
    missing_values = int(df.isnull().sum().sum())
    duplicate_rows = int(df.duplicated().sum())

    # KPI cards
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Shipments", total_records)
    col2.metric("Total Columns", total_columns)
    col3.metric("Missing Values", missing_values)
    col4.metric("Duplicate Rows", duplicate_rows)

    st.divider()

    # Data preview
    st.subheader("📋 Cleaned Logistics Data")
    st.dataframe(df, use_container_width=True)

    st.divider()

    # Numerical columns
    numeric_columns = df.select_dtypes(include="number").columns.tolist()

    if numeric_columns:
        st.subheader("📊 Numerical Data Analysis")

        selected_column = st.selectbox(
            "Select a numerical column",
            numeric_columns
        )

        st.bar_chart(df[selected_column].value_counts().head(20))

    # Column information
    st.subheader("🔎 Data Quality Summary")

    quality = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str),
        "Missing Values": df.isnull().sum().values,
        "Unique Values": df.nunique().values
    })

    st.dataframe(quality, use_container_width=True)

else:
    st.error("Cleaned data file not found.")
    st.write("Expected file:", file_path)