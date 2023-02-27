import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('star_stats.csv')

# create a log-log scatter plot of the data with x as temperature and y as luminosity and color the points by their
# star type loop through the values of star_type and assign a color to each type
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
for i, star_type in enumerate(data['star_type'].unique()):
    plt.scatter(data[data['star_type'] == star_type]['absolute_magnitude'], data[data['star_type'] == star_type]['radius'], c=colors[i], label=star_type)
# add a legend
plt.legend()
# add axis labels
plt.xlabel('Absolute Magnitude')
plt.ylabel('Radius')
# add a title
plt.title('Absolute Magnitude vs. Radius')
# add a log scale to both axes
# plt.xscale('log')
plt.yscale('log')
# show the plot
plt.show()

# calculate the r^2 value for the correlation between temperature and luminosity
r_squared = np.corrcoef(data['radius'], data['luminosity'])[0, 1] ** 2
# print('r^2:', r_squared)

# calculate the r value for the correlation between radius and temperature
r = np.corrcoef(data['absolute_magnitude'], data['temperature'])[0, 1]
# print('r:', r)
