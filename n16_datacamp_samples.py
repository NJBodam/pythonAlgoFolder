# Import numpy as np
import numpy as np
import matplotlib.pyplot as plt


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