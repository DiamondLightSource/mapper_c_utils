#!/usr/bin/env python3
# encoding: utf-8

import sysconfig
from setuptools import setup, Extension
import numpy


EXTRA_COMPILE_ARGS = sysconfig.get_config_var('CFLAGS').split()
EXTRA_COMPILE_ARGS += ["-std=c99"]

ext_modules = [
    Extension(
        "mapper_c_utils",
        sources=["src/mapper_c_utils/mapper_c_utils.c"],
        include_dirs=[numpy.get_include()],
        extra_compile_args=EXTRA_COMPILE_ARGS,
        language="c99"
    )
]



if __name__ == "__main__":  
    setup(
        name="mapper_c_utils",
        version="1.1.0",
        ext_modules=ext_modules,
    )

