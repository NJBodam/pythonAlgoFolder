# %%
data = [1, 2, 1, 3, 3, 1, 4, 2]

%matplotlib inline
import matplotlib.pyplot as plt
plt.hist(data)

# %%
y_values = [34, 44, 23, 46, 12, 24]
y_values.sort()

x_values = ['A', 'B', 'C', 'D', 'E', 'F']

# Plot a graph
plt.plot(x_values, y_values)

# Display the graph
plt.show()

# %%
y_values = [34, 44, 23, 46, 12, 24]
y_values.sort()

x_values = ['A', 'B', 'C', 'D', 'E', 'F']

# Plot a graph
plt.plot(x_values, y_values)

plt.xlabel("Letters")
plt.ylabel("Amount")
plt.title("Graphicalico")
# Display the graph
plt.show()

# %%
import seaborn as sns

sns.plot(x_values, y_values)
sns.show()


# %%
sns.set(style='whitegrid')
sns.lineplot(x=x_values, y=y_values)

plt.show()

# %%
 plt.hist(data, bins=20) 

# %%
 plt.hist(data, bins=40) 

# %%
import numpy as np

# First 20 countries with employment data
countries = np.array([
    'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
    'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina'
])

# Employment data in 2007 for those 20 countries
employment = np.array([
    55.70000076,  51.40000153,  50.5       ,  75.69999695,
    58.40000153,  40.09999847,  61.5       ,  57.09999847,
    60.90000153,  66.59999847,  60.40000153,  68.09999847,
    66.90000153,  53.40000153,  48.59999847,  56.79999924,
    71.59999847,  58.40000153,  70.40000153,  41.20000076
])

# Change False to True for each block of code to see what it does

# Accessing elements
if False:
    print(countries[0])
    print(countries[3])

# Slicing
if False:
    print(countries[0:3])
    print(countries[:3])
    print(countries[17:])
    print(countries[:])

# Element types
if False:
    print(countries.dtype)
    print(employment.dtype)
    print(np.array([0, 1, 2, 3]).dtype)
    print(np.array([1.0, 1.5, 2.0, 2.5]).dtype)
    print(np.array([True, False, True]).dtype)
    print(np.array(['AL', 'AK', 'AZ', 'AR', 'CA']).dtype)

# Looping
if False:
    for country in countries:
        print('Examining country {}'.format(country))

    for i in range(len(countries)):
        country = countries[i]
        country_employment = employment[i]
        print('Country {} has employment {}'.format(country),
                country_employment)

# Numpy functions
if False:
    print(employment.mean())
    print(employment.std())
    print(employment.max())
    print(employment.sum())

def max_employment(countries, employment):
    '''
    Fill in this function to return the name of the country
    with the highest employment in the given employment
    data, and the employment in that country.
    '''
    max_country = None      # Replace this with your code
    max_value = None   # Replace this with your code

    return (max_country, max_value)

# %%
import numpy as np

# First 20 countries with employment data
countries = np.array([
    'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
    'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina'
])

# Employment data in 2007 for those 20 countries
employment = np.array([
    55.70000076,  51.40000153,  50.5       ,  75.69999695,
    58.40000153,  40.09999847,  61.5       ,  57.09999847,
    60.90000153,  66.59999847,  60.40000153,  68.09999847,
    66.90000153,  53.40000153,  48.59999847,  56.79999924,
    71.59999847,  58.40000153,  70.40000153,  41.20000076
])

# Change False to True for each block of code to see what it does

# Accessing elements
if True:
    print(countries[0])
    print(countries[3])

# Slicing
if True:
    print(countries[0:3])
    print(countries[:3])
    print(countries[17:])
    print(countries[:])

# Element types
if True:
    print(countries.dtype)
    print(employment.dtype)
    print(np.array([0, 1, 2, 3]).dtype)
    print(np.array([1.0, 1.5, 2.0, 2.5]).dtype)
    print(np.array([True, False, True]).dtype)
    print(np.array(['AL', 'AK', 'AZ', 'AR', 'CA']).dtype)

# Looping
if True:
    for country in countries:
        print('Examining country {}'.format(country))

    for i in range(len(countries)):
        country = countries[i]
        country_employment = employment[i]
        print("Country {} has employment {}".format(country, country_employment))
        
# Numpy functions
if True:
    print(employment.mean())
    print(employment.std())
    print(employment.max())
    print(employment.sum())

def max_employment(countries, employment):
    '''
    Fill in this function to return the name of the country
    with the highest employment in the given employment
    data, and the employment in that country.
    '''
    
    max_value = employment.max()   # Replace this with your code
    index = np.where(employment == max_value)[0]
    max_country = countries[index][0]
    
    return (max_country, max_value)

print(max_employment(countries, employment))

# %%
import numpy as np

# First 20 countries with employment data
countries = np.array([
    'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
    'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina'
])

# Employment data in 2007 for those 20 countries
employment = np.array([
    55.70000076,  51.40000153,  50.5       ,  75.69999695,
    58.40000153,  40.09999847,  61.5       ,  57.09999847,
    60.90000153,  66.59999847,  60.40000153,  68.09999847,
    66.90000153,  53.40000153,  48.59999847,  56.79999924,
    71.59999847,  58.40000153,  70.40000153,  41.20000076
])

