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

df = query_db(COLD_WATER_QUERY, conn)

plot = sns.barplot(
    data=df,
    x="temp",
    y="longestSwim",
    hue="year",
    hue_order=["2023", "2024", "2025"],
    width=0.6,
    edgecolor="black",
)
sns.despine()

plt.ylim(0, 6.5)
plt.ylabel("")
plt.xlabel("")
plt.title(
    "Duration of longest swim vs water temperature (°F)", loc="left", fontweight="bold"
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

col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    st.pyplot(plot.get_figure())

st.markdown(COLD_WATER_TEXT_2)

with st.expander("View Query"):
    st.code(COLD_WATER_QUERY)
    st.markdown(COLD_WATER_QUERY_DESCRIPTION)
