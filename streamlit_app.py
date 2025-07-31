import streamlit as st
import pandas as pd
from src.generator import generate_synthetic_data

st.title("Synthetic Robotaxi Data Generator")

prompt = st.text_input("Enter a prompt for synthetic data", value="Generate 3 synthetic robotaxi scenarios")

if st.button("Generate Data"):
    data = generate_synthetic_data(prompt)
    df = pd.DataFrame(data)
    st.write("Generated Data:")
    st.dataframe(df)

    # Add download options
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download as CSV", csv, "synthetic_data.csv", "text/csv")

    json = df.to_json(orient="records", indent=2)
    st.download_button("Download as JSON", json, "synthetic_data.json", "application/json")
