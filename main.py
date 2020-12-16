'''Proccesses teams creats districts'''
import graph
from team import Team
import requests  # abblity to request api
import json
def get_district_data(district_code):
    '''creates a dictorary for the given district year and returns a list'''
    url = "https://www.thebluealliance.com/api/v3/district/" + district_code + "/teams"
    header = {
        "X-TBA-Auth-Key": 'bDf8f29vaRS5Q5Zecj9ZRadHcZZz1c2l7rwgMIiXZfcIWMlMQYWbcTtqiJPQDWRh'
    }
    response = requests.request("GET", url, headers=header)
    # print(response.text)
    teams = json.loads(response.text)
    url = "https://www.thebluealliance.com/api/v3/district/" + district_code + "/rankings"
    response = requests.request("GET", url, headers=header)
    rankings = json.loads(response.text)

    for element in teams:
        '''delete unesseary info'''
        del element['name']
        del element["school_name"]
        del element["gmaps_place_id"]
        del element["gmaps_url"]
        del element["country"]
        del element['lat']
        del element["lng"]
        del element["location_name"]
        del element["website"]
        del element["motto"]
        del element["address"]
        del element["home_championship"]
        for rank in rankings:
            if element['key'] == rank['team_key']:
                element['points'] = int(rank['point_total'])
                element['rank'] = int(rank['rank'])
    return teams
def createYear(district_code):
    teams=get_district_data(district_code)
    year=[]
    for element in teams:
       if element.get('points') != None:
            year.append(Team(element['key'], element['team_number'], element['nickname'],element['rookie_year'], element['postal_code'],
                             element.get('points'), element.get('rank')))
    return year
def create_district(district_codes):
    district=[]
    for year in district_codes:
        district.append(createYear(year))
    return district
chs = ['2016chs' , '2017chs', '2018chs','2019chs']
chesapeake = create_district(chs)
graph.chart_year(chesapeake[0])