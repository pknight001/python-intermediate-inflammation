import numpy as np

def test_normals():

    mean = 10.0
    std = 2.0
    sample_size = 1000000

    sample = np.random.normal(mean, std, sample_size)

    np.testing.assert_almost_equal(mean, np.mean(sample), decimal=2)
    np.testing.assert_almost_equal(std, np.std(sample), decimal=2)

    print(mean, np.mean(sample))
    print(std, np.std(sample))

test_normals()