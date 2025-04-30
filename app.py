from pickletools import long1
from flask import Flask
# Importing geopy library and nominatim class, currenntly unknown nominatim class
from geopy.geocoders import Nominatim
# Call the nominatim tool and create nominatim class
location = Nominatim(user_agent="Geopy Library")
# Uses Flask WTF for forms
# Uses bootstrap flask to use bootstrap css
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
# Flask-WTF’s FlaskForm will automatically create a secure session with CSRF (cross-site request forgery) protection if this key-value is set and the csrf variable is set. Don’t publish an actual key on GitHub!
import os
SECRET_KEY = os.urandom(32)



#Enter the Location Name
#

#print address
# print(str(location_info) + "test")

# Print lat and long
# print(f'Latitude  {location_info.latitude}, \n'
#       f'Longitude {location_info.longitude}')


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

class NameForm(FlaskForm):
    name = StringField('Which actor is your favorite?', validators=[DataRequired(), Length(10, 40)])
    submit = SubmitField('Submit')

@app.route("/latlong")
def hello_world():
    location_info = location.geocode("717 w 17th place, chicago, il")
    return f'Latitude  {location_info.latitude}, \n Longitude {location_info.longitude}'
# This is a sample Python script.

def get_names(type):
    if type == "actors":
        return ['Robert', 'greg']

def get_id():
    return 2

@app.route('/', methods=['GET', 'POST'])
def index():
    names = get_names('ACTORS')
    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html
    form = NameForm()
    message = "hewwo"
    if form.validate_on_submit():
        name = form.name.data
        if name.lower() in names:
            # empty the form field
            form.name.data = ""
            id = get_id('ACTORS', name)
            # redirect the browser to another route and template
            return redirect( url_for('actor', id=id) )
        else:
            message = "That actor is not in our database."
    return render_template('index.html', names=names, form=form, message=message)



hello_world()

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

