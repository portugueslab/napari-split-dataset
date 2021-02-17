#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
import os

with open('README.rst') as readme_file:
    readme = readme_file.read()

# with open('HISTORY.rst') as history_file:
#     history = history_file.read()

requirements = []
with open('requirements.txt') as f:
    for line in f:
        splitted = line.split("#")
        stripped = splitted[0].strip()
        if len(stripped) > 0:
            requirements.append(stripped)

with open("requirements_dev.txt") as f:
    requirements_dev = f.read().splitlines()

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="You Wu",
    author_email='ykure.w@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="hdf5/split-dataset file reader for napari",
    extras_require=dict(dev=requirements_dev),
    install_requires=requirements,
    license="GNU General Public License v3",
    # long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='napari_split_dataset',
    name='napari_split_dataset',
    packages=find_packages(include=['napari_split_dataset', 'napari_split_dataset.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/portugueslab/napari_split_dataset',
    version='0.1.0',
    zip_safe=False,
)
