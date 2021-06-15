@echo off
py -m venv virt
pip install PyQt5
pip install librosa
sudo apt-get install ffmpeg
sudo apt-get install gstreamer1.0-plugins-base gstreamer1.0-plugins-ugly
py ./gui.py