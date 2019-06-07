from setuptools import setup, find_packages

import my_upper_level_project

setup(
    name='my_upper_level_project',
    packages=find_packages(),
    version=my_upper_level_project.__version__
)
