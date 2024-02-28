# %%
from vptree import *
from numpy.random import default_rng


x = default_rng().normal(0, 1, size=(100, 2))

T = vptree(x)

# %%
z = np.array([0, 0]).reshape(1, 2)
A = T.nearest_pts(z, 5)
# %%
