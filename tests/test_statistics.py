"""Module containing tests for the statistics module"""

import pytest
import numpy as np
import kwindy 


@pytest.mark.parametrize(
        ("U","V"), 
        [(1,2), (np.arange(1, 5, 1), np.arange(3,7,1))]
)
def test_calc_windspeed(U,V):
    """Test windspeed calculation from u and v components."""
    windspeed = kwindy.calc_windspeed(U,V)

    np.testing.assert_allclose(windspeed, np.sqrt(U**2+V**2))