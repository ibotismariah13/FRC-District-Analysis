from geopy import  Nominatim
from geopy import distance as distance
import uszipcode as uszip  # zipcode data https://uszipcode.readthedocs.io/01-Tutorial/index.html
import requests
import json
"calculate distance to competions for teams and eventually travel cost"
class Travel:

    def __init__(self,key,year,district_code,team_add):
        '''creates a dictorary for the given district year and returns a list'''
        url = "https://www.thebluealliance.com/api/v3/team/" +key + "/events/"+year
        header = {
            "X-TBA-Auth-Key": 'bDf8f29vaRS5Q5Zecj9ZRadHcZZz1c2l7rwgMIiXZfcIWMlMQYWbcTtqiJPQDWRh'
        }
        response = requests.request("GET", url, headers=header)
        #print(response.text)
        team_events = json.loads(response.text)

        url = "https://www.thebluealliance.com/api/v3/district/" + district_code + "/events/keys"
        header = {
            "X-TBA-Auth-Key": 'bDf8f29vaRS5Q5Zecj9ZRadHcZZz1c2l7rwgMIiXZfcIWMlMQYWbcTtqiJPQDWRh'
        }
        response = requests.request("GET", url, headers=header)
        #print(response.text)
        district_events = json.loads(response.text)#events in the district this year
        event_data=[] #2d array of the long, lat, start, and end date of events
        for event in team_events:
            if (str(year)+event['event_code']) in district_events:
                event_data.append([event['lat'],event['lng'],event['start_date'],event['end_date']])
        self.event_data=event_data
        self.distances = []
        for item in event_data:
            event_cor = (item[0], item[1])
            self.distances.append(distance.distance(team_add,event_cor).miles)

    def total_distance(self):
        sum = 0
        distances=self.distances
        for item in distances:
            sum += item
        return sum


    def average_distance(self):
        total=self.total_distance()
        num=len(self.distances)
        if num != 0:
            return float(total/num)
        else:
            return float(0)