# Change this country name to change what country will be printed when you
# click "Test Run". Your function will be called to determine the standardized
# score for this country for each of the given 5 Gapminder variables in 2007.
# The possible country names are available in the Downloadables section.

country_name = 'Albania'

def standardize_data(values):
    '''
    Fill in this function to return a standardized version of the given values,
    which will be in a NumPy array. Each value should be translated into the
    number of standard deviations that value is away from the mean of the data.
    (A positive number indicates a value higher than the mean, and a negative
    number indicates a value lower than the mean.)
    '''
    mean = np.mean(values)
    sd = np.std(values)
    data = []
    for i in values:
        value = (i - mean)/ sd
        data.append(value)
    return np.array(data)
    
print(standardize_data(employment))

# %%
import numpy as np

# Change False to True for each block of code to see what it does

# Using index arrays
if True:
    a = np.array([1, 2, 3, 4])
    b = np.array([True, True, False, False])
    
    print(a[b])
    print(a[np.array([True, False, True, False])])
    
# Creating the index array using vectorized operations
if True:
    a = np.array([1, 2, 3, 2, 1])
    b = (a >= 2)
    
    print(a[b])
    print(a[a >= 2])
    
# Creating the index array using vectorized operations on another array
if True:
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([1, 2, 3, 2, 1])
    
    print(b == 2)
    print(a[b == 2])

def mean_time_for_paid_students(time_spent, days_to_cancel):
    '''
    Fill in this function to calculate the mean time spent in the classroom
    for students who stayed enrolled at least (greater than or equal to) 7 days.
    Unlike in Lesson 1, you can assume that days_to_cancel will contain only
    integers (there are no students who have not canceled yet).
    
    The arguments are NumPy arrays. time_spent contains the amount of time spent
    in the classroom for each student, and days_to_cancel contains the number
    of days until each student cancel. The data is given in the same order
    in both arrays.
    '''
    # returns boolean that fufils condition
    enrolled_1_week = (days_to_cancel > 6)
    bool_time_spent = time_spent[enrolled_1_week]
    
    print(np.mean(bool_time_spent))
    
    enroll = []
    
    for i in range(len(time_spent)):
        if days_to_cancel[i] > 6:
            enroll.append(time_spent[i])
    print(np.mean(np.array(enroll)))
    return None

# Time spent in the classroom in the first week for 20 students
time_spent = np.array([
       12.89697233,    0.        ,   64.55043217,    0.        ,
       24.2315615 ,   39.991625  ,    0.        ,    0.        ,
      147.20683783,    0.        ,    0.        ,    0.        ,
       45.18261617,  157.60454283,  133.2434615 ,   52.85000767,
        0.        ,   54.9204785 ,   26.78142417,    0.
])

# Days to cancel for 20 students
days_to_cancel = np.array([
      4,   5,  37,   3,  12,   4,  35,  38,   5,  37,   3,   3,  68,
     38,  98,   2, 249,   2, 127,  35
])

mean_time_for_paid_students(time_spent, days_to_cancel)


# %%
import pandas as pd

countries = ['Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
             'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan',
             'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
             'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia']

life_expectancy_values = [74.7,  75. ,  83.4,  57.6,  74.6,  75.4,  72.3,  81.5,  80.2,
                          70.3,  72.1,  76.4,  68.1,  75.2,  69.8,  79.4,  70.8,  62.7,
                          67.3,  70.6]

gdp_values = [ 1681.61390973,   2155.48523109,  21495.80508273,    562.98768478,
              13495.1274663 ,   9388.68852258,   1424.19056199,  24765.54890176,
              27036.48733192,   1945.63754911,  21721.61840978,  13373.21993972,
                483.97086804,   9783.98417323,   2253.46411147,  25034.66692293,
               3680.91642923,    366.04496652,   1175.92638695,   1132.21387981]

# Life expectancy and gdp data in 2007 for 20 countries
life_expectancy = pd.Series(life_expectancy_values)
gdp = pd.Series(gdp_values)

# Change False to True for each block of code to see what it does

# Accessing elements and slicing
if True:
    print(life_expectancy[0])
    print(gdp[3:6])
    
# Looping
if True:
    for country_life_expectancy in life_expectancy:
        print('Examining life expectancy {}'.format(country_life_expectancy))
        
# Pandas functions
if True:
    print(life_expectancy.mean())
    print(life_expectancy.std())
    print(gdp.max())
    print(gdp.sum())

# Vectorized operations and index arrays
if True:
    a = pd.Series([1, 2, 3, 4])
    b = pd.Series([1, 2, 1, 2])
  
    print(a + b)
    print(a * 2)
    print(a >= 3)
    print(a[a >= 3])
   
