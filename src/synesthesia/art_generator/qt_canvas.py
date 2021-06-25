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
        

    def paintEvent(self,e):
        if not self.is_ready:
            return

        painter = QPainter(self)

        self.shapes.append([i for i in self.args])

        for shape in self.shapes:
            shape_type, x, y, color, size, style, *dimensions = shape
            if shape_type == 'circle':
                painter.setPen(QPen(color, size, style))
                painter.drawEllipse(x, y, dimensions[0], dimensions[1])
            if shape_type == 'square':
                painter.setPen(QPen(color, size, style))
                painter.drawRect(QRect(x, y, dimensions[0], dimensions[1]))
        


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
