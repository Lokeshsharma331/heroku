from flask import Flask
import pandas as pd
import json
from flask import request,jsonify
from sklearn import model_selection
from sklearn.naive_bayes import GaussianNB
app = Flask(__name__)
@app.route("/")
def home():
  df=pd.read_csv('data.csv')
  array=df.values
  X = array[:,0:5]
  Y = array[:,5] 
  X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=0.33)
  clf = GaussianNB()
  clf.fit(X_train, Y_train) 
  pred = clf.predict([[float(request.args.get('ph')),float(request.args.get('n')),float(request.args.get('p')),float(request.args.get('k')),float(request.args.get('rainfall'))]])
  data={"result":pred[0]}
  return jsonify(data)

@app.route("/weather")
def weather():
  a=[]
  df=pd.read_csv('2018_pune')
  for i in df.Holt_Winter:
    a.append(i)
  data={"result":a}
  return jsonify(data)

