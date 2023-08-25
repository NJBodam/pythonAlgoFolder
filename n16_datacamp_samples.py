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

# Seed - sets the random seed, so that your results are reproducible between simulations.

# Dice Game
# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1, 7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice < 6 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)



# Random Walk - a path that has no clear direction but is determined by a series of random decisions, each of which is left entirely to chance.
# Heads or Tails
np.random.seed(123)
outcomes = []
for x in range(10):
    coin = np.random.randint(0,2)
    if coin == 0:
        outcomes.append("heads")
    else:
        outcomes.append("tails")

# Output
# ['tails', 'heads', 'tails', 'tails', 'tails', 'heads', 'heads', 'heads', 'tails', 'tails']

# The above is not a random walk, because the next step does not depend on the previous step

# Random Walk
np.random.seed(123)
tails = [0]
for x in range(10):
    coin = np.random.randint(0,2)
    tails.append(tails[x] + coin)

# Output
# [0, 0, 1, 1, 1, 1, 1, 1, 2, 3, 3]     # the final element tells you how many times tails was drawn


# Using max
# In the case where a value should not go below a certain minimum, we can use max()
# If you pass max() two arguments, the biggest one gets returned. For example, to make sure that a variable x never goes below 10 when you decrease it, you can use:
x = max(10, x - 1)

# Visualize the walk

# Transpose
# numpy and matplotlib imported, seed set.

# initialize and populate all_walks
all_walks = []
for i in range(5) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)
    
np_aw = np.array(all_walks)
print(np_aw)
# Plot np_aw and show
plt.plot(np_aw)
plt.show()

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)
plt.show()

# [[ 0  0  1  2  3  2  3  2  1  2  3  4  5  6  5  4  3  4  5  4  5  6  7  8
#    9 10 11 16 17 16 17 16 17 16 18 19 20 21 22 23 22 21 20 19 18 17 16 15
#   16 17 18 17 18 19 18 17 18 17 18 19 18 19 20 19 20 21 22 21 20 19 24 23
#   24 25 24 26 27 26 25 26 25 28 29 30 29 30 32 35 40 45 44 45 44 45 46 45
#   46 45 44 45 46]
#  [ 0  1  2  1  2  1  0  0  1  3  2  1  0  1  2  3  4  3  4  3  2  3  4  5
#    6  5  4  3  2  1  3  4  5  4  3  2  1  2  3  4  5 11 12 11 10 11 10  9
#   14 18 19 20 21 22 21 22 23 26 27 28 27 28 29 30 34 33 32 31 30 31 30 29
#   28 29 28 29 28 29 30 31 34 35 36 41 42 43 44 43 44 45 44 45 46 47 48 47
#   48 47 48 47 48]
#  [ 0  1  2  3  5  4  8  9 10 11 16 17 18 21 20 19 23 22 21 22 21 22 21 22
#   23 24 23 22 21 27 26 27 28 32 33 34 35 34 35 34 35 36 35 36 37 36 37 38
#   39 40 39 40 39 40 39 38 37 36 35 36 37 36 35 36 37 38 39 44 45 46 47 48
#   47 48 49 50 51 52 53 52 53 54 58 57 56 57 60 59 60 61 63 64 65 66 65 66
#   67 68 69 70 71]
#  [ 0  1  0  6  8  9  8  7  6  5  6  5  6  8  9  8  9 10  9 10  9 10  9 10
#   11 13 14 15 18 24 25 24 23 24 26 25 26 27 32 31 32 33 34 35 36 35 34 35
#   36 37 36 35 34 39 38 39 38 39 41 46 47 46 45 44 45 46 47 48 47 48 49 50
#   49 50 56 61 62 63 64 68 67 71 72 73 78 79 80 81 82 85 86 87 86 87 88 91
#   92 98 99 98 99]
#  [ 0  2  1  6  5  6  9  8  7  6  5  6  7  8  9  8  7  6  5  4  3  4  5  8
#   14 15 16 17 16 15 16 17 18 17 16 15 16 15 14 15 14 15 16 17 18 19 20 19
#   20 21 22 21 22 23 24 25 24 25 26 25 26 27 28 29 28 29 30 29 35 37 36 37
#   39 38 43 47 48 51 50 49 50 49 50 56 55 58 57 58 59 60 59 60 59 60 61 62
#   63 62 61 60 61]]

