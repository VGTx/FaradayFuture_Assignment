import json
import os

"""
   Loads the data from the JSON file and stores it in a Dictionary
   The Keys for this Dictionary are the City Names and the Data Values are
   a Tuple made up of the required data fields for the GUI
"""

class Model_Data(object):

    json_path = "./ca.json"
    def __init__(self, json_path = "./ca.json"):

    # Check if JSON file path is valid, exit for invalid path

        if os.path.exists(json_path) and os.path.isfile(json_path):
            myfp = open(json_path, 'r')
        else:
            print "Invalid file path"
            exit()

        self.json_dict= json.load(myfp)
        myfp.close()
        self.mydict = dict()

    # Import relevant data into Dictionary from quick lookup and replace invalid inputs with a Warning message

        for city_data in self.json_dict:
            city_name = city_data['name']
            new_city_data = []
            if city_data['full_county_name']:
                new_city_data.append(city_data['full_county_name'])
            else:
                new_city_data.append('Data not available!')
            if city_data['primary_latitude']:
                new_city_data.append(city_data['primary_latitude'])
            else:
                new_city_data.append('Data not available!')
            if city_data['primary_longitude']:
                new_city_data.append(city_data['primary_longitude'])
            else:
                new_city_data.append('Data not available!')
            self.mydict[city_name] = new_city_data

    def Return_Data(self, name):

    # Provide Tuple data for corresponding city if it exists in the Dictionary
        if(name in self.mydict):
            return self.mydict[name]

    def Get_List(self):

    # Provide the entire alphabetically sorted list of city names from the Dictionary

        return sorted(self.mydict.keys())
