from SentimentAnalysis import SA
from AnalysisEmotionTone import AET
from FaceEmotionDetection import FED
from ManageData import GetFEDData
from DataMerging import MergingData
from SensitiveMoment import SM, CreateSound, CreateText, SaveText
import os, sys
import matplotlib.pyplot as plt

frame = 10
clip = os.path.join(os.path.dirname(__file__), './happy_disgust_suprprise.mkv')
save_sm = False

for j in range(1, len(sys.argv)):
    if len(sys.argv) == 1:
        break
    if sys.argv[j] == '-c':
        clip = sys.argv[j+1]
    if sys.argv[j] == '-f':
        frame = int(sys.argv[j+1])
    if sys.argv[j] == '-sm':
        save_sm = True

    
SA_output = SA(clip, 10)
AET_output = AET(clip, 4)
FED_output = FED(clip, frame, show=True)
graphFED = GetFEDData(FED_output, clip, frame, 10, rs_check = False, change_defult_rs = True)

print (SA_output)
print (AET_output)


merged_data = MergingData(SA_output, AET_output, graphFED, frame, 1, 1.6)

emotions = ['Surprise', 'Neutral', 'Anger', 'Happy', 'Sad', 'Disgust', 'Fear']
def SeparateData (data, emotion):
    result = []
    for i in range(1, len(data)+1):
        result.append(data[i][emotion])
    return result

Surprise = SeparateData(merged_data, 0)
Neutral = SeparateData(merged_data, 1)
Anger = SeparateData(merged_data, 2)
Happy = SeparateData(merged_data, 3)
Sad = SeparateData(merged_data, 4)
Disgust = SeparateData(merged_data, 5)
Fear = SeparateData(merged_data, 6)
X = list(merged_data)

if save_sm:
    SM = SM(Surprise, Neutral, Anger, Happy, Sad, Disgust, Fear)
    filename = CreateSound(clip, SM, frame, only_one=False)
    persian_text = CreateText(filename)
    SaveText(persian_text, filename)


plt.style.use('seaborn-whitegrid')

plt.plot(X, Surprise, label = emotions[0])
plt.plot(X, Neutral, label = emotions[1])
plt.plot(X, Anger, label = emotions[2])
plt.plot(X, Happy, label = emotions[3])
plt.plot(X, Sad, label = emotions[4])
plt.plot(X, Disgust, label = emotions[5])
plt.plot(X, Fear, label = emotions[6])

plt.ylabel('value')
plt.xlabel('time/frame')

plt.legend()
plt.show()