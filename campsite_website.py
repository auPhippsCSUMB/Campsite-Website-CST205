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


# Configure API request
endpoint = "https://developer.nps.gov/api/v1/alerts?"
HEADERS = {
    "X-Api-Key":"5Ejw0mGYYPhdABAjwaOzlDFtQQ7IyJik1DldHmuu"
    }

# Additional code would follow

try: 
    req = requests.get(endpoint,headers=HEADERS)
    data = req.json()
    pprint(data)
except:
    print('please try again')

