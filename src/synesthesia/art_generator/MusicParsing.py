from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QEventLoop, pyqtSignal, pyqtSlot
import wsl
from QtDrawing import Window
from pydub import AudioSegment
import pyaudio
import librosa
import numpy as np
import wsl
import wave
import time


def done():
    return


def main():
    sound = AudioSegment.from_mp3("mp3_around_the_sun.mp3")
    sound.export("around_the_sun.wav", format="wav")
    wf = wave.open("around_the_sun.wav")

    # Start Cavnas
    wsl.set_display_to_host()
    app = QApplication([])
    window = Window()
    window.show()

    # instantiate PyAudio (1)
    p = pyaudio.PyAudio()
   

    def lib_analysis(data):
        s = np.abs(librosa.stft(data))
        notes = librosa.hz_to_note(s)
        return notes

    # define callback (2)
    def callback(in_data, frame_count, time_info, status):
        # convert data to array
        data = np.fromstring(in_data, dtype=np.float32)
        bars = lib_analysis(data)
        for bar in bars:
            for note in bar:
                if '-' in note:
                    window.draw_something(note.split('-'))
        return in_data, pyaudio.paContinue

    # open stream using callback (3)
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=44100,
                    input=True,
                    output=True,
                    frames_per_buffer=int(1024),
                    stream_callback=callback)

    # start the stream (4)
    stream.start_stream()
    # wait for stream to finish (5)
    while stream.is_active():
        time.sleep(1)

    # stop stream (6)
    stream.stop_stream()
    stream.close()
    wf.close()
    done()

    # close PyAudio (7)
    p.terminate()


if __name__ == "__main__":
    main()
