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
}

# Configure API request
endpoint = 'https://developer.nps.gov/api/v1/parks'

try:
    r = requests.get(endpoint, params=payload)
    data = r.json()
except:
    print('please try again')
    
#EITHER GOING TO CHANGE ALL THESE TO STATE ABBRV OR TRANLSATE THEM IN FOR API SOMEWHERE ELSE
#WORKING WITH CALIFORNIA RN
statesWithAbbr = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY"
}


states = [
    "",
    "Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
    "North Dakota",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "West Virginia",
    "Wisconsin",
    "Wyoming"
]          

#stateSearch form!  -  String field to enter a state? that string can then.. be used to filter some parks.
class StateSearch(FlaskForm):
   stateSearch = SelectField(
    'Search by State',
     choices=states,
     validators=[DataRequired()],
     default = ""
     )



#parkSearch form - User will be able to select desired park
class Parks(FlaskForm):
    parks = SelectField("Select a park", choices=[], validators=[DataRequired()])
    submit = SubmitField('Search')


#main page: should dynamically react to a user's selecting of states? or a user's searching of states(implemented with form)??
@app.route('/', methods=('GET', 'POST'))
def index():
    form = StateSearch()
    stateText = ""
    parkList = []
    if form.validate_on_submit():
    
        payload['q'] = statesWithAbbr[form.stateSearch.data]

        try:
            r = requests.get(endpoint, params=payload)
            data = r.json()
        except:
            print('please try again')

        for parks in data["data"]:
            if (parks['states'] == statesWithAbbr[form.stateSearch.data]):
                parkList.append(parks['fullName'])

    return render_template('main.html', form = form, parkList = parkList)

#details page: should display details about a single facility/national park.
    #details: ammenities, fees/costs
@app.route('/details')
def details():

    return render_template('example.html')#example.html
# testing: curly brace added?
