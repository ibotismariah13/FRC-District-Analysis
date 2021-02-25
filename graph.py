'''Graphs either year, district, all districts in a year, or all years based on parameters.
The graph will choose x-axis options (  income, distance from competition, travel cost, population density, etc.)and y-axis(district points, district rank, income, distance from competition, travel cost) options
'''

'''imports'''



import pandas as pd
import matplotlib.pyplot as plt


def plot_file(file, x, y,color):
    '''uses pandas and the colum names to make a scatter plot of the csv file annd given color'''
    msft = pd.read_csv(file +'.csv')
    t=file+' '+ x + ' vs. ' + y
    '''  if x == 'income':
        x=msft.income
      if y== 'points':
        y=msft.points
    plt.scatter(x, y,c=color, alpha = 0.5 )'''
    msft.plot.scatter( x, y,c=color, alpha = 0.5, title =t,subplots=False)

def chart_district(district, x,y):
    '''given a csv name and an x and y colum plots values for each year in a district'''
    colors = ['red', 'orange', 'green', 'blue', 'purple']
    i = 0
    for year in district:
        plot_file(year, x, y, colors[i])
        i += 1
