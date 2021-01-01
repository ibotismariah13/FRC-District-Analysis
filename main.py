'''Proccesses teams creats districts'''
import json

import requests  # abblity to request api

import graph
from team import Team
import csv
import pandas


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
        for rank in rankings:
            if element['key'] == rank['team_key']:
                element['points'] = int(rank['point_total'])
                element['rank'] = int(rank['rank'])

    return teams


def createYear(district_code, states):
    teams = get_district_data(district_code)
    year = []
    for element in teams:
        if element.get('state_prov') in states:
            year.append(Team(element['key'], element['team_number'], element['nickname'], element['rookie_year'],
                                 element['postal_code'], element['state_prov'],
                                 element.get('points'), element.get('rank'), district_code))

    return year


def createYearSheetPandas(district_code, states):
    year = createYear(district_code, states)
    df = pandas.DataFrame([team.__dict__ for team in year])
    df.to_csv(district_code + '.csv', encoding='utf-8-sig', index=False)

def create_district(district_codes,states):
    district = []
    for year in district_codes:
        district.append(createYear(year,states))
    return district

def create_district_sheets(district_codes,states):
    district = []
    for year in district_codes:
        district.append(createYearSheetPandas(year,states))
    return district
'''District years'''
chs = ['2016chs', '2017chs','2018chs', '2019chs'] #chesepeake 2016-2020
fim = ['2015fim','2016fim', '2017fim','2018fim', '2019fim'] #michigan 2010-2020
fit = ['2019tx'] #first in texas 2019-2020
fin = ['2015in', '2016in', '2017in','2018in', '2019in'] #first indiana robotics 2015-2020
fma =['2015mar', '2016mar', '2017mar','2018mar', '2019fma'] #first mid Atlantic 2012-2020
fnc=['2016nc', '2017nc','2018nc', '2019fnc'] #first north carolina 2016-2020
nef=['2015ne', '2016ne', '2017ne','2018ne', '2019ne'] #new england first 2014-2020
pnw = ['2015pnw', '2016pnw', '2017pnw','2018pnw', '2019pnw'] #pacific north west'2014-2020
pch =['2016pch', '2017pch','2018pch', '2019pch'] #peachtree 2016-2020

chs_states = ['Maryland', 'Virginia', 'Washington, District Of Columbia'] #chesepeake 2016-2020
fim_states = [ 'Michigan'] #michigan 2010-2020
fit_states = ['Texas', 'New Mexico'] #first in texas 2019-2020
fin_states = [ 'Indiana'] #first indiana robotics 2015-2020
fma_states =['New Jersey', 'Pennsylvania', 'Delaware'] #first mid Atlantic 2012-2020
fnc_states=['North Carolina'] #first north carolina 2016-2020
nef_states=['Massachusetts', 'Maine', 'Vermont', 'Rhode Island', 'New Hampshire', 'Connecticut'] #new england first 2014-2020
pnw_states = ['Alaska', 'Washington','Oregon'] #pacific north west'2014-2020
pch_states =['Georgia'] #peachtree 2016-2020


'''create_district_sheets(fit,fit_states)
create_district_sheets(fin, fin_states)
create_district_sheets(fnc,fnc_states)
create_district_sheets(pch,pch_states)
create_district_sheets(chs,chs_states)
create_district_sheets(fma,fma_states)
create_district_sheets(pnw,pnw_states)
create_district_sheets(nef,nef_states)
create_district_sheets(fim,fim_states)'''

#graph.chart_district(chesapeake,'income','points')
#graph.chart_district(mich,'income','points')
#graph.chart_district(ind,'income','points')
#graph.chart_district(peach,'income','points')
#graph.chart_district(ind,'av_miles','points')
#graph.chart_district(mich,'av_miles','points')
#graph.chart_district(chesapeake,'qual_av','points')






