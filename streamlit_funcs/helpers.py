import pymysql
import toml
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import warnings
warnings.filterwarnings('ignore')

@st.cache_data
def query_db(query, _connection: st.connection, return_df=True):
    """Helper function to run queries"""
    return _connection.query(query)


