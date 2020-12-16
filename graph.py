'''Graphs either year, district, all districts in a year, or all years based on parameters.
The graph will choose x-axis options (  income, distance from competition, travel cost, population density, etc.)and y-axis(district points, district rank, income, distance from competition, travel cost) options
'''

'''imports'''
import team
"""import matplotlib.pyplot as plt
def income_points_chart(district):
    '''creates plot of income verse district points'''
    color = 0
    rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    for year in district:
        for team in year:
            x = team[0]
            y = team[1]
            plt.scatter(x, y, c=rainbow[color], label=year)
        color += 1
    plt.legend()
    plt.grid(True)
    plt.show()

#income_points_chart(chespeake)"""