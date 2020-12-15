'''Importing the classes and api needed'''
import pip
import requests  # abblity to request api
import uszipcode as uszip  # zipcode data https://uszipcode.readthedocs.io/01-Tutorial/index.html
import pandas
import matplotlib.pyplot as plt
import numpy as np  # numpy
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
        search = uszip.SearchEngine()
        zipcode = search.by_zipcode((element['postal_code']))
        zipcode.zipcode
        element['pop_density'] = zipcode.population_density
        element['income'] = zipcode.median_household_income
        for rank in rankings:
            if element['key'] == rank['team_key']:
                element['points'] = int(rank['point_total'])
                element['rank'] = int(rank['rank'])
    return teams


'''Chs data lists'''
chs2016 = get_district_data('2016chs')
chs2017 = get_district_data('2017chs')
chs2018 = get_district_data('2016chs')
chs2019 = get_district_data('2017chs')
#chs = {2016:chs2017, 2017:chs2017, 2018:chs2018, 2019:chs2019}
chs =[chs2016,chs2017,chs2018,chs2019]

def income_points_chart(district):
    '''creates plot of income verse district points'''
    color = 0
    rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    for year in district:
        for team in year:
            x = int(team['income'])
            y = team['rank']
            plt.scatter(x, y, c=rainbow[color], label=year)
        color += 1
    plt.legend()
    plt.grid(True)
    plt.show()


income_points_chart(chs)
#print(chs)

