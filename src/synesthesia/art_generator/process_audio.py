
from . import genre_colors, shapes_algo, curvy_algo, lines_algo, dbm
import os
import subprocess
from collections import Counter
import pickle
import librosa
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainterPath
from wsl import *
import warnings
set_display_to_host()


def drawer(canvas, algo, note, frq, oct_selection, genre):
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
        elif algo == 'Speech':
            1 + 1  #TODO draw word cloud off most common words


def proc_audio(algo, canvas, song_path, sr_selection, oct_selection, freq_scale):
    if algo == 'Speech':
        transcribedText = transcribeSpeech(song_path)
        print(transcribedText)

    is_mp3 = False
    have_sample = False
    try:
        S, bars, genre = dbm.db_driver(
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
            bars = librosa.hz_to_note(S)
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



    if not have_sample:
        disp_notes = []
        disp_frq = []
        for i, bar in enumerate(bars):

            c = Counter(bar)
            result = c.most_common(1)
            note = result[0]
            disp_notes.append(note)

            c = Counter(S[i])
            result = c.most_common(1)
            frq = result[0]
            disp_frq.append(frq)
            drawer(canvas, algo, note, frq, oct_selection, genre)

        dbm.db_driver('i', song_path, freq_scale, sr_selection, disp_frq, disp_notes, genre)
        if is_mp3:
            os.remove(wav_path)
    else: # we have a sample of the audio
        for i, note in enumerate(bars):
            drawer(canvas, algo, note, S[i], oct_selection, genre)

    return True




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
        min_silence_len = 500,
        # adjust this per requirement
        silence_thresh = sound.dBFS-14,
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