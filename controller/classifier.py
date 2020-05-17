from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
import pickle
import joblib
import nltk

class Classifier():

    def __init__(self, path):
        self.thres = 0.576
        self.path = path
        #self.stopwords = nltk.corpus.stopwords.words('portuguese')

    def stopwords(self):
        with open(self.path + 'portuguese') as f:
            lines = f.readlines()
        words = [line[:-2] for line in lines]
        return words

    def get_model(self):
        model = joblib.load(self.path + 'clf_voting.joblib')
        return model

    def get_vectorizer(self):
        vectorizer = joblib.load(self.path + 'tfidf_voting.joblib')
        return vectorizer

    def preprocessing(self, text):
        vect = self.get_vectorizer()
        #vect = TfidfVectorizer(analyzer='word', stop_words = self.stopwords(), min_df = 3, max_df = 0.8, lowercase=False, ngram_range=(1,3), vocabulary = vocab)
        text_vect = vect.transform([text])
        return text_vect
        
    def make_classification(self, text):
        vect_text = self.preprocessing(text)
        model = self.get_model()
        prob = model.predict_proba(vect_text)[0][1]
        metric = (self.thres - prob) / self.thres
        if metric <= -0.2 * self.thres:
            msg = 'Essa noticia parece falsa'
        elif -0.2 * self.thres <  metric < 0:
            msg = 'Nao sei, essa noticia talvez seja falsa'
        elif 0 < metric < 0.2 * self.thres:
            msg = 'Nao sei, essa noticia talvez seja verdadeira'
        else:
            msg = 'Essa noticia parece verdadeira'
        return (msg.upper(), prob)


