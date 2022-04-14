import speech_recognition as sr
import os, sys, subprocess
from ExtractingAudio import CutSound, GetTheFilm

def SA(film, how_much):
    GetTheFilm(film)
    time_range = CutSound(how_much, 'text')
    result = dict((el, None) for el in time_range)

    for i in range(len(time_range)):
        audiofile = os.path.join(os.path.dirname(__file__), f'LivaData\\Text\\{time_range[i]}.wav')
        filename = sr.AudioFile(audiofile)

        r = sr.Recognizer()

        with filename as source: 
            r.adjust_for_ambient_noise(source) 
            audio = r.record(source)

        a = r.recognize_google(audio, language = 'fa-IR', show_all = True )
        PersianText = a['alternative'][0]['transcript']

        print (PersianText)

        test = subprocess.Popen(["py", "-3.6", "persiantextED.py", PersianText], stdout=subprocess.PIPE)
        output = test.communicate()[0].decode("utf-8")

        result[time_range[i]] = int(output)
    
    return result


