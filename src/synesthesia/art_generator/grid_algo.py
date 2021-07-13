import random
from PyQt5.QtCore import Qt
import math

def draw_note(canvas, note, octave_scale, colors, bar_index):
    if bar_index == 0:
        canvas.clear_args()
        color = colors[random.randint(0, len(colors) - 1)]  # picks random color from list
        canvas.style = Qt.SolidLine
        canvas.append_args('circle')
        canvas.append_args(canvas.x)
        canvas.append_args(canvas.y)
        canvas.grid_x_y(canvas.x, canvas.y)
        canvas.append_args(color)
        canvas.append_args(canvas.size)
        canvas.append_args(canvas.style)
        canvas.append_args(min(canvas.grid_dimensions[0], canvas.grid_dimensions[1]))  # filler
        canvas.append_args(None)
        canvas.ready()
    elif bar_index % canvas.grid_dimensions[2] == 0:
        canvas.x = canvas.grid_state[5]+ (canvas.grid_state[0] * canvas.grid_dimensions[0])
        canvas.y = canvas.grid_state[6]+ (canvas.grid_state[1] * canvas.grid_dimensions[1])
        canvas.grid_x_y(canvas.x, canvas.y)
        canvas.seg_passed()
        if canvas.grid_state[2] == canvas.grid_state[3]:
            canvas.reset_seg_passed()
            temp = canvas.grid_state[0]
            canvas.grid_state[0] = -canvas.grid_state[1]
            canvas.grid_state[1] = temp

            if canvas.grid_state[1] == 0:
                canvas.inc_seg_len()

        octave = int(int(note[1]) * (3 + (octave_scale / 100)))
        canvas.clear_args()
        color = colors[random.randint(0, len(colors) - 1)] # picks random color from list
        canvas.style = Qt.SolidLine
        canvas.append_args('circle')
        canvas.append_args(canvas.x)
        canvas.append_args(canvas.y)
        canvas.append_args(color)
        canvas.append_args(canvas.size)
        canvas.append_args(canvas.style)
        canvas.append_args(min(canvas.grid_dimensions[0], canvas.grid_dimensions[1])) # filler
        canvas.append_args(None)
        canvas.ready()
    else:
        note = note[0]
        if note == 'A':  # draw a circle
            angle = random.randint(0,70)
            end_points = 365, 400
        elif note == 'B':  # draw a square
            angle = random.randint(70,120)
            end_points = 400, 253
        elif note == 'C':  # draw a triangle
            angle = random.randint(120,170)
            end_points = 400, 125
        elif note == 'D':  # draw a hexagon
            angle = random.randint(170,220)
            end_points = 139, 0
        elif note == 'E':  # draw an octogon
            angle = random.randint(220,270)
            end_points = 35, 0
        elif note == 'F':  # draw a star
            angle = random.randint(270,320)
            end_points = 0, 193
        else:
            angle = random.randint(320,360)
            end_points = 0, 361
        radius = min(canvas.grid_dimensions[0], canvas.grid_dimensions[1]) / 2
        new_x = math.floor((canvas.grid_state[5]+radius) + (radius * math.sin(math.radians(angle))))
        new_y = math.floor((canvas.grid_state[6]+radius) + (radius * math.cos(math.radians(angle))))
        xdiff = end_points[0] - new_x
        ydiff = end_points[1] - new_y
        canvas.clear_args()
        canvas.append_args('line')
        color = colors[random.randint(0, len(colors) - 1)]
        canvas.append_args(new_x)
        canvas.append_args(new_y)
        canvas.append_args(color)
        canvas.append_args(canvas.size)
        canvas.append_args(canvas.style)
        canvas.append_args(xdiff)
        canvas.append_args(ydiff)  # filler
        canvas.ready()