def variable_correlation(variable1, variable2):
    '''
    Fill in this function to calculate the number of data points for which
    the directions of variable1 and variable2 relative to the mean are the
    same, and the number of data points for which they are different.
    Direction here means whether each value is above or below its mean.
    
    You can classify cases where the value is equal to the mean for one or
    both variables however you like.
    
    Each argument will be a Pandas series.
    
    For example, if the inputs were pd.Series([1, 2, 3, 4]) and
    pd.Series([4, 5, 6, 7]), then the output would be (4, 0).
    This is because 1 and 4 are both below their means, 2 and 5 are both
    below, 3 and 6 are both above, and 4 and 7 are both above.
    
    On the other hand, if the inputs were pd.Series([1, 2, 3, 4]) and
    pd.Series([7, 6, 5, 4]), then the output would be (0, 4).
    This is because 1 is below its mean but 7 is above its mean, and
    so on.
    '''
    num_same_direction = None        # Replace this with your code
    num_different_direction = None   # Replace this with your code
    
    mean_v1 = variable1.mean()
    mean_v2 = variable2.mean()
    
    a = variable1 > mean_v1
    b = variable2 > mean_v2
    c = a == b
    
    num_same_direction = len(c[c == True])
    num_different_direction = len(c[c == False])
    
    return (num_same_direction, num_different_direction)

a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 1, 2])
variable_correlation(a, b)


# %%
import pandas as pd

# Change False to True for each block of code to see what it does

# Addition when indexes are the same
if True:
    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
    print(s1 + s2)

# Indexes have same elements in a different order
if True:
    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([10, 20, 30, 40], index=['b', 'd', 'a', 'c'])
    print(s1 + s2)

# Indexes overlap, but do not have exactly the same elements
if True:
    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([10, 20, 30, 40], index=['c', 'd', 'e', 'f'])
    print(s1 + s2)

# Indexes do not overlap
if True:
    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([10, 20, 30, 40], index=['e', 'f', 'g', 'h'])
    print(s1 + s2)

# %%
import pandas as pd

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([10, 20, 30, 40], index=['c', 'd', 'e', 'f'])

# Try to write code that will add the 2 previous series together,
# but treating missing values from either series as 0. The result
# when printed out should be similar to the following line:
# print pd.Series([1, 2, 13, 24, 30, 40], index=['a', 'b', 'c', 'd', 'e', 'f'])
s1.fillna(0)
s2.fillna(0)

print(s1 + s2)


# %%


# %%
import pandas as pd

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([10, 20, 30, 40], index=['c', 'd', 'e', 'f'])

# Try to write code that will add the 2 previous series together,
# but treating missing values from either series as 0. The result
# when printed out should be similar to the following line:
# print pd.Series([1, 2, 13, 24, 30, 40], index=['a', 'b', 'c', 'd', 'e', 'f'])


print((s1 + s2).fillna(0))

# %%
import pandas as pd
import seaborn as sns


# The following code reads all the Gapminder data into Pandas DataFrames. You'll
# learn about DataFrames next lesson.

path = '/Users/mac/Documents/pythonLearning/pythonAlgo/Data Spreadsheet/'
employment = pd.read_csv(path + 'employment_above_15.csv', index_col='Country')
female_completion = pd.read_csv(path + 'female_completion_rate.csv', index_col='Country')
male_completion = pd.read_csv(path + 'male_completion_rate.csv', index_col='Country')
life_expectancy = pd.read_csv(path + 'life_expectancy.csv', index_col='Country')
gdp = pd.read_csv(path + 'gdp_per_capita.csv', index_col='Country')

# The following code creates a Pandas Series for each variable for the United States.
# You can change the string 'United States' to a country of your choice.

employment_us = employment.loc['United States']
female_completion_us = female_completion.loc['United States']
male_completion_us = male_completion.loc['United States']
life_expectancy_us = life_expectancy.loc['United States']
gdp_us = gdp.loc['United States']

# Uncomment the following line of code to see the available country names
# print(employment.index.values)

# Use the Series defined above to create a plot of each variable over time for
# the country of your choice. You will only be able to display one plot at a time
# with each "Test Run".

year = range(1991, 2008)

# data = pd.DataFrame({'x_column': [1, 2, 3, 4], 'y_column': [5, 6, 7, 8]})

# # Add an index to the DataFrame
# data.index = range(1991, 2008)

# # Create a scatter plot
# sns.scatterplot(x=data.index, y='employment', data=employment_us)

# Show the plot
#plt.show()
female_completion_us.plot()


# %%
import pandas as pd

# Subway ridership for 5 stations on 10 different days
ridership_df = pd.DataFrame(
    data=[[   0,    0,    2,    5,    0],
          [1478, 3877, 3674, 2328, 2539],
          [1613, 4088, 3991, 6461, 2691],
          [1560, 3392, 3826, 4787, 2613],
          [1608, 4802, 3932, 4477, 2705],
          [1576, 3933, 3909, 4979, 2685],
          [  95,  229,  255,  496,  201],
          [   2,    0,    1,   27,    0],
          [1438, 3785, 3589, 4174, 2215],
          [1342, 4043, 4009, 4665, 3033]],
    index=['05-01-11', '05-02-11', '05-03-11', '05-04-11', '05-05-11',
           '05-06-11', '05-07-11', '05-08-11', '05-09-11', '05-10-11'],
    columns=['R003', 'R004', 'R005', 'R006', 'R007']
)

# Change False to True for each block of code to see what it does

# DataFrame creation
if False:
    # You can create a DataFrame out of a dictionary mapping column names to values
    df_1 = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]})
    print(df_1)

    # You can also use a list of lists or a 2D NumPy array
    df_2 = pd.DataFrame([[0, 1, 2], [3, 4, 5]], columns=['A', 'B', 'C'])
    print(df_2)
   

