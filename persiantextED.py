from __future__ import division, print_function, unicode_literals
import sklearn
import sys
from PersianSentimentAnalysis.CTWCT import CommentToWordCounterTransformer
from PersianSentimentAnalysis.WCTVT import WordCounterToVectorTransformer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
import numpy as np
import pickle, os


np.random.seed(42)

svm_model = os.path.join(os.path.dirname(__file__), './PersianSentimentAnalysis/resources/svm_model.pkl')
preprocessing_pipline = os.path.join(os.path.dirname(__file__), './PersianSentimentAnalysis/resources/preprocessing_pipline.pkl')

svm_model = pickle.load(open(svm_model, 'rb'))
preprocess_pipeline = pickle.load(open(preprocessing_pipline, 'rb'))

def predict_sentiment(new_comment, return_class_label = False):
    p_class = svm_model.predict(preprocess_pipeline.transform(new_comment).toarray())
    if return_class_label:
        return p_class[0]
    return "Positive!" if p_class[0] > 0 else "Negative!"

Sentence = str(sys.argv[1])
for i in range(2, 15):
    try:
        Sentence = Sentence+ " "+ sys.argv[i]
    except IndexError:
        break


print (predict_sentiment(np.array([Sentence]), return_class_label=True))
