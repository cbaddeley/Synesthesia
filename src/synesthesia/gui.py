from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from synesthesia.wsl import *
from synesthesia.image_helper import *
from PIL.ImageQt import ImageQt
from synesthesia.essentia_helper import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        # set widow titles
        self.setWindowTitle(' ')
        self.setWindowIcon(QIcon('./images/title_logo.png'))

        # resize window
        self.resize(610, 580)

        # set the logo
        logo_file = QPixmap('./images/main_logo.svg')
        logo_file = logo_file.scaled(400, 150)
        self.logo = QLabel(self)
        self.logo.setPixmap(logo_file)
        self.logo.move(110, 0)

        # line seperators
        sep = QPixmap('./images/line.png')
        sep = sep.scaled(610, 1)
        self.mid_line = QLabel(self)
        self.mid_line.setPixmap(sep)
        self.mid_line.move(-10, 190)
        sep = sep.scaled(1, 400)  # rotate vertically
        self.vert_line = QLabel(self)
        self.vert_line.setPixmap(sep)
        self.vert_line.move(200, 190)

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

        # select algorithm label
        self.select_algo = QLabel(self)
        self.select_algo.move(10, 200)
        self.select_algo.setText('Algorithm:')

        # ComboBox for different algorithms
        self.algo_combo = QComboBox(self)
        self.algo_combo.move(75, 200)
        self.algo_combo.resize(90, 20)
        algos = [
            '',  # blank so when displayed nothing is autoselected
            'Algorithm 1',
            'Algorithm 2',
            'Algorithm 3',
            'Algorithm 4',
            'Algorithm 5',
        ]
        self.algo_combo.addItems(algos)
        self.algo_combo.activated[str].connect(self.on_algo_change)

        # label for algorithm label
        self.algo_lbl = QLabel(self)
        self.algo_lbl.move(25, 375)
        self.algo_lbl.setWordWrap(True)
        self.algo_lbl.setAlignment(Qt.AlignCenter)

        # Tempo Slider
        self.tempo_lbl = QLabel(self)
        self.tempo_lbl.setText('Tempo:')
        self.tempo_lbl.move(10, 225)
        self.tempo_val = QLabel(self)
        self.tempo_val.move(165, 225)
        self.tempo_val.resize(35, 10)
        self.tempo_val.setText('0%')
        self.tempo_sld = QSlider(Qt.Horizontal, self)
        self.tempo_sld.setRange(-100, 100)
        self.tempo_sld.setFocusPolicy(Qt.NoFocus)
        self.tempo_sld.setPageStep(1)
        self.tempo_sld.move(75, 225)
        self.tempo_sld.valueChanged.connect(
            lambda val: self.tempo_val.setText(str(val) + '%'))

        # Frequency Slider
        self.frq_lbl = QLabel(self)
        self.frq_lbl.setText('Frequency:')
        self.frq_lbl.move(10, 250)
        self.frq_val = QLabel(self)
        self.frq_val.move(165, 250)
        self.frq_val.resize(35, 10)
        self.frq_val.setText('0%')
        self.frq_sld = QSlider(Qt.Horizontal, self)
        self.frq_sld.setRange(-100, 100)
        self.frq_sld.setFocusPolicy(Qt.NoFocus)
        self.frq_sld.setPageStep(1)
        self.frq_sld.move(75, 250)
        self.frq_sld.valueChanged.connect(
            lambda val: self.frq_val.setText(str(val) + '%'))

        # Tone Slider
        self.tone_lbl = QLabel(self)
        self.tone_lbl.setText('Tone:')
        self.tone_lbl.move(10, 275)
        self.tone_val = QLabel(self)
        self.tone_val.move(165, 275)
        self.tone_val.resize(35, 10)
        self.tone_val.setText('0%')
        self.tone_sld = QSlider(Qt.Horizontal, self)
        self.tone_sld.setRange(-100, 100)
        self.tone_sld.setFocusPolicy(Qt.NoFocus)
        self.tone_sld.setPageStep(1)
        self.tone_sld.move(75, 275)
        self.tone_sld.valueChanged.connect(
            lambda val: self.tone_val.setText(str(val) + '%'))

        # Pitch Slider
        self.pitch_lbl = QLabel(self)
        self.pitch_lbl.setText('Pitch:')
        self.pitch_lbl.move(10, 300)
        self.pitch_val = QLabel(self)
        self.pitch_val.move(165, 300)
        self.pitch_val.resize(35, 10)
        self.pitch_val.setText('0%')
        self.pitch_sld = QSlider(Qt.Horizontal, self)
        self.pitch_sld.setRange(-100, 100)
        self.pitch_sld.setFocusPolicy(Qt.NoFocus)
        self.pitch_sld.setPageStep(1)
        self.pitch_sld.move(75, 300)
        self.pitch_sld.valueChanged.connect(
            lambda val: self.pitch_val.setText(str(val) + '%'))

        # Octave Sliders
        self.octave_lbl = QLabel(self)
        self.octave_lbl.setText('Octave:')
        self.octave_lbl.move(10, 325)
        self.octave_val = QLabel(self)
        self.octave_val.move(165, 325)
        self.octave_val.resize(35, 10)
        self.octave_val.setText('0%')
        self.octave_sld = QSlider(Qt.Horizontal, self)
        self.octave_sld.setRange(-100, 100)
        self.octave_sld.setFocusPolicy(Qt.NoFocus)
        self.octave_sld.setPageStep(1)
        self.octave_sld.move(75, 325)
        self.octave_sld.valueChanged.connect(
            lambda val: self.octave_val.setText(str(val) + '%'))

        # Other Slider
        self.bs_lbl = QLabel(self)
        self.bs_lbl.setText('Bull Shit:')
        self.bs_lbl.move(10, 350)
        self.bs_val = QLabel(self)
        self.bs_val.move(165, 350)
        self.bs_val.resize(35, 10)
        self.bs_val.setText('0%')
        self.bs_sld = QSlider(Qt.Horizontal, self)
        self.bs_sld.setRange(-100, 100)
        self.bs_sld.setFocusPolicy(Qt.NoFocus)
        self.bs_sld.setPageStep(1)
        self.bs_sld.move(75, 350)
        self.bs_sld.valueChanged.connect(
            lambda val: self.bs_val.setText(str(val) + '%'))

        # button to process file
        self.proc_file = QPushButton('Process...', self)
        self.proc_file.setGeometry(150, 150, 100, 40)
        self.proc_file.move(50, 500)
        self.proc_file.clicked.connect(self.process_file)

        # place holder for processed image
        self.result = QLabel(self)
        self.result.move(200, 200)

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

    def on_algo_change(self):
        algo_desc = {
            '': '',
            'Algorithm 1': 'Brief description for algorithm 1',
            'Algorithm 2': "A longer desctription for how algorithm 2 works with some of it's functionalities",
            'Algorithm 3': 'Brief description for algorithm 3',
            'Algorithm 4': 'Brief description for algorithm 4',
            'Algorithm 5': 'Brief description for algorithm 5',
        }
        self.algo_lbl.setText(algo_desc[self.algo_combo.currentText()])
        self.algo_lbl.resize(150,80)

    def process_file(self):
        blank_image = create_image_array(512, 512)
        img = create_image_from_array(blank_image)
        qim = ImageQt(img)
        proc_img = QPixmap.fromImage(qim)
        self.result.setPixmap(proc_img)
        self.result.adjustSize()

def main_func():
    set_display_to_host()
    # instantiate application and create a window
    app = QApplication([])
    app.setStyle('Fusion')
    window = Window()
    app.setPalette(window.dark_mode())  # turn on dark mode
    window.show()
    app.exec()

if __name__ == '__main__':
    main_func()



