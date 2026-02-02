import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from streamlit_funcs.helpers import *
warnings.filterwarnings('ignore')
import streamlit as st
from text import *
from plot_config import set_plot_style

set_plot_style()

st.header("Putting in the Hours")
st.markdown(PUTTING_IN_THE_HOURS_TEXT_1)
st.write("""
**NOTE**: For this section, I am using the results of the same SQL query described in the *Focusing on Training* section.
Refer back to that section if you're interested in the code.
"""
)

conn = st.connection("mysql", type="sql")
df=query_db(FOCUSING_ON_TRAINING_QUERY, conn)

tab1, tab2 = st.tabs(["Total Training Volume", "Weekly Schedule"])
css = '''
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:1.4rem;
    }
</style>
'''
st.markdown(css, unsafe_allow_html=True)
with tab1:
    st.markdown(TRAINING_VOLUME_TEXT_1)
    fix, ax = plt.subplots(figsize = (8,6))
    plot = sns.lineplot(
        data=df,
        x="doy",
        y="cumulative_duration",
        hue="year",
        linewidth=2.5
    )

    ax.set_xticks([1, 32, 60, 91, 121, 152, 182, 213, 244])
    ax.set_xticklabels(
        [
            "Jan-1",
            "Feb-1",
            "Mar-1",
            "Apr-1",
            "May-1",
            "Jun-1",
            "Jul-1",
            "Aug-1",
            "Sep-1",
        ],
        rotation=45
    )
    plt.ylabel('')
    plt.xlabel('')
    plt.title("Cumulative training hours by year")


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

    st.markdown(TRAINING_VOLUME_TEXT_2)

with tab2:
    
    st.markdown(WEEKLY_SCHEDULE_TEXT_1)

    day_order = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
    ]
    g = sns.FacetGrid(
        df,
        row="dayOfWeek",
        hue="type",
        row_order=day_order,
        height=1.8, 
        aspect=8.5/1.9,
        sharex=True
    )
    g.map(
        sns.kdeplot,
        "time",
        fill=True,
        alpha=0.2,
        bw_adjust=0.2
    )

    #Custom Facet Titles
    g.set_titles("")
    for ax, day in zip(g.axes.flat, g.row_names):
        ax.text(
            x=0, 
            y=0.25,  # near top
            s=day, 
            ha="left", 
            va="top",
            fontweight="bold",
            fontsize=13
        )

    #Main plot title
    g.fig.suptitle(
        "Activities by start time: 2023-2025", 
        fontweight="bold",
        x=0.09,
        y=0.99,
        ha="left"
        )

    #Formatting
    g.set(
        yticks=[], 
        ylabel="",
        xlabel=""
        )
    g.despine(left=True)

    for ax in g.axes.flat:
        ax.tick_params(labelbottom=True, labelsize=10)
        ax.set_xticks([0,3,6,9,12,15,18,21,24])
        ax.set_xticklabels([0,3,6,9,12,15,18,21,24])

    #Reduce gaps between facets
    g.fig.subplots_adjust(hspace=0.2)

    #Legend
    handles, labels = g.axes[0,0].get_legend_handles_labels()
    leg=plt.legend(
        handles=handles,
        labels=labels,
        ncol=3,
        frameon=False,
        bbox_to_anchor=(0.67, 8.2),
        handletextpad=0.4,
        columnspacing=1.2,
        markerscale=2,
    )
    leg.set_title(None)

    col1, col2, col3 = st.columns([1,3,1])
    with col2:
        st.pyplot(g.figure, use_container_width=False)

    st.markdown(WEEKLY_SCHEDULE_TEXT_2)

