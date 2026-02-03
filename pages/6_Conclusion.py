import streamlit as st
from text import CONCLUSION_TEXT
from streamlit_funcs.helpers import load_custom_css

load_custom_css()
st.header("Conclusion")
st.markdown(CONCLUSION_TEXT)

col1, col2, col3 = st.columns([1,6,1])
with col2:
    st.image("images/deuces.jpg", caption="Floating along somewhere in the San Francisco Bay")