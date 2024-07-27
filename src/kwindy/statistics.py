"""Module containing statistical tools."""

import numpy as np


def calc_windspeed(u, v):
    """Calculates windspeed from u and v components."""
    windspeed = np.sqrt(u**2+v**2)
    return windspeed


def calc_winddirection(u, v):
    """Calculates wind direction from the u and v components."""
    wind_dir = 90 - np.rad2deg(np.arctan2(-v, -u))
    wind_dir = wind_dir % 360 
    return wind_dir