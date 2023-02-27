import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('star_stats.csv')

# create plots to show the average luminosity for each star color
# create a figure with 1 row and 2 columns
fig, ax = plt.subplots(1, 2)
# create a bar plot of the average luminosity for each star color, only include stars with luminosity > 50
# create a list of booleans that are True if the luminosity is > 50
lum_bool = data['luminosity'] > 50
# create a new dataframe with only those stars
data = data[lum_bool]
# create the bar plot
ax[0].bar(data['star_color'].unique(), data.groupby('star_color')['luminosity'].mean())
# add axis labels
ax[0].set_xlabel('Star Color')
ax[0].set_ylabel('Average Luminosity')
# add a title
ax[0].set_title('Average Luminosity by Star Color')
# create a pie chart of the average luminosity for each star color, only include stars with luminosity > 50
# create a list of booleans that are True if the luminosity is > 50
lum_bool = data['luminosity'] > 50
# create a new dataframe with only those stars
data = data[lum_bool]
# create the pie chart
ax[1].pie(data.groupby('star_color')['luminosity'].mean(), labels=data['star_color'].unique(), autopct='%1.1f%%')
# add a title
ax[1].set_title('Average Luminosity by Star Color')
# show the plot
plt.show()
