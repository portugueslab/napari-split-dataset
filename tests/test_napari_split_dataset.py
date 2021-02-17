#!/usr/bin/env python

"""Tests for `napari_split_dataset` package."""

import pytest
from dask.array.core import Array
from numpy import ndarray
from . import ASSETS_PATH
from napari_split_dataset import _reader


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
    reader = _reader.napari_get_reader(path)
    assert callable(reader) == expected


@pytest.mark.parametrize(
    "path, expected",
    [
        (ASSETS_PATH / "sample_3d", ndarray),
        (ASSETS_PATH / "sample_4d", Array),
        (ASSETS_PATH / "random", type(None)),
        (ASSETS_PATH / "array.h5", type(None)),
    ],
)
def test_dir_reader(path, expected):
    data = _reader.read_directory(path)
    if isinstance(data, list):
        data = data[0][0]
    assert isinstance(data, expected)


@pytest.mark.parametrize(
    "path, expected",
    [
        (ASSETS_PATH / "sample_4d", type(None)),
        (ASSETS_PATH / "random", type(None)),
        (ASSETS_PATH / "array.h5", ndarray),
        (ASSETS_PATH / "dict_stack.h5", ndarray),
        (ASSETS_PATH / "dict_shift.h5", type(None)),
    ],
)
def test_h5_reader(path, expected):
    data = _reader.read_hdf5(path)
    if isinstance(data, list):
        data = data[0][0]
    assert isinstance(data, expected)
