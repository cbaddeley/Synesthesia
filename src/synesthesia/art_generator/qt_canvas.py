import random
from math import *
from PyQt5 import QtWidgets
from random import randrange
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QtCanvas(QtWidgets.QWidget):
    def __init__(self, parent):
        super(QtCanvas, self).__init__(parent)
        self._pixmap = QPixmap()
        self.width = 400
        self.height = 400
        self.resize(self.width, self.height)
        self.x = 215
        self.y = 215
        self.color = Qt.white
        self.size = 1
        self.style = Qt.SolidLine
        self.args = []
        self.shapes = []
        self.is_ready = False
        self._grid_dimensions = 0, 0
        self._grid_state = [1, 0, 1, 0, 0, 200, 200]

    @property
    def pixmap(self):
        return self._pixmap

    @property
    def dimensions(self):
        return self.width, self.height

    @property
    def grid_dimensions(self):
        return self._grid_dimensions

    @property
    def grid_state(self):
        return self._grid_state

    @pixmap.setter
    def pixmap(self, pixmap):
        self._pixmap = pixmap.copy()
        self.update()
        size = self.pixmap.size()
        if size.isValid():
            self.resize(size)
        else:
            self.resize(400, 400)

    def set_grid_dimensions(self, total_bars):
        mod = 3
        pixels_per_grid = floor(sqrt(self.width * self.height / (total_bars)))
        self._grid_dimensions = floor(self.width / self.height * pixels_per_grid) * (mod/2), floor(self.height / self.width * pixels_per_grid) * (mod/2), mod
        self.x = self.width / 2 - floor(self._grid_dimensions[0] / 2)
        self.y = self.height / 2 - floor(self._grid_dimensions[1] / 2)
        self._grid_state = [1, 0, 1, 0, total_bars, 200, 200]

    def ready(self):
        self.is_ready = True
        self.repaint()

    def seg_passed(self):
        self._grid_state[3] += 1

    def inc_seg_len(self):
        self._grid_state[2] += 1

    def reset_seg_passed(self):
        self._grid_state[3] = 0

    def grid_x_y(self, x, y):
        self._grid_state[5] = x
        self._grid_state[6] = y

    def clear_args(self):
        self.args.clear()
        self.is_ready = False

    def append_args(self, val):
        self.args.append(val)

    def paintEvent(self, e):
        if not self.is_ready:
            return

        painter = QPainter(self)
        self.shapes.append([i for i in self.args])
        for shape in self.shapes:
            if shape != []:
                shape_type, x, y, color, size, style, dim, ydiff = shape  # for line, dim is xdiff. for path, dim is path
                painter.setPen(QPen(color, size, style))
                if shape_type == 'circle':
                    painter.drawEllipse(x, y, dim, dim)
                elif shape_type == 'square':
                    painter.drawRect(QRect(x, y, dim, dim))
                elif shape_type == 'line':
                    painter.drawLine(x, y, x + dim, y + ydiff)
                    self.x += dim
                    if self.x > 400:
                        self.x = 200
                    self.y += ydiff
                    if self.y > 400:
                        self.y = 200
                elif shape_type == 'path':
                    painter.drawPath(dim)
                elif shape_type == 'triangle':
                    # go up and right, down and right, left left forming isosceles
                    painter.drawLine(x, y, x + dim, y + dim)
                    x += dim
                    y += dim
                    painter.drawLine(x, y, x + dim, y - dim)
                    x += dim
                    y -= dim  # return y to original pos
                    painter.drawLine(x, y, x - dim * 2, y)
                    x -= dim * 2  # return x to original pos
                elif shape_type == 'hexagon':
                    # go right, down and right, down left, left, up left, up right
                    painter.drawLine(x, y, x + dim, y)  # right
                    x += dim
                    painter.drawLine(x, y, x + dim, y - dim)  # down and right
                    x += dim
                    y -= dim
                    painter.drawLine(x, y, x - dim, y - dim)  # down left
                    x -= dim
                    y -= dim
                    painter.drawLine(x, y, x - dim, y)  # left
                    x -= dim
                    painter.drawLine(x, y, x - dim, y + dim)  # up left
                    x -= dim
                    y += dim
                    painter.drawLine(x, y, x + dim, y + dim)  # up right
                    x += dim
                    y += dim
                elif shape_type == 'octogon':
                    # go right, down and right, down, down left, left, up left, up, up right
                    painter.drawLine(x, y, x + dim, y)  # right
                    x += dim
                    painter.drawLine(x, y, x + dim, y - dim)  # down and right
                    x += dim
                    y -= dim
                    painter.drawLine(x, y, x, y - dim)  # down
                    y -= dim
                    painter.drawLine(x, y, x - dim, y - dim)  # down left
                    x -= dim
                    y -= dim
                    painter.drawLine(x, y, x - dim, y)  # left
                    x -= dim
                    painter.drawLine(x, y, x - dim, y + dim)  # up left
                    x -= dim
                    y += dim
                    painter.drawLine(x, y, x, y + dim)  # up
                    y += dim
                    painter.drawLine(x, y, x + dim, y + dim)  # up right
                    x += dim
                    y += dim
                elif shape_type == 'star':
                    painter.drawLine(x, y, x + dim, y + dim / 2)  # up right
                    x += dim
                    y += dim / 2
                    painter.drawLine(x, y, x + dim / 2, y + dim)  # up right
                    x += dim / 2
                    y += dim
                    painter.drawLine(x, y, x + dim / 2, y - dim)  # down right
                    x += dim / 2
                    y -= dim
                    painter.drawLine(x, y, x + dim, y - dim / 2)  # down right
                    x += dim
                    y -= dim / 2
                    painter.drawLine(x, y, x - dim, y - dim / 2)  # down left
                    x -= dim
                    y -= dim / 2
                    painter.drawLine(x, y, x, y - dim)  # down 
                    y -= dim
                    painter.drawLine(x, y, x - dim / 2, y + dim)  # up left
                    x -= dim / 2
                    y += dim
                    painter.drawLine(x, y, x - dim / 2, y - dim)  # down left
                    x -= dim / 2
                    y -= dim
                    painter.drawLine(x, y, x, y + dim)  # up
                    y += dim
                    painter.drawLine(x, y, x - dim, y + dim / 2)  # up left
                    x -= dim
                    y += dim / 2

    def refresh(self):
        self.update()
