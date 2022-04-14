import os
import wave
import keras
import pyaudio
import numpy as np
import pandas as pd
import IPython.display as ipd
from keras.models import model_from_json
from ExtractingAudio import CutSound, GetTheFilm
from models.feature_extraction import get_audio_features

emotions = ['Anger','disgust','fear','happy','Neutral', 'sad', 'surprise']

json_file = open(os.path.join(os.path.dirname(__file__), './models/model.json'), 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights(os.path.join(os.path.dirname(__file__), './models/AET.h5'))

def AET(film, how_much, return_number = True):
    GetTheFilm(film)
    time_range = CutSound(how_much, "speech")
    result = dict((el, None) for el in time_range)
    str_result = dict((el, None) for el in time_range)

    for i in range(len(time_range)):
        live_audio = os.path.join(os.path.dirname(__file__), f'LivaData\\Speech\\{time_range[i]}.wav')

        ipd.Audio(live_audio)
        demo_mfcc, demo_pitch, demo_mag, demo_chrom = get_audio_features(live_audio,20000)
        mfcc = pd.Series(demo_mfcc)
        pit = pd.Series(demo_pitch)
        mag = pd.Series(demo_mag)
        C = pd.Series(demo_chrom)
        demo_audio_features = pd.concat([mfcc,pit,mag,C],ignore_index=True)
        demo_audio_features= np.expand_dims(demo_audio_features, axis=0)
        demo_audio_features= np.expand_dims(demo_audio_features, axis=2)
        demo_audio_features.shape
        livepreds = loaded_model.predict(demo_audio_features, batch_size=32, verbose=1)

        index = livepreds.argmax(axis=1).item()

        if return_number:
            result[time_range[i]] = int(index)
        else:
            str_result[time_range[i]] = emotions[index]

    if return_number:
        return result
    else:
        return str_result
        

