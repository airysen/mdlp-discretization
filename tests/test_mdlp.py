from sklearn.utils.testing import assert_array_equal
from sklearn.utils.testing import assert_equal
from sklearn.utils.testing import assert_almost_equal
from sklearn.utils.testing import assert_array_almost_equal

import sys
sys.path.insert(0, "..")

from discretization import MDLP
from _mdlp import _slice_entropy

import numpy as np

def test_slice_entropy():

    y = np.array([0, 0, 0, 1, 1, 0, 1, 3, 1, 1])

    entropy1, k1 = _slice_entropy(y, 0, 3)
    entropy2, k2 = _slice_entropy(y, 3, 10)

    assert_equal(entropy1, 0, "Entropy was not calculated correctly.")
    assert_equal(k1, 1, "Incorrect number of classes found.")
    assert_almost_equal(entropy2, 0.796311640173813,
                        err_msg="Entropy was not calculated correctly.")
    assert_equal(k2, 3, "Incorrect number of classes found.")


def test_mdlp_iris():
    from sklearn.datasets import load_iris

    iris = load_iris()
    X = iris.data
    y = iris.target
    mdlp = MDLP(shuffle=False)
    transformed = mdlp.fit_transform(X, y)

    expected = [[ 0.,  1.,  0.,  0.],
        [ 0.,  0.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  0.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  0.,  0.,  0.],
        [ 0.,  0.,  0.,  0.],
        [ 1.,  1.,  0.,  0.],
        [ 1.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 1.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  0.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  0.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  0.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  0.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 1.,  1.,  1.,  1.],
        [ 1.,  1.,  1.,  1.],
        [ 1.,  1.,  1.,  1.],
        [ 0.,  0.,  1.,  1.],
        [ 1.,  0.,  1.,  1.],
        [ 1.,  0.,  1.,  1.],
        [ 1.,  1.,  1.,  1.],
        [ 0.,  0.,  1.,  1.],
        [ 1.,  0.,  1.,  1.],
        [ 0.,  0.,  1.,  1.],
        [ 0.,  0.,  1.,  1.],
        [ 1.,  0.,  1.,  1.],
        [ 1.,  0.,  1.,  1.],
        [ 1.,  0.,  1.,  1.],
        [ 1.,  0.,  1.,  1.],
        [ 1.,  1.,  1.,  1.],
        [ 1.,  0.,  1.,  1.],
        [ 1.,  0.,  1.,  1.],
        [ 1.,  0.,  1.,  1.],
        [ 1.,  0.,  1.,  1.],
        [ 1.,  1.,  1.,  2.],
        [ 1.,  0.,  1.,  1.],
        [ 1.,  0.,  1.,  1.],
        [ 1.,  0.,  1.,  1.],
        [ 1.,  0.,  1.,  1.],
        [ 1.,  0.,  1.,  1.],
        [ 1.,  0.,  1.,  1.],
        [ 1.,  0.,  2.,  1.],
        [ 1.,  0.,  1.,  1.],
        [ 1.,  0.,  1.,  1.],
        [ 0.,  0.,  1.,  1.],
        [ 0.,  0.,  1.,  1.],
        [ 1.,  0.,  1.,  1.],
        [ 1.,  0.,  2.,  1.],
        [ 0.,  0.,  1.,  1.],
        [ 1.,  1.,  1.,  1.],
        [ 1.,  1.,  1.,  1.],
        [ 1.,  0.,  1.,  1.],
        [ 1.,  0.,  1.,  1.],
        [ 0.,  0.,  1.,  1.],
        [ 0.,  0.,  1.,  1.],
        [ 1.,  0.,  1.,  1.],
        [ 1.,  0.,  1.,  1.],
        [ 0.,  0.,  1.,  1.],
        [ 1.,  0.,  1.,  1.],
        [ 1.,  0.,  1.,  1.],
        [ 1.,  0.,  1.,  1.],
        [ 1.,  0.,  1.,  1.],
        [ 0.,  0.,  1.,  1.],
        [ 1.,  0.,  1.,  1.],
        [ 1.,  1.,  2.,  2.],
        [ 1.,  0.,  2.,  2.],
        [ 1.,  0.,  2.,  2.],
        [ 1.,  0.,  2.,  2.],
        [ 1.,  0.,  2.,  2.],
        [ 1.,  0.,  2.,  2.],
        [ 0.,  0.,  1.,  1.],
        [ 1.,  0.,  2.,  2.],
        [ 1.,  0.,  2.,  2.],
        [ 1.,  1.,  2.,  2.],
        [ 1.,  1.,  2.,  2.],
        [ 1.,  0.,  2.,  2.],
        [ 1.,  0.,  2.,  2.],
        [ 1.,  0.,  2.,  2.],
        [ 1.,  0.,  2.,  2.],
        [ 1.,  1.,  2.,  2.],
        [ 1.,  0.,  2.,  2.],
        [ 1.,  1.,  2.,  2.],
        [ 1.,  0.,  2.,  2.],
        [ 1.,  0.,  2.,  1.],
        [ 1.,  1.,  2.,  2.],
        [ 1.,  0.,  1.,  2.],
        [ 1.,  0.,  2.,  2.],
        [ 1.,  0.,  1.,  2.],
        [ 1.,  1.,  2.,  2.],
        [ 1.,  1.,  2.,  2.],
        [ 1.,  0.,  1.,  2.],
        [ 1.,  0.,  1.,  2.],
        [ 1.,  0.,  2.,  2.],
        [ 1.,  0.,  2.,  1.],
        [ 1.,  0.,  2.,  2.],
        [ 1.,  1.,  2.,  2.],
        [ 1.,  0.,  2.,  2.],
        [ 1.,  0.,  2.,  1.],
        [ 1.,  0.,  2.,  1.],
        [ 1.,  0.,  2.,  2.],
        [ 1.,  1.,  2.,  2.],
        [ 1.,  1.,  2.,  2.],
        [ 1.,  0.,  1.,  2.],
        [ 1.,  1.,  2.,  2.],
        [ 1.,  1.,  2.,  2.],
        [ 1.,  1.,  2.,  2.],
        [ 1.,  0.,  2.,  2.],
        [ 1.,  1.,  2.,  2.],
        [ 1.,  1.,  2.,  2.],
        [ 1.,  0.,  2.,  2.],
        [ 1.,  0.,  2.,  2.],
        [ 1.,  0.,  2.,  2.],
        [ 1.,  1.,  2.,  2.],
        [ 1.,  0.,  2.,  2.]]

    assert_array_equal(transformed, expected,
                       err_msg="MDLP output is inconsistent with previous runs.")
