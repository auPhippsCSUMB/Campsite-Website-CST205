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
    # pprint(data)
    
    # for parks in data["data"]:
        # print (parks['fullName'], parks['states'])
        
        

except:
    print('please try again')
    
#EITHER GOING TO CHANGE ALL THESE TO STATE ABBRV OR TRANLSATE THEM IN FOR API SOMEWHERE ELSE
#WORKING WITH CALIFORNIA RN
states = [
    "",
    "Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "CA",
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
    if form.validate_on_submit():
        for parks in data["data"]:
            if (parks['states'] == form.stateSearch.data):
                stateText = stateText + parks['fullName'] + " "

    return render_template('main.html', form = form, stateText = stateText)

#details page: should display details about a single facility/national park.
    #details: ammenities, fees/costs
@app.route('/details')
def details():

    return render_template('example.html')#example.html
# testing: curly brace added?
