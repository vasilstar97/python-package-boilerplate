"""
my_package.py

Python package boilerplate for IDU.

This package serves as a boilerplate for developing Python packages
for Institute of Design and Urban Studies (IDU). It includes basic metadata
such as versioning, author information, and license details.

Module Attributes
-----------------
__version__ : str
    The current version of the package as defined in the `pyproject.toml`.
__author__ : str
    The name of the package author.
__email__ : str
    The email address of the package author.
__credits__ : list
    A list of contributors to the package.
__license__ : str
    The license under which the package is distributed.
"""

import importlib

__version__ = importlib.metadata.version("my_package") # TODO поменять название в соответствии с pyproject.toml
__author__ = "Vasilii Starikov"
__email__ = "vasilstar97@gmail.com"
__credits__ = []
__license__ = "BSD-3"
