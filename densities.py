import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv('star_stats.csv')

# create a density plot of the data with x as temperature and y as the density of the temperature values
plt.hist(data['absolute_magnitude'], density=True)
# add axis labels
plt.xlabel('Absolute Magnitude')
plt.ylabel('Density')
# add a title
plt.title('Absolute Magnitude Density Plot')
# show the plot
plt.show()

# calculate the mean temperature across all star types
mean = np.mean(data['absolute_magnitude'])
print('Mean:', mean)

# calculate the variance of radius across all star types
variance = np.var(data['absolute_magnitude'])
print('Variance:', variance)
