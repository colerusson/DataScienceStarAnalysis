import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('star_stats.csv')

# create box plots for each star type and its temperature
# create a figure with 1 row and 1 column
fig, ax = plt.subplots(1, 1)
# create a box plot of the temperature data for each star type
ax.boxplot([data[data['star_type'] == 'Brown Dwarf']['temperature'], data[data['star_type'] == 'Red Dwarf']['temperature'], data[data['star_type'] == 'White Dwarf']['temperature'], data[data['star_type'] == 'Main Sequence']['temperature'], data[data['star_type'] == 'Super Giant']['temperature'], data[data['star_type'] == 'Hyper Giant']['temperature']])
# add axis labels
ax.set_xlabel('Star Type')
ax.set_ylabel('Temperature')
# add a title
ax.set_title('Temperature by Star Type')
# add x tick labels
ax.set_xticklabels(['BD', 'RD', 'WD', 'Main Sequence', 'SuperG', 'HyperG'])
# show the plot
plt.show()
