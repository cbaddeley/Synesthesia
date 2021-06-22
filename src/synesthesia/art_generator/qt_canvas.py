import random

from PyQt5 import QtCore, QtGui, QtWidgets
from random import randrange
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QtCanvas(QtWidgets.QWidget):
    def __init__(self, parent):
        super(QtCanvas, self).__init__(parent)
        self._pixmap = QPixmap()
        self.resize(400, 400)
        self.x = 200
        self.y = 200
        self.lines = []
        self.arcs = []
        self.grads = []
        self.brush = QBrush(Qt.red, Qt.SolidPattern)

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

    def paintEvent(self,e):
        event = randrange(100)
        if event < 50:
            self.add_line()
        elif event < 90:
            self.add_arc()
        else:
            self.add_gradient()

        painter = QtGui.QPainter(self)
        painter.drawPixmap(self.rect(), self.pixmap)

        for x, y, width, height, grad, pen in self.grads:
            painter.setPen(pen)
            painter.setBrush(QBrush(grad))
            painter.drawRect(x, y, width, height)

        for x1, y1, x2, y2, pen in self.lines:
            painter.setPen(pen)
            painter.drawLine(x1, y1, x2, y2)

        for x, y, width, height, start_angle, span_angle, pen in self.arcs:
            painter.setPen(pen)
            painter.drawArc(x, y, width, height,start_angle, span_angle)

    def add_line(self):
        new_x = randrange(400)
        new_y = randrange(400)
        self.lines.append(tuple([self.x, self.y, new_x, new_y, self.get_pen()]))
        self.x = new_x
        self.y = new_y

    def add_arc(self):
        new_x = randrange(400)
        new_y = randrange(400)
        height = abs(new_y - self.y)
        width = abs(new_x - self.x)
        start_angle = random.randrange(-90, 90) * 16
        span_angle = random.randrange(-360, 360) * 16
        self.arcs.append(tuple([self.x, self.y, width, height, start_angle, span_angle, self.get_pen()]))
        self.x = new_x
        self.y = new_y

    def add_gradient(self):
        x = randrange(400)
        y = randrange(400)
        width = randrange(400)
        height = randrange(400)
        grad = QLinearGradient(randrange(400), randrange(400), randrange(400), randrange(400))
        self.grads.append(tuple([x, y, width, height, grad, self.get_pen()]))

    def get_pen(self):
        event = randrange(100)
        if event < 15:
            return QPen(Qt.red, 2, Qt.SolidLine)
        elif event < 30:
            return QPen(Qt.green, 2, Qt.SolidLine)
        elif event < 45:
            return QPen(Qt.blue, 2, Qt.SolidLine)
        elif event < 60:
            return QPen(Qt.yellow, 2, Qt.SolidLine)
        elif event < 75:
            return QPen(Qt.black, 2, Qt.SolidLine)
        else:
            return QPen(Qt.white, 2, Qt.SolidLine)

    def refresh(self):
        self.update()
