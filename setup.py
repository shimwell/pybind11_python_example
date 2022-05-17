import sys

from pybind11 import get_cmake_dir
# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup
import os

__version__ = "0.0.7"

# The main interface is through Pybind11Extension.
# * You can add cxx_std=11/14/17, and then build_ext can be removed.
# * You can set include_pybind11=false to add the include directory yourself,
#   say from a submodule.
#
# Note:
#   Sort input source files if you glob sources to ensure bit-for-bit
#   reproducible builds (https://github.com/pybind/dagmc_volume_finder/pull/53)

dagmc_path = os.path.abspath(".")
print('dagmc_path', dagmc_path)
print('dagmc_path', dagmc_path)
print('dagmc_path', dagmc_path)
print('dagmc_path', dagmc_path)
print('dagmc_path', dagmc_path)
print('dagmc_path', dagmc_path)
print()
print()
print()
print()

conda_path = os.getenv('CONDA_PREFIX')
SRC_DIR = os.getenv('SRC_DIR')
print('SRC_DIR', SRC_DIR)
print('SRC_DIR', SRC_DIR)
print('SRC_DIR', SRC_DIR)
print('SRC_DIR', SRC_DIR)
print('SRC_DIR', SRC_DIR)
print('SRC_DIR', SRC_DIR)
print()
print()
print()
print()

# # attempting to write the missing file to the folder
# from pathlib import Path
# with open(Path(SRC_DIR)/ "vendor/dagmc/src/dagmc/DagMCVersion.hpp", 'w') as opened_file:
#     opened_file.write('define DAGMC_VERSION 3.2\n')
#     opened_file.write('define DAGMC_VERSION_STRING "3.2"\n')
#     opened_file.write('define DAGMC_GIT_SHA "3fd335ea3f4360aa6043b30371795ade6ec9919c"\n')



# export BUILD_PREFIX=/tmp/conda-build/dagmc-volumer-finder/dagmc_volume_finder_1652696316582/_build_env
# export SRC_DIR=/tmp/conda-build/dagmc-volumer-finder/dagmc_volume_finder_1652696316582/work

print('dagmc_path', dagmc_path)

ext_modules = [
    Pybind11Extension(
        "dagmc_volume_finder",
        ["src/main.cpp"],
        # ext_modules
        include_dirs=[
            # 'include/',
            # 'include/dagmc/',
            # 'include/dagmc/src/',
            # 'include/dagmc/src/dagmc/',
            'vendor/',
            'vendor/dagmc/',
            'vendor/dagmc/src/',
            'vendor/dagmc/src/dagmc/',
            'vendor/moab/',
            'vendor/moab/src/',
            'vendor/moab/src/moab/',
        ],
        define_macros=[('VERSION_INFO', __version__)],
        ),
]

# ext_modules = [
#     Pybind11Extension("dagmc_volume_finder",
#         ["src/main.cpp"],
#         # ext_modules
#         include_dirs=[f'{conda_path}/include/'],
#         # include_dirs=['/home/jshimwell/miniconda3/envs/dagmc_volume_finder_dev/include/'],  # includes a local folder
#         # include_dirs=['/home/jshimwell/miniconda3/envs/dagmc_volume_finder_dev/include/'],  # includes a local folder
#         # Example: passing in the version to the compiled code
#         define_macros = [('VERSION_INFO', __version__)],
#         ),
# ]

setup(
    name="dagmc_volume_finder",
    version=__version__,
    author="Sylvain Corlay",
    author_email="sylvain.corlay@gmail.com",
    url="https://github.com/pybind/dagmc_volume_finder",
    description="A test project using pybind11",
    long_description="",
    ext_modules=ext_modules,
    extras_require={"test": "pytest"},
    # Currently, build_ext only provides an optional "highest supported C++
    # level" feature, but in the future it may provide more features.
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.6",
)
