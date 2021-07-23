from ctypes import c_float
from . import dbm
import subprocess
import pickle
import librosa
import numpy as np
from PyQt5.QtGui import QPainterPath

from wsl import *
import warnings
from wordcloud import WordCloud

from ctypes import *

set_display_to_host()
from . import genre_colors, shapes_algo, curvy_algo, lines_algo, grid_algo


def drawer(canvas, algo, note, oct_selection, genre, bar_index):
    if '-' in note[0]:
        if algo == 'Shape of You':
            shapes_algo.draw_note(canvas, note[0].split(
                '-'), oct_selection, genre_colors.getColors(genre))
        elif algo == 'Line Rider':
            lines_algo.draw_note(canvas, note[0].split(
                '-'), oct_selection, genre_colors.getColors(genre))
        elif algo == 'Curvy':
            path = QPainterPath()
            curvy_algo.draw_note(canvas, note[0].split(
                '-'), oct_selection, genre_colors.getColors(genre), path)
        elif algo == 'Grid':
            grid_algo.draw_note(canvas, note[0].split(
                '-'), oct_selection, genre_colors.getColors(genre), bar_index)


def proc_audio(algo, song_path, sr_selection, oct_selection, freq_scale):
    is_mp3 = False
    have_sample = False
    if algo == 'Speech':
        if song_path[-4:] == '.mp3':
            wav_path = song_path[:-4] + '.wav'
            is_mp3 = True
            if not os.path.exists(wav_path):
                subprocess.call(['ffmpeg', '-i', song_path, wav_path])

        if is_mp3:
            transcribedText = transcribeSpeech(wav_path)
        else:
            transcribedText = transcribeSpeech(song_path)

        print(transcribedText)
        wordcloud = WordCloud(width=400, height=400, max_words=1000, margin=10, random_state=1, background_color=None, mode='RGBA').generate(transcribedText)
        cloud_path = song_path[:-4] + '.png'
        wordcloud.to_file(cloud_path)
        return cloud_path

    try:
        bars, genre = dbm.db_driver(
            'r', song_path, freq_scale, sr_selection)[0]
        bars = pickle.loads(bars)
        have_sample = True
    except:  # when song not found
        if song_path[-4:] == '.mp3':
            wav_path = song_path[:-4] + '.wav'
            is_mp3 = True
            if not os.path.exists(wav_path):
                subprocess.call(['ffmpeg', '-i', song_path, wav_path])
        if is_mp3:
            y, sr = librosa.load(wav_path, sr=sr_selection)
        else:
            y, sr = librosa.load(song_path, sr=sr_selection)
        S = np.abs(librosa.stft(y))
        if freq_scale != 0:
            S *= (1 + (freq_scale / 100))
        try:
            lib = cdll.LoadLibrary(r'./art_generator/rusty.so')
            lib.note.restype = c_int
            lib.note.argtypes = [c_double]
            note_list = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

            bars = []
            for freq_bars in S:
                bar = []
                for frq in freq_bars:
                    notes_oct = abs(lib.note(frq))
                    note = notes_oct // 1000
                    oct = notes_oct - note * 1000
                    bar.append(note_list[note] + '-' + str(oct))
                bars.append(bar)
        except:
            return False

        # Musicnn gives a bunch of useless console warnings that we don't need to see and should just try to block out AMAP
        try:
            warnings.filterwarnings("ignore")
            from musicnn.tagger import top_tags
            genre = top_tags(song_path, model='MSD_musicnn', topN=1)
            genre = genre[0]
            warnings.filterwarnings("default")
        except:
            genre = ''

    if is_mp3:
        os.remove(wav_path)
    return True, bars, genre, have_sample, freq_scale, sr_selection, oct_selection


def transcribeSpeech(path):
    import speech_recognition as sr
    from pydub import AudioSegment
    from pydub.silence import split_on_silence

    r = sr.Recognizer()

    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    # open the audio file using pydub
    sound = AudioSegment.from_wav(path)
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
                              # experiment with this value for your target audio file
                              min_silence_len=500,
                              # adjust this per requirement
                              silence_thresh=sound.dBFS - 14,
                              # keep the silence for 1 second, adjustable as well
                              keep_silence=500,
                              )
    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                # print("Error:", str(e))
                1 + 1
            else:
                text = f"{text.capitalize()}. "
                # print(chunk_filename, ":", text)
                whole_text += text
    # return the text for all chunks detected
    return whole_text
