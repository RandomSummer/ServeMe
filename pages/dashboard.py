import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


with st.sidebar:
    st.info(f"Dashboard for monitoring the data. (Role) : {st.session_state.role}.")
        

a, b = st.columns(2)
c, d = st.columns(2)

a.metric("E-Dustbin", "100", border=True)
b.metric("Location", "20", border=True)

c.metric("Truck", "8", border=True)
d.metric("Worker", "24", border=True)


if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

uploaded_files = st.file_uploader(
    "Upload Your Dataset Here ...", accept_multiple_files=True
)
# for uploaded_file in uploaded_files:

#     st.write("filename:", uploaded_file.name)

#     chart, data = st.tabs(["🗃 Data", "📈 Chart"])
#     df = pd.read_csv(uploaded_file, index_col = None)

#     data.subheader("Data Tab")
#     st.dataframe(df.style.highlight_max(axis=0), width=None)

#     # bytes_data = uploaded_file.read()
#     chart.subheader("Chart Tab")
#     df_chart = pd.DataFrame(df)
#     chart.line_chart(df_chart)



