"""Module for data input/output handling."""

import xarray as xr 


def load_era5_from_cloud(desired_chunks):
    """Load ERA5 dataset from GCS.
    Inputs: 
        desired chunks: string or dictionary with desired chunks

    Returns: 
        full_era5_ds: xarray dataset containing full ERA5 dataset
    """
    full_era5_ds = xr.open_zarr(
        'gs://gcp-public-data-arco-era5/ar/full_37-1h-0p25deg-chunk-1.zarr-v3',
        chunks=desired_chunks,
        storage_options=dict(token='anon'),
    )
    return full_era5_ds