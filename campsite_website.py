import requests, json
from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'otters2025'
bootstrap = Bootstrap5(app)

params = {

}

endpoint = "https://developer.nps.gov/api/v1/alerts?parkCode=acad,dena"

try: 
    r = requests.get(endpoint, params=params)
    data = r.json()
except:
    print('please try again')