# Accessing elements
if False:
    print(ridership_df.iloc[0])
    print(ridership_df.loc['05-05-11'])
    print(ridership_df['R003'])
    print(ridership_df.iloc[1, 3])
    
# Accessing multiple rows
if False:
    print(ridership_df.iloc[1:4])
    
# Accessing multiple columns
if False:
    print(ridership_df[['R003', 'R005']])
    
# Pandas axis
if True:
    df = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]})
    print(df.sum())
    print(df.sum(axis=1))
    print(df.values.sum())
    
def mean_riders_for_max_station(ridership):
    '''
    Fill in this function to find the station with the maximum riders on the
    first day, then return the mean riders per day for that station. Also
    return the mean ridership overall for comparsion.
    
    This is the same as a previous exercise, but this time the
    input is a Pandas DataFrame rather than a 2D NumPy array.
    '''
    overall_mean = None # Replace this with your code
    mean_for_max = None # Replace this with your code
    
    
    return (overall_mean, mean_for_max)

ridership_df.describe()


# %%
import pandas as pd
import numpy as np
path = '/Users/mac/Documents/pythonLearning/pythonAlgo/Data Spreadsheet/'
filename = path + 'nyc_subway_weather.csv'
subway_df = pd.read_csv(filename)

def correlation(x, y):
    '''
    Fill in this function to compute the correlation between the two
    input variables. Each input is either a NumPy array or a Pandas
    Series.
    
    correlation = average of (x in standard units) times (y in standard units)
    
    Remember to pass the argument "ddof=0" to the Pandas std() function!
    '''
    
    # Easy way
    pearson_corr = x.corr(y, method='pearson')
    
    # Hard way

    # Calculate means
    mean_x = x.mean()
    mean_y = y.mean()

    # Calculate deviations from the mean
    deviations_x = x - mean_x
    deviations_y = y - mean_y

    # Calculate sum of products of deviations
    sum_product_deviations = np.sum(deviations_x * deviations_y)

    # Calculate sum of squares of deviations
    sum_squared_deviations_x = np.sum(deviations_x**2)
    sum_squared_deviations_y = np.sum(deviations_y**2)

    # Calculate correlation coefficient
    correlation_coefficient = sum_product_deviations / np.sqrt(sum_squared_deviations_x * sum_squared_deviations_y)

    print(correlation_coefficient)
    return pearson_corr

entries = subway_df['ENTRIESn_hourly']
cum_entries = subway_df['ENTRIESn']
rain = subway_df['meanprecipi']
temp = subway_df['meantempi']

print(correlation(entries, rain))
print(correlation(entries, temp))
print(correlation(rain, temp))

print(correlation(entries, cum_entries))

# %%
import pandas as pd

# Examples of vectorized operations on DataFrames:
# Change False to True for each block of code to see what it does

# Adding DataFrames with the column names
if True:
    df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
    df2 = pd.DataFrame({'a': [10, 20, 30], 'b': [40, 50, 60], 'c': [70, 80, 90]})
    print(df1 + df2)
    
# Adding DataFrames with overlapping column names 
if False:
    df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
    df2 = pd.DataFrame({'d': [10, 20, 30], 'c': [40, 50, 60], 'b': [70, 80, 90]})
    print(df1 + df2)

# Adding DataFrames with overlapping row indexes
if True:
    df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]},
                       index=['row1', 'row2', 'row3'])
    df2 = pd.DataFrame({'a': [10, 20, 30], 'b': [40, 50, 60], 'c': [70, 80, 90]},
                       index=['row4', 'row3', 'row2'])
    print(df1 + df2)

# --- Quiz ---
# Cumulative entries and exits for one station for a few hours.
entries_and_exits = pd.DataFrame({
    'ENTRIESn': [3144312, 3144335, 3144353, 3144424, 3144594,
                 3144808, 3144895, 3144905, 3144941, 3145094],
    'EXITSn': [1088151, 1088159, 1088177, 1088231, 1088275,
               1088317, 1088328, 1088331, 1088420, 1088753]
})

def get_hourly_entries_and_exits(entries_and_exits):
    '''
    Fill in this function to take a DataFrame with cumulative entries
    and exits (entries in the first column, exits in the second) and
    return a DataFrame with hourly entries and exits (entries in the
    first column, exits in the second).
    '''
    
    entries_and_exits = entries_and_exits - entries_and_exits.shift(1)
    print(entries_and_exits)
    entries_and_exits.iloc[0] = 0
    print(entries_and_exits.diff())
    return entries_and_exits

print(get_hourly_entries_and_exits(entries_and_exits))

# %%
import pandas as pd

# Change False to True for this block of code to see what it does

# DataFrame applymap()
if True:
    df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [10, 20, 30],
        'c': [5, 10, 15]
    })
    
    def add_one(x):
        return x + 1
        
    print(df.applymap(add_one))
    
grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio', 
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)
    
def convert_grades(grades):
    '''
    Fill in this function to convert the given DataFrame of numerical
    grades to letter grades. Return a new DataFrame with the converted
    grade.
    
    The conversion rule is:
        90-100 -> A
        80-89  -> B
        70-79  -> C
        60-69  -> D
        0-59   -> F
    '''
    def grade(score):
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'
    
    return grades.applymap(grade)
    
