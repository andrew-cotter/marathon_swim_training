import streamlit as st
from text import *
from streamlit_funcs.helpers import load_custom_css

# Load custom CSS
load_custom_css()

st.set_page_config(
    page_title="Training for Marathon Swimming", page_icon=":swimmer:", layout="wide"
)
st.title("Training for Marathon Swimming")
st.subheader("An Exploratory Analysis with SQL and Seaborn")
st.subheader("By Andrew Cotter")
st.divider()

st.header("Introduction")

st.markdown(INTRO_TEXT_1)
col1, col2 = st.columns(2)
with col1:
    st.image(
        "images/ec_map.jpeg",
        caption="Map of my English Channel crossing in August 2025",
    )
with col2:
    st.image(
        "images/rthi.jpeg",
        caption="Me (yellow cap on the left) doing a long swim in Tomales Bay, CA in August 2024",
    )
st.markdown(INTRO_TEXT_2)
