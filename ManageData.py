import seaborn as sn
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import soundfile
import shutil
import glob, os
from ExtractingAudio import CutSound, GetTheFilm


emotions = {'Anger':0, 'Happy':0, 'Sad':0, 'Surprise':0, 'Neutral':0}
def ManageData(emotion, reduce_surprise = True):
    global emotions
    if emotion == 0:
        if  reduce_surprise:
            emotions['Surprise'] += 0.5
            for value in emotions:
                if emotions[value] > 0 and value != 'Surprise':
                    emotions[value] -= 0.5
        else:
            emotions['Surprise'] += 1
            for value in emotions:
                if emotions[value] > 0 and value != 'Surprise':
                    emotions[value] -= 1

    elif emotion == 1:
        emotions['Neutral'] += 0.3
        for value in emotions:
            if emotions[value] > 0 and value != 'Neutral':
                emotions[value] -= 0.3

    elif emotion == 2:
        emotions['Anger'] += 1
        for value in emotions:
            if emotions[value] > 0 and value != 'Anger':
                emotions[value] -= 1

    elif emotion == 3:
        emotions['Happy'] += 1
        for value in emotions:
            if emotions[value] > 0 and value != 'Happy':
                emotions[value] -= 1

    elif emotion == 4:
        emotions['Sad'] += 1.3
        for value in emotions:
            if emotions[value] > 0 and value != 'Sad':
                emotions[value] -= 1

    return (emotions['Surprise'], emotions['Neutral'], emotions['Anger'], emotions['Happy'], emotions['Sad'])       

def GetFEDData(data, clip, frame, how_much_fps, rs_check = True, change_defult_rs = True):
    '''
    data = FED data
    clip = filmi ke dari analyzesh mikni
    fram = tedad kole frame ha 
    how_much_fps = clipet be qesmate chand saniyeii cut she 
    re_check = mikhaii moqe harf zadan surprize nagire ? True kn (bydefault = True)
    change_defult_rs = default def ManageData ro taqir bede (default = True)
    '''
    if rs_check:
        GetTheFilm(clip)
        time_range = CutSound(how_much_fps, "reduce")
        result = dict((el, None) for el in time_range)
        for i in range(len(time_range)):
            live_audio = os.path.join(os.path.dirname(__file__), f'LivaData\\Speech\\{time_range[i]}.wav')
            x, fs = np.read(source_path + f)
            vol_rms =  x.max() - x.min()
            if vol_rms <= 6.103515625e-05:
                time_range[i] = True #true => file seda nadarad
            else:
                time_range[i] = False #false => file seda darad
    
        limited_fps = []
        for i in time_range:
            if not result[i]:
                x = i.split('_')
                limited_fps.append(range(x[0]*frame, x[1]*frame))

    total_frame = list(data)[-1]
    graph_dict = dict((el, None) for el in range(1, total_frame+1))

    for i in range(1, total_frame+1):
        if rs_check:
            change_defult_rs = check_fps(i, limited_fps)
        graph_dict[i] = ManageData(data[i], change_defult_rs)
        
    return graph_dict

def check_fps(x, y):
    for i in range(len(y)):
        if x in y[i]:
            return True
        else:
            return False