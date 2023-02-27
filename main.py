import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('star_stats.csv')
# create a log-log scatter plot of the data with x as temperature and y as luminosity and color the points by their
# star type loop through the values of star_type and assign a color to each type
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
for i, star_type in enumerate(data['star_type'].unique()):
    plt.scatter(data[data['star_type'] == star_type]['temperature'], data[data['star_type'] == star_type]['luminosity'], c=colors[i], label=star_type)
# add a legend
plt.legend()
# add axis labels
plt.xlabel('Temperature (K)')
plt.ylabel('Luminosity (L$_\odot$)')
# add a title
plt.title('Star Luminosity vs. Temperature')
# add a log scale to both axes
plt.xscale('log')
plt.yscale('log')
# show the plot
plt.show()
