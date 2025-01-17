"""Setup for the ClassyFire package."""

import os
import re
from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the relevant file
with open(os.path.join(here, "README.md"), encoding="utf8") as f:
    long_description = f.read()


def read(*parts):
    with open(os.path.join(here, *parts), "r", encoding="utf8") as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


__version__ = find_version("classyfire", "__version__.py")

test_deps = [
    "pytest",
    "pytest-readme",
    "validate_version_code",
]

extras = {
    "test": test_deps,
}

setup(
    name="brics_dag",
    version=__version__,
    description="Python package to generate BRICS-based DAGs from your favourite chemical sources, like PubChem.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LucaCappelletti94/BRICS-DAG",
    author="LucaCappelletti94",
    license="MIT",
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    tests_require=test_deps,
    python_requires=">=3.9",
    install_requires=["typeguard", "tqdm", "pandas", "compress_json"],
    extras_require=extras,
    entry_points={
        "console_scripts": [
            "brigs_dag=brigs_dag.cli:main",
        ],
    },
)
