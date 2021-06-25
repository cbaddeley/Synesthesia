import librosa
import numpy as np
from PyQt5.QtCore import Qt
from wsl import *
import warnings
set_display_to_host()
from collections import Counter
import subprocess
import os


# Purely for reference: All possible music genres a song can be (can be deleted later)
# “rock”, “pop”, “alternative”, “indie”, “electronic”, “female vocalists”, “dance”, “00s”, “alternative rock”, “jazz”, “beautiful”, “metal”, “chillout”, “male vocalists”, “classic rock”, “soul”, “indie rock”, “Mellow”, “electronica”, “80s”, “folk”, “90s”, “chill”, “instrumental”, “punk”, “oldies”, “blues”, “hard rock”, “ambient”, “acoustic”, “experimental”, “female vocalist”, “guitar”, “Hip-Hop”, “70s”, “party”, “country”, “easy listening”, “sexy”, “catchy”, “funk”, “electro”, “heavy metal”, “Progressive rock”, “60s”, “rnb”, “indie pop”, “sad”, “House”, “happy”

# blank until gotten below
musicGenre = ''

def draw_note(canvas, note, octave_scale):
    octave = int(int(note[1]) * (3 + (octave_scale / 100)))
    note = note[0] # exclude sharps
    canvas.clear_args()

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
        canvas.append_args(canvas.color)
        canvas.append_args(canvas.size)
        canvas.append_args(canvas.style)
        canvas.append_args(octave) 
        canvas.ready()
    # elif note[0] == 'F':  # change the pen color to random color
    #     colors = [Qt.red, Qt.magenta, Qt.yellow,
    #               Qt.green, Qt.blue, Qt.white, Qt.cyan]
    #     canvas.color = colors[octave % len(colors)]


def notes_to_canvas(canvas, song_path, tempo_scale, octave_scale, freq_scale):
    delete_wav_file = False
    if song_path[-4:] == '.mp3':
        wav_song_path = song_path[:-4] + '.wav'
        if not os.path.exists(wav_song_path):
            subprocess.call(['ffmpeg', '-i', song_path,
                             wav_song_path])
        song_path = wav_song_path
        delete_wav_file = True

    sr = 11025 * (1 - (tempo_scale / 100))
    y, sr = librosa.load(song_path, sr=sr)
    S = np.abs(librosa.stft(y))
    if freq_scale != 0:
        if freq_scale == -100:
            freq_scale == -99
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
            draw_note(canvas, note[0].split('-'), octave_scale)
    
    if delete_wav_file:
        os.remove(song_path)
