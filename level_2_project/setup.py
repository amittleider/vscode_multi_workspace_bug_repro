from setuptools import setup, find_packages

import my_level_2_project

setup(
    name='my_level_2_project',
    packages=find_packages(),
    version=my_level_2_project.__version__
)
