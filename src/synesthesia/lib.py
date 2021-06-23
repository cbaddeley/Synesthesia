import librosa
import turtle
import numpy as np
from wsl import *
set_display_to_host()


def draw_note(note, t, octave_scale):
    octave = int(int(note[1]) * (1 + (octave_scale / 100)))
    note = note[0]

    if note == 'A':  # draw a circle
        t.circle(octave)
    elif note == 'B':  # draw a square
        for _ in range(4):
            t.fd(octave)
            t.rt(90)
    elif note == 'C':  # draw a triangle
        for _ in range(3):
            t.fd(octave)
            t.lt(120)
    elif note == 'D':  # draw a octogon
        for _ in range(8):
            t.fd(octave)
            t.lt(45)
    elif note == 'E':  # draw a hexagon
        for _ in range(6):
            t.fd(octave)
            t.lt(60)
    elif note == 'F':  # draw a star
        for _ in range(5):
            t.rt(108)
            t.fd(octave)
            t.lt(36)
            t.fd(octave)
    # sharp notes, don't want the sharp char to cause issues
    elif note[0] == 'A':  # rotate angle right by octave
        t.rt(octave)
    elif note[0] == 'B':  # rotate angle left by octave
        t.lt(octave)
    elif note[0] == 'C':  # do a 180
        t.lt(180)
    elif note[0] == 'D':  # pick up pen to octave places forward
        t.up()
        t.fd(octave)
        t.down()
    elif note[0] == 'E':  # pick up pen to octave places back
        t.up()
        t.lt(180)
        t.fd(octave)
        t.down()
    elif note[0] == 'F':  # change the pen color to random color
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
        t.pencolor(colors[octave % len(colors)])

def notes_to_canvas(song_path, speed_scale, octave_scale):
    y, sr = librosa.load(librosa.ex('trumpet'), sr=22050)
    S = np.abs(librosa.stft(y))
    bars = librosa.hz_to_note(S)

    turtle.screensize(canvwidth=400, canvheight=400)
    t = turtle.Turtle()
    t.speed(6 * (1 + (speed_scale / 100)))
    t.hideturtle()

    for bar in bars:
        for note in bar:
            if '-' in note:
                draw_note(note.split('-'), t, octave_scale)
