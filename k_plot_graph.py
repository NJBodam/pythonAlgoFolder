
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

plt.hist(data)

# Seaborn for plotting and styling
sns.set(style='whitegrid')
sns.lineplot(x=x_values, y=y_values)

plt.show()