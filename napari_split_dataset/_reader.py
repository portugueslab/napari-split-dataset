"""Main module."""
from napari_plugin_engine import napari_hook_implementation
from pathlib import Path
import numpy as np
import flammkuchen as fl
from split_dataset import SplitDataset


@napari_hook_implementation
def napari_get_reader(path):
    path = Path(path)
    if path.is_dir():
        return read_directory
    elif path.suffix in [".h5", ".hdf5"]:
        return read_hdf5


def read_directory(path):
    # read the image stack from a split dataset directory

    try:
        data = SplitDataset(path)
    except:
        return None

    if len(data.shape) > 3:
        # set contrast limits for 4D data
        # otherwise napari tries to set them after reading everything, which would take too long if the data was large.
        data_for_contrast = data[min(2, data.shape[0]-1):min(7, data.shape[0]), :, :, :]
        contrast_limits = (np.percentile(data_for_contrast, 0.1), np.percentile(data_for_contrast, 99.9))



        data = data.as_dask()  # read as a dask array
        # optional kwargs for the corresponding viewer.add_* method
        add_kwargs = {"contrast_limits": contrast_limits,}
    else:
        data = data[:,:,:]
        add_kwargs = {}

    layer_type = "image"  # optional, default is "image"
    return [(data, add_kwargs, layer_type)]


def read_hdf5(path):
    # read the image if the h5 file is an array or part of split dataset files

    data = fl.load(path)
    if not isinstance(data, (np.ndarray, dict)):
        return None
    elif isinstance(data, dict):
        key = [key for key in list(data.keys()) if "stack" in key]
        if key:
            data = data[key[0]]
        else:
            return None

    add_kwargs = {}
    return [(data, add_kwargs)]
