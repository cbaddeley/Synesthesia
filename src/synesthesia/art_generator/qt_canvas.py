import random

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
        self.color = Qt.black
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

    def ready(self, val):
        self.is_ready = val
        self.repaint()

    def clear_args(self):
        self.args.clear()
        self.is_ready = False

    def append_args(self, val):
        self.args.append(val)

    def paintEvent(self, e):
        if not self.is_ready or self.args == []:
            return

        painter = QPainter(self)
        self.shapes.append([i for i in self.args])
        for shape in self.shapes:
            shape_type, x, y, color, size, style, *dimensions = shape
            painter.setPen(QPen(color, size, style))
            if shape_type == 'circle':
                painter.drawEllipse(x, y, dimensions[0], dimensions[1])
            elif shape_type == 'square':
                painter.drawRect(QRect(x, y, dimensions[0], dimensions[1]))
            elif shape_type == 'triangle':
                # we will go up and right, down and right, left left forming isosceles
                painter.drawRect(QRect(x, y, x + dimensions[0], y + dimensions[0]))
                x += dimensions[0]
                y += dimensions[0]
                painter.drawRect(QRect(x, y, x + dimensions[0], y - dimensions[0]))
                x += dimensions[0]
                y -= dimensions[0] # return y to original pos
                painter.drawRect(QRect(x, y, x - dimensions[0] * 2, y))
                x -= dimensions[0] * 2 # return x to original pos

    def refresh(self):
        self.update()
