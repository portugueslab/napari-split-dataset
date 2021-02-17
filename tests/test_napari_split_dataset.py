#!/usr/bin/env python

"""Tests for `napari_split_dataset` package."""

import pytest
from dask.array.core import Array
from numpy import ndarray

from napari_split_dataset import _reader


@pytest.mark.parametrize(
    "path",
    [
        "fake.h5",
        "fake.hdf5",
        "fake.tif",
        "fake",
        "asset/sample_3d",
        "asset/sample_4d",
        "asset/empty",
        "asset/array.h5",
        "asset/dict_stack.h5",
        "asset/dict_shift.h5",
    ],
)
def test_reader(path):
    reader = _reader.napari_get_reader(path)
    assert callable(reader)


@pytest.mark.parametrize(
    "path",
    [
        "asset/sample_3d",
        "asset/sample_4d",
        "asset/empty",
        "asset/array.h5",
    ],
)
def test_dir_reader(path):
    data = _reader.read_directory(path)
    assert isinstance(data[0][0], (ndarray, Array))


@pytest.mark.parametrize(
    "path",
    [
        "asset/sample_4d",
        "asset/empty",
        "asset/array.h5",
        "asset/dict_stack.h5",
        "asset/dict_shift.h5",
    ],
)
def test_h5_reader(path):
    data = _reader.read_hdf5(path)
    assert isinstance(data[0][0], ndarray)
