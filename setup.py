#!/usr/bin/env python

"""The setup script."""

from setuptools import find_namespace_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("requirements_dev.txt") as f:
    requirements_dev = f.read().splitlines()

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="You Wu @portugueslab",
    author_email="youkwu@neuro.mpg.de",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="hdf5/split-dataset file reader for napari",
    long_description=readme,
    long_description_content_type="text/markdown",
    extras_require=dict(dev=requirements_dev),
    entry_points={
        "napari.plugin": ["split-dataset = napari_split_dataset"],
    },
    install_requires=requirements,
    license="MIT",
    include_package_data=True,
    keywords="napari_split_dataset",
    name="napari_split_dataset",
    packages=find_namespace_packages(exclude=("docs", "tests*")),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/portugueslab/napari_split_dataset",
    version="0.2.0",
    zip_safe=False,
)
