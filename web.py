from flask import Flask
import pandas as pd
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
  pred_clf = clf.predict(X_validation)
  kfold = model_selection.KFold(n_splits=10, random_state=5)
  scoring="accuracy"
  cv_results = model_selection.cross_val_score(GaussianNB(), X_train, Y_train, cv=kfold, scoring=scoring)

  msg = "%s: %f (%f)" % ('NB accuracy', cv_results.mean(), cv_results.std())
  
  return jsonify(result:"dsvsd")
  return msg
