'''team object and its attribute's'''
import uszipcode as uszip  # zipcode data https://uszipcode.readthedocs.io/01-Tutorial/index.html
class Team:

    def __init__(self, key, number, name, rookie_year, postal_code, points, rank):
        self.key = key
        self.number = int(number)
        self.name = name
        self.rookie_year = int(rookie_year)
        self.postal_code = postal_code
        self.points = points
        if points is None:
            self.points = 0
        self.rank = rank
        if rank is None:
            self.rank = 0

        search= uszip.SearchEngine()
        zipcode = search.by_zipcode(postal_code)
        zipcode.zipcode
        self.pop_density = zipcode.population_density
        self.income = zipcode.median_household_income



    def __str__(self):
        return self.key + ' ' + str(self.number) + ' '+self.name + ' ' + str(self.rookie_year) + ' '+ str(self.postal_code) + ' ' + str(self.points) + ' '+ str(self.rank)+ ' ' + str(self.pop_density) + ' '+ str(self.income)
    def get_points(self):
        return self.points
    def get_income(self):
        return self.income