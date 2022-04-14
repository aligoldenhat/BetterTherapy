import os, glob
from ExtractingAudio import GetTheFilm
import speech_recognition as sr
from pathlib import Path

def SM(Surprise, Neutral, Anger, Happy, Sad, Disgust, Fear):
    a = [Surprise, Neutral, Anger, Happy, Sad, Disgust, Fear]
    maximum = 0 
    wh_emotion = None
    for i in range(len(a)):
        second = max(a[i])
        if second > maximum:
            maximum = second
            wh_emotion = i
            index = a[i].index(maximum)
    return maximum, wh_emotion, index
        
def CreateSound(clip, SM, frame, only_one = True):
    sound_info = GetTheFilm(clip, return_option=True)
    sec = int(SM[2]/frame)
    start_sec = sec - 10
    end_sec = sec + 3
    if end_sec > int(sound_info[0]):
        end_sec = int(sound_info[0])

    if only_one:
        folder = os.path.join(os.path.dirname(__file__), './Sensetive_moment/*')
        files = glob.glob(folder)
        for file in files:
            os.remove(file)

    emotions = ['Surprise', 'Neutral', 'Anger', 'Happy', 'Sad', 'Disgust', 'Fear']
    emotion = emotions[SM[1]]
    sound = sound_info[1]
    newsound = sound.subclip(start_sec, end_sec)
    start_sec = SecToMin(start_sec)
    end_sec = SecToMin(end_sec)
    filename = f"{emotion}__{start_sec}_{end_sec}"
    fp = Path(os.path.join(os.path.dirname(__file__), 'Sensetive_moment\\'), filename+'.wav')
    newsound.audio.write_audiofile(fp)

    return filename
    
def CreateText(fn):
    audiofile = os.path.join(os.path.dirname(__file__), f'Sensetive_moment\\{fn}.wav')
    filename = sr.AudioFile(audiofile)

    r = sr.Recognizer()

    with filename as source: 
        r.adjust_for_ambient_noise(source) 
        audio = r.record(source)

    a = r.recognize_google(audio, language = 'fa-IR', show_all = True )
    persian_text = a['alternative'][0]['transcript']

    return persian_text

def SaveText(text, emotion_detail):
    dir = os.path.join(os.path.dirname(__file__), './Sensetive_moment/all_sensetive_moment.txt')
    emotion_detail = emotion_detail.replace('-', ':')
    if os.path.isfile(dir):
        with open(dir, "a", encoding="utf-8") as file:
            file.write(f"\n{emotion_detail}  : {text}")

    else:
        with open(dir, "w", encoding="utf-8") as file:
            file.write(f"{emotion_detail}  : {text}")

def SecToMin(sec):
    if sec < 60:
        if len(str(sec)) == 1:
            return f'0-0{sec}'
        else:
            return f'0-{sec}'
    else:
        b = int(sec / 60)
        c = sec % (b*60)
        if len(str(c)) == 1:
            return f'{b}-0{c}'
        else:
            return f'{b}-{c}'

