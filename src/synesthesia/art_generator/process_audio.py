
import librosa
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainterPath
from wsl import *
import warnings
set_display_to_host()
from collections import Counter
import subprocess
from . import genre_colors, shapes_algo, curvy_algo, lines_algo
import os

def proc_audio(algo,canvas, song_path, sr_selection, oct_selection, freq_scale):
    delete_wav_file = False
    if song_path[-4:] == '.mp3':
        wav_song_path = song_path[:-4] + '.wav'
        if not os.path.exists(wav_song_path):
            subprocess.call(['ffmpeg', '-i', song_path,
                             wav_song_path])
        song_path = wav_song_path
        delete_wav_file = True

    sr = sr_selection

    y, sr = librosa.load(song_path, sr=sr)
    S = np.abs(librosa.stft(y))
    if freq_scale != 0:
        S *= (1 +  (freq_scale / 100))
    try:
        bars = librosa.hz_to_note(S)
    except:
        return False

    # Musicnn gives a bunch of useless console warnings that we don't need to see and should just try to block out AMAP
    try:
        warnings.filterwarnings("ignore")
        from musicnn.tagger import top_tags
        musicGenre = top_tags(song_path, model='MSD_musicnn', topN=1)
        musicGenre = musicGenre[0]
        warnings.filterwarnings("default")
    except:
        musicGenre = ''

    path = QPainterPath()
    for i, bar in enumerate(bars):
        if i == len(bars) -1:
            pass
        d = Counter(bar)
        result = d.most_common(1)
        note = result[0]
        if '-' in note[0]:  
            if algo == 'Shape of You':
                shapes_algo.draw_note(canvas, note[0].split('-'), oct_selection, genre_colors.getColors(musicGenre))
            elif algo == 'Line Rider':
                lines_algo.draw_note(canvas, note[0].split('-'), oct_selection, genre_colors.getColors(musicGenre))
            elif algo == '/r/curvy':
                curvy_algo.draw_note(canvas, note[0].split('-'), oct_selection, genre_colors.getColors(musicGenre), path)
            
    if delete_wav_file:
        os.remove(song_path)
    return True