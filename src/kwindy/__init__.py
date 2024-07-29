"""kwindy: Katie's windy package."""

from kwindy.dataio import load_era5_from_cloud
from kwindy.dataio import subsample_era5_variables
from kwindy.statistics import calc_winddirection
from kwindy.statistics import calc_windspeed
from kwindy.statistics import fit_weibull
from kwindy.statistics import fit_weibull_xarray


__all__ = [
    "load_era5_from_cloud",
    "subsample_era5_variables",
    "calc_winddirection",
    "calc_windspeed",
    "fit_weibull",
    "fit_weibull_xarray",
]
