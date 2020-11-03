"""
Sample use of the Polygonate class.
"""
import matplotlib.pyplot as plt

# [start1]
import polygonation.polygonate as pg
import numpy as np

points = np.random.rand(20, 2)

plgn1 = pg.Polygonate(points)
# [end1]

# [start2]
plgn2 = pg.Polygonate(points, convex=False)
# [end2]


def plot_plgn(plgn: pg.Polygonate):
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))

    ax.plot(*plgn.points.T, "ko")  # points
    ax.triplot(*plgn.points.T, "k:", alpha=0.3)  # delaunay
    for shape in plgn.shapes:
        ax.plot(*plgn.points[[*shape, shape[0]]].T, "b")  # resulting polygons

    ax.set_xticks([])
    ax.set_yticks([])
    fig.tight_layout()
    return fig


def plot1():
    plot_plgn(plgn1)


def plot2():
    plot_plgn(plgn2)
