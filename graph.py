'''Graphs either year, district, all districts in a year, or all years based on parameters.
The graph will choose x-axis options (  income, distance from competition, travel cost, population density, etc.)and y-axis(district points, district rank, income, distance from competition, travel cost) options
'''

'''imports'''
import team
import matplotlib.pyplot as plt
def chart(year, x, y,color):
    "year is age of the district"
    for team in year:
        if x == "income" and y=='points':
            if team.get_points() and team.get_income()is not None:
                xv=team.get_income()
                yv=team.get_points()
                plt.scatter(xv, yv, c=color, alpha = 0.5)
def chart_year(year, x, y,color):
    chart(year,x,y,color)
    plt.show()

def chart_district(district, x,y):
    colors = ['red','orange','green','blue','purple']
    i=0
    for year in district:
        chart(year, x,y, colors[i])
        i += 1
    plt.show

