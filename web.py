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

  return "ssfb"
