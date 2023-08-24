
import matplotlib.pyplot as plt
import seaborn as sns



y_values = [34, 44, 23, 46, 12, 24]
y_values.sort()

x_values = ['A', 'B', 'C', 'D', 'E', 'F']

# Plot a graph
plt.plot(x_values, y_values)

# Display the graph
plt.show()

data = [1, 2, 1, 3, 3, 1, 4, 2]
# For iPython notebook only
# %matplotlib inline
plt.xlabel("Label for x axis")
plt.ylabel("Label for y axis")
plt.title("Title of plot")

# You can aswell add a bin parameter to specify the number of bins, which is the width of each bar
plt.hist(data, bins=5)

# You can use the following syntax to clear the plot:
plt.yticks([0, 1, 2, 3, 4, 5, 6, 7])
# We can also change the label displayed on the Y axis using same yticks function
plt.yticks([0, 1, 2, 3, 4, 5, 6, 7], ['0', '10k', '20k', '30k', '40k', '50k', '60k', '70k'])
# We can also change the label displayed on the X axis using same xticks function
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val, tick_lab)

# After customizing, display the plot
plt.show()

# Adding more data to the plot
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

year = [1800, 1850, 1900] + year
pop = [1.0, 1.262, 1.650] + pop

plt.clf()
# Histogram are for ascertaining if the distribution of data

# Seaborn for plotting and styling
sns.set(style='whitegrid')
sns.lineplot(x=x_values, y=y_values)

plt.show()