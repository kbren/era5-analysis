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
    assert np.allclose(windspeed, np.sqrt(U**2+V**2))


@pytest.mark.parametrize(
        ("U","V","expected_angle"), 
        [(1,1,225), (1,-1,315),(-1,-1,45),(-1,1,135)]
)
def test_calc_winddirection(U,V,expected_angle):
    """Test windspeed calculation from u and v components."""
    winddirection= kwindy.calc_winddirection(U,V)
    assert winddirection == expected_angle