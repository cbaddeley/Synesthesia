from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QPixmap, QIcon
from PyQt5.QtWidgets import (
    QApplication,
    QFormLayout,
    QLabel,
    QPushButton,
    QWidget,
    QLineEdit,
    QFileDialog,
    QRadioButton)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        # set widow titles
        self.setWindowTitle(' ')
        self.setWindowIcon(QIcon('./images/title_logo.png'))

        # resize window
        self.resize(610, 580)

        # set the logo
        logo_file = QPixmap('./images/synesthesia-white.png')
        logo_file = logo_file.scaled(200, 125)
        self.logo = QLabel(self)
        self.logo.setPixmap(logo_file)
        self.logo.move(200, 15)

        # select file label
        self.select_file = QLabel(self)
        self.select_file.move(10, 153)
        self.select_file.setText('Audio File:')

        # input for folder path
        self.file_path = QLineEdit(self)
        self.file_path.move(65, 150)
        self.file_path.resize(450, 20)

        # button for file picker
        self.get_file = QPushButton('Choose...', self)
        self.get_file.move(520, 150)
        self.get_file.clicked.connect(self.pick_file)

        # radio buttons for different algorithms
        self.algo1 = QRadioButton('Algorithm 1', self)
        self.algo2 = QRadioButton('Algorithm 2', self)
        self.algo3 = QRadioButton('Algorithm 3', self)
        self.algo4 = QRadioButton('Algorithm 4', self)
        self.algo5 = QRadioButton('Algorithm 5', self)

        self.algo1.move(65 + 90 * 0, 180)
        self.algo2.move(65 + 90 * 1, 180)
        self.algo3.move(65 + 90 * 2, 180)
        self.algo4.move(65 + 90 * 3, 180)
        self.algo5.move(65 + 90 * 4, 180)

        # button to process file
        self.proc_file = QPushButton('Process...', self)
        self.proc_file.move(520, 180)
        self.proc_file.clicked.connect(self.process_file)

        # white line across screen
        sep = QPixmap('./images/line.png')
        self.line = QLabel(self)
        self.line.setPixmap(sep)
        self.line.move(0, 220)

        # place holder for processed image
        self.result = QLabel(self)
        self.result.move(10, 250)

    def dark_mode(self):
        # https://gist.github.com/mstuttgart/37c0e6d8f67a0611674e08294f3daef7
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, Qt.white)
        dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
        dark_palette.setColor(QPalette.ToolTipText, Qt.white)
        dark_palette.setColor(QPalette.Text, Qt.white)
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, Qt.white)
        dark_palette.setColor(QPalette.BrightText, Qt.red)
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, Qt.black)
        return dark_palette

    def pick_file(self):
        # https://pythonspot.com/pyqt5-file-dialog/
        # params for getOpenFileName are the window, the title, default file, file types
        file_name, _ = QFileDialog.getOpenFileName(
            self, 'Select MP3 file', '', 'MP3 File (*.mp3)')
        if file_name:
            self.file_path.setText(file_name)

    def process_file(self):
        proc_img = QPixmap('./images/proc_img.png')
        proc_img = proc_img.scaled(590,300)
        self.result.setPixmap(proc_img)
        self.result.adjustSize()


if __name__ == '__main__':
    # instantiate application and create a window
    app = QApplication([])
    app.setStyle('Fusion')
    window = Window()
    app.setPalette(window.dark_mode())  # turn on dark mode
    window.show()
    app.exec()
