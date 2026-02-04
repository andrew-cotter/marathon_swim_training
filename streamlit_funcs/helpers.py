import streamlit as st
import warnings
import os

warnings.filterwarnings("ignore")


@st.cache_data
def query_db(query, _connection: st.connection, return_df=True):
    """Helper function to run queries"""
    return _connection.query(query)


def load_custom_css():
    """Load custom CSS from .streamlit/style.css"""
    css_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), ".streamlit", "style.css"
    )
    if os.path.exists(css_path):
        with open(css_path, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
