import librosa
import numpy as np
from PyQt5.QtCore import Qt
from wsl import *
set_display_to_host()


def draw_note(canvas, note, octave_scale):
    octave = int(int(note[1]) * (1 + (octave_scale / 100)))
    note = note[0]
    canvas.clear_args()

    if note == 'A':  # draw a circle
        canvas.append_args('circle')
        canvas.append_args(canvas.x)
        canvas.append_args(canvas.y)
        canvas.append_args(canvas.color) 
        canvas.append_args(canvas.size)
        canvas.append_args(canvas.style)
        canvas.append_args(octave) # height
        canvas.append_args(octave) # width
        canvas.ready(True)
    elif note == 'B':  # draw a square
        for _ in range(4):
            pass
    elif note == 'C':  # draw a triangle
        for _ in range(3):
            pass
    elif note == 'D':  # draw a octogon
        for _ in range(8):
            pass
    elif note == 'E':  # draw a hexagon
        for _ in range(6):
            pass
    elif note == 'F':  # draw a star
        for _ in range(5):
            pass
    # sharp notes, don't want the sharp char to cause issues
    elif note[0] == 'A':  # move up by octave pixels
        canvas.y = (canvas.y + octave) % 400
    elif note[0] == 'B':   # move down by octave pixels
        canvas.y = (canvas.y - octave) % 400
    elif note[0] == 'C':  # move right by octave pixels
        canvas.x = (canvas.x + octave) % 400 
    elif note[0] == 'D': # move left by octave pixels
        canvas.x = (canvas.x - octave ) % 400
    elif note[0] == 'E':  # pick up pen to octave places back
        styles = [Qt.SolidLine, Qt.DashLine, Qt.DotLine, Qt.DashDotLine, Qt.DashDotDotLine, Qt.CustomDashLine]
        canvas.style = styles[octave % len(styles)]

    elif note[0] == 'F':  # change the pen color to random color
        colors = [Qt.red, Qt.magenta, Qt.yellow, Qt.green, Qt.blue, Qt.white, Qt.cyan]
        canvas.color = colors[octave % len(colors)]


def notes_to_canvas(canvas, song_path, speed_scale, octave_scale):
    y, sr = librosa.load(librosa.ex('trumpet'), sr=22050)
    S = np.abs(librosa.stft(y))
    bars = librosa.hz_to_note(S)

    for bar in bars:
        for note in bar:
            if '-' in note:
                draw_note(canvas, note.split('-'), octave_scale)
