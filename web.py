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
  X = array[:,0:4]
  Y = array[:,4] 
  X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=0.33)
  clf = GaussianNB()
  clf.fit(X_train, Y_train) 
  pred = clf.predict([[request.args.get('ph'),request.args.get('n'),request.args.get('p'),request.args.get('k')]])
  data={"result":pred[0]}
  return jsonify(data)

