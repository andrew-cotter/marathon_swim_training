import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from streamlit_funcs.helpers import *

warnings.filterwarnings("ignore")
import streamlit as st
from text import *

load_custom_css()
st.header("Cold Water")
st.markdown(COLD_WATER_TEXT_1)

conn = st.connection("mysql", type="sql")

# Initialize units in session state
if "units" not in st.session_state:
    st.session_state.units = "°F"

# Query database once
df_original = query_db(COLD_WATER_QUERY, conn)

def create_plot(units):
    """Create the plot with the specified units"""
    # Create a copy of the dataframe for conversion
    df = df_original.copy()
    
    # Convert to Celsius if needed
    if units == "°C":
        df["temp"] = round((df["temp"]-32)/1.8, 0).astype(int)
    
    # Create the plot
    fig, ax = plt.subplots()
    sns.barplot(
        data=df,
        x="temp",
        y="longestSwim",
        hue="year",
        hue_order=["2023", "2024", "2025"],
        width=0.6,
        edgecolor="black",
        ax=ax
    )
    sns.despine()
    
    plt.ylim(0, 6.5)
    plt.ylabel("")
    plt.xlabel("")
    plt.title(
        f"Duration of longest swim vs water temperature ({units})", loc="left", fontweight="bold"
    )
    leg = plt.legend(
        ncol=3,
        frameon=False,
        loc="upper left",
        bbox_to_anchor=(0, 1.02),
        handletextpad=0.4,
        columnspacing=1.2,
        markerscale=2,
    )
    leg.set_title(None)
    
    return fig

col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    def update_plot():
        """Callback function to update units in session state when radio changes"""
        st.session_state.units = st.session_state.units_radio
    
    units = st.radio(
        "Select units", 
        ["°F", "°C"],
        horizontal=True,
        index=0 if st.session_state.units == "°F" else 1,
        on_change=update_plot,
        key="units_radio"
    )
    # Create and display the plot with the selected units
    # The callback updates session_state.units, which triggers a rerun
    fig = create_plot(st.session_state.units)
    st.pyplot(fig)

st.markdown(COLD_WATER_TEXT_2)

with st.expander("View Query"):
    st.code(COLD_WATER_QUERY)
    st.markdown(COLD_WATER_QUERY_DESCRIPTION)
