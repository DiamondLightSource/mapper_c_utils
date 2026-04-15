"""
latest version created: distcalc in mapper_c_utils/
"""

import sysconfig

from numpy.distutils.core import setup
from numpy.distutils.misc_util import Configuration, get_info

EXTRA_COMPILE_ARGS = sysconfig.get_config_var("CFLAGS").split() + ["-std=c99"]


def configuration(parent_package="", top_path=None):
    info = get_info("npymath")
    config = Configuration("", parent_package, top_path)
    config.add_extension(
        "mapper_c_utils",
        ["src/mapper_c_utils/mapper_c_utils.c"],
        extra_info=info,
        language="c99",
        extra_compile_args=EXTRA_COMPILE_ARGS,
    )
    return config


if __name__ == "__main__":
    setup(name="mapper_c_utils", version="1.1.0", configuration=configuration)
