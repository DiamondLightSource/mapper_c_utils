import sysconfig

import numpy as np
from setuptools import Extension, setup

EXTRA_COMPILE_ARGS = sysconfig.get_config_var("CFLAGS").split() + ["-std=c99"]


ext = Extension(
    name="mapper_c_utils",
    sources=["src/mapper_c_utils/mapper_c_utils.c"],
    include_dirs=[
        sysconfig.get_paths()["include"],  # correct python
        np.get_include(),
    ],
    extra_compile_args=["-std=c99", "-I/dls_sw/apps/mamba/2.0.5/include/python3.12"],
)


setup(
    name="mapper_c_utils",
    version="1.1.0",
    ext_modules=[ext],
)
