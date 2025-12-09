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
}

# Configure API request
endpoint = 'https://developer.nps.gov/api/v1/parks'

try:
    r = requests.get(endpoint, params=payload)
    data = r.json()
    # pprint(data)
    
    for parks in data["data"]:
        print (parks['fullName'], parks['states'])
        

except:
    print('please try again')
    

#stateSearch form!  -  String field to enter a state? that string can then.. be used to filter some parks.
class StateSearch(FlaskForm):
   stateSearch = StringField('Search by State', validators=[DataRequired()])



#parkSearch form - User will be able to select desired park
class Parks(FlaskForm):
    parks = SelectField("Select a park", choices=[], validators=[DataRequired()])
    submit = SubmitField('Search')


#main page: should dynamically react to a user's selecting of states? or a user's searching of states(implemented with form)??
@app.route('/')
@app.route('/<state>')
def index():
    return render_template('main.html', state = state)

#details page: should display details about a single facility/national park.
    #details: ammenities, fees/costs
@app.route('/details')
def details():

    return render_template('example.html', )#example.html
# testing: curly brace added?


# gets the parks for selected state
def get_parks(state):
    my_key = 'HDF4Pw02rLOOv9EuM4rU8LMgjIXs2O7FzxdfVEaX'

    payload = {
        'api_key': my_key,
        'stateCode' : state,
        'limit' : 475
    }

    endpoint = 'https://developer.nps.gov/api/v1/parks'

    try:
        r = requests.get(endpoint, params=payload)
        data = r.json()
        return data.get('data')
            
    except:
        print('please try again')
        

