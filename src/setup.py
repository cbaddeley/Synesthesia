from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.60'
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
                      'pillow', 'pycairo'],
    keywords=['audio', 'visualizer', "image"],

    entry_points =
    {   "console_scripts":
        [
            "syne = synesthesia:pip_main_func"
        ]
    }

)