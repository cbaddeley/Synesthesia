from setuptools import setup, find_packages
from setuptools.command.install import install
import codecs
import os, sys, subprocess


VERSION = '0.1.05'
DESCRIPTION = 'A Python audio image creation tool'
LONG_DESCRIPTION = 'A Python audio image creation tool that takes audio and creates images from them.'


# Setting up
setup(
    name="synesthesia-uf",
    version=VERSION,
    author="Super Fun Adventure Club Dude Man Squad",
    author_email="<georgekolasa@ufl.edu",
    description=DESCRIPTION,
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/cbaddeley/Synesthesia",
    license="GPL 3",
    install_requires=['PyQt5', 'librosa', 'essentia',
                      'pillow', 'pycairo', 'musicnn'],
    keywords=['audio', 'visualizer', "image"],

    entry_points =
    {   "console_scripts":
        [
            "syne = synesthesia:pip_main_func"
        ]
    }

)



