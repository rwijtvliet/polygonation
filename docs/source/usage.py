"""
Sample use of the Polygonate class.
"""

import matplotlib.pyplot as plt


import polygonation as pg
import numpy as np

points = np.random.rand(20, 2)

plgn1 = pg.Polygonate(points)
plgn1.shapes


print([pg.is_convex(points[s]) for s in plgn1.shapes])


plgn2 = pg.Polygonate(points, convex=False)
plgn2.shapes


def plot1():
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    for i, (plgn, ax) in enumerate(zip([plgn1, plgn2], axes)):
        ax.plot(*points.T, "ko")  # points
        ax.triplot(*plgn.points.T, "k:", alpha=0.3)  # delaunay
        for shape in plgn.shapes:
            ax.plot(*plgn.points[[*shape, shape[0]]].T, "b")  # resulting polygons
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title("convex = " + ["True", "False"][i])
    fig.tight_layout()
    return fig


plot1()  # .savefig('source/savefig/plot1.png') #not using @savefig, because it leaves an empty line

points = np.random.rand(20, 2)


def plot2a():
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].set_title("points")
    axes[1].triplot(*points.T, "k-", alpha=0.5)
    axes[1].set_title("Delaunay grid")
    for ax in axes:
        ax.plot(*points.T, "ko")
        ax.set_xticks([])
        ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(False)
    fig.tight_layout()
    return fig


def plot2(convex):
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    for ax in axes:
        ax.set_xticks([])
        ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(False)
        ax.triplot(*points.T, "k:", alpha=0.3)
    for ax, pickedge in zip(axes, ["long", "acute", "round"]):
        ax.set_title(f"pickedge = {pickedge}")
        for shape in pg.Polygonate(points, pickedge=pickedge, convex=convex).shapes:
            ax.plot(*points[[*shape, shape[0]]].T, "b")  # resulting polygons
    fig.tight_layout()
    return fig


plot2a()  # .savefig('source/savefig/plot2a.png')

plot2(True)  # .savefig('source/savefig/plot2convextrue.png')

plot2(False)  # .savefig('source/savefig/plot2convexfalse.png')
