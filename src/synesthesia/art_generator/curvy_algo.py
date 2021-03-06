import random
from PyQt5.QtGui import QPainterPath

def draw_note(canvas, note, oct_selection, colors, path):

    octave = int(note[1]) + oct_selection
    note = note[0] # exclude sharps
    canvas.clear_args()
    color = colors[random.randint(0, len(colors) - 1)] # picks random color from list
    canvas.append_args('path')

    newpath = QPainterPath(path)
    x = (((ord(note[0]) % 65) * 50) + octave) % 400
    y = (((ord(note[0]) % 65) * 50) - octave) % 400

    newpath.cubicTo(200, 200, (octave*octave) % 400, octave % 400 ,x,y)

    canvas.append_args(canvas.x) # filler
    canvas.append_args(canvas.y) # filler
    canvas.append_args(color)
    canvas.append_args(canvas.size)
    canvas.append_args(canvas.style)
    canvas.append_args(newpath) 
    canvas.append_args(None) # filler
    canvas.ready()