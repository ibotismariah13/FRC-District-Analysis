from geopy import  Nominatim
from geopy import distance as distance
import uszipcode as uszip  # zipcode data https://uszipcode.readthedocs.io/01-Tutorial/index.html
import requests
import json
"calculate distance to competions for teams and eventually travel cost"
class Travel:

    def __init__(self,key,postal_code,year):
        '''creates a dictorary for the given district year and returns a list'''
        url = "https://www.thebluealliance.com/api/v3/team/" +key + "/events/"+year
        header = {
            "X-TBA-Auth-Key": 'bDf8f29vaRS5Q5Zecj9ZRadHcZZz1c2l7rwgMIiXZfcIWMlMQYWbcTtqiJPQDWRh'
        }
        response = requests.request("GET", url, headers=header)
        # print(response.text)
        events = json.loads(response.text)
        event_data=[]
        for event in events:
            event_data.append([event['lat'],event['lng'],event['start_date'],event['end_date']])
        self.event_data=event_data
        self.distances = []
        search = uszip.SearchEngine()
        zipcode = search.by_zipcode(postal_code)
        zipcode.zipcode
        team_add = ( zipcode.lat,zipcode.lng)
        for item in event_data:
            event_cor = (item[0], item[1])
            self.distances.append(distance.distance(team_add,event_cor).miles)

    def total_distance(self):
        sum = 0
        for item in self.distances:
            sum += item
        return sum

    def average_distance(self):
        self.total_distance()
        if len(self.distances) != 0:
            return float(self.total_distance()/len(self.distances))


