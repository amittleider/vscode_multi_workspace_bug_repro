from setuptools import setup, find_packages

import my_level_1_project

setup(
    name='my_level_1_project',
    packages=find_packages(),
    version=my_level_1_project.__version__
)