convert_grades(grades_df)

# %%
import pandas as pd

grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio', 
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)

# Change False to True for this block of code to see what it does

# DataFrame apply()
if False:
    def convert_grades_curve(exam_grades):
        # Pandas has a bult-in function that will perform this calculation
        # This will give the bottom 0% to 10% of students the grade 'F',
        # 10% to 20% the grade 'D', and so on. You can read more about
        # the qcut() function here:
        # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.qcut.html
        return pd.qcut(exam_grades,
                       [0, 0.1, 0.2, 0.5, 0.8, 1],
                       labels=['F', 'D', 'C', 'B', 'A'])
        
    # qcut() operates on a list, array, or Series. This is the
    # result of running the function on a single column of the
    # DataFrame.
    print(convert_grades_curve(grades_df['exam1']))
    
    # qcut() does not work on DataFrames, but we can use apply()
    # to call the function on each column separately
    print(grades_df.apply(convert_grades_curve))
    
def standardize(df):
    '''
    Fill in this function to standardize each column of the given
    DataFrame. To standardize a variable, convert each value to the
    number of standard deviations it is above or below the mean.
    '''
 
    grades_df_standardized = grades_df.apply(lambda column: (column - column.mean()) / column.std(ddof=0), axis=0)
    
    print(grades_df_standardized)
    
    def standardize_column(column):
        return (column - column.mean()) / column.std(ddof=0)
        
    return df.apply(standardize_column, axis=1)


print(standardize(grades_df))

# %%
import pandas as pd

# Change False to True for each block of code to see what it does

# Adding a Series to a square DataFrame
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        0: [10, 20, 30, 40],
        1: [50, 60, 70, 80],
        2: [90, 100, 110, 120],
        3: [130, 140, 150, 160]
    })
    
    print(df)
    print('')# Create a blank line between outputs
    print(df + s)
    
# Adding a Series to a one-row DataFrame 
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({0: [10], 1: [20], 2: [30], 3: [40]})
    
    print(df)
    print('') # Create a blank line between outputs
    print(df + s)

# Adding a Series to a one-column DataFrame
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({0: [10, 20, 30, 40]})
    
    print(df)
    print('') # Create a blank line between outputs
    print(df + s)
    

    
# Adding when DataFrame column names match Series index
if False:
    s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    df = pd.DataFrame({
        'a': [10, 20, 30, 40],
        'b': [50, 60, 70, 80],
        'c': [90, 100, 110, 120],
        'd': [130, 140, 150, 160]
    })
    
    print(df)
    print('') # Create a blank line between outputs
    print(df + s)
    
# Adding when DataFrame column names don't match Series index
if True:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        'a': [10, 20, 30, 40],
        'b': [50, 60, 70, 80],
        'c': [90, 100, 110, 120],
        'd': [130, 140, 150, 160]
    })
    
    print(df)
    print('') # Create a blank line between outputs
    print(df + s)

# %%
import pandas as pd

# Adding using +
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        0: [10, 20, 30, 40],
        1: [50, 60, 70, 80],
        2: [90, 100, 110, 120],
        3: [130, 140, 150, 160]
    })
    
    print(df)
    print('') # Create a blank line between outputs
    print(df + s)
    
# Adding with axis='index'
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        0: [10, 20, 30, 40],
        1: [50, 60, 70, 80],
        2: [90, 100, 110, 120],
        3: [130, 140, 150, 160]
    })
    
    print(df)
    print('') # Create a blank line between outputs
    print(df.add(s, axis='index'))
    # The functions sub(), mul(), and div() work similarly to add()
    
# Adding with axis='columns'
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        0: [10, 20, 30, 40],
        1: [50, 60, 70, 80],
        2: [90, 100, 110, 120],
        3: [130, 140, 150, 160]
    })
    
    print(df)
    print('') # Create a blank line between outputs
    print(df.add(s, axis='columns'))
    # The functions sub(), mul(), and div() work similarly to add()
    
grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio', 
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)

def standardize(df):
    '''
    Fill in this function to standardize each column of the given
    DataFrame. To standardize a variable, convert each value to the
    number of standard deviations it is above or below the mean.
    
    This time, try to use vectorized operations instead of apply().
    You should get the same results as you did before.
    '''
    
    mean = df.mean(axis='index')
    std = df.std(axis='index', ddof=0) 
    return (df.sub(mean)).div(std)

def standardize_rows(df):
    '''
    Optional: Fill in this function to standardize each row of the given
    DataFrame. Again, try not to use apply().
    
    This one is more challenging than standardizing each column!
    '''
    mean = df.mean(axis='columns')
    std = df.std(axis='columns', ddof=0)
    return (df.sub(mean, axis='index')).div(std, axis='index')

print(standardize(grades_df))
print(standardize_rows(grades_df))

# %%
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

# Change False to True for each block of code to see what it does

# Examine DataFrame
if False:
    print(example_df)
    
# Examine groups
if False:
    grouped_data = example_df.groupby('even')
    # The groups attribute is a dictionary mapping keys to lists of row indexes
    print(grouped_data.groups)
    
