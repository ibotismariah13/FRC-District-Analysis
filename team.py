'''team object and its attribute's'''
import uszipcode as uszip  # zipcode data https://uszipcode.readthedocs.io/01-Tutorial/index.html
class Team:

    def __init__(self, key, number, name, rookie_year, postal_code, points, rank):
        self.key = key
        self.number = int(number)
        self.name = name
        self.rookie_year = int(rookie_year)
        self.postal_code = int(postal_code)
        self.points = int(points)
        self.rank = int(rank)
        search = uszip.SearchEngine()
        zipcode = search.by_zipcode(postal_code)
        zipcode.zipcode
        self.pop_density = int(zipcode.population_density)
        self.income = int(zipcode.median_household_income)


    def __str__(self):
        return self.key + ' ' + self.number + ' '+self.name + ' ' + self.rookie_year + ' '+ self.postal_code + ' ' + self.points + ' '+ self.rank+ ' ' + self.pop_density + ' '+ self.income
