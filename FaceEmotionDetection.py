import numpy as np
import cv2
import tensorflow as tf
import os, glob
import ffmpeg
from tqdm import tqdm

face_detection = cv2.CascadeClassifier(os.path.join(os.path.dirname(__file__), './models/haar_cascade_face_detection.xml'))
model = tf.keras.models.load_model(os.path.join(os.path.dirname(__file__), './models/FED.h5'))
labels = ['Surprise', 'Neutral', 'Anger', 'Happy', 'Sad']

def FED(film, fps_limit=None, show=False):
	if fps_limit is not None:
		files = glob.glob(os.path.join(os.path.dirname(__file__), './LivaData/Video/*'))
		for f in files:
			os.remove(f)
		stream = ffmpeg.input(film)
		stream = stream.filter('fps', fps=fps_limit, round='up')
		dir = os.path.join(os.path.dirname(__file__), './LivaData/Video/livevideo.mkv')
		stream = ffmpeg.output(stream, dir)
		ffmpeg.run(stream)
		film = dir

	capture = cv2.VideoCapture(film)

	capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
	capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)
	settings = {'scaleFactor': 1.3, 'minNeighbors': 5, 'minSize': (50, 50)}
	frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
	frameNr = 1
	global result
	result = dict((el, None) for el in range(1, frame_count+1))

	show_process = tqdm(total=frame_count, desc="FED ")
	while True:
		ret, frame = capture.read()
		if not ret:
			break

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		detected = face_detection.detectMultiScale(gray, **settings)
		predictions = -1

		for x, y, w, h in detected:
			cv2.rectangle(frame, (x, y), (x+w, y+h), (245, 135, 66), 2)
			face = gray[y+5:y+h-5, x+20:x+w-20]
			face = cv2.resize(face, (48,48)) 
			face = face/255.0
			predictions = model.predict(np.array([face.reshape((48,48,1))])).argmax()
			state = labels[predictions]
		
		result[frameNr] = int(predictions)
		frameNr += 1

		show_process.update(1)

		if show:
			cv2.imshow('Facial Expression', frame)

		if cv2.waitKey(5) != -1:
			break

	capture.release()
	cv2.destroyAllWindows()

	return result
