import moviepy.editor as mp
from moviepy.editor import VideoFileClip
from pathlib import Path
import os, glob
import cv2


#get the film
def GetTheFilm(film, return_option = False): #use this ===>  os.path.join(os.path.dirname(__file__), './happy_surprise_test.mkv')
    my_clip = film
    cap = cv2.VideoCapture(my_clip)
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    global duration
    global sound
    duration = round(frame_count/60, 2)
    sound = mp.VideoFileClip(my_clip)

    if return_option:
        return duration, sound

# cut the sound with diffrent value
def CutSound(value, textORspeechORreduce):
    if textORspeechORreduce == "speech":
        folder = os.path.join(os.path.dirname(__file__), './LivaData/Speech/*')
    elif textORspeechORreduce == "reduce":
        folder = os.path.join(os.path.dirname(__file__), './LivaData/ReduceSurprice/*')
    else:
        folder = os.path.join(os.path.dirname(__file__), './LivaData/Text/*')
    files = glob.glob(folder)
    for f in files:
        os.remove(f)
    
    count = int(duration/value)
    first = 0
    second = 0
    TotalList = []
    for i in range(count):
        second = first + value
        newsound = sound.subclip(first, second)
        if textORspeechORreduce == "text":
            x = f"{first}_{second}"
            fp=Path(os.path.join(os.path.dirname(__file__), 'LivaData\Text'), x+'.wav')
            TotalList.append(x)
        elif textORspeechORreduce == "reduce":
            x = f"{first}_{second}"
            fp=Path(os.path.join(os.path.dirname(__file__), 'LivaData\ReduceSurprice'), x+'.wav')
            TotalList.append(x)
        else:
            x = f"{first}_{second}"
            fp=Path(os.path.join(os.path.dirname(__file__), 'LivaData\Speech'), x+'.wav')
            TotalList.append(x)
        first = second
        newsound.audio.write_audiofile(fp)

    if int(duration)-second > 2:
        finalsound = sound.subclip(second, int(duration))
        if textORspeechORreduce == "text":
            x = f"{second}_{int(duration)}"
            fp=Path(os.path.join(os.path.dirname(__file__), 'LivaData\Text'), x+'.wav')
            TotalList.append(x)
        elif textORspeechORreduce == "reduce":
                x = f"{first}_{second}"
                fp=Path(os.path.join(os.path.dirname(__file__), 'LivaData\ReduceSurprice'), x+'.wav')
                TotalList.append(x)
        else:
            x = f"{second}_{int(duration)}"
            fp=Path(os.path.join(os.path.dirname(__file__), 'LivaData\Speech'), x+'.wav')
            TotalList.append(x)
        finalsound.audio.write_audiofile(fp)

    if textORspeechORreduce == "text":
        return TotalList
    elif textORspeechORreduce == "reduce":
        return TotalList
    else:
        return TotalList
