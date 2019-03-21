from flask import Flask
import pandas as pd
app = Flask(__name__)

@app.route("/")
def home():
  df=pd.read_csv('data.csv')
  return "ssfb"