# Group by multiple columns
if False:
    grouped_data = example_df.groupby(['even', 'above_three'])
    print(grouped_data.groups)
    
# Get sum of each group
if True:
    grouped_data = example_df.groupby('even')
    print(grouped_data.sum())
    
# Limit columns in result
if False:
    grouped_data = example_df.groupby('even')
    
    # You can take one or more columns from the result DataFrame
    print(grouped_data.sum()['value'])
    
    print('\n') # Blank line to separate results
    
    # You can also take a subset of columns from the grouped data before 
    # collapsing to a DataFrame. In this case, the result is the same.
    print(grouped_data['value'].sum())
    
filename = '/Users/mac/Documents/pythonLearning/pythonAlgo/Data Spreadsheet/nyc_subway_weather.csv'
subway_df = pd.read_csv(filename)

### Write code here to group the subway data by a variable of your choice, then
### either print out the mean ridership within each group or create a plot.

if True:
    grouped_data = subway_df[:10]
    gdt1 = subway_df[:865].groupby('station')
    gdt2 = subway_df.groupby('meantempi')
    print(grouped_data.groupby('hour').sum()['ENTRIESn_hourly'])
    print(gdt2.sum()['EXITSn_hourly'])
    rs = subway_df.groupby('hour').sum()['ENTRIESn_hourly']
    
#     plt.plot(subway_df.groupby('day_week').sum()['ENTRIESn_hourly'])
#     plt.plot(rs)
    plt.plot(gdt2.sum()['ENTRIESn'], linewidth=2, markersize=40)


# %%


# %%
import numpy as np
import pandas as pd

