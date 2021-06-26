from setuptools import setup, find_packages
from setuptools.command.install import install
import codecs
import os, sys, subprocess


VERSION = '0.0.77'
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
    package_data={'synesthesia': ['images/*.png', 'images/*.svg' ]},
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



