import requests, json
from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from pprint import pprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'otters2025'
bootstrap = Bootstrap5(app)

my_key = 'HDF4Pw02rLOOv9EuM4rU8LMgjIXs2O7FzxdfVEaX'

payload = {
    'api_key': my_key,
    'q' : 'CA',
    'limit' : 5

# Configure API request
<<<<<<< HEAD
endpoint = "https://developer.nps.gov/api/v1/parks"
HEADERS = {
    'X-Api-Key':'5Ejw0mGYYPhdABAjwaOzlDFtQQ7IyJik1DldHmuu',
    'q':'CA',
    'limit':'1'
    }
=======
endpoint = 'https://developer.nps.gov/api/v1/parks'
>>>>>>> 0450994d25918ae58e83d929ffdae13cc610e952

try:
    r = requests.get(endpoint, params=payload)
    data = r.json()
    # pprint(data)
    
    for parks in data["data"]:
        print (parks['fullName'], parks['states'])
        

<<<<<<< HEAD
try: 
    req = requests.get(endpoint,headers=HEADERS)
    data = req.json()
    # pprint(data)
    pprint(data)
    for parks in data["data"]:
        pprint(parks['fullName'])
=======
>>>>>>> 0450994d25918ae58e83d929ffdae13cc610e952
except:
    print('please try again')

