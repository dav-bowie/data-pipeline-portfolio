import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.title("📊 My Data Pipeline Dashboard")

# Use path relative to script for both local and Streamlit Cloud
data_path = Path(__file__).parent.parent / "data" / "revenue.csv"
df = pd.read_csv(data_path)

fig = px.line(df, x="month", y="revenue", title="MoM Revenue")
st.plotly_chart(fig)
