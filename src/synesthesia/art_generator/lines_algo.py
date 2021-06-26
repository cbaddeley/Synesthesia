import random 

def draw_note(canvas, note, octave_scale, colors):

    octave = int(int(note[1]) * (3 + (octave_scale / 100)))
    note = note[0]
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
    elif note[0] == 'A': # move NW
        xdiff = -7
        ydiff = 7
    elif note[0] == 'C': # move NNE
        ydiff = 8
        xdiff = 6
    elif note[0] == 'F': # move WSW
        xdiff = -8
        ydiff = -6
    elif note[0] == 'G': # move SSE
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

