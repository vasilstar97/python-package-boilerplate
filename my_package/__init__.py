"""
This package helps one to automatically generate master plan requirements for urban areas.
"""

import importlib

__version__ = importlib.metadata.version("my_package") #TODO поменять название в соответствии с pyproject.toml
__author__ = "Vasilii Starikov"
__email__ = "vasilstar97@gmail.com"
__credits__ = []
__license__ = "BSD-3"

from blocksnet.method import *
from blocksnet.models import *
from blocksnet.preprocessing import *
