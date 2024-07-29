"""Module containing statistical tools."""

import numpy as np
import xarray as xr
from scipy.stats import weibull_min


def calc_windspeed(u, v):
    """Calculates windspeed from u and v components."""
    windspeed = np.sqrt(u**2 + v**2)
    return windspeed


def calc_winddirection(u, v):
    """Calculates wind direction from the u and v components."""
    wind_dir = 90 - np.rad2deg(np.arctan2(-v, -u))
    wind_dir = wind_dir % 360
    return wind_dir


def fit_weibull(data):
    """Fit weibull distribution to data.
    Inputs:
        data: Array of float values to be fit
    Returns:
        shape: float, parameter of weibull distribution
        loc: float, parameter of weibull distribution
        scale: float, parameter of weibull distribution
    """
    shape, loc, scale = weibull_min.fit(data, floc=0)
    return shape, loc, scale


def fit_weibull_xarray(data, dim):
    """Apply Weibull fit function to Xarrary DataArray.
    Inputs:
        data: Xarray DataArray to be fit
        dim: string with name of dimension to fit along
    Outputs:
        shape: float, parameter of weibull distribution
        loc: float, parameter of weibull distribution
        scale: float, parameter of weibull distribution
    """
    return xr.apply_ufunc(
        fit_weibull,
        data,
        input_core_dims=[[dim]],
        output_core_dims=[[], [], []],
        vectorize=True,
        dask="parallelized",
        output_dtypes=[float, float, float],
    )
