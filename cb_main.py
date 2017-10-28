#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import json
import os
import sys
from sklearn.externals import joblib
import pandas as pd
from cb_classifier import vectorize_text, CBClassifier
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def check():
	return "it works", 200


@app.route("/clickbait_predict",  methods=["POST"])
def clickbait_proba():
	title_json = request.get_json(silent=True)
	if type(title_json) in (list, tuple):
		df = pd.DataFrame(title_json)
	elif type(title_json) == dict:
		df = pd.DataFrame([title_json])
	else:
		return "Bad Request. Input must be in proper json format ", 400
	
	try:
		vec, clf = cbc.load_pickle()
		X = vec.transform(df.ix[:,0])
		predx = clf.predict_proba(X)
		df["clickbait_probability"] = predx[:,1].round(4)
	except Exception as e:
		return jsonify({"error": str(e), "trace": traceback.format_exc()})
	
	df_json = df.to_json(orient="records")
	return jsonify(df_json)


@app.route("/train", methods = ["GET"])
def train():
	cbc.train()
	return "success", 200

@app.route("/classification_report", methods = ["GET"])
def classification_report():
	clf = cbc.load_pickle()
	scores = cbc.model_report()
	if scores:
		return jsonify(scores)
	else:
		return "You must train the model first. GET /train", 400

if __name__ == "__main__":
     cbc = CBClassifier()
     app.run(host='0.0.0.0', port=5000)
