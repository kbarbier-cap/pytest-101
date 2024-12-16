from pathlib import Path
from setuptools import setup, find_packages

import sys
sys.path.append('./src')

this_filepath = Path(__file__)
this_abs_filepath = this_filepath.resolve()
this_dir = this_abs_filepath.parent

requirements_filepath = Path(this_dir, "requirements.txt")
assert requirements_filepath.is_file() == True, f"{requirements_filepath} file cannot be found"
with open(requirements_filepath) as requirements_file:
    requirements = requirements_file.read().splitlines()


import python_unit_tests_101

setup(
    name="python_unit_tests_101",
    python_requires='>=3.10',
    version=python_unit_tests_101.__version__,
    packages=find_packages(where='./src', exclude="tests"),
    package_dir={'': 'src'},
    install_requires=requirements
)
