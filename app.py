from pickletools import long1
from flask import Flask
# Importing geopy library and nominatim class, currenntly unknown nominatim class
from geopy.geocoders import Nominatim
# Call the nominatim tool and create nominatim class
location = Nominatim(user_agent="Geopy Library")

#Enter the Location Name
location_info = location.geocode("717 w 17th place, chicago, il")

#print address
print(str(location_info) + "test")

# Print lat and long
print(f'Latitude  {location_info.latitude}, \n'
      f'Longitude {location_info.longitude}')


app = Flask(__name__)

@app.route("/")
def hello_world():
    return f'Latitude  {location_info.latitude}, \n Longitude {location_info.longitude}'
# This is a sample Python script.







hello_world()

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

