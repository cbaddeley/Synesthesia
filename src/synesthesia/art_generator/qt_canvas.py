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
        self.resize(400, 400)
        self.x = 215
        self.y = 215
        self.color = Qt.white
        self.size = 1
        self.style = Qt.SolidLine
        self.args = []
        self.shapes = []
        self.is_ready = False

    @property
    def pixmap(self):
        return self._pixmap

    @pixmap.setter
    def pixmap(self, pixmap):
        self._pixmap = pixmap.copy()
        self.update()
        size = self.pixmap.size()
        if size.isValid():
            self.resize(size)
        else:
            self.resize(400, 400)

    def ready(self):
        self.is_ready = True
        self.repaint()

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
                shape_type, x, y, color, size, style, dim, ydiff = shape
                painter.setPen(QPen(color, size, style))
                if shape_type == 'circle':
                    painter.drawEllipse(x, y, dim, dim)
                elif shape_type == 'square':
                    painter.drawRect(QRect(x, y, dim, dim))
                elif shape_type == 'line':
                    painter.drawLine(x % 400, y % 400, (x + dim) % 400, (y + ydiff) % 400)
                    self.x += dim
                    self.x %= 400
                    self.y += ydiff
                    self.y %= 400
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
                    painter.drawLine(x, y, x + dim, y + dim/2)  # up right
                    x += dim
                    y += dim/2
                    painter.drawLine(x, y, x + dim/2, y + dim)  # up right
                    x += dim/2
                    y += dim
                    painter.drawLine(x, y, x + dim/2, y - dim)  # down right
                    x += dim/2
                    y -= dim
                    painter.drawLine(x, y, x + dim, y - dim/2)  # down right
                    x += dim
                    y -= dim/2
                    painter.drawLine(x, y, x - dim, y - dim/2)  # down left
                    x -= dim
                    y -= dim/2
                    painter.drawLine(x, y, x, y - dim)  # down 
                    y -= dim
                    painter.drawLine(x, y, x - dim/2, y + dim)  # up left
                    x -= dim/2
                    y += dim
                    painter.drawLine(x, y, x - dim/2, y - dim)  # down left
                    x -= dim/2
                    y -= dim
                    painter.drawLine(x, y, x, y + dim)  # up
                    y += dim
                    painter.drawLine(x, y, x - dim, y + dim/2)  # up left
                    x -= dim
                    y += dim/2
                    
    def refresh(self):
        self.update()