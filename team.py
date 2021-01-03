'''team object and its attribute's'''
import uszipcode as uszip  # zipcode data https://uszipcode.readthedocs.io/01-Tutorial/index.html
from geopy import distance as distance
import requests
import json


class Team:

    def __init__(self, key, number, name, rookie_year, postal_code, state, points, rank, district_code):
        self.key = key #blue alliance team key
        self.number = int(number) #team number
        self.name = name #team name
        self.rookie_year = int(rookie_year) #rookie year of team
        self.postal_code = postal_code #team zip as in blue allaince

        self.points = points #district points for a team in a year
        self.rank = rank #teams district rank for a year

        self.state = state #state the team is in
        self.year = district_code[0:4] #year of the data
        self.district_code = district_code #the district code
        invalid_zips = { #zip codes for teams who had an invalid zip in blue alliance
            '1731': '20186', '1817': '79406', '2640': '27320', '2910': '98012', '3331': '27516',
                        '3737': '27534', '3767': '49686', '3997': '78230', '4970': '49896', '5070': '77045',
                        '5212': '76201', '5214': '48080',
                        '5468': '97702', '5748': '98532', '5962': '01854', '6003': '27546', '6139': '31021',
                        '6248': '27615', '6312': '23092',
                        '6547': '77355', '7511': '76701', '7760': '06259', '7771': '08701', '7801': '07652',
                        '7821': '49451', '7857': '48237',
                        '7860': '48310', '7862': '48503', '7863': '48212', '7912': '48375', '896': '07103',
                        '6313': '23092', '3886': '49686', '6465': '76701'
                        }
        if str(number) in invalid_zips:
            #makes sure the zip code is valid
            postal_code = invalid_zips.get(str(number))
        search = uszip.SearchEngine()
        zipcode = search.by_zipcode(postal_code)
        zipcode.zipcode
        self.pop_density = zipcode.population_density #population density of the teams zip code
        self.income = zipcode.median_household_income #median income in the teams zip code
        self.team_add = (zipcode.lat, zipcode.lng) # the teams coridiants
        #creates a dictorary for the events a team partipates in during a year
        url = "https://www.thebluealliance.com/api/v3/team/" + key + "/events/" + self.year
        header = {
            "X-TBA-Auth-Key": 'bDf8f29vaRS5Q5Zecj9ZRadHcZZz1c2l7rwgMIiXZfcIWMlMQYWbcTtqiJPQDWRh'
        }
        response = requests.request("GET", url, headers=header)
        team_events = json.loads(response.text)
        # creates a dictorary for the event keys in a district during a year
        url = "https://www.thebluealliance.com/api/v3/district/" + district_code + "/events/keys"
        header = {
            "X-TBA-Auth-Key": 'bDf8f29vaRS5Q5Zecj9ZRadHcZZz1c2l7rwgMIiXZfcIWMlMQYWbcTtqiJPQDWRh'
        }
        response = requests.request("GET", url, headers=header)
        district_events = json.loads(response.text)  # events in the district this year
        event_data = []  # 2d array of the long, lat, start, and end date of events

        for event in team_events:
            if (str(self.year) + event['event_code']) in district_events:
                #creates list of start and end dates of competions
                event_data.append([event['lat'], event['lng'], event['start_date'], event['end_date']])
        self.event_data = event_data
        self.distances = [] #list of distances a team travels to events
        for item in event_data:
            event_cor = (item[0], item[1]) #cordinates for an event
            self.distances.append(distance.distance(self.team_add, event_cor).miles)


        self.total_distance = self.total_distance() #total distance a team travels in a season
        self.average_distance = self.average_distance() #average distance a team travels to a competion in a season


        #self.q_distance = self.q_distance()
        #self.q_av = self.q_av()

    def __str__(self):
        team = self.key + ' ' + str(self.number) + ' ' + self.name + ' ' + str(self.rookie_year) + ' ' + str(
            self.postal_code) + ' ' + str(self.points) + ' ' + str(self.rank) + ' ' + str(self.pop_density) + ' ' + str(
            self.income) + ' ' + str(self.income) + ' ' + self.state
        return team

    def total_distance(self):
        '''returns a sum of the distance a team travels to each event'''
        t_distance = 0
        distances = self.distances
        for item in distances:
            t_distance += item
        return t_distance

    def average_distance(self):
        '''returns an average of the distance a team travels to each event'''
        total = self.total_distance
        num = len(self.distances)
        if num != 0:
            return total / num
        else:
            return float(0)

    def q_distance(self):
        '''returns a sum of the distance a team travels to each qual event'''
        q_distance = 0
        distances = self.distances
        i = 0
        if len(self.distances) > 1:
            for item in distances:
                if i < 2:
                    q_distance += item
                    i += 1
        return q_distance

    def q_av(self):
        '''returns an average of the distance a team travels to each event'''
        return self.q_distance()/2

    def to_dict(self):
        return {
            'key': self.key,
            'number': self.number,
            'name': self.name,
            'district_code': self.district_code,
            'rookie_year': self.rookie_year,
            'state': self.state,
            'year': self.year,
            'postal_code': self.postal_code,
            'pop_density': self.pop_density,
            'income': self.income,
            'team_cord': self.team_add,
            'event_date': self.event_data,
            'distances': self.distances,
            'total_distance': self.total_distance,
            'av_distance': self.average_distance,
            #'q_distance': self.q_distance,
            #'q_av': self.q_av,
            'points': self.points,
            'rank': self.rank,
        }