values = np.array([1, 3, 2, 4, 1, 6, 4])
example_df = pd.DataFrame({
    'value': values,
    'even': values % 2 == 0,
    'above_three': values > 3 
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# Change False to True for each block of code to see what it does

# Standardize each group
if False:
    def standardize(xs):
        return (xs - xs.mean()) / xs.std()
    grouped_data = example_df.groupby('even')
    
    print(grouped_data['value'].apply(standardize))
    
# Find second largest value in each group
if False:
    def second_largest(xs):
        sorted_xs = xs.sort_values(inplace=False, ascending=False)
        return sorted_xs.iloc[1]
    grouped_data = example_df.groupby('even')
    print(example_df)
    print(grouped_data.groups)
    print(grouped_data['value'].apply(second_largest))

# --- Quiz ---
# DataFrame with cumulative entries and exits for multiple stations
ridership_df = pd.DataFrame({
    'UNIT': ['R051', 'R079', 'R051', 'R079', 'R051', 'R079', 'R051', 'R079', 'R051'],
    'TIMEn': ['00:00:00', '02:00:00', '04:00:00', '06:00:00', '08:00:00', '10:00:00', '12:00:00', '14:00:00', '16:00:00'],
    'ENTRIESn': [3144312, 8936644, 3144335, 8936658, 3144353, 8936687, 3144424, 8936819, 3144594],
    'EXITSn': [1088151, 13755385,  1088159, 13755393,  1088177, 13755598, 1088231, 13756191,  1088275]
})

def get_hourly_entries_and_exits(entries_and_exits):
    '''
    Fill in this function to take a DataFrame with cumulative entries
    and exits and return a DataFrame with hourly entries and exits.
    The hourly entries and exits should be calculated separately for
    each station (the 'UNIT' column).
    
    Hint: Take a look at the `get_hourly_entries_and_exits()` function
    you wrote in a previous quiz, DataFrame Vectorized Operations. If
    you copy it here and rename it, you can use it and the `.apply()`
    function to help solve this problem.
    '''

    def diff(x):
        return x.diff()
    
    def get_hourly_entries_and_exits_for_group(entries_and_exits):
        return entries_and_exits - entries_and_exits.shift(1)
    grouped_data = entries_and_exits.groupby('UNIT')
    
    return grouped_data['ENTRIESn', 'EXITSn'].apply(diff)
print(get_hourly_entries_and_exits(ridership_df))

# %%
import pandas as pd

subway_df = pd.DataFrame({
    'UNIT': ['R003', 'R003', 'R003', 'R003', 'R003', 'R004', 'R004', 'R004',
             'R004', 'R004'],
    'DATEn': ['05-01-11', '05-02-11', '05-03-11', '05-04-11', '05-05-11',
              '05-01-11', '05-02-11', '05-03-11', '05-04-11', '05-05-11'],
    'hour': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'ENTRIESn': [ 4388333,  4388348,  4389885,  4391507,  4393043, 14656120,
                 14656174, 14660126, 14664247, 14668301],
    'EXITSn': [ 2911002,  2911036,  2912127,  2913223,  2914284, 14451774,
               14451851, 14454734, 14457780, 14460818],
    'latitude': [ 40.689945,  40.689945,  40.689945,  40.689945,  40.689945,
                  40.69132 ,  40.69132 ,  40.69132 ,  40.69132 ,  40.69132 ],
    'longitude': [-73.872564, -73.872564, -73.872564, -73.872564, -73.872564,
                  -73.867135, -73.867135, -73.867135, -73.867135, -73.867135]
})

weather_df = pd.DataFrame({
    'DATEn': ['05-01-11', '05-01-11', '05-02-11', '05-02-11', '05-03-11',
              '05-03-11', '05-04-11', '05-04-11', '05-05-11', '05-05-11'],
    'hour': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'latitude': [ 40.689945,  40.69132 ,  40.689945,  40.69132 ,  40.689945,
                  40.69132 ,  40.689945,  40.69132 ,  40.689945,  40.69132 ],
    'longitude': [-73.872564, -73.867135, -73.872564, -73.867135, -73.872564,
                  -73.867135, -73.872564, -73.867135, -73.872564, -73.867135],
    'pressurei': [ 30.24,  30.24,  30.32,  30.32,  30.14,  30.14,  29.98,  29.98,
                   30.01,  30.01],
    'fog': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'rain': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'tempi': [ 52. ,  52. ,  48.9,  48.9,  54. ,  54. ,  57.2,  57.2,  48.9,  48.9],
    'wspdi': [  8.1,   8.1,   6.9,   6.9,   3.5,   3.5,  15. ,  15. ,  15. ,  15. ]
})

def combine_dfs(subway_df, weather_df):
    '''
    Fill in this function to take 2 DataFrames, one with subway data and one with weather data,
    and return a single dataframe with one row for each date, hour, and location. Only include
    times and locations that have both subway data and weather data available.
    '''
    return subway_df.merge(weather_df, on=['DATEn', 'hour', 'latitude', 'longitude'], how='left')

print(combine_dfs(subway_df, weather_df))

# %%
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
# groupby() without as_index
if False:
    first_even = example_df.groupby('above_three').first()
    print(first_even)
    #print first_even['even'] # Causes an error. 'even' is no longer a column in the DataFrame
    
# groupby() with as_index=False
if False:
    first_even = example_df.groupby('even', as_index=False).first()
    print(first_even)
    print(first_even['even']) # Now 'even' is still a column in the DataFrame

filename = '/Users/mac/Documents/pythonLearning/pythonAlgo/Data Spreadsheet/nyc_subway_weather.csv'
subway_df = pd.read_csv(filename)

if True:
    def diff(x):
        return x.diff()
    
    plt.figure()
    data_by_location = subway_df.groupby(['latitude', 'longitude'], as_index=False).mean()
    print(data_by_location[:4])
    scaled_entries = data_by_location['ENTRIESn_hourly'] / data_by_location['ENTRIESn_hourly'].std()
    plt.scatter(data_by_location['latitude'], data_by_location['longitude'], s=scaled_entries)
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.show()
    
    plt.figure()
    data_by_weekday = subway_df.groupby('day_week').mean()['ENTRIESn_hourly']
    plt.plot(data_by_weekday)
    plt.xlabel('Day of the week')
    plt.ylabel('Average ridership')
    plt.show()
    
#     plt.figure()
#     data_by_station = subway_df.groupby('station', as_index=False).mean()['ENTRIESn_hourly']
#     plt.plot(data_by_station)
    
#     keys_list = data_by_station.index.tolist()
#     val_list = data_by_station.values.tolist()
    
#     plt.xticks(val_list, keys_list, rotation='vertical')

#     plt.xlabel('Station')
#     plt.ylabel('Average ridership')
#     plt.show()

    plt.figure()
    data_by_station = subway_df.groupby('station', as_index=False).mean()['ENTRIESn_hourly']
    plt.plot(data_by_station)
    plt.xlabel('Station')
    plt.ylabel('Average ridership')
    plt.show()
    
    plt.figure()
    data_by_hour = subway_df.groupby('hour').mean()['ENTRIESn_hourly']
    plt.plot(data_by_hour)
    plt.xlabel('Hour')
    plt.ylabel('Average ridership')
    plt.show()
    
    plt.figure()
    data_by_weather = subway_df.groupby('conds').mean()['ENTRIESn_hourly']
    plt.plot(data_by_weather)
   
#     plt.xticks(val_list, keys_list, rotation='vertical')
    plt.xlabel('Weather')
    plt.ylabel('Average ridership')
    plt.show()
    
    plt.figure()
    data_by_date = subway_df.groupby('DATEn').mean()['ENTRIESn_hourly']
    plt.plot(data_by_date)
    plt.show()
    
#     plt.figure()
#     data_by_time = subway_df.groupby(['day_week', 'hour'], as_index=False).mean()
#     scaled_entries = data_by_time['ENTRIESn'] / data_by_time['ENTRIESn'].std()
#     plt.scatter(data_by_location['day_week'], data_by_location['hour'], s=scaled_entries)
#     plt.xlabel('day_week')
#     plt.ylabel('hour')
#     plt.show()

    


## Make a plot of your choice here showing something interesting about the subway data.
## Matplotlib documentation here: http://matplotlib.org/api/pyplot_api.html
## Once you've got something you're happy with, share it on the forums!

# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

filename = '/Users/mac/Documents/pythonLearning/pythonAlgo/Data Spreadsheet/titanic_data.csv'
df = pd.read_csv(filename)

if True:
    print(titanic_df[:10])
    
#     grouped_data = titanic_df.groupby('Sex')
    
    # You can take one or more columns from the result DataFrame
#     print(grouped_data.groups)
    
    print('\n') # Blank line to separate results
    
#     first_even = titanic_df.groupby('Survived', as_index=False).first()
#     print(first_even)
    # You can also take a subset of columns from the grouped data before 
    # collapsing to a DataFrame. In this case, the result is the same.
#     print(grouped_data['Survived'].sum())
    print(df.isnull().sum())
    print(df.dtypes)


# %%
    df['Age'] = df['Age'].fillna(df['Age'].mean())
    df['Age'] = df['Age'].fillna(df['Age'].mean())

    print(df.isnull().sum())
    
    embarked = df['Embarked'].unique()
    for embark in embarked:
        print(embark)
    
    df['Embarked'] = df['Embarked'].fillna('N')
    df['Embarked'] = df['Embarked'].map({'Q': 0,'S':1,'C':2, 'N':3}).astype(int)
    df['Sex'] = df['Sex'].map({'female': 0,'male':1}).astype(int)
    df['Age'] = df['Age'].astype(int)
    df['Fare'] = df['Fare'].astype(int)
    
    print(df.dtypes)
    print(df.isnull().sum())


    

# %%
print(df.head())
data = df.drop(['PassengerId','Name','Cabin','Ticket'], axis =1, inplace=True)


# %%
fig = plt.figure(figsize =(10, 7))
plt.hist(x = [df[df['Survived']==1]['Age'], df[df['Survived']==0]['Age']],stacked=True, color = ['g','r'],label = ['Survived','Not survived'])
plt.title('Age Histogram with Survival')
plt.xlabel('Age')
plt.ylabel('No of passengers')
plt.legend()

# fig = plt.figure(figsize = (7, 5))
# plt.hist(x = [df[df['Survived']==1]['Sex'], df[df['Survived']==0]['Sex']], stacked=True, color = ['blue', 'red'], label = ['Survived', 'Not survived'])
# plt.title('Sex Histogram with Survival')
# plt.xlabel('Sex')
# plt.ylabel('No of passengers')
# plt.legend()

survival_counts = df['Survived'].value_counts()
survival_counts.plot(kind='bar', rot=3)
plt.title('Survival by Sex')
plt.ylabel('No of passengers')
plt.xlabel('Sex')

fig = plt.figure(figsize = (5, 5))
plt.hist(x = [df[df['Survived']==1]['Fare'], df[df['Survived']==0]['Fare']], stacked=True, label = ['Survived', 'Not survived'])
plt.title('Fare Histogram with Survival')
plt.xlabel('Fare')
plt.ylabel('No of passengers')
plt.legend()




# %%
# Survival Count

column = 'Survived'

# Create a bar chart
survival_counts = df[column].value_counts()
survival_counts.plot(kind='bar', rot=0)

# Adding labels and title
plt.xlabel('Survived')
plt.ylabel('Count')
plt.title('Survival Count (0 = No, 1 = Yes)')

# Show the plot
plt.show()



# %%
Train = df.drop(['Survived'], axis=1)
Test = df.iloc[:,1]
print(Train)
print(Test)
x_train, x_test, y_train, y_test = train_test_split(Train, Test, test_size = 0.2, random_state = 1)

LR = LogisticRegression(solver='liblinear', max_iter=200)
LR.fit(x_train, y_train)
y_pred = LR.predict(x_test)
LRAcc = accuracy_score(y_pred,y_test)
print('Logistic regression accuracy: {:.2f}%'.format(LRAcc*100))

# %%

age_groups = pd.cut(df['Age'], bins=range(0, 100, 10), include_lowest=True)
pd.crosstab(age_groups, df.Survived).plot(kind='bar')

plt.ylabel('No.of Passengers')
plt.title('Age over Survival')
plt.grid(color="red", linestyle="--", alpha=0.5)
# print(age_groups)


def convert_sex(column):
    return pd.qcut(column, [0, 1], labels=['Female', 'Male'])
# sex_class = df.Sex.apply(convert_sex)

# df['Sex'] = df['Sex'].map({0: 'Female',1:'Male'}).astype(object)

print(df.Sex)
pd.crosstab(df.Sex, df.Survived).plot(kind='bar')
plt.ylabel('No of Passengers')
plt.title('Sex of Survival')
plt.grid(color='red', linestyle=':', alpha=0.5)

# %%
from sklearn.preprocessing import LabelEncoder
obj=LabelEncoder()
df['Sex']=obj.fit_transform(df['Sex'])
df.head(4)

# %%
# from sklearn import tree
# from sklearn.model_selection import train_test_split

# model = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3)

# x_train, x_test, y_train, y_test = train_test_split(df, df['Survived'], test_size=0.3)
# model.fit(x_train,y_train)

survived_df=df['Survived'].value_counts()
survived_df.plot(kind='pie',autopct='%1.1f%%',title='Survival Distribution')

# %%
df.groupby('Pclass').count()
print(df[df['Survived']==1].groupby('Pclass')['Survived'].count())
print(df[df['Survived']==0].groupby('Pclass')['Survived'].count())
print(df.groupby('Pclass')['Survived'].mean()*100)



# %%
#To Predict Your Survival You can use. Pclass=[1 or 2 or 3] Sex=[male=1,female=0], Age=[Your_Age], Fare[0-512]

# %%



