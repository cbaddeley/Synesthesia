from ctypes import c_float
from synesthesia.art_generator import dbm
import subprocess
import pickle
import librosa
import numpy as np
from PyQt5.QtGui import QPainterPath

from synesthesia.art_generator.wsl import *
import warnings
from wordcloud import WordCloud

from ctypes import *

from timeit import default_timer as timer
import traceback

set_display_to_host()
from synesthesia.art_generator import genre_colors, shapes_algo, curvy_algo, lines_algo, grid_algo


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


def proc_audio(gui, algo, song_path, sr_selection, oct_selection, freq_scale):
    is_mp3 = False
    have_sample = False
    wav_path = ''
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

        try:
            wordcloud = WordCloud(width=400, height=400, max_words=1000, margin=10, random_state=1, background_color=None, mode='RGBA').generate(transcribedText)
        except:
            return False
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
        if gui.stopped:
            del_file(is_mp3, wav_path)
            return 'stopped'
        if is_mp3:
            y, _ = librosa.load(wav_path, sr=sr_selection)
        else:
            y, _ = librosa.load(song_path, sr=sr_selection)
        if gui.stopped:
            del_file(is_mp3, wav_path)
            return 'stopped'
        S = np.abs(librosa.stft(y))
        if gui.stopped:
            del_file(is_mp3, wav_path)
            return 'stopped'
        if freq_scale != 0:
            S *= (1 + (freq_scale / 100))


        try:
            import pkgutil
            import synesthesia.images as syne_pkg
            syne_path = syne_pkg.__file__
            print(syne_path)
            syne_path = syne_path[:-18]
            syne_path = syne_path + "art_generator/rusty.so"
            print(syne_path)

            lib = cdll.LoadLibrary(syne_path)

            lib.note.restype = c_int
            lib.note.argtypes = [c_double]
            note_list = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
            bars = []
            for freq_bars in S:
                bar = []
                for frq in freq_bars:
                    if gui.stopped:
                        del_file(is_mp3, wav_path)
                        return 'stopped'
                    notes_oct = abs(lib.note(frq))
                    note = notes_oct // 1000
                    oct = notes_oct - note * 1000
                    bar.append(note_list[note] + '-' + str(oct))
                bars.append(bar)
        except Exception as error:
            traceback.print_exc()
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
        del_file(is_mp3, wav_path)
    return True, bars, genre, have_sample, freq_scale, sr_selection, oct_selection


def del_file(is_mp3, wav_path):
    if is_mp3:
        try:
            os.remove(wav_path)
        except:
            pass

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
                pass
            else:
                text = f"{text.capitalize()}. "
                whole_text += text
    # return the text for all chunks detected
    return whole_text
