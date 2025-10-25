#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Set page configuration
st.set_page_config(page_title="Pie Chart Visualization", page_icon="🥧")

st.title("🥧 Pie Chart Visualization")

# Path to the CSV file
data_path = os.path.join("..", "data", "pie_demo.csv")

# Load data
try:
    df = pd.read_csv(data_path)
    st.subheader("📄 Data Preview")
    st.dataframe(df)
except FileNotFoundError:
    st.error(f"CSV file not found at: {data_path}")
    st.stop()

# Ensure CSV has at least 5 data points
if len(df) < 5:
    st.warning("The dataset should contain at least 5 data points.")
    st.stop()

# Let user choose which columns to use
numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
text_cols = df.select_dtypes(exclude=["number"]).columns.tolist()

if not numeric_cols or not text_cols:
    st.error("The CSV must contain both categorical (text) and numerical columns.")
    st.stop()

category_col = st.selectbox("Select a categorical column for labels:", text_cols)
value_col = st.selectbox("Select a numerical column for values:", numeric_cols)

# Create pie chart
fig = px.pie(df, names=category_col, values=value_col, title=f"Pie Chart of {value_col} by {category_col}")
st.plotly_chart(fig, use_container_width=True)

