import random
from PyQt5.QtCore import Qt

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