"""Module containing tests for the statistics module"""

import numpy as np
import pytest
import scipy.stats as stats

import kwindy


@pytest.mark.parametrize(("U", "V"), [(1, 2), (np.arange(1, 5, 1), np.arange(3, 7, 1))])
def test_calc_windspeed(U, V):
    """Test windspeed calculation from u and v components."""
    windspeed = kwindy.calc_windspeed(U, V)
    assert np.allclose(windspeed, np.sqrt(U**2 + V**2))


@pytest.mark.parametrize(
    ("U", "V", "expected_angle"),
    [(1, 1, 225), (1, -1, 315), (-1, -1, 45), (-1, 1, 135)],
)
def test_calc_winddirection(U, V, expected_angle):
    """Test winddirection calculation from u and v components."""
    winddirection = kwindy.calc_winddirection(U, V)
    assert winddirection == expected_angle


@pytest.mark.parametrize(("expected_shape", "expected_scale"), [(1, 2), (2, 10)])
def test_fit_weibull(expected_shape, expected_scale):
    """Test weibull distribution fit of data."""
    data = stats.weibull_min.rvs(expected_shape, scale=expected_scale, size=10000)
    shape, loc, scale = kwindy.fit_weibull(data)

    assert np.allclose(shape, expected_shape, atol=1e-1)
    assert np.allclose(scale, expected_scale, atol=1e-1)
