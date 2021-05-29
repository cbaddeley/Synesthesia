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
    QVBoxLayout)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # set widow titles 
        self.setWindowTitle(' ')
        self.setWindowIcon(QIcon('logo.png'))
        
        # resize window
        self.resize(600, 600)

        # select file label
        logo_file = QPixmap('logo.png')
        self.logo = QLabel(self)
        self.logo.setPixmap(logo_file)
        self.logo.move(-60,0)

        # select file label
        self.select_file = QLabel(self)
        self.select_file.move(10,77)
        self.select_file.setText('Select File:')

        # input for folder path 
        self.file_path = QLineEdit(self)
        self.file_path.move(65, 75)
        self.file_path.resize(450, 20)

        # button for file picker
        self.get_file = QPushButton('Choose...', self) 
        self.get_file.move(520,75)
        self.get_file.clicked.connect(self.pick_file)

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
        file_name, _ = QFileDialog.getOpenFileName(self,'Select MP3 file','','MP3 File (*.mp3)')
        if file_name:
            self.file_path.setText(file_name)

if __name__ == '__main__':
    # instantiate application and create a window
    app = QApplication([]) 
    window = Window()
    app.setPalette(window.dark_mode()) # turn on dark mode
    window.show()
    app.exec()