============
polygonation
============

.. image:: https://img.shields.io/travis/rwijtvliet/polygonation.svg
        :target: https://travis-ci.org/rwijtvliet/polygonation

.. image:: https://img.shields.io/pypi/v/polygonation.svg
        :target: https://pypi.python.org/pypi/polygonation


Python package to tessellate a set of points in the plane with polygons.

Done by identifying the removable edges, and then removing one of them by some selection criterion. Rinse-repeat until no further edges can be removed.

Sample use, finding a set of convex polygons:

.. code-block:: python
  import numpy as np
  from polygonation.polygonate import Polygonate
  n = 20
  points = np.random.rand(n*2).reshape(-1, 2)
  pg = Polygonate(points)
  
.. plot::
  import numpy as np
  import matplotlib.pyplot as plt
  from polygonation.polygonate import Polygonate
  n = 20
  points = np.random.rand(n*2).reshape(-1, 2)
  pg = Polygonate(points)
  fig, ax = plt.subplots(1, 1, figsize=(10,10))
  pg.plotdelaunay(ax, alpha=0.2)
  pg.plotpolygons(ax)
  pg.plotpoints(ax)
  
