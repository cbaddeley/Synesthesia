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

def draw_note(canvas, note, oct_selection, colors):
    octave = int(note[1]) * (3 + oct_selection)
    note = note[0][0] # exclude sharps
    canvas.clear_args()
    color = colors[random.randint(0, len(colors) - 1)] # picks random color from list
    
    if note == 'A':  # draw a circle
        canvas.append_args('circle')
    elif note == 'B':  # draw a square
        canvas.append_args('square')
    elif note == 'C':  # draw a triangle
        canvas.append_args('triangle')
    elif note == 'D':  # draw a hexagon
        canvas.append_args('hexagon')
    elif note == 'E':  # draw an octogon
        canvas.append_args('octogon')
    elif note == 'F': # draw a star
        canvas.append_args('star') 
    elif note == 'G': # change pen style
        styles = [Qt.SolidLine, Qt.DashLine, Qt.DotLine,
                   Qt.DashDotLine, Qt.DashDotDotLine, Qt.CustomDashLine]
        canvas.style = styles[octave % len(styles)]

    if octave % 8 == 0: # move up
        canvas.y = (canvas.y + octave) % 400
    elif octave % 8 == 1: # move down
        canvas.y = (canvas.y - octave) % 400
    elif octave % 8 == 2:  # move right
        canvas.x = (canvas.x + octave) % 400
    elif octave % 8 == 3: # move left
        canvas.x = (canvas.x - octave) % 400
    elif octave % 8 == 4: # move diag up right
        canvas.y = (canvas.y + octave) % 400
        canvas.x = (canvas.x + octave) % 400
    elif octave % 8 == 5: # move diag up left
        canvas.y = (canvas.y - octave) % 400
        canvas.x = (canvas.x - octave) % 400
    elif octave % 8 == 6:  # move diag down right
        canvas.y = (canvas.y - octave) % 400
        canvas.x = (canvas.x + octave) % 400
    elif octave % 8 == 7: # move diag down  left
        canvas.y = (canvas.y - octave) % 400
        canvas.x = (canvas.x - octave) % 400

    if note != 'G':
        canvas.append_args(canvas.x)
        canvas.append_args(canvas.y)
        canvas.append_args(color)
        canvas.append_args(canvas.size)
        canvas.append_args(canvas.style)
        canvas.append_args(octave) 
        canvas.append_args(None) # this is for the 8th attribute which only applies to the line algo
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
