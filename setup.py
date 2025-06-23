import re

from pkg_resources import DistributionNotFound, get_distribution
from setuptools import setup, find_packages




MIN_OPENCV_VERSION = "4.9.0.80"

INSTALL_REQUIRES = [
    "numpy>=1.24.4",
    "typing-extensions>=4.9.0; python_version<'3.10'",
    "stringzilla>=3.10.4",
    "simsimd>=5.9.2",
]

setup(
    packages=find_packages(exclude=["tests", "benchmark"], include=['albucore*']),
    install_requires=INSTALL_REQUIRES,
    extras_require={
        "opencv": [f"opencv-python>={MIN_OPENCV_VERSION}"],
        "opencv-contrib": [f"opencv-contrib-python>={MIN_OPENCV_VERSION}"],
        "opencv-contrib-headless": [f"opencv-contrib-python-headless>={MIN_OPENCV_VERSION}"],
    },
)
