import matplotlib.pyplot as plt
import seaborn as sns


def set_plot_style():
    sns.set_theme(style="white", context="talk", font="DejaVu Sans", font_scale=1)

    plt.rcParams.update(
        {
            # --- Figure ---
            "figure.figsize": (8.5, 5),
            "figure.dpi": 110,
            "figure.facecolor": "white",
            # --- Axes ---
            "axes.facecolor": "white",
            "axes.edgecolor": "#111111",
            "axes.linewidth": 1.4,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": False,
            # --- Ticks ---
            "xtick.color": "#111111",
            "ytick.color": "#111111",
            "xtick.major.size": 6,
            "ytick.major.size": 6,
            "xtick.major.width": 1.2,
            "ytick.major.width": 1.2,
            "ytick.left": True,
            "xtick.bottom": True,
            # --- Text ---
            "axes.labelsize": 13,
            "axes.titlesize": 17,
            "axes.titleweight": "bold",
            "axes.labelcolor": "#111111",
            "axes.titlelocation": "left",
            # --- Legend ---
            "legend.frameon": False,
            "legend.fontsize": 12,
            "legend.title_fontsize": 13,
            # --- Lines ---
            "lines.linewidth": 3,
            "lines.markersize": 8,
            # --- Bars ---
            "patch.edgecolor": "none",
        }
    )

    athletic_palette = {
        "Open Water Swim": "#0A2540",  # deep ocean
        "Pool Swim": "#5C9EAD",  # cold steel blue
        "Lifting": "#8B5E34",  # sand / earth
    }

    sns.set_palette(list(athletic_palette.values()))
