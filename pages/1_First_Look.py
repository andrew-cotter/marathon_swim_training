import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from streamlit_funcs.helpers import *
warnings.filterwarnings('ignore')
import streamlit as st
from text import *
from plot_config import set_plot_style

set_plot_style()
st.header("A First Look")
st.markdown(FIRST_LOOK_TEXT_1)

conn = st.connection("mysql", type="sql")
df = query_db(
    FIRST_LOOK_QUERY,
    conn
)

fix, ax = plt.subplots(figsize=(12,5))

plot = sns.swarmplot(
    data = df,
    x="year",
    y="duration_hr",
    hue ="type",
    size=3,
)
plt.ylabel("Duration (Hours)")
plt.xlabel("")
plt.title("Activity types and durations by year", loc="left", fontweight="bold")

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

col1, col2, col3 = st.columns([1,3,1])
with col2:
    st.pyplot(plot.get_figure())

st.markdown(FIRST_LOOK_TEXT_2)
with st.expander("View Query"):
    st.code(FIRST_LOOK_QUERY)
    st.divider()
    st.markdown(FIRST_LOOK_QUERY_DESCRIPTION)
