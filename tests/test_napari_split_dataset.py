#!/usr/bin/env python

"""Tests for `napari_split_dataset` package."""

from pathlib import Path

import pytest
from numpy import ndarray
from split_dataset import SplitDataset

from napari_split_dataset import napari_split_dataset

ASSETS_PATH = Path(__file__).parent / "assets"


@pytest.mark.parametrize(
    "path, expected",
    [
        ("fake.h5", True),
        ("fake.hdf5", True),
        ("fake.tif", False),
        ("fake", False),
        (ASSETS_PATH / "sample_3d", True),
        (ASSETS_PATH / "sample_4d", True),
        (ASSETS_PATH / "random", True),
        (ASSETS_PATH / "array.h5", True),
        (ASSETS_PATH / "dict_stack.h5", True),
        (ASSETS_PATH / "dict_shift.h5", True),
    ],
)
def test_reader(path, expected):
    reader = napari_split_dataset.napari_get_reader(path)
    assert callable(reader) == expected


@pytest.mark.parametrize(
    "path, expected",
    [
        (ASSETS_PATH / "sample_3d", ndarray),
        (ASSETS_PATH / "sample_4d", SplitDataset),
        (ASSETS_PATH / "random", type(None)),
        (ASSETS_PATH / "array.h5", type(None)),
    ],
)
def test_dir_reader(path, expected):
    data = napari_split_dataset.read_directory(path)
    if isinstance(data, list):
        data = data[0][0]
    assert isinstance(data, expected)


@pytest.mark.parametrize(
    "path, expected",
    [
        (ASSETS_PATH / "sample_3d", type(None)),
        (ASSETS_PATH / "array.h5", ndarray),
        (ASSETS_PATH / "dict_stack.h5", ndarray),
        (ASSETS_PATH / "dict_shift.h5", type(None)),
        (ASSETS_PATH / "nodict.h5", type(None)),
    ],
)
def test_h5_reader(path, expected):
    data = napari_split_dataset.read_hdf5(path)
    if isinstance(data, list):
        data = data[0][0]
    assert isinstance(data, expected)
