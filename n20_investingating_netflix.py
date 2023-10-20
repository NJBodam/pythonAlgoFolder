
# Your friend suspects that movies are getting shorter and they've found some initial evidence of this. Having peaked your interest, you will perform exploratory data analysis on the netflix_data.csv data to understand what may be contributing to movies getting shorter over time. Your analysis will follow these steps:

# Load the CSV file and store as netflix_df.
# Filter the data to remove TV shows and store as netflix_subset.
# Investigate the Netflix movie data, keeping only the columns "title", "country", "genre", "release_year", "duration", and saving this into a new DataFrame called netflix_movies.
# Filter netflix_movies to find the movies that are shorter than 60 minutes, saving the resulting DataFrame as short_movies; inspect the result to find possible contributing factors.
# Using a for loop and if/elif statements, iterate through the rows of netflix_movies and assign colors of your choice to four genre groups ("Children", "Documentaries", "Stand-Up", and "Other" for everything else). Save the results in a colors list. Initialize a figure object called fig and create a scatter plot for movie duration by release year using the colors list to color the points and using the labels "Release year" for the x-axis, "Duration (min)" for the y-axis, and the title "Movie Duration by Year of Release".
# After inspecting the plot, answer the question "Are we certain that movies are getting shorter?" by assigning either "yes", "no", or "maybe" to the variable answer.
# Click the "Submit Project" button to check your solution.


# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

dt_netflix = pd.read_csv('netflix_data.csv')

netflix_subset = dt_netflix[dt_netflix['type'] != 'TV Show']
netflix_movies = netflix_subset[['title', 'country', 'genre', 'release_year', 'duration']]

short_movies = netflix_movies[netflix_movies['duration'] < 60]

# print(short_movies.genre.value_counts().sort_values(ascending=False).head())
# print(short_movies.country.value_counts().sort_values(ascending=False).head())
# print(short_movies.release_year.value_counts().sort_values(ascending=False).head())


colors = []

for i in netflix_movies['genre']:
    if i == 'Children':
        colors.append('Blue')
    elif i == 'Documentaries':
        colors.append('Green')
    elif i == 'Stand-Up':
        colors.append('Red')
    else:
        colors.append('Orange')
    
fig = plt.figure(figsize=[12, 8])
plt.scatter(x = netflix_movies['release_year'], y = netflix_movies['duration'], c = colors)
plt.xlabel('Release year')
plt.ylabel('Duration (min)')


# Start coding!