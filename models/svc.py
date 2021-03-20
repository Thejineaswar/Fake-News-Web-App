# from sklearn.svm import SVC
import re
import string
from nltk.corpus import stopwords
import numpy as np
import pandas as pd
import joblib
from nltk.tokenize import word_tokenize
import importlib
from .word_preprocess import clean_tweet
from .word_abbreviations import get_abbr

abbreviations = get_abbr()

def take_tfidf():
    pick = pd.read_pickle(r"C:\Users\Thejin\Desktop\Deep Learning\rexcoe\models\tfidf_vectorizer.pickle")
    return pick

def load_model():
    model = joblib.load(r"C:\Users\Thejin\Desktop\Deep Learning\rexcoe\models\svc_using_tfidf_vector.joblib")
    return model

def tfidf_vector(data):
    tfidf_vectorizer = take_tfidf()
    vect = tfidf_vectorizer.transform(data)
    return vect

def predict(data):
    text = clean_tweet(data, abbreviations)
    text = np.asarray([text])
    text = tfidf_vector(text)
    model = load_model()
    res = model.predict(text)
    print(res)

# if __name__ == "__main__":
#     sentence = "earthquake safety los angeles safety fasteners"
#     text = clean_tweet(sentence, abbreviations)
#     text = np.asarray([text])
#     text = tfidf_vector(text)
#     model = load_model()
#     res = model.predict(text)
#     print(res)







