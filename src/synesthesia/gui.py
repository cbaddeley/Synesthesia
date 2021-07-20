import glob
import os
import shutil
import os
import sys
from PyQt5.QtCore import Qt, QObject
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import urllib.request
from wsl import *
from PIL.ImageQt import ImageQt
from art_generator import qt_canvas, process_audio, dbm
from images import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        # set widow titles
        self.setWindowTitle(' ')
        url_data_title_logosvg = urllib.request.urlopen(
            "https://raw.githubusercontent.com/cbaddeley/Synesthesia/main/src/synesthesia/images/title_logo.svg").read()
        title_logosvg = QPixmap()
        title_logosvg.loadFromData(url_data_title_logosvg)
        self.setWindowIcon(QIcon(title_logosvg))

        # resize window
        self.resize(620, 650)

        # set the logo
        url_data = urllib.request.urlopen(
            "https://raw.githubusercontent.com/cbaddeley/Synesthesia/d17641714e1f5978bf894684c8604c6ef320754a/src/synesthesia/images/main_logo.svg").read()
        pixmap = QPixmap()
        pixmap.loadFromData(url_data)
        # lbl.setPixmap(pixmap)
        # logo_file = QPixmap('main_logo.svg')
        logo_file = pixmap.scaled(380, 130)
        self.logo = QLabel(self)
        self.logo.setPixmap(logo_file)
        self.logo.move(110, 0)

        # line seperators
        url_data = urllib.request.urlopen(
            "https://raw.githubusercontent.com/cbaddeley/Synesthesia/d17641714e1f5978bf894684c8604c6ef320754a/src/synesthesia/images/line.png").read()
        pixmap2 = QPixmap()
        pixmap2.loadFromData(url_data)
        # sep = QPixmap('line.png')
        sep = pixmap2.scaled(700, 1)
        self.mid_line = QLabel(self)
        self.mid_line.setPixmap(sep)
        self.mid_line.move(-50, 220)
        sep = sep.scaled(1, 500)  # rotate vertically
        self.vert_line = QLabel(self)
        self.vert_line.setPixmap(sep)
        self.vert_line.move(205, 220)

        # select file label
        self.select_file = QLabel(self)
        self.select_file.move(8, 143)
        self.select_file.setText('Audio File:')

        # input for folder path
        self.file_path = QLineEdit(self)
        self.file_path.move(85, 140)
        self.file_path.resize(440, 20)

        # button for file picker
        self.get_file = QPushButton('Choose...', self)
        self.get_file.move(530, 140)
        self.get_file.resize(80, 20)
        self.get_file.clicked.connect(self.pick_file)

        # audio sample label
        self.sample_lbl = QLabel(self)
        self.sample_lbl.move(8, 173)
        self.sample_lbl.setText('Audio Sample:')

        # combo box for audio samples
        self.sample_combo = QComboBox(self)
        self.sample_combo.move(85, 170)
        self.sample_combo.resize(440, 20)
        self.sample_combo.addItems(self.get_samples())
        self.sample_combo.activated[str].connect(self.set_specs)

        # select specs label
        self.spec_lbl = QLabel('', self)
        self.spec_lbl.move(318, 197)

        # combo box for specs
        self.spec_combo = QComboBox(self)
        self.spec_combo.move(385, 195)
        self.spec_combo.resize(0, 0)
        self.spec_combo.activated[str].connect(self.set_sample)

        # select algorithm label
        self.select_algo = QLabel(self)
        self.select_algo.move(8, 232)
        self.select_algo.setText('Algorithm:')

        # ComboBox for different algorithms
        self.algo_combo = QComboBox(self)
        self.algo_combo.move(75, 230)
        self.algo_combo.resize(120, 20)
        algos = [
            '',  # blank so when displayed nothing is autoselected
            'Shape of You',
            'Line Rider',
            'Curvy',
            'Speech',
            'Grid',
        ]
        self.algo_combo.addItems(algos)
        self.algo_combo.activated[str].connect(self.on_algo_change)

        # label for algorithm label
        self.algo_lbl = QLabel(self)
        self.algo_lbl.move(25, 330)
        self.algo_lbl.setWordWrap(True)
        self.algo_lbl.setAlignment(Qt.AlignCenter)

        # Frequency Slider
        frq_tt = 'Increases or decreases the frequencies by the percent selected'
        self.frq_lbl = QLabel(self)
        self.frq_lbl.setText('Frequency:')
        self.frq_lbl.move(8, 255)
        self.frq_lbl.resize(0,0)
        self.frq_lbl.setToolTip(frq_tt)
        self.frq_val = QLabel(self)
        self.frq_val.move(170, 257)
        self.frq_val.resize(0, 0)
        self.frq_val.setText('0%')
        self.frq_val.setFont(QFont('', 8))
        self.frq_val.setToolTip(frq_tt)
        self.frq_sld = QSlider(Qt.Horizontal, self)
        self.frq_sld.setRange(-99, 100)
        self.frq_sld.setFocusPolicy(Qt.NoFocus)
        self.frq_sld.setPageStep(1)
        self.frq_sld.setToolTip(frq_tt)
        self.frq_sld.move(90, 257)
        self.frq_sld.resize(0, 0)
        self.frq_sld.valueChanged.connect(
            lambda val: self.frq_val.setText(str(val) + '%'))

        # sr Slider
        sr_tt = 'Determines the number of samples taken per second of audio'
        self.sr_lbl = QLabel(self)
        self.sr_lbl.setText('Sample Rate:')
        self.sr_lbl.move(8, 280)
        self.sr_lbl.setToolTip(sr_tt)
        self.sr_lbl.resize(0,0)
        self.sr_val = QLabel(self)
        self.sr_val.move(170, 282)
        self.sr_val.resize(0, 0)
        self.sr_val.setText('11.5k')
        self.sr_val.setFont(QFont('', 8))
        self.sr_val.setToolTip(sr_tt)
        self.sr_sld = QSlider(Qt.Horizontal, self)
        self.sr_sld.setRange(1000, 22050)
        self.sr_sld.setValue(11525)
        self.sr_sld.setFocusPolicy(Qt.NoFocus)
        self.sr_sld.setPageStep(1)
        self.sr_sld.setToolTip(sr_tt)
        self.sr_sld.move(90, 281)
        self.sr_sld.resize(0, 0)
        self.sr_sld.valueChanged.connect(
            lambda val: self.sr_val.setText(str(round(val/1000, 1)) + 'k'))

        # Octave Sliders
        octave_tt = 'Increases or decreases the octaves by the number selected'
        self.octave_lbl = QLabel(self)
        self.octave_lbl.setText('Octave:')
        self.octave_lbl.move(8, 305)
        self.octave_lbl.setToolTip(octave_tt)
        self.octave_lbl.resize(0,0)
        self.octave_val = QLabel(self)
        self.octave_val.move(170, 307)
        self.octave_val.resize(0,0)
        self.octave_val.setText('0')
        self.octave_val.setFont(QFont('', 8))
        self.octave_val.setToolTip(octave_tt)
        self.octave_sld = QSlider(Qt.Horizontal, self)
        self.octave_sld.setRange(-7, 7)
        self.octave_sld.setFocusPolicy(Qt.NoFocus)
        self.octave_sld.setPageStep(1)
        self.octave_sld.move(90, 306)
        self.octave_sld.resize(0,0)
        self.octave_sld.setToolTip(octave_tt)
        self.octave_sld.valueChanged.connect(
            lambda val: self.octave_val.setText(str(val)))

        # button to process file
        self.proc_file = QPushButton('Process...', self)
        self.proc_file.setGeometry(150, 150, 100, 40)
        self.proc_file.move(50, 430)
        self.proc_file.clicked.connect(self.process_file)
        self.proc_lbl = QLabel('', self)
        self.proc_lbl.move(53, 530)
        self.proc_lbl.setFont(QFont('', 12))

        # error Label
        self.error_lbl = QLabel('', self)
        self.error_lbl.resize(300, 20)
        self.error_lbl.move(20, 475)
        self.error_lbl.setFont(QFont('', 11))

        # create the canvas for drawing
        self.canvas = qt_canvas.QtCanvas(self)
        self.canvas.resize(410, 410)
        self.canvas.move(210, 230)
        
        # create the label for word cloud viewing
        self.word_cloud_lbl = QLabel('', self)
        self.word_cloud_lbl.resize(410, 410)
        self.word_cloud_lbl.move(210, 230)

        # used when saving generated images
        self.enable_save = False

    def dark_mode(self):
        # https://gist.github.com/mstuttgart/37c0e6d8f67a0611674e08294f3daef7
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, Qt.white)
        dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
        dark_palette.setColor(QPalette.Text, Qt.white)
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, Qt.white)
        dark_palette.setColor(QPalette.BrightText, Qt.red)
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, Qt.black)
        dark_palette.setColor(QPalette.ToolTipText, Qt.black)
        return dark_palette

    def pick_file(self):
        # https://pythonspot.com/pyqt5-file-dialog/
        # params for getOpenFileName are the window, the title, default file, file types
        file_name, _ = QFileDialog.getOpenFileName(
            self, 'Select Audio file', '', 'Audio Files (*.mp3 *.wav)')
        if file_name:
            self.file_path.setText(file_name)
            self.error_lbl.setText('')
            self.sample_combo.addItems(self.get_samples())
            self.clear_specs()

    def set_specs(self):
        path = self.sample_combo.currentText()
        if path == '':
            self.clear_specs()
            return
        self.file_path.setText('')
        specs = dbm.db_driver('ss', path)
        self.clear_specs()
        self.spec_lbl.setText('Select Specs:')
        self.spec_lbl.resize(300, 15)
        self.spec_combo.resize(140, 20)
        specs_list = ['']
        specs_list += [
            f'FRQ={s[0]}%, SR={round(int(s[1])/1000,1)}k' for s in specs]
        self.spec_combo.addItems(specs_list)

    def set_sample(self): 
        self.on_algo_change()
        if self.sample_combo.currentText() == '' or self.spec_combo.currentText() == '':
            return
        specs = self.spec_combo.currentText().split(',')
        frq = specs[0].replace('FRQ=', '').replace('%', '')
        sr = int(float(specs[1].replace('SR=', '').replace('k', '')) * 1000)
        self.frq_sld.setValue(int(frq))
        self.sr_sld.setValue(sr)

    def get_samples(self):
        self.sample_combo.clear()
        samples = ['']
        samples += [s for s in dbm.db_driver('s')]
        return samples

    def clear_specs(self):
        self.spec_combo.clear()
        self.spec_lbl.setText('')
        self.spec_combo.resize(0, 0)
        self.spec_lbl.resize(0, 0)

    def clear_toggles(self):
        self.frq_val.resize(0,0) 
        self.frq_sld.resize(0,0) 
        self.frq_lbl.resize(0,0)
        self.sr_val.resize(0,0) 
        self.sr_sld.resize(0,0)
        self.sr_lbl.resize(0,0)
        self.octave_val.resize(0,0) 
        self.octave_sld.resize(0,0)
        self.octave_lbl.resize(0,0)

    def on_algo_change(self):
        algo_desc = {
            '': ['',''],
            'Shape of You': ['Draw a collection of shapes based on notes and octaves','fso'],
            'Line Rider': ['Draws a collection of lines based on notes and octaves','fso'],
            'Curvy': ['Draws a collection of arcs based on notes and octaves','fso'],
            'Speech': ['Draws a word map based on the most common words in the selected speech',''],
            'Grid': ['Draws a collection of arcs based on notes and octaves','fs'],
        }
        self.algo_lbl.setText(algo_desc[self.algo_combo.currentText()][0])
        self.algo_lbl.resize(150, 80)

        self.clear_toggles()
        toggles = algo_desc[self.algo_combo.currentText()][1]
        if self.spec_combo.currentText() != '':
            toggles = toggles.replace('f','').replace('s','')

        if 'f' in toggles:
            self.frq_lbl.adjustSize()
            self.frq_val.resize(35, 10)
            self.frq_sld.resize(75, 15)
            self.frq_val.setText(str(self.frq_sld.value()) + '%')
        if 's' in toggles:
            self.sr_lbl.adjustSize()
            self.sr_val.resize(35, 10)
            self.sr_sld.resize(75, 15)
            self.sr_val.setText(str(round(self.sr_sld.value()/1000, 1)) + 'k')
        if 'o' in toggles:
            self.octave_lbl.adjustSize()
            self.octave_val.resize(35, 10)
            self.octave_sld.resize(75, 15)        
            self.octave_val.setText(str(self.octave_sld.value()))


    def process_file(self):
        self.word_cloud_lbl.setHidden(True)
        if self.algo_combo.currentText() == '':
            self.error_lbl.setText(
                '<font color=red>Error: Choose an Algorithm</font>')
            return
        if self.sample_combo.currentText() != '' and self.spec_combo.currentText() == '':
            self.error_lbl.setText(
                '<font color=red>Error: Choose Specifications</font>')
            return
        success = False
        file = self.file_path.text() if self.sample_combo.currentText() == '' else self.sample_combo.currentText()
        if file[-4:].lower() in ('.mp3', '.wav') and os.path.exists(file):
            self.error_lbl.setText('')
            self.proc_lbl.setText('Processing...')
            self.proc_lbl.adjustSize()
            self.canvas.clear_args()
            self.canvas.shapes = []
            self.canvas.repaint()

            # p = multiprocessing.Process(target=shapes_algo.notes_to_canvas, args=(self.canvas,file),self.sr_sld.value(),self.octave_sld.value()))
            # p.start()
            self.enable_save = False
            success = process_audio.proc_audio(self.algo_combo.currentText(), self.canvas, file,
                                               int(round(self.sr_sld.value()/1000, 1) * 1000), self.octave_sld.value(), self.frq_sld.value(), self.word_cloud_lbl)
            self.proc_lbl.setText('')
            file = self.sample_combo.currentText()
            self.sample_combo.addItems(self.get_samples())
            if file != '':
                self.sample_combo.setCurrentText(file)
        else:
            self.error_lbl.setText(
                '<font color=red>Error: Invalid Audio File</font>')
            return
        if not success:
            self.error_lbl.setText(
                '<font color=red>Error Processing Audio File</font>')
        else:
            self.enable_save = True

    # https://stackoverflow.com/questions/20930764/how-to-add-a-right-click-menu-to-each-cell-of-qtableview-in-pyqt
    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.RightButton and self.enable_save:
            if QMouseEvent.pos().x() > 205 and QMouseEvent.pos().y() > 220:
                menu = QMenu(self)
                save_as = QAction('Save As', self)
                save_as.triggered.connect(lambda: self.save_img())
                menu.addAction(save_as)
                menu.popup(QCursor.pos())

    def save_img(self):
        if not self.enable_save or not self.canvas.save(QFileDialog.getSaveFileName(self, 'Save Image')[0]):
            self.error_lbl.setText(
                '<font color=red>Errror: Image Not Saved</font>')

def main_func():
    set_display_to_host()
    # instantiate application and create a window
    app = QApplication([])
    app.setStyle('Fusion')
    window = Window()
    app.setPalette(window.dark_mode())  # turn on dark mode
    window.show()
    app.exec()


def pip_main_func():
    # only called with pip package. Special changing of directory below
    print("Welcome to Synesthesia (installed via Pip)")
    # os.chdir('synesthesia')
    main_func()

if __name__ == '__main__':
    main_func()
