import streamlit as st
from text import CONCLUSION_TEXT

st.header("Conclusion")
st.markdown(CONCLUSION_TEXT)

col1, col2, col3 = st.columns([1,3,1])
with col2:
    st.image("images/deuces.jpg", caption="Floating along somewhere in the San Francisco Bay")