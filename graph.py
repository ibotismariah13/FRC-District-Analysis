'''Graphs either year, district, all districts in a year, or all years based on parameters.
The graph will choose x-axis options (  income, distance from competition, travel cost, population density, etc.)and y-axis(district points, district rank, income, distance from competition, travel cost) options
'''

'''imports'''
import team
import matplotlib.pyplot as plt
def chart(year, x, y,color):
    "year is age of the district"
    if x == "income" and y=='points':
        for team in year:
            if team.points and team.income is not None:
                xv=team.income
                yv=team.points
                plt.scatter(xv, yv, c=color, alpha = 0.5)
    elif x== "income" and y== "total_miles":
        for team in year:
            if team.income and team.total_distance is not None:
                xv = team.income
                yv = team.total_distance
                plt.scatter(xv, yv, c=color, alpha=0.5)
    elif x== 'total_miles' and y=='points':
       for team in year:
            if team.points and team.total_distance is not None:
                xv = team.total_distance
                yv = team.points
                plt.scatter(xv, yv, c=color, alpha=0.5)
    elif x == 'av_miles' and y == 'points':
        for team in year:
            if team.points and team.average_distance is not None:
                xv = team.average_distance
                yv = team.points
                plt.scatter(xv, yv, c=color, alpha=0.5)

    elif x == 'qual_av' and y == 'points':
        for team in year:
            #if team.points and team.average_distance is not None:
            xv = team.qual_av()
            yv = team.points
            plt.scatter(xv, yv, c=color, alpha=0.5)
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

