'''Proccesses teams creats districts'''
import graph
from team import Team
import requests  # abblity to request api
import json
def createYear(district_code):
    '''creates a list of teams for the given year and district'''
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
    year=[]

    for t in teams:
        for rank in rankings:
            if ['key'] == rank['team_key']:
                t['points'] = int(rank['point_total'])
                t['rank'] = int(rank['rank'])
                break
        year.append(Team(t['key'],t['number'],t['nickname'],t['rookie_year'],t['postal_code'],t['points'],t['rank']))
    return year
chs2016 = createYear('2016chs')
print(chs2016)