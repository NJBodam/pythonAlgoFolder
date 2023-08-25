# Import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop

np_pop = np_pop * 2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()

# CUSTOMIZATION
# making the plot more colorful
# Specify c and alpha inside plt.scatter()
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)
# alpha is for transparency

# ADDITIONAL CUSTOMIZATIONS

# Additional customizations
plt.text(1550, 71, 'India')     # x and y coordinates of the text
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)      # to add grid lines to the plot


#Dictionary
# From string in countries and capitals, create dictionary europe
europe = {'spain':'madrid', "france":'paris', "germany":'berlin', 'norway':'oslo' }
# Print europe
print(europe['spain'])


# Print out the keys in europe
print(europe.keys())    # returns a list of the keys in the dictionary

'spain' in europe   # returns True if 'spain' is a key in the dictionary europe

# Update capital of germany
europe['germany'] = 'berlin'

# Remove australia
del(europe['australia'])

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe["france"]['capital'])

# Create sub-dictionary data
data = {'capital':'rome', 'population':59.83}

# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
print(europe)

# Numpy - used for working with arrays of one datatype\

# Pandas - used for working with tables of data of different datatypes
# the data are stored in an object called DataFrame

# When read from a csv file, passing an index_col argument to read_csv() 
# will use the column with that index as the row labels in the DataFrame 
# that is created. Example: 
pd.read_csv('file.csv', index_col=0)


# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country':names, 'drives_right':dr, 'cars_per_cap':cpc}




# Dictionary to DataFrame
# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)



# Column Access
# Print out country column as Pandas Series
print(cars['country'])      # returns a Pandas Series
# Print out country column as Pandas DataFrame
print(cars[['country']])    # returns a Pandas DataFrame

# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])    # returns a Pandas DataFrame


# Row Access
# Print out first 3 observations
print(cars[0:3])    # returns a Pandas DataFrame
# Print out fourth, fifth and sixth observation
print(cars[3:6])    # returns a Pandas DataFrame


# loc and iloc - with Pandas
# loc - label-based

# Print out observation for Japan
print(cars.loc['JPN'])      # returns a Pandas Series
# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])      # returns a Pandas DataFrame

# Print beginning to end of two columns in cars
print(cars.loc[:, ['country', 'capital']])      # returns a Pandas DataFrame

# Print out country and capital for Russia, India and China
print(cars.loc[['RU', 'IN', 'CH'], ['country', 'capital']])      # returns a Pandas DataFrame

# iloc - integer position-based
print(cars.iloc[[1, 2, 3], [0, 1]])    # returns a Pandas DataFrame
# Prints same result as above

print(cars.iloc[:, [1, 2]])    # returns all rows with columns 1 and 2



# Comparison Operators

# comparing arrays
# Create arrays
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)

# my_house less than your_house
print(my_house < your_house)

# Boolean Operators
# and, or, not
True and True  # returns True
True and False  # returns False
False and True  # returns False

True or False  # returns True
False or True # returns True
False or False  # returns False

not True  # returns False

bmi = np.array([21.852, 20.975, 21.75, 24.747, 21.441])
bmi > 21 and bmi < 22       # results in Value error

# In this case use logical_and(), logical_or(), logical_not()
# Hence
np.logical_and(bmi > 21 and bmi < 22)
# results in [True, False, True, False, True]       returns True for all values between 21 and 22.

bmi[np.logical_and(bmi > 21 and bmi < 22)]
# results in [21.852, 21.75, 21.441]


# And or not
# Define variables
my_kitchen = 18.0
your_kitchen = 14.0
# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen>10 and my_kitchen<18)

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen<14 or my_kitchen>17)

# Double my_kitchen smaller than triple your_kitchen?
print(2*my_kitchen < 3*your_kitchen)


# Filtering
# Import numpy, you'll need this

# Create medium: observations with cars_per_cap between 100 and 500
medium = cars[np.logical_and(cars['cars_per_cap'] > 100, cars['cars_per_cap'] < 500)]

# Print medium
print(medium)


# For Loop
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, a in enumerate(areas) :
    print(f"room {index} : {a}")

#  Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index + 1) + ": " + str(area))

# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for room, sqm in house:
    print(f"the {room} is {sqm} sqm")

# house list of lists
house = [["hallway", 11.25, 0], 
         ["kitchen", 18.0, 2], 
         ["living room", 20.0, 3], 
         ["bedroom", 10.75, 2], 
         ["bathroom", 9.50, 1]]
         
# Build a for loop from scratch
for room, sqm, window in house:
    print(f"the {room} is {sqm} sqm with {window} window(s)")

#Output
# the hallway is 11.25 sqm with 0 window(s)
# the kitchen is 18.0 sqm with 2 window(s)
# the living room is 20.0 sqm with 3 window(s)
# the bedroom is 10.75 sqm with 2 window(s)
# the bathroom is 9.5 sqm with 1 window(s)


# Loop over dictionary
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for country, capital in europe.items():
    print(f"the capital of {country} is {capital}")

# For two dimensional numpy array, should you want to print all values separately
# # For loop over np_baseball
for x in np.nditer(np_baseball):
    print(x) 


# Iterrows command - used for generating the labels of the row and the actual data in the row
# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(lab)
    print(row)

# Output

# US
# cars_per_cap        809
# country     United States
# drives_right         True
# Name: US, dtype: object

# AUS
# cars_per_cap    731
# country       Australia
# drives_right      False
# Name: AUS, dtype: object

# JPN
# cars_per_cap    588
# country          Japan
# drives_right     False
# Name: JPN, dtype: object
#...

# We can also print the labels and a specific column
# Adapt for loop
for lab, row in cars.iterrows() :
    print(f"{lab}: {row['cars_per_cap']}")

# Output
# US: 809
# AUS: 731
# JPN: 588
# IN: 18
#...

# Add column - for loop
for lab, row in cars.iterrows() :
    # Creating series in every iteration
    cars.loc[lab, "NAME_LENGHT"] = len(row["country"])

# Output
#            country  drives_right  cars_per_cap  NAME_LENGHT
# US   United States          True           809         13.0
# AUS      Australia         False           731          9.0
# JPN          Japan         False           588          5.0
# IN           India         False            18          5.0
# RU          Russia          True           200          6.0
# MOR        Morocco          True            70          7.0
# EG           Egypt          True            45          5.0

# Alternatively, we can use apply() method
cars["NAME_LENGHT"] = cars["country"].apply(len)

# Adding Column with apply()
cars['COUNTRY'] = cars['country'].apply(str.upper)

# Output
#            country  drives_right  cars_per_cap  NAME_LENGHT        COUNTRY
# US   United States          True           809           13  UNITED STATES
# AUS      Australia         False           731            9      AUSTRALIA
#...

# Random Numbers
np.random.rand()    # returns a random float between 0 and 1

# Consistency in pseudorandom numbers
print(np.random.seed(123))
print(np.random.rand())
print(np.random.rand())
print("...")
print(np.random.seed(123))
print(np.random.rand())
print(np.random.rand())