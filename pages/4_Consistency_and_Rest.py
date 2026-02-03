import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from streamlit_funcs.helpers import *
from sqlalchemy import text
warnings.filterwarnings('ignore')
import streamlit as st
from text import *
from plot_config import set_plot_style

load_custom_css()
set_plot_style()
st.header("Consistency and Rest Days")
st.markdown(CONSISTENCY_TEXT_1)

conn = st.connection("mysql", type="sql")

df = query_db(
    ACTIVITIES_PER_WEEK_QUERY,
    conn
)

tab1, tab2, tab3 = st.tabs(["Activities Per Week", "Rest Days", "Activity Streaks"])
css = '''
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:1.4rem;
    }
</style>
'''
st.markdown(css, unsafe_allow_html=True)

with tab1:
    fig, ax = plt.subplots(figsize=(8.5, 7))
    #Stacked bar chart
    bottom=None
    for col in df.columns[1:]:
        bars = plt.bar(
            df["year"].astype(str),
            df[col],
            bottom=bottom,
            label=col,
            edgecolor="black"
        )
        # Add labels
        for bar in bars:
            if bar.get_xy()[1] == 0:
                textcolor="white"
            else:
                textcolor="black"
            height = bar.get_height()
            if height > 0:
                plt.text(
                    bar.get_x() + bar.get_width() / 2,
                    bar.get_y() + height / 2,
                    f"{height:.1f}",
                    ha="center",
                    va="center",
                    fontsize=12,
                    fontweight="bold",
                    color = textcolor
                )
        bottom = df[col] if bottom is None else bottom + df[col]

    #Formatting
    plt.title("Average weekly activities by year", loc="left", fontweight="bold")

    #Legend
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

    col1, col2, col3 = st.columns([1,6,1])
    with col2:
        st.pyplot(fig)

    st.markdown(ACTIVITIES_PER_WEEK_TEXT_1)

    plt.show()
    with st.expander("View Query"):
        st.code(ACTIVITIES_PER_WEEK_QUERY)
        st.markdown(ACTIVITIES_PER_WEEK_QUERY_DESCRIPTION)

with tab2:
    st.markdown(REST_TEXT_1)
    
    with conn.session as session:
        session.execute(text("SET @@cte_max_recursion_depth = 2000;"))
    df = query_db(
        REST_QUERY,
        conn
    )
    
    fig, ax = plt.subplots(figsize=(8.5, 9))

    #Stacked bar chart
    bottom=None
    for col in df.columns[1:]:
        bars = plt.bar(
            df["year"],
            df[col],
            bottom=bottom,
            label=col,
            edgecolor="black"
        )
        # Add labels
        for bar in bars:
            if bar.get_xy()[1] == 0:
                textcolor="white"
            else:
                textcolor="black"
            height = bar.get_height()
            if height > 0:
                plt.text(
                    bar.get_x() + bar.get_width() / 2,
                    bar.get_y() + height / 2,
                    f"{height:.1f}",
                    ha="center",
                    va="center",
                    fontsize=12,
                    fontweight="bold",
                    color=textcolor
                )
        bottom = df[col] if bottom is None else bottom + df[col]

        plt.yticks(ticks=[0,5,10,15,20,25,30], labels=["0%", "5%", "10%", "15%", "20%", "25%", "30%"])

    #Formatting
    sns.despine(ax=ax)
    plt.xticks(rotation=45, ha="right")
    plt.title("Percentage of rest days during training windows", loc="left", fontweight="bold")

    #Legend
    handles, labels = plt.gca().get_legend_handles_labels()
    plt.legend(
        handles[::-1],
        labels[::-1],
        ncol=2,
        frameon=False,
        loc="upper left",
        bbox_to_anchor=(0, 1.02),
        handletextpad=0.4,
        columnspacing=1.2,
        markerscale=2,
    )


    leg.set_title(None)

    col1, col2, col3 = st.columns([1,6,1])
    with col2:
        st.pyplot(fig)
    st.markdown(REST_TEXT_2)

    with st.expander("View Query"):
        st.code(REST_QUERY)
        st.markdown(REST_QUERY_DESCRIPTION)


with tab3:
    st.markdown(STREAKS_TEXT_1)
    df = query_db(
        STREAKS_QUERY,
        conn
    )

    fig, ax = plt.subplots(figsize=(8.5, 4.5))

    #Setup Formating
    year_positions = {year: i for i, year in enumerate(sorted(df["year"].unique()))}

    type_offset = {
        "Active Streak": -0.1,
        "Raw Streak": 0.1
    }

    palette = {
        "Active Streak": "#0A2540",
        "Raw Streak": "#5C9EAD"
    }


    #Plotting
    for _, row in df.iterrows():
        y = year_positions[row["year"]] + type_offset[row["type"]]
        ax.hlines(
            y=y,
            xmin=row["streakStart"],
            xmax=row["streakEnd"],
            color=palette[row["type"]],
            linewidth=15,
            label=row["type"]
        )
        #Annotations
        if row["type"]=="Active Streak":
            textcolor="white"
        else:
            textcolor="black"
        ax.text(
            row["streakStart"],
            y,
            f"{row['streak']}d ",
            va="center",
            ha="left",
            fontsize=9,
            fontweight="bold",
            color=textcolor
        )

    # Axis and title formatting
    ax.set_xticks([1, 32, 60, 91, 121, 152, 182])
    ax.set_xticklabels(
        [
            "Jan-1",
            "Feb-1",
            "Mar-1",
            "Apr-1",
            "May-1",
            "Jun-1",
            "Jul-1",

        ]
    )

    ax.set_yticks(list(year_positions.values()))
    ax.set_yticklabels(list(year_positions.keys()))
    plt.gca().invert_yaxis()
    plt.title("Activity streaks by year", loc="left", fontweight="bold", y=1.08)

    # Legend
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    labels = list(by_label.keys())
    handles = list(by_label.values())
    ax.legend(
        handles, 
        labels, 
        ncol=2,
        frameon=False,
        loc="upper left",
        bbox_to_anchor=(-0.015, 1.12),
        handletextpad=0.4,
        columnspacing=1.2,
        markerscale=2,
    )
    leg.set_title(None)

    plt.tight_layout()
    col1, col2, col3 = st.columns([1,6,1])
    with col2:
        st.pyplot(fig)
    
    st.write(STREAKS_TEXT_2)



    with st.expander("View Query"):
        st.code(STREAKS_QUERY)
        st.markdown(STREAKS_QUERY_DESCRIPTION)