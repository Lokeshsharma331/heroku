from flask import Flask
import pandas as pd

from sklearn import model_selection
from sklearn.naive_bayes import GaussianNB
app = Flask(__name__)
@app.route("/")
def home():
  df=pd.read_csv('data.csv')
  array=df.values
  X = array[:,0:6]
  Y = array[:,6]
  X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=0.33)
  clf = GaussianNB()
  clf.fit(X_train, Y_train) 
  pred_clf = clf.predict(X_validation)
 
  return "ssfb"
