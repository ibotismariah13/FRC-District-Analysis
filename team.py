'''team object and its attribute's'''
import uszipcode as uszip  # zipcode data https://uszipcode.readthedocs.io/01-Tutorial/index.html
from travel import Travel
class Team:

    def __init__(self, key, number, name, rookie_year, postal_code, state, points, rank, year):
        self.key = key
        self.number = int(number)
        self.name = name
        self.rookie_year = int(rookie_year)
        self.postal_code = postal_code
        self.points = points
        self.rank = rank
        self.state = state
        self.year =year
        travel = Travel(self.key, self.postal_code, self.year)
        self.average_distance = travel.average_distance()
        self.total_distance = travel.total_distance()

        search= uszip.SearchEngine()
        zipcode = search.by_zipcode(postal_code)
        zipcode.zipcode
        self.pop_density = zipcode.population_density
        self.income = zipcode.median_household_income



    def __str__(self):
            team= self.key + ' ' + str(self.number) + ' '+self.name + ' ' + str(self.rookie_year) +' ' + str(self.postal_code) + ' ' + str(self.points) + ' '+ str(self.rank)+ ' ' + str(self.pop_density) + ' '+ str(self.income) + ' '+ str(self.income) + ' '+ self.state
            return team

