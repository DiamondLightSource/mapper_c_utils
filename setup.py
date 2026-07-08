"""
latest version created: parsing_detector in mapper_c_utils/
"""

import numpy
from setuptools import Extension, setup

ext_modules = [
    Extension(
        "mapper_c_utils",
        sources=["src/mapper_c_utils/mapper_c_utils.c"],
        include_dirs=[numpy.get_include()],
        extra_compile_args=["-std=c99"],
    )
]

setup(
    name="mapper_c_utils",
    version="1.1.0",
    ext_modules=ext_modules,
)
