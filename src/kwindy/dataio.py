"""Module for data input/output handling."""

import xarray as xr


def open_era5_from_cloud(desired_chunks):
    """Open ERA5 dataset from GCS.
    Inputs:
        desired_chunks: string or dictionary with desired chunks

    Returns:
        full_era5_ds: xarray dataset containing full ERA5 dataset
    """
    full_era5_ds = xr.open_zarr(
        "gs://gcp-public-data-arco-era5/ar/full_37-1h-0p25deg-chunk-1.zarr-v3",
        chunks=desired_chunks,
        storage_options=dict(token="anon"),
    )
    return full_era5_ds


def subsample_era5_variables(full_era5_ds, variables):
    """Subsample relevant variables from full ERA5 dataset.
    Inputs:
        full_era5_ds: xarray.dataset will all ERA5 variables
        variables: list of strings with desired variable names

    Return:
        era5_subset_ds: xarray.dataset with subsampled variables
    """

    vars_to_drop = [var for var in list(full_era5_ds.data_vars) if var not in variables]

    era5_subset_ds = full_era5_ds.drop_vars(vars_to_drop)
    era5_subset_ds = era5_subset_ds.drop_vars("level")

    return era5_subset_ds
