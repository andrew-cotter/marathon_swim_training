import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from streamlit_funcs.helpers import *
warnings.filterwarnings('ignore')
import streamlit as st
from text import *
from plot_config import set_plot_style

load_custom_css()
set_plot_style()
st.header("Focusing on Training")
st.markdown(FOCUSING_ON_TRAINING_TEXT_1)


conn = st.connection("mysql", type="sql")
df=query_db(FOCUSING_ON_TRAINING_QUERY, conn)

g = sns.FacetGrid(
    df,
    row="type",
    hue="type",
    height=3,
    aspect=8.5/3,
    sharey=False,
    margin_titles=False
)

g.map(
    sns.swarmplot,
    "year",
    "duration_hr",
    size=3,        # more presence
    alpha=0.85,
    edgecolor="none"
)

g.fig.set_dpi(100)


# Remove default titles
g.set_titles("")

# Axis labels (x only once, y only once visually)
g.set_xlabels('')
for ax in g.axes.flat:
    ax.set_ylabel("")

g.fig.text(
    0.05, 0.5,
    "Duration (hours)",
    va="center",
    rotation="vertical",
    fontsize=13
)

# Per-row tweaks + labels
for ax, activity in zip(g.axes.flat, g.row_names):
    if activity == "Open Water Swim":
        ax.set_yticks([0,2,4,6])
    if activity == "Lifting":
        ax.set_ylim(0, 1.45)
        ax.set_yticks([0, 0.5, 1.0])
        ax.set_yticklabels(["0", ".5", "1"])

    # Activity label
    ax.text(
        -0.45,
        ax.get_ylim()[1],
        activity,
        ha="left",
        va="top",
        fontsize=10,
        fontweight="bold"
    )


# Main title
g.fig.suptitle(
    "Activity types and durations by year",
    fontweight="bold",
    fontsize=16,
    x=0.11,
    y=.93,
    ha="left"
)

g.fig.subplots_adjust(hspace=0.35, top=0.9)

col1, col2, col3 = st.columns([1,6,1])
with col2:
    st.pyplot(g.figure, use_container_width=False)

st.markdown(FOCUSING_ON_TRAINING_TEXT_2)

with st.expander("View Query"):
    st.code(FOCUSING_ON_TRAINING_QUERY)
    st.divider()
    st.markdown(FOCUSING_ON_TRAINING_QUERY_DESCRIPTION)