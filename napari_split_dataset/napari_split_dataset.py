"""Main module."""
from pathlib import Path

import flammkuchen as fl
import numpy as np
from napari_plugin_engine import napari_hook_implementation
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
    except (IndexError, KeyError, ValueError):
        return None

    if len(data.shape) > 3:
        # set contrast limits for 4D data.
        # otherwise napari tries to set them after reading everything,
        # which would take too long if the data was large.
        partial = data[min(2, data.shape[0] - 1) : min(7, data.shape[0]), :, :, :]
        contrast_limits = (
            np.percentile(partial, 0.1),
            np.percentile(partial, 99.9),
        )

        add_kwargs = {
            "contrast_limits": contrast_limits,
        }
    else:
        data = data[:, :, :]
        add_kwargs = {}

    layer_type = "image"  # default
    return [(data, add_kwargs, layer_type)]


def read_hdf5(path):
    # read the image if the h5 file is an array or part of split dataset files
    try:
        data = fl.load(path)
    except (OSError, RuntimeError):
        return None

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
