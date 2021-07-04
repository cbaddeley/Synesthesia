
from . import genre_colors, shapes_algo, curvy_algo, lines_algo, dbm
import os
import subprocess
from collections import Counter
import pickle
import librosa
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainterPath
from synesthesia.wsl import *
import warnings
set_display_to_host()


def drawer(canvas, algo, note, frq, oct_selection, genre):
    if '-' in note[0]:
        if algo == 'Shape of You':
            shapes_algo.draw_note(canvas, note[0].split(
                '-'), oct_selection, genre_colors.getColors(genre))
        elif algo == 'Line Rider':
            lines_algo.draw_note(canvas, note[0].split(
                '-'), oct_selection, genre_colors.getColors(genre))
        elif algo == 'Curvy':
            path = QPainterPath()
            curvy_algo.draw_note(canvas, note[0].split(
                '-'), oct_selection, genre_colors.getColors(genre), path)


def proc_audio(algo, canvas, song_path, sr_selection, oct_selection, freq_scale):
    is_mp3 = False
    have_sample = False
    try:
        S, bars, genre = dbm.db_driver(
            'r', song_path, freq_scale, sr_selection)[0]
        S = np.frombuffer(S, dtype="float32")
        bars = pickle.loads(bars)
        have_sample = True
    except IndexError or TypeError:  # when song not found
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
            S *= (1 + (freq_scale / 100))
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

    if not have_sample:
        disp_notes = []
        disp_frq = []
        for i, bar in enumerate(bars):

            c = Counter(bar)
            result = c.most_common(1)
            note = result[0]
            disp_notes.append(note)

            c = Counter(S[i])
            result = c.most_common(1)
            frq = result[0]
            disp_frq.append(frq)
            drawer(algo, canvas, note, frq, oct_selection, genre)

        dbm.db_driver('i', song_path, freq_scale, sr_selection, S, bars, genre)
        if is_mp3:
            os.remove(wav_path)
    else: # we have a sample of the audio
        for i, note in enumerate(bars):
            drawer(algo, canvas, note, S[i], oct_selection, genre)

    return True
