from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import ffmpeg
import pydub
import wsl


class Window(QMainWindow):
    x = 0
    y = 0

    def __init__(self):
        super().__init__()

        title = "Glorious painting of your music"

        top = 400
        left = 400
        width = 1200
        height = 900

        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        menu_bar = self.menuBar()
        file_button = menu_bar.addMenu("File")
        save_action = QAction("Save", self)
        save_action.setShortcut("Ctrl + S")
        file_button.addAction(save_action)
        save_action.triggered.connect(self.save)
        canvas_creation = QPainter(self)
        canvas_creation.drawImage(self.rect(), self.image, self.image.rect())

    # makes the blank canvas

    # does the drawing
    def draw_something(self, note=None):
        painter = QPainter(self.image)
        painter.setPen(QPen(Qt.black, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        octave = int(note[1])
        note = note[0]

        if note == 'A':  # draw a point
            painter.drawPoint(self.x % 1200, self.y + 750)
            self.x += 1
        elif note == 'B':  # draw a rectangle
            painter.drawRect(self.x % 1200, self.y + 600, 20, 15)
            self.x += 1
        elif note == 'C':  # draw a circle
            painter.drawEllipse(self.x % 1200, self.y + 450, 20, 20)
            self.x += 1
        elif note == 'D':  # draw a pie
            painter.drawPie(self.x % 1200, self.y + 300, 20, 15, 30 * 16, 20 * 16)
            self.x += 1
        elif note == 'E':  # draw a hexagon
            path = QPainterPath(self.x % 1200, self.y + 150)
            path.lineTo(self.x % 1200 + 5, self.y + 150 + 8)
            path.cubicTo(self.x % 1200 + 20, 0, self.x % 1200, self.y + 150 + 5, self.x % 1200 + 20, self.y + 20)
            self.x += 1
        elif note == 'F':  # draw a star
            path = QPainterPath(self.x % 1200, self.y + 150)
            path.lineTo(self.x % 1200 + 3, self.y + 150 + 6)
            path.lineTo(self.x % 1200 + 6, self.y + 150)
            path.lineTo(self.x % 1200, self.y + 150)
        # sharp notes, don't want the sharp char to cause issues
        elif note[0] == 'F':  # change the pen color to random color
            colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
            i = 0
            pen_color = QColor
            pen_color.setNamedColor(colors[i])
            i += 1
            painter.setpen(pen_color)

        self.update()

    # save method
    def save(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG(*.png)")

        # if file path is blank return back
        if file_path == "":
            return

        # saves image
        self.image.save(file_path + ".png")


