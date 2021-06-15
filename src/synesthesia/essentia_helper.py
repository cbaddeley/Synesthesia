import essentia
import essentia.standard as es
import json
import numpy as np



def get_happy_percentage():
    audio = es.MonoLoader(filename='../mp3/around_the_sun.mp3', sampleRate=44100)()
    # happiness_preds = es.TensorflowPredictMusiCNN(graphFilename='essentia_models/mood_happy-musicnn-msd-1.pb')(audio)
    # happiness_metadata = json.load(open('essentia_models/mood_happy-musicnn-msd-1.json', 'r'))['classes']
    # # Average predictions over the time axis
    # happiness_preds = np.mean(happiness_preds, axis=0)
    # print('{}: {}%'.format(happiness_metadata[0] , happiness_preds[0] * 100))