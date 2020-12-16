'''Graphs either year, district, all districts in a year, or all years based on parameters.
The graph will choose x-axis options (  income, distance from competition, travel cost, population density, etc.)and y-axis(district points, district rank, income, distance from competition, travel cost) options
'''

'''imports'''
import team
import matplotlib.pyplot as plt
def chart_year(year):
    "year is age of the district"
    for team in year:
        plt.plot(team.get_income(), team.get_points(),'bo')
    plt.show()