# [[ 0  0  0  0  0]
#  [ 0  1  1  1  2]
#  [ 1  2  2  0  1]
#  [ 2  1  3  6  6]
#  [ 3  2  5  8  5]
#  [ 2  1  4  9  6]
#  [ 3  0  8  8  9]
#  [ 2  0  9  7  8]
#  [ 1  1 10  6  7]
#  [ 2  3 11  5  6]
#  [ 3  2 16  6  5]
#  [ 4  1 17  5  6]
#  [ 5  0 18  6  7]
#  [ 6  1 21  8  8]
#  [ 5  2 20  9  9]
#  [ 4  3 19  8  8]
#  [ 3  4 23  9  7]
#  [ 4  3 22 10  6]
#  [ 5  4 21  9  5]
#  [ 4  3 22 10  4]
#  [ 5  2 21  9  3]
#  [ 6  3 22 10  4]
#  [ 7  4 21  9  5]
#  [ 8  5 22 10  8]
#  [ 9  6 23 11 14]
#  [10  5 24 13 15]
#  [11  4 23 14 16]
#  [16  3 22 15 17]
#  [17  2 21 18 16]
#  [16  1 27 24 15]
#  [17  3 26 25 16]
#  [16  4 27 24 17]
#  [17  5 28 23 18]
#  [16  4 32 24 17]
#  [18  3 33 26 16]
#  [19  2 34 25 15]
#  [20  1 35 26 16]
#  [21  2 34 27 15]
#  [22  3 35 32 14]
#  [23  4 34 31 15]
#  [22  5 35 32 14]
#  [21 11 36 33 15]
#  [20 12 35 34 16]
#  [19 11 36 35 17]
#  [18 10 37 36 18]
#  [17 11 36 35 19]
#  [16 10 37 34 20]
#  [15  9 38 35 19]
#  [16 14 39 36 20]
#  [17 18 40 37 21]
#  [18 19 39 36 22]
#  [17 20 40 35 21]
#  [18 21 39 34 22]
#  [19 22 40 39 23]
#  [18 21 39 38 24]
#  [17 22 38 39 25]
#  [18 23 37 38 24]
#  [17 26 36 39 25]
#  [18 27 35 41 26]
#  [19 28 36 46 25]
#  [18 27 37 47 26]
#  [19 28 36 46 27]
#  [20 29 35 45 28]
#  [19 30 36 44 29]
#  [20 34 37 45 28]
#  [21 33 38 46 29]
#  [22 32 39 47 30]
#  [21 31 44 48 29]
#  [20 30 45 47 35]
#  [19 31 46 48 37]
#  [24 30 47 49 36]
#  [23 29 48 50 37]
#  [24 28 47 49 39]
#  [25 29 48 50 38]
#  [24 28 49 56 43]
#  [26 29 50 61 47]
#  [27 28 51 62 48]
#  [26 29 52 63 51]
#  [25 30 53 64 50]
#  [26 31 52 68 49]
#  [25 34 53 67 50]
#  [28 35 54 71 49]
#  [29 36 58 72 50]
#  [30 41 57 73 56]
#  [29 42 56 78 55]
#  [30 43 57 79 58]
#  [32 44 60 80 57]
#  [35 43 59 81 58]
#  [40 44 60 82 59]
#  [45 45 61 85 60]
#  [44 44 63 86 59]
#  [45 45 64 87 60]
#  [44 46 65 86 59]
#  [45 47 66 87 60]
#  [46 48 65 88 61]
#  [45 47 66 91 62]
#  [46 48 67 92 63]
#  [45 47 68 98 62]
#  [44 48 69 99 61]
#  [45 47 70 98 60]
#  [46 48 71 99 61]]
