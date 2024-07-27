"""Module containing statistical tools."""

import numpy as np


def calc_windspeed(u, v):
    """Calculates windspeed from u and v components."""
    windspeed = np.sqrt(u**2+v**2)
    return windspeed


def calc_winddirection(u, v):
    """Calculates wind direction from the u and v components."""
    wind_dir = np.arctan2(-u, -v) * (180 / np.pi)
    wind_dir = (wind_dir + 360) % 360 
    return wind_dir