import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('star_stats.csv')

# calculate the 5 number summary for the M spectral type stars
m_spectral_type = data[data['spectral_class'] == 'M']
m_spectral_type_five_number_summary = m_spectral_type['temperature'].describe()
# print(m_spectral_type_five_number_summary)
# create a box plot of the radius for the M spectral type stars
plt.boxplot(m_spectral_type['temperature'], vert=False)
# add axis labels
plt.xlabel('M Spectral Class')
plt.ylabel('Temperature')
# add a title
plt.title('Temperature for M Spectral Class Stars')
# show the plot
#plt.show()

# calculate which spectral class has the largest absolute magnitude
largest_absolute_magnitude = data['absolute_magnitude'].max()
largest_absolute_magnitude_spectral_class = data[data['absolute_magnitude'] == largest_absolute_magnitude]['spectral_class'].values[0]
print('Largest Absolute Magnitude:', largest_absolute_magnitude)
print('Largest Absolute Magnitude Spectral Class:', largest_absolute_magnitude_spectral_class)
