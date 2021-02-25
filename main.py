'''Proccesses teams creats districts'''
import json

import requests  # abblity to request api

import graph
from team import Team
import csv
import pandas as pd
from datetime import datetime, timedelta
import header

def get_district_data(district_code):
    '''creates a dictorary of teams for the given  district year and returns a list'''
    # creates a dictorary for the teams in a district during a year
    url = "https://www.thebluealliance.com/api/v3/district/" + district_code + "/teams"
    header = header.key
    response = requests.request("GET", url, headers=header)
    teams = json.loads(response.text)
      # creates a dictorary of teams rankings and points in a district during a year
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
    '''creates a list of team objects in a year'''
    teams = get_district_data(district_code)
    year = []
    for element in teams:
        if element.get('state_prov') in states:
            year.append(Team(element['key'], element['team_number'], element['nickname'], element['rookie_year'],
                                 element['postal_code'], element['state_prov'],
                                 element.get('points'), element.get('rank'), district_code))

    return year


def createYearSheetPandas(district_code, states):
    '''creates a csv for a year in a district'''
    year = createYear(district_code, states)
    df = pandas.DataFrame([team.__dict__ for team in year])
    df.to_csv(district_code + '.csv', encoding='utf-8-sig', index=False)

def create_district(district_codes,states):
    '''creates a list of team objects in a district for a year'''
    district = []
    for year in district_codes:
        district.append(createYear(year,states))
    return district

def create_district_sheets(district_codes,states):
    '''creates a csv for each year in a district'''
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

'dicts of years and district codes'
chesapeake = {
    2016:chs[0],
    2017: chs[1],
    2018: chs[2],
    2019: chs[3]
    }
indiana = {
    2015: fin[0],
    2016:fin[1],
    2017: fin[3],
    2018:fin[3],
    2019:fin[4]
    }
michigan ={
    2015: fim[0],
    2016:fim[1],
    2017: fim[3],
    2018:fim[3],
    2019:fim[4]
}
mid_alantic = {
    2015: fma[0],
    2016: fma[1],
    2017: fma[3],
    2018: fma[3],
    2019: fma[4]
}
new_england={
    2015: nef[0],
    2016:nef[1],
    2017: nef[3],
    2018:nef[3],
    2019:nef[4]
}
north_carolina = {
    2016:fnc[0],
    2017: fnc[1],
    2018:fnc[2],
    2019:fnc[3]
}
pacific_north_west={
    2015: pnw[0],
    2016: pnw[1],
    2017: pnw[3],
    2018: pnw[3],
    2019: pnw[4]
}
peach_tree={
    2016:pch[0],
    2017: pch[1],
    2018:pch[2],
    2019:pch[3]
}
texas = {
    2019:fit[0]
}
'''List of states in each district for data validation'''
chs_states = ['Maryland', 'Virginia', 'Washington, District Of Columbia'] #chesepeake 2016-2020
fim_states = [ 'Michigan'] #michigan 2010-2020
fit_states = ['Texas', 'New Mexico'] #first in texas 2019-2020
fin_states = [ 'Indiana'] #first indiana robotics 2015-2020
fma_states =['New Jersey', 'Pennsylvania', 'Delaware'] #first mid Atlantic 2012-2020
fnc_states=['North Carolina'] #first north carolina 2016-2020
nef_states=['Massachusetts', 'Maine', 'Vermont', 'Rhode Island', 'New Hampshire', 'Connecticut'] #new england first 2014-2020
pnw_states = ['Alaska', 'Washington','Oregon'] #pacific north west'2014-2020
pch_states =['Georgia'] #peachtree 2016-2020

'''creates sheets for each district'''
'''create_district_sheets(fit,fit_states)
create_district_sheets(fin, fin_states)
create_district_sheets(fnc,fnc_states)
create_district_sheets(pch,pch_states)
create_district_sheets(chs,chs_states)
create_district_sheets(fma,fma_states)
create_district_sheets(pnw,pnw_states)
create_district_sheets(nef,nef_states)
create_district_sheets(fim,fim_states)'''

'''charts districts'''
#graph.chart_district(chesapeake,'income','points')
#graph.chart_district(mich,'income','points')
#graph.chart_district(ind,'income','points')
#graph.chart_district(peach,'income','points')
#graph.chart_district(ind,'av_miles','points')
#graph.chart_district(mich,'av_miles','points')
#graph.chart_district(chesapeake,'qual_av','points')
#graph.plot_file('2016chs', 'income', 'points')

#graph.chart_district(fim, 'income', 'points')

#graph.chart_year(fin2019, 'average_distance','points')

#graph.chart_district(nef, 'income','average_distance')
#graph.chart_district(fin, 'average_distance','income')
#graph.chart_district(fit, 'average_distance','income')
#graph.chart_district(fim, 'average_distance','income')

def travel_cost(district):

    MILE=0.58 #us milage
    HOTEL=1040 #average mid grade hotel cost for 30 people per night
    for year in district:
        with open(year+'.csv') as csvfile:
            file = csv.reader(csvfile, delimiter=',' )
            next(file)
            for team in file:
                if(team[15]!='0.0'):

                    #print(team)
                    i=0
                    tc = 0
                    edistances=team[14].split(', ')
                    distances =[]

                    for item in edistances:
                        item=item.strip("[ ]")
                        item=float(item)
                        distances.append(item)
                    print(distances)
                    fevents=(team[13]).split('')
                    print(fevents)
                    events=[]
                    dayL=[]

                    for event in fevents:
                        day1 = (event[2].strip(" ]'")).split('-')
                        day2 = (event[3].strip(" ]'")).split('-')
                        day1 = datetime(int(day1[0]), int(day1[1]), int(day1[2]))
                        day2 = datetime(int(day2[0]), int(day2[1]), int(day2[2]))
                        days = (day2 - day1).days  # lenght of events
                        print(event)
                        dayL.append(days)

                    evnum=len(dayL)
                    print(dayL)
                    print(evnum)
                    if evnum == 1:
                       events.append([dayL[0],distances[0]])
                    elif evnum == 2:
                        events.append([dayL[0], distances[0]])
                        events.append([dayL[1], distances[1]])
                    elif evnum >= 3:
                        events.append([dayL[0], distances[0]])
                        events.append([dayL[1], distances[1]])
                        events.append([dayL[2], distances[2]])



                    print(events)
                    for event in events:

                       if events[1] <= 50.0:
                           hotel=0
                           print('hotel  ',hotel)
                           miles=2*MILE*days
                           print('miles  ', hotel)
                       elif events[1]<50.0:
                           hotel = (days-1)*HOTEL
                           print('hotel  ', hotel)
                           miles=   2*events[1]+ 2*10*(days-1)
                           print('miles  ', hotel)
                       tc=tc+miles+hotel
                       print('tc' , tc)
                       i+=1


#travel_cost(chs)
graph.chart_district(chs,'income','average_distance')






