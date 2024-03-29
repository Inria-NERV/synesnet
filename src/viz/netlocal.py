import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib import font_manager


def plot_3d_local_metric(S, C, xyz, n_name, cmap=None, return_scatter=False, **kwargs):
    """
    Generate a 3D scatter plot with variable point sizes and colors.

    Arguments:
        :param S: local metric vector
        :param C: local metric value vector
        :param xyz: numpy array of xyz coordinates
        :param n_name: list of strings representing the names of each point
        :param cmap: colormap to use (default is 'RdYlBu')
        :param return_scatter:
    """

    # Define colormap
    if cmap is None:
        cmap_colors = [
            "#11205E",
            "#203FB6",
            "#86CAFF",
            "white",
            "#FFEC4A",
            "#F62336",
            "#80121B",
        ]
        positions = np.linspace(0, 1, len(cmap_colors))
        cmap = LinearSegmentedColormap.from_list(
            "custom_colormap", list(zip(positions, cmap_colors))
        )

    fig = plt.figure(figsize=(8, 8), dpi=600)
    ax = fig.add_subplot(111, projection="3d")

    x = xyz[:, 0]
    y = xyz[:, 1]
    z = xyz[:, 2]
    scatter = ax.scatter(
        x, y, z, s=S, c=C, cmap=cmap, alpha=0.8, linewidth=0.5, **kwargs
    )
    for i in range(len(n_name)):
        ax.text(x[i], y[i], z[i], n_name[i], fontdict={"size": 3, "color": "grey"})

    # Show the plot
    ax.view_init(elev=90, azim=-90)
    ax.grid(False)
    ax.axis("off")

    # Set the background color to transparent
    ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

    # Adjust the spacing between the plot and the color-bar
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.83, 0.25, 0.03, 0.5])

    # Add a colorbar to the plot
    font = font_manager.FontProperties(family="Arial", style="normal", size=18)
    cbar = fig.colorbar(
        scatter,
        cax=cbar_ax,
    )
    cbar.ax.set_yticklabels(cbar.ax.get_yticklabels(), fontproperties=font)

    # Set the line width of y-tick lines
    for line in cbar.ax.yaxis.get_ticklines():
        line.set_markeredgewidth(1.5)  # Adjust the width as needed

    cbar.outline.set_visible(False)
    fig.tight_layout()

    # Set the title of the plot
    # title = ax.set_title( '{0}{1}'.format( X_name, corr_type), fontsize=10)
    # title.set_position( [0.5, -0.9] )

    if return_scatter:
        return fig, ax, scatter, cbar

    return fig, ax
