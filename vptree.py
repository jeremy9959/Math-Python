import numpy as np


class _nqueue(list):
    """A simple fixed length priority queue of tuples used by the vptree class to track
    the closest points found so far.  Contains pairs (dist, node) where node refers to the
    vptree structure and dist is the distance from the given point to the corresponding node.
    Only the smallest max_size examples are kept.

    Does a simple append followed by sort, so is intended for short lists.
    """

    def __init__(self, max_size, *args):

        super(_nqueue, self).__init__(*args)
        self.max_size = max_size

    def append(self, item):

        super(_nqueue, self).append(item)
        self.sort(key=lambda x: x[0])
        if len(self) > self.max_size:
            self.pop()

    @property
    def is_empty(self):
        return len(self) == 0

    @property
    def is_full(self):
        return len(self) == self.max_size

    @property
    def farthest_distance(self):
        if self:
            return self[-1][0]
        else:
            return 0

class vptree:
    """A vantage point tree class.  Given a set of points z, this class is useful for finding
    the n points in z closest to a given point p.

    Attributes
    ----------
        T -- a dict with integer keys, where T[2*i+1] and T[2*i+2] are the left and right children of T[i]
        and the value of z[T[i]] is the corresponding data pont.
        D -- a dict with integer keys, where D[i] is the median (splitting) distance from the point z[T[i]]
        that separates the left and right subtrees at node i.
        z -- the original data, given as a numpy array with dimensions n x d where n is the number of points and
        d is the dimension of the vector space where they lie.

    Methods
    -------
        nearest_pts -- finds the n nearest points among the points in z to a given point p.
    """

    def __init__(self, z):
        self.T = {}
        self.D = {}
        self.z = z
        self._dim = z.shape[1]
        self._r = np.arange(z.shape[0])
        self._make_tree(z, self._r, self.T, self.D, 0)

    @property
    def dim(self):
        return self._dim

    def _dist(self, a, b):
        return np.sqrt(np.square(a-b).sum(axis=1))
 
    # recursive construction of the tree from the data
    # r is a list of indices into z that are under consideration
    # they are sorted so that r[-1] is the farthest from the parent
    # among the points z[r,:]
    def _make_tree(self, z, r, T, D, i):

        self.T[i] = r[-1]
        # if len(r)==1, we are at a leaf node, so no need to descend
        if len(r) > 1:

            d = self._dist(z[r[-1], :], z[r[:-1], :])
            s = np.argsort(d)

            m0 = len(s)//2

            # compute the median distance to the node under consideration
            D[i] = d[s[m0]] if len(s) % 2 == 1 else (d[s[m0-1]]+d[s[m0]])/2

            # make the right subtree from the larger half
            self._make_tree(z, r[s[m0:]], T, D, 2*i+2)

            # if the smaller half is non-empty, make the left subtree from the smaller
            # half
            if m0 > 0:
                self._make_tree(z, r[s[0:m0]], T, D, 2*i+1)

        return

    # find the nearest points.  Maintain the list closest_so_far of pairs (dist, node)
    def _nni(self, p, i, closest_so_far):

        this_distance = self._dist(p, self.z[self.T[i]])[0]
        test_distance = closest_so_far.farthest_distance

        # if the current point is a potential nearest point, insert it for consideration
        if closest_so_far.is_empty or this_distance < test_distance:
            closest_so_far.append((this_distance, i))

        # if the left subtree is nonempty, and there could be closer points to the left,
        # look left
        if 2*i+1 in self.T:
            if this_distance <= self.D[i] + test_distance or not closest_so_far.is_full:
                self._nni(p, 2*i+1, closest_so_far)

        # if the right subtree is nonempty, and there could be closer points to the right,
        # look right
        if 2*i+2 in self.T:
            if this_distance >= self.D[i] - test_distance or not closest_so_far.is_full:
                self._nni(p, 2*i+2, closest_so_far)

        return
          
    def nearest_pts(self, p, n):
        """Given p (a 1 x d numpy array) and n (an integer) finds the n points in z closest to p. Returns
        an n x d numpy array.
        """
        if type(p) != np.ndarray or p.shape != (1, self._dim):
            raise TypeError("Expecting a 1 x {} numpy array representing the point".format(self.d))

        # set up the empty queu
        closest_so_far = _nqueue(n)

        # start the recursive process at the root of the tree
        self._nni(p, 0, closest_so_far)

        # extract the points from the indices
        closest_z = [self.T[x[1]] for x in closest_so_far]

        return self.z[closest_z, :]