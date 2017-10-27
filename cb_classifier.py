#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import json
import os, sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn.externals import joblib
from sklearn.metrics import f1_score, precision_score, accuracy_score, recall_score


def load_data():
    data_dir = "./data/"
    files = []
    fnames = ["buzzfeed.json", "dose.json", "clickhole.json", "nytimes.json"]
    for fname in os.listdir(data_dir):
        if fname in fnames:
            with open(os.path.join(data_dir, fname)) as f:
                files += [pd.DataFrame(json.loads(f.read()))[["article_title", "clickbait"]]]
            
    df = pd.concat(files)
    df = df.sample(frac=1).reset_index(drop=True)
    return df.article_title, df.clickbait


def vectorize_text(X):
    self.vec = TfidfVectorizer(stop_words="english", lowercase=True, sublinear_tf=True)
    return vec.fit_transform(X)


class cb_classifier(object):
	def __init__(self):
		self.clf = RandomForestClassifier(n_estimators=30, max_features=2)
		self.trained = False
		self.vec_file = "./model/tfidfvec.pkl"
		self.model_file = "./model/cb_model_rf.pkl"


	def train(self):
		X, y = load_data()
		self.vec = TfidfVectorizer(stop_words="english")
		X = self.vec.fit_transform(X)
		self.Xtrain, self.Xtest, self.ytrain, self.ytest = train_test_split(X, y, test_size=0.2, random_state=100)
		self.clf.fit(self.Xtrain, self.ytrain)
		self.persist_model()
		self.trained = True


	def predict_proba(self, Xtest, clf=None):
		if not clf:
			clf = self.clf
		pred_probs = clf.predict_proba(self.Xtest)
		return pred_probs[:,1]


	def model_report(self):
		class_names = ["news", "clickbait"]
		if not self.trained:
			return False

		y_pred = self.clf.predict(self.Xtest)
		scores = {'creport': classification_report(y_true=self.ytest, y_pred=y_pred, target_names=class_names),
				'f1score':round(f1_score(y_true=self.ytest, y_pred=y_pred),4),
				'accuracy':round(accuracy_score(y_true=self.ytest, y_pred=y_pred), 4),
				'precision':round(precision_score(y_true=self.ytest, y_pred=y_pred), 4),
				'recall':round(recall_score(y_true=self.ytest, y_pred=y_pred), 4)}

		return scores

	def persist_model(self):
		joblib.dump(self.vec, filename=self.vec_file)
		joblib.dump(self.clf, filename=self.model_file)
		

	def load_pickle(self):
		vec_obj = joblib.load(self.vec_file)
		model_obj = joblib.load(self.model_file)

		return vec_obj, model_obj
