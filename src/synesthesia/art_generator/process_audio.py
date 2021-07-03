
import pickle
import librosa
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainterPath
from synesthesia.wsl import *
import warnings
set_display_to_host()
from collections import Counter
import subprocess
import os
from . import genre_colors, shapes_algo, curvy_algo, lines_algo, dbm

def proc_audio(algo,canvas, song_path, sr_selection, oct_selection, freq_scale):
    is_mp3 = False
    try:
        S, bars, genre = dbm.db_driver('r', song_path, freq_scale, sr_selection)[0]
        S = np.frombuffer(S, dtype="float32") ## Error here
        bars = pickle.loads(bars)
    except IndexError or TypeError: # when song not found
        if song_path[-4:] == '.mp3':
            wav_path = song_path[:-4] + '.wav'
            is_mp3 = True
            if not os.path.exists(wav_path):
                subprocess.call(['ffmpeg', '-i', song_path, wav_path])
        if is_mp3:
            y, sr = librosa.load(wav_path, sr=sr_selection)
        else:
            y, sr = librosa.load(song_path, sr=sr_selection)
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
            genre = top_tags(song_path, model='MSD_musicnn', topN=1)
            genre = genre[0]
            warnings.filterwarnings("default")
        except:
            genre = ''
            
        # TODO: store only the most common notes and freq
        dbm.db_driver('i', song_path, freq_scale, sr_selection,S,bars,genre)

    path = QPainterPath()
    for i, bar in enumerate(bars):
        if i == len(bars) -1:
            pass
        d = Counter(bar)
        result = d.most_common(1)
        note = result[0]
        if '-' in note[0]:  
            if algo == 'Shape of You':
                shapes_algo.draw_note(canvas, note[0].split('-'), oct_selection, genre_colors.getColors(genre))
            elif algo == 'Line Rider':
                lines_algo.draw_note(canvas, note[0].split('-'), oct_selection, genre_colors.getColors(genre))
            elif algo == 'Curvy':
                curvy_algo.draw_note(canvas, note[0].split('-'), oct_selection, genre_colors.getColors(genre), path)
            
    if is_mp3:
        os.remove(wav_path)
    return True