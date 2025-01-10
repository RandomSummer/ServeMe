import streamlit as st


a, b = st.columns(2)
c, d = st.columns(2)

a.metric("E-Dustbin", "100", border=True)
b.metric("Location", "20", border=True)

c.metric("Truck", "8", border=True)
d.metric("Worker", "24", border=True)



