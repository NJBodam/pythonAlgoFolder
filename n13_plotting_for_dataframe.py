import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

values = np.array([1, 3, 2, 4, 1, 6, 4])
example_df = pd.DataFrame({
    'value': values,
    'even': values % 2 == 0,
    'above_three': values > 3 
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# Change False to True for this block of code to see what it does
print(example_df)

# value   even      above_three
# a      1  False        False
# b      3  False        False
# c      2   True        False
# d      4   True         True
# e      1  False        False
# f      6   True         True
# g      4   True         True


# groupby() without as_index
if False:
    first_even = example_df.groupby('even').first() 
    print first_even
    print first_even['even'] # Causes an error. 'even' is no longer a column in the DataFrame

# Out[5]:
#        value  above_three         # Returns the first False and True values for 'even      
# even
# False      1        False
# True       2        False
# ---------------------------------------------------------------------------


# groupby() with as_index=False
if False:
    first_even = example_df.groupby('even', as_index=False).first()
    print first_even
    print first_even['even'] # Now 'even' is still a column in the DataFrame

# Out[6]:
#       even  value  above_three
# 0    False      1        False
# 1     True      2        False

# 0    False
# 1     True
filename = '/datasets/ud170/subway/nyc_subway_weather.csv'
subway_df = pd.read_csv(filename)

## Make a plot of your choice here showing something interesting about the subway data.
## Matplotlib documentation here: http://matplotlib.org/api/pyplot_api.html
## Once you've got something you're happy with, share it on the forums!

plt.figure()
data_by_location = subway_df.groupby(['latitude', 'longitude'], as_index=False).mean()
scaled_entries = data_by_location['ENTRIESn_hourly'] / data_by_location['ENTRIESn_hourly'].std()
plt.scatter(data_by_location['latitude'], data_by_location['longitude'], s=scaled_entries)
# To convert the x axis to log values, you can use
#   plt.xscale('log')
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.show()

plt.figure()
data_by_weekday = subway_df.groupby('day_week').mean()['ENTRIESn_hourly']
plt.plot(data_by_weekday)
plt.xlabel('Day of the week')
plt.ylabel('Average ridership')
# We can also add the yticks function to put the y axis in perspective, make it start from zero
plt.yticks([0, 10000, 20000, 30000, 40000, 50000, 60000, 70000])
# We can also change the label displayed on the Y axis using same yticks function
plt.yticks([0, 10000, 20000, 30000, 40000, 50000, 60000, 70000], ['0', '10k', '20k', '30k', '40k', '50k', '60k', '70k'])
plt.show()

plt.figure()
data_by_weather = subway_df.groupby('conds').mean()['ENTRIESn_hourly']
plt.plot(data_by_weather)
plt.xlabel('Weather')
plt.ylabel('Average ridership')
plt.show()

plt.figure()
data_by_hour = subway_df.groupby('hour').mean()['ENTRIESn_hourly']
plt.plot(data_by_hour)
plt.xlabel('Hour')
plt.ylabel('Average ridership')
plt.show()

plt.figure()
data_by_station = subway_df.groupby('station').mean()['ENTRIESn_hourly']
plt.hist(data_by_station)
plt.xlabel('Station')
plt.ylabel('Average ridership')
plt.show()

plt.figure()
