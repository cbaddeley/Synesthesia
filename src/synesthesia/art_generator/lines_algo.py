import librosa
import numpy as np
from PyQt5.QtCore import Qt
from wsl import *
import warnings
set_display_to_host()
from collections import Counter
import subprocess
import os
from . import genre_colors
import random

# blank until gotten below
musicGenre = ''


def draw_note(canvas, note, octave_scale, colors):

    octave = int(int(note[1]) * (3 + (octave_scale / 100)))
    note = note[0][0] # exclude sharps
    x = canvas.x
    y = canvas.y
    xdiff = 0
    ydiff = 0
    stretch_factor = 1
    canvas.clear_args()
    color = colors[random.randint(0, len(colors) - 1)] # picks random color from list
    canvas.append_args('line')
    
    if note == 'A':  # move N
        ydiff = 10
    elif note == 'B':  # move NE
        xdiff = 7
        ydiff = 7
    elif note == 'C':  # move E
        xdiff = 10
    elif note == 'D':  # move SE
        xdiff = 7
        ydiff = -7
    elif note == 'E':  # move S
        ydiff = -10
    elif note == 'F': # move SW
        ydiff = -7
        xdiff = -7
    elif note == 'G': # move W
        xdiff = -10
    elif note == 'A#': # move NW
        xdiff = -7
        ydiff = 7
    elif note == 'C#': # move NNE
        ydiff = 8
        xdiff = 6
    elif note == 'F#': # move WSW
        xdiff = -8
        ydiff = -6
    elif note == 'G#': # move SSE
        ydiff = -8
        xdiff = 6
        

    stretch_factor = ((octave % 8) + 1) / 2
    canvas.x = x
    canvas.y = y
    xdiff *= stretch_factor
    ydiff *= stretch_factor

    canvas.append_args(canvas.x)
    canvas.append_args(canvas.y)
    canvas.append_args(color)
    canvas.append_args(canvas.size)
    canvas.append_args(canvas.style)
    canvas.append_args(xdiff)
    canvas.append_args(ydiff) 
    canvas.ready()


def notes_to_canvas(canvas, song_path, sr_selection, oct_selection, freq_scale):
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
    bars = librosa.hz_to_note(S)

    # Musicnn gives a bunch of useless console warnings that we don't need to see and should just try to block out AMAP
    try:
        warnings.filterwarnings("ignore")
        from musicnn.tagger import top_tags
        musicGenre = top_tags(song_path, model='MSD_musicnn', topN=1)
        musicGenre = musicGenre[0]
        warnings.filterwarnings("default")
        print("The genre is " + musicGenre)
    except:
        print("\nNo file path given.")

    for i, bar in enumerate(bars):
        if i == len(bars) -1:
            pass
        d = Counter(bar)
        result = d.most_common(1)
        note = result[0]
        if '-' in note[0]:  
            draw_note(canvas, note[0].split('-'), oct_selection, genre_colors.getColors(musicGenre))
    
    if delete_wav_file:
        os.remove(song_path)
