from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import wsl


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "Glorious painting of your music"

        top = 400
        left = 400
        width = 800
        height = 600

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
        self.draw_something()

    # makes the blank canvas
    def paintEvent(self, event):
        canvas_creation = QPainter(self)
        canvas_creation.drawImage(self.rect(), self.image, self.image.rect())

    # does the drawing
    def draw_something(self):
        painter = QPainter(self.image)
        painter.setPen(QPen(Qt.black, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        painter.drawLine(100, 100, 300, 300)
        self.update()

    # save method
    def save(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG(*.png)")

        # if file path is blank return back
        if file_path == "":
            return

        # saves image
        self.image.save(file_path + ".png")


if __name__ == "__main__":
    wsl.set_display_to_host()
    app = QApplication([])
    window = Window()
    window.show()

    app.exec